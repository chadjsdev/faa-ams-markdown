#!/usr/bin/env python3
"""Make a click-to-download page of the next outstanding checklist items.

Reads unchecked ([ ]) items from the checklist (run status.py first so
converted/broken items are ticked), writes curated/next_batch.html, opens it in
the default browser and prints the same links.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import webbrowser

from common import DOC_EXTS
from settings import CHECKLIST, CURATED, INBOX


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-n", type=int, default=20, help="how many items (default 20)")
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args()

    items = re.findall(r"^- \[ \] \[([^\]]+)\]\((https?://[^)\s]+)\)",
                       CHECKLIST.read_text(encoding="utf-8"), re.M)[: args.n]
    if not items:
        print("Nothing outstanding on the checklist.")
        return 0

    rows = []
    for i, (label, url) in enumerate(items, 1):
        page = not url.lower().split("?")[0].endswith(DOC_EXTS)
        hint = ' <span class="hint">web page: use the bookmarklet (or Save As if it shows a PDF)</span>' if page else ""
        rows.append(f'<li><label><input type="checkbox"> <a href="{html.escape(url)}">{html.escape(label)}</a></label>{hint}</li>')
        print(f"{i:2d}. {label}: {url}")

    out = CURATED / "next_batch.html"
    out.write_text(f"""<!doctype html><html><head><meta charset="utf-8"><title>Next downloads</title>
<style>body{{font:16px system-ui,sans-serif;max-width:780px;margin:2rem auto;padding:0 16px;line-height:1.7}}
a{{color:#0645ad}} input:checked+a{{color:#888;text-decoration:line-through}} p,.hint{{color:#666}} .hint{{font-size:13px;margin-left:.4em}}</style>
</head><body><h1>Next {len(items)} downloads</h1>
<p>Save everything to <code>{html.escape(str(INBOX))}</code> with the original filenames, then run convert.</p>
<ol>{''.join(rows)}</ol></body></html>""", encoding="utf-8")
    if not args.no_open:
        webbrowser.open(out.resolve().as_uri())
    return 0


if __name__ == "__main__":
    sys.exit(main())
