#!/usr/bin/env python3
"""Polite, scoped crawler for www.faa.gov. Writes Markdown to output/faa_gov/.

Respects robots.txt, rate-limits, and only follows URLs under the prefixes in
config.yaml. Re-runs skip pages/documents already saved.
"""
from __future__ import annotations

import argparse
import sys
import time
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
import yaml
from bs4 import BeautifulSoup

from common import file_to_md, front_matter, html_to_md, slugify

ROOT = Path(__file__).parent
HOST = "www.faa.gov"
DOC_EXTS = (".pdf", ".docx", ".pptx", ".xlsx")


class Crawler:
    def __init__(self, cfg: dict, out: Path):
        self.cfg = cfg
        self.out = out
        self.pages_dir = out / "pages"
        self.docs_dir = out / "documents"
        self.raw_dir = out / "_raw"  # original downloaded documents
        for d in (self.pages_dir, self.docs_dir, self.raw_dir):
            d.mkdir(parents=True, exist_ok=True)

        self.session = requests.Session()
        self.session.headers["User-Agent"] = cfg["user_agent"]
        self.robots = RobotFileParser(f"https://{HOST}/robots.txt")
        self.robots.read()
        self.last_request = 0.0

    # --- scope ---------------------------------------------------------
    def _ok(self, url: str, prefixes: list[str]) -> bool:
        p = urlparse(url)
        return (
            p.scheme in ("http", "https")
            and p.netloc == HOST
            and any(p.path.startswith(pre) for pre in prefixes)
            and not any(x in url for x in self.cfg.get("exclude", []))
            and self.robots.can_fetch(self.cfg["user_agent"], url)
        )

    def is_page(self, url: str) -> bool:
        return not urlparse(url).path.lower().endswith(DOC_EXTS) and self._ok(url, self.cfg["allowed_prefixes"])

    def is_document(self, url: str) -> bool:
        return urlparse(url).path.lower().endswith(DOC_EXTS) and self._ok(url, self.cfg["document_prefixes"])

    # --- fetching ------------------------------------------------------
    def get(self, url: str, **kw) -> requests.Response | None:
        wait = self.cfg["delay_seconds"] - (time.monotonic() - self.last_request)
        if wait > 0:
            time.sleep(wait)
        self.last_request = time.monotonic()
        try:
            r = self.session.get(url, timeout=60, **kw)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            print(f"FAIL  {url}: {e}", file=sys.stderr)
            return None

    @staticmethod
    def page_slug(url: str) -> str:
        return slugify(urlparse(url).path.strip("/").replace("/", "__"), 180)

    def save_page(self, url: str, html: str) -> None:
        title, body = html_to_md(html, url)
        (self.pages_dir / f"{self.page_slug(url)}.md").write_text(
            front_matter(title, url, "html") + f"# {title}\n\n" + body + "\n"
        )

    def save_document(self, url: str) -> None:
        name = Path(unquote(urlparse(url).path)).name
        target = self.docs_dir / f"{slugify(Path(name).stem)}.md"
        if target.exists():
            return
        raw = self.raw_dir / name
        if not raw.exists():
            r = self.get(url, stream=True)
            if r is None:
                return
            limit = self.cfg["max_document_mb"] * 1024 * 1024
            if int(r.headers.get("Content-Length") or 0) > limit:
                print(f"skip  {url} (larger than {self.cfg['max_document_mb']} MB)")
                return
            raw.write_bytes(r.content)
        try:
            result = file_to_md(raw, url)
        except Exception as e:
            print(f"FAIL  convert {name}: {e}", file=sys.stderr)
            return
        if result:
            target.write_text(result[1])
            print(f"doc   {url}")

    # --- main loop -----------------------------------------------------
    def run(self) -> None:
        queue = deque((urldefrag(s)[0], 0) for s in self.cfg["seeds"])
        seen = {u for u, _ in queue}
        docs: set[str] = set()
        pages = 0

        while queue and pages < self.cfg["max_pages"]:
            url, depth = queue.popleft()
            if not self.is_page(url):
                print(f"skip  {url} (out of scope or robots.txt)")
                continue
            r = self.get(url)
            if r is None or "text/html" not in r.headers.get("Content-Type", ""):
                continue
            pages += 1
            self.save_page(url, r.text)
            print(f"page  [{pages}] {url}")

            for a in BeautifulSoup(r.text, "html.parser").find_all("a", href=True):
                link = urldefrag(urljoin(url, a["href"]))[0]
                if self.cfg["download_documents"] and self.is_document(link):
                    docs.add(link)
                elif depth < self.cfg["max_depth"] and link not in seen and self.is_page(link):
                    seen.add(link)
                    queue.append((link, depth + 1))

        print(f"\n{pages} pages crawled; {len(docs)} linked documents found")
        for d in sorted(docs):
            self.save_document(d)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", type=Path, default=ROOT / "config.yaml")
    ap.add_argument("--out", type=Path, default=ROOT / "output" / "faa_gov")
    ap.add_argument("--max-pages", type=int, help="override config max_pages")
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())
    if args.max_pages is not None:
        cfg["max_pages"] = args.max_pages
    Crawler(cfg, args.out).run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
