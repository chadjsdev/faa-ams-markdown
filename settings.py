"""Per-installation settings. Edit this file, not the scripts."""
from pathlib import Path

ROOT = Path(__file__).parent

# Where things live.
CHECKLIST = ROOT / "curated" / "fast_downloads.md"  # links to download, with [ ]/[x]/[!] boxes
CURATED = ROOT / "curated"                           # status, references, broken links, skip lists
INBOX = ROOT / "inbox"                               # new downloads go here
ARCHIVE = ROOT / "archive"                           # originals, after conversion
OUTPUT = ROOT / "output" / "fast"                    # converted .md files (upload these)

# references.py only tracks links whose host ends with one of these.
TRACK_HOSTS = ("faa.gov",)

# Hosts this machine can't reach (e.g. FAA-internal sites from a personal laptop).
# Links to them are reported as "other network" instead of "untracked".
OTHER_NETWORK_HOSTS = (
    "sep.faa.gov", "ksn2.faa.gov", "my.faa.gov", "employees.faa.gov", "tableau.faa.gov",
    "nasea.faa.gov", "technet.faa.gov", "nas.amc.faa.gov", "sharepoint.com",
)

# How you save web pages: "bookmarklet" (one click; needs javascript: bookmarks allowed)
# or "save-as" (Ctrl+S -> Webpage, Complete; works where bookmarklets are blocked).
# Only changes the hint shown by next_batch.py.
SAVE_PAGE_METHOD = "bookmarklet"
