#!/usr/bin/env python3
"""Build dist/faa-md-kit.zip: the scripts plus an empty workspace for another machine.

The kit contains code, templates and a starter checklist only. It never includes
downloaded files, converted output or this machine's status files.
"""
from __future__ import annotations

import csv
import shutil
import sys
import zipfile
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
KIT = DIST / "faa-md-kit"
SCRIPTS = ["common.py", "convert.py", "status.py", "references.py", "next_batch.py"]

SETTINGS = '''"""Per-installation settings. Edit this file, not the scripts."""
from pathlib import Path

ROOT = Path(__file__).parent

# Where things live.
CHECKLIST = ROOT / "curated" / "downloads.md"  # links to download, with [ ]/[x]/[!] boxes
CURATED = ROOT / "curated"                     # status, references, broken links, skip lists
INBOX = ROOT / "inbox"                         # new downloads go here
ARCHIVE = ROOT / "archive"                     # originals, after conversion
OUTPUT = ROOT / "output" / "md"                # converted .md files

# references.py only tracks links whose host ends with one of these.
TRACK_HOSTS = ("faa.gov", "sharepoint.com")

# Hosts this machine can't reach; links to them are reported as "other network".
OTHER_NETWORK_HOSTS = ()
'''

REQUIREMENTS = """beautifulsoup4
markdownify
pymupdf4llm==1.28.2
markitdown[docx,pptx,xlsx]
# Optional, Windows only: lets convert.py read legacy .doc files through Microsoft Word.
# pywin32
"""

GITIGNORE = """.venv/
__pycache__/
inbox/
archive/
output/
curated/status.md
curated/references.*
curated/next_batch.html
"""


def starter_checklist() -> str:
    """Seed the checklist with FAA-network links cited by the public documents converted here."""
    by_host: dict[str, list[tuple[str, str]]] = defaultdict(list)
    refs = ROOT / "curated" / "references.csv"
    if refs.exists():
        with refs.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["kind"] == "link" and r["status"] == "other network":
                    by_host[urlparse(r["ref"]).netloc.lower()].append((r["label"] or r["ref"], r["ref"]))
    lines = [
        "# Download checklist", "",
        "Download each link into `inbox/` (keep the original filename), then run convert.py.",
        "Web pages: open, then click the save-page bookmarklet. status.py ticks the boxes:",
        "[x] converted, [!] broken (see broken_links.txt), [ ] still to download.", "",
        "## Start here", "",
        "- [ ] [Systems Engineering Portal: Policy and Guidance](https://sep.faa.gov/policy_and_guidance/main)",
        "- [ ] [Systems Engineering Portal: home](https://sep.faa.gov/)", "",
        f"## FAA-network links cited by public FAST/faa.gov documents (as of {date.today().isoformat()})", "",
    ]
    for host in sorted(by_host, key=lambda h: (h != "sep.faa.gov", h)):
        lines += [f"### {host}", ""]
        lines += [f"- [ ] [{label}]({url.replace(' ', '%20')})" for label, url in sorted(by_host[host], key=lambda x: x[1])
                  if "sep.faa.gov/policy_and_guidance/main" not in url and url.rstrip("/") != "https://sep.faa.gov"]
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    if KIT.exists():
        shutil.rmtree(KIT)
    (KIT / "curated").mkdir(parents=True)
    for d in ("inbox", "archive", "output/md"):
        (KIT / d).mkdir(parents=True)
        (KIT / d / ".keep").write_text("")

    for s in SCRIPTS:
        shutil.copy2(ROOT / s, KIT / s)
    shutil.copy2(ROOT / "KIT_README.md", KIT / "README.md")
    for name in ("save_page_bookmarklet.txt", "references_skip.txt"):
        shutil.copy2(ROOT / "curated" / name, KIT / "curated" / name)
    (KIT / "settings.py").write_text(SETTINGS, encoding="utf-8")
    (KIT / "requirements.txt").write_text(REQUIREMENTS, encoding="utf-8")
    (KIT / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    (KIT / "curated" / "downloads.md").write_text(starter_checklist(), encoding="utf-8")
    (KIT / "curated" / "broken_links.txt").write_text(
        "# Links that failed to download (404 etc.). One URL per line; text after '#' is a note.\n"
        "# Add one with:  python status.py --broken URL \"note\"\n", encoding="utf-8")
    (KIT / "curated" / "references_ignore.txt").write_text(
        "# Converted documents whose outbound links references.py should not count as\n"
        "# \"untracked\" (link-heavy index pages). One output name (without .md) per line.\n", encoding="utf-8")

    zip_path = DIST / "faa-md-kit.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(KIT.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(DIST))
    print(f"Wrote {zip_path.relative_to(ROOT)} ({zip_path.stat().st_size // 1024} KB)")
    for p in sorted(KIT.rglob("*")):
        if p.is_file() and p.name != ".keep":
            print("  ", p.relative_to(DIST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
