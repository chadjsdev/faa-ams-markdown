#!/usr/bin/env python3
"""Track every document: checklist -> inbox -> output.

Writes manifest.csv next to the output folder (one row per converted file) and
curated/status.md (checklist items grouped as converted / downloaded-not-converted /
broken / not downloaded, plus converted files that aren't on the checklist). Also
ticks the checklist boxes: [x] converted, [!] broken, [ ] still to download.
Broken links come from curated/broken_links.txt; for each, it lists which
converted documents mention it. Reads local files only.

    status.py                       # report
    status.py --broken URL "note"   # record a 404 and report
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

from common import DOC_EXTS, norm, read_front_matter as front_matter, slugify
from settings import ARCHIVE, CHECKLIST, CURATED, INBOX, OUTPUT as OUT

BROKEN = CURATED / "broken_links.txt"
FIELDS = ["output", "title", "source_type", "source_url", "converted", "size_kb", "input"]


def checklist() -> list[tuple[str, str, str]]:
    """(section, label, url) for every link in the checklist."""
    items, section = [], ""
    for line in CHECKLIST.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        for label, url in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", line):
            items.append((section, label, url))
    return items


def broken_links() -> dict[str, str]:
    """url -> note, from curated/broken_links.txt."""
    out = {}
    if BROKEN.exists():
        for line in BROKEN.read_text(encoding="utf-8").splitlines():
            url, _, note = line.partition("#")
            if url.strip():
                out[url.strip()] = note.strip()
    return out


def referenced_in(targets: set[str]) -> dict[str, set[str]]:
    """Which converted documents mention each target URL (normalized, scheme-less).

    Searches the converted .md text, so PDFs, Word files and web pages all count.
    """
    refs: dict[str, set[str]] = {t: set() for t in targets}
    for md in OUT.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace").lower().replace("\\_", "_")
        for t in targets:
            if t in text:
                refs[t].add(md.stem)
    return refs


def tick_checklist(converted_urls: set[str], broken_norm: set[str]) -> None:
    """Mark checklist lines [x] when converted, [!] when broken, [ ] otherwise."""
    out = []
    for line in CHECKLIST.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- \[[ x!]\] .*?\((https?://[^)\s]+)\)", line)
        if m:
            url = m.group(1)
            mark = "x" if url.lower() in converted_urls else "!" if norm(url) in broken_norm else " "
            line = f"- [{mark}]" + line[5:]
        out.append(line)
    CHECKLIST.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--broken", nargs="+", metavar=("URL", "NOTE"), help="record a broken link, then report")
    args = ap.parse_args()
    if args.broken:
        url, note = args.broken[0], " ".join(args.broken[1:]) or "404"
        if norm(url) not in {norm(u) for u in broken_links()}:
            with BROKEN.open("a", encoding="utf-8") as f:
                f.write(f"{url}  # {note} ({date.today().isoformat()})\n")
            print(f"Recorded broken link: {url}")

    OUT.mkdir(parents=True, exist_ok=True)
    downloaded = [p for d in (ARCHIVE, INBOX) if d.exists() for p in d.rglob("*") if p.is_file()]
    inputs = {slugify(p.stem): p.name for p in downloaded}
    rows = []
    for md in sorted(OUT.glob("*.md")):
        m = front_matter(md)
        rows.append({
            "output": md.name, "title": m.get("title", ""), "source_type": m.get("source_type", ""),
            "source_url": m.get("source_url", ""), "converted": m.get("converted", ""),
            "size_kb": round(md.stat().st_size / 1024, 1), "input": inputs.get(md.stem, ""),
        })
    with (OUT.parent / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS)
        w.writeheader()
        w.writerows(rows)

    converted_urls = {r["source_url"].lower() for r in rows if r["source_url"]}
    downloaded_names = {p.name.lower() for p in downloaded}
    broken = broken_links()
    broken_norm = {norm(u) for u in broken}
    groups: dict[str, list[str]] = {
        "Converted": [], "Downloaded, not converted": [], "Broken (404)": [], "Not downloaded": []}
    for section, label, url in checklist():
        name = Path(unquote(urlparse(url).path)).name.lower()
        # Documents keep their filename; web pages (.cfm, .aspx, no extension) are saved as <stem>.html.
        if Path(name).suffix not in DOC_EXTS:
            name = Path(name).stem + ".html"
        if url.lower() in converted_urls:
            key = "Converted"
        elif norm(url) in broken_norm:
            key = "Broken (404)"
        elif name in downloaded_names:
            key = "Downloaded, not converted"
        else:
            key = "Not downloaded"
        groups[key].append(f"- [{label}]({url}) — {section}")

    tick_checklist(converted_urls, broken_norm)

    refs = referenced_in(broken_norm) if broken else {}
    broken_lines = []
    for url, note in broken.items():
        where = ", ".join(sorted(refs.get(norm(url), set()))) or "no converted document mentions it"
        broken_lines += [f"- {url}" + (f" — {note}" if note else ""), f"  - referenced in: {where}"]

    checklist_urls = {u.lower() for _, _, u in checklist()}
    extra = [f"- {r['output']} ({r['source_url'] or 'no source URL'})"
             for r in rows if r["source_url"].lower() not in checklist_urls]

    lines = ["# Document status", "", "Generated by `status.py`.", ""]
    for name, items in groups.items():
        lines += [f"## {name} ({len(items)})", ""] + items + [""]
    lines += [f"## Broken links detail ({len(broken)})", ""] + broken_lines + [""]
    lines += [f"## Converted but not on the checklist ({len(extra)})", ""] + extra + [""]
    (CURATED / "status.md").write_text("\n".join(lines), encoding="utf-8")

    total = sum(len(v) for v in groups.values())
    print(f"Checklist: {total} items")
    for name, items in groups.items():
        print(f"  {name:<28} {len(items)}")
    print(f"Converted files: {len(rows)} ({len(extra)} not on checklist)")
    for line in broken_lines:
        print(line)
    print("Wrote manifest.csv and curated/status.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
