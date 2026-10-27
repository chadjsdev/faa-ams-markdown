"""Shared conversion helpers: HTML / PDF / Office -> Markdown with front matter.

Converter libraries are imported only when a file of that type is converted, so
a missing package affects just that file type.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

# Tried in order; first match wins. faa.gov (Drupal) uses <article>/<main>.
# FAST pages use div.mainColumn: on lifecycle pages the What/Who/Outputs/Toolkit
# block (div#whoWhatWrapper) sits outside div#content.
CONTENT_SELECTORS = ["article", "main", "div.mainColumn", "div#content", "body"]
STRIP_TAGS = ["script", "style", "noscript", "nav", "header", "footer", "form", "iframe", "aside"]
DOC_EXTS = (".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx")


def slugify(text: str, max_len: int = 100) -> str:
    text = re.sub(r"[^\w\s.-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)[:max_len].strip("-.") or "untitled"


def norm(url: str) -> str:
    """Scheme-less, lowercase URL for comparisons."""
    return re.sub(r"^https?://", "", url.strip()).lower()


def front_matter(title: str, source: str | None, kind: str) -> str:
    lines = ["---", f'title: "{title.replace(chr(34), chr(39))}"']
    if source:
        lines.append(f"source_url: {source}")
    lines += [f"source_type: {kind}", f"converted: {date.today().isoformat()}", "---", ""]
    return "\n".join(lines)


def read_front_matter(path: Path) -> dict:
    meta = {}
    with path.open(encoding="utf-8", errors="replace") as f:
        if f.readline().strip() != "---":
            return meta
        for line in f:
            if line.strip() == "---":
                break
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta


def html_to_md(html: str, base_url: str | None = None) -> tuple[str, str]:
    """Return (title, markdown) for the main content of an HTML page."""
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    soup = BeautifulSoup(html, "html.parser")
    title = (soup.title.get_text(strip=True) if soup.title else "") or "Untitled"
    title = re.sub(r"\s*\|\s*Federal Aviation Administration\s*$", "", title)

    node = next((n for sel in CONTENT_SELECTORS if (n := soup.select_one(sel))), soup)
    for tag in node.find_all(STRIP_TAGS):
        tag.decompose()
    for a in node.find_all("a", href=True):
        if base_url:
            a["href"] = urljoin(base_url, a["href"])
        # Spaces in hrefs break Markdown links; encode them.
        a["href"] = a["href"].strip().replace(" ", "%20")
        # Icon-only links (e.g. download buttons) would vanish once images are
        # stripped; give them a text label so the URL survives.
        if not a.get_text(strip=True):
            img = a.find("img")
            label = (img and (img.get("alt") or img.get("title"))) or a.get("title") \
                or unquote(urlparse(a["href"]).path.rsplit("/", 1)[-1]) or a["href"]
            a.string = label.strip()

    md = markdownify(str(node), heading_style="ATX", strip=["img"])
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, md


def pdf_to_md(path: Path) -> str:
    import pymupdf4llm
    return pymupdf4llm.to_markdown(str(path), show_progress=False)


def office_to_md(path: Path) -> str:
    from markitdown import MarkItDown
    return MarkItDown().convert(str(path)).text_content


def doc_to_md(path: Path) -> str:
    """Legacy Word .doc. Tries, in order: macOS textutil, LibreOffice, Microsoft Word (Windows)."""
    if shutil.which("textutil"):
        html = subprocess.run(["textutil", "-convert", "html", "-stdout", str(path)],
                              check=True, capture_output=True, text=True).stdout
        return html_to_md(html)[1]

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice and sys.platform == "win32":
        for p in (r"C:\Program Files\LibreOffice\program\soffice.exe",
                  r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"):
            if Path(p).exists():
                soffice = p
    if soffice:
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([soffice, "--headless", "--convert-to", "docx", "--outdir", tmp, str(path)],
                           check=True, capture_output=True)
            return office_to_md(Path(tmp) / (path.stem + ".docx"))

    if sys.platform == "win32":
        try:
            import win32com.client  # pywin32; drives the installed Microsoft Word
        except ImportError:
            win32com = None
        if win32com:
            with tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / (path.stem + ".docx")
                word = win32com.client.DispatchEx("Word.Application")
                word.Visible = False
                try:
                    doc = word.Documents.Open(str(path.resolve()), ReadOnly=True)
                    doc.SaveAs2(str(out), FileFormat=16)  # 16 = wdFormatDocumentDefault (.docx)
                    doc.Close(False)
                finally:
                    word.Quit()
                return office_to_md(out)

    raise RuntimeError("can't read legacy .doc here: open it in Word and Save As .docx, "
                       "or install LibreOffice or pywin32")


def file_to_md(path: Path, source_url: str | None = None) -> tuple[str, str] | None:
    """Convert a local file. Returns (title, full markdown with front matter) or None if unsupported."""
    ext = path.suffix.lower()
    if ext in (".html", ".htm"):
        title, body = html_to_md(path.read_text(encoding="utf-8", errors="replace"), source_url)
        kind = "html"
    elif ext == ".pdf":
        title, body, kind = path.stem, pdf_to_md(path), "pdf"
    elif ext == ".doc":
        title, body, kind = path.stem, doc_to_md(path), "doc"
    elif ext in (".docx", ".pptx", ".xlsx"):
        title, body, kind = path.stem, office_to_md(path), ext[1:]
    else:
        return None
    heading = "" if body.lstrip().startswith("# ") else f"# {title}\n\n"
    return title, front_matter(title, source_url, kind) + heading + body + "\n"
