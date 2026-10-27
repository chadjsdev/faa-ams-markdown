#!/usr/bin/env python3
"""Convert everything in inbox/ to Markdown in the output folder.

Each successfully converted file is moved to archive/, so inbox/ only holds new
downloads and archive/ is the record of what's already been downloaded.

Source URLs are recovered by matching filenames against links in the checklist,
or from the "saved from url" stamp the save-page bookmarklet writes into pages.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from common import file_to_md, norm, slugify
from settings import ARCHIVE, CHECKLIST, INBOX, OUTPUT


def url_index() -> dict[str, str]:
    """Map lowercase filename stem -> URL for every link in the checklist.

    Broken links are skipped, so a file fetched from a replacement source
    (e.g. a web archive) gets the working URL.
    """
    from status import broken_links
    broken = {norm(u) for u in broken_links()}
    index = {}
    for url in re.findall(r"\((https?://[^)\s]+)\)", CHECKLIST.read_text(encoding="utf-8")):
        if norm(url) in broken:
            continue
        stem = Path(unquote(urlparse(url).path)).stem.lower()
        index[stem] = url
    return index


def saved_from_url(path: Path) -> str | None:
    """Source URL of a saved web page.

    Prefers the '<!-- saved from url=(NNNN)URL -->' stamp (written by the save-page
    bookmarklet, and by some browsers on Save As). Falls back to the page's own
    <link rel="canonical"> or og:url, which covers a plain Ctrl+S save.
    """
    if path.suffix.lower() not in (".html", ".htm"):
        return None
    with path.open(encoding="utf-8", errors="replace") as f:
        head = f.read(200_000)
    m = re.search(r"saved from url=\(\d+\)(\S+?)\s*-->", head[:4096])
    if m:
        return m.group(1)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(head, "html.parser")
    tag = soup.find("link", rel="canonical", href=True)
    url = tag["href"] if tag else None
    if not url:
        og = soup.find("meta", property="og:url", content=True)
        url = og["content"] if og else None
    return url if url and url.startswith(("http://", "https://")) else None


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--inbox", type=Path, default=INBOX)
    ap.add_argument("--out", type=Path, default=OUTPUT)
    ap.add_argument("--archive", type=Path, default=ARCHIVE)
    ap.add_argument("--force", action="store_true",
                    help="re-convert everything in inbox/ and archive/, overwriting output")
    args = ap.parse_args()

    for d in (args.inbox, args.out, args.archive):
        d.mkdir(parents=True, exist_ok=True)
    urls = url_index()
    done = dupes = failed = 0

    folders = [args.inbox, args.archive] if args.force else [args.inbox]
    archived_hashes = {} if args.force else {
        file_hash(p): p.name for p in args.archive.iterdir() if p.is_file() and not p.name.startswith(".")}
    def wanted(p: Path, root: Path) -> bool:
        # Skip dotfiles and the "<page>_files" asset folders Chrome/Edge create next to a saved page.
        return p.is_file() and not p.name.startswith(".") \
            and not any(part.lower().endswith("_files") for part in p.relative_to(root).parts[:-1])

    for path in sorted(p for d in folders for p in d.rglob("*") if wanted(p, d)):
        target = args.out / f"{slugify(path.stem)}.md"
        archived = args.archive / path.name
        same = archived_hashes.get(file_hash(path)) if path.parent != args.archive else None
        if same:
            print(f"dup   {path.name} (identical to archive/{same}; left in inbox)")
            dupes += 1
            continue
        if target.exists() and not args.force:
            note = "already in archive/" if archived.exists() else "output already exists"
            print(f"dup   {path.name} ({note}; left in inbox)")
            dupes += 1
            continue
        source = urls.get(path.stem.lower()) or saved_from_url(path)
        try:
            result = file_to_md(path, source)
        except ImportError as e:
            print(f"FAIL  {path.name}: missing Python package ({e.name}); see README setup", file=sys.stderr)
            failed += 1
            continue
        except Exception as e:  # keep going on a single bad file
            print(f"FAIL  {path.name}: {e}", file=sys.stderr)
            failed += 1
            continue
        if result is None:
            print(f"skip  {path.name} (unsupported type)")
            continue
        body = result[1].split("\n---\n", 1)[-1]
        if path.suffix.lower() in (".html", ".htm") and len(body.strip()) < 300:
            print(f"FAIL  {path.name}: page is nearly empty (a PDF viewer or a script-only page?); left in inbox",
                  file=sys.stderr)
            failed += 1
            continue
        target.write_text(result[1], encoding="utf-8")
        if path.parent != args.archive:
            path.replace(archived)
        print(f"ok    {path.name} -> {target.name}" + ("" if source else "  (no source URL match)"))
        done += 1

    print(f"\n{done} converted and archived, {dupes} duplicates, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
