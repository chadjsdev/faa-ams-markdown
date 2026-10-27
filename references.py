#!/usr/bin/env python3
"""Track every reference inside the converted documents.

Scans the converted .md files (so it covers PDFs, Word files and web pages alike) for:
  - links (unwrapping FAST's "_leaving.cfm?uri=" redirects)
  - cited documents without links: FAA/JO/NG orders, FAA-STD/-HDBK standards,
    advisory circulars

Each link gets a status: converted / on checklist / broken / skipped (matches
curated/references_skip.txt) / ignored source (only cited by pages listed in
curated/references_ignore.txt) / other network / untracked. Writes
curated/references.csv (everything) and curated/references.md (summary:
untracked links ranked by how often they're cited, plus cited orders and
standards). Reads local files only.

    references.py                     # report
    references.py --add 20            # also append the top 20 untracked links to the checklist
    references.py --add 20 --match sep.faa.gov   # ...only those whose URL/label matches a regex
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from common import norm, read_front_matter
from settings import CHECKLIST, CURATED, OTHER_NETWORK_HOSTS, OUTPUT as OUT, TRACK_HOSTS
from status import broken_links, checklist

IGNORE = CURATED / "references_ignore.txt"
SKIP_FILE = CURATED / "references_skip.txt"
NOISE = ("/changerequest/", "/images/", "/css/", "/javascript/")
CITATION = re.compile(
    r"\b(?:(?:FAA|JO|NG)\s+)?(?:Order\s+)?(?:JO\s+)?\d{4}\.\d{1,3}[A-Z]?\b(?=[^.\w]|$)"
    r"|\bFAA-(?:STD|HDBK|E)-\d{3}[A-Z]?\b"
    r"|\bAC\s+\d{2,3}-\d{1,3}[A-Z]?\b"
)
STATUSES = ("untracked", "on checklist", "broken", "other network", "in full AMS",
            "converted", "skipped", "ignored source")


def unwrap(url: str) -> str:
    p = urlparse(url)
    if p.path.lower().endswith("_leaving.cfm"):
        uri = parse_qs(p.query).get("uri")
        if uri:
            return unquote(uri[0])
    return url


def clean(url: str) -> str:
    url = unwrap(url.replace("\\_", "_")).split("#")[0].rstrip(".,;:")
    # Drop FAST's cosmetic ?p_title=... so page links compare equal.
    return re.sub(r"\?p_title=.*$", "", url)


def read_list(path: Path) -> list[str]:
    """Non-empty lines with '#' comments removed."""
    if not path.exists():
        return []
    return [l.split("#")[0].strip() for l in path.read_text(encoding="utf-8").splitlines()
            if l.split("#")[0].strip()]


def tracked_host(host: str) -> bool:
    return any(host == h or host.endswith("." + h) for h in TRACK_HOSTS)


def other_network(host: str) -> bool:
    return any(host == h or host.endswith("." + h) for h in OTHER_NETWORK_HOSTS)


def add_to_checklist(rows: list[dict], n: int, match: str | None) -> int:
    pattern = re.compile(match, re.I) if match else None
    picks = [r for r in rows if r["kind"] == "link" and r["status"] == "untracked"
             and (not pattern or pattern.search(r["ref"] + " " + r["label"]))][:n]
    if not picks:
        return 0
    lines = [f"## Added from references.py ({date.today().isoformat()})", ""]
    for r in picks:
        label = r["label"] or Path(unquote(urlparse(r["ref"]).path)).name or r["ref"]
        url = r["ref"].replace(" ", "%20").replace("(", "%28").replace(")", "%29")
        lines.append(f"- [ ] [{label}]({url})")
    with CHECKLIST.open("a", encoding="utf-8") as f:
        f.write("\n" + "\n".join(lines) + "\n")
    return len(picks)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--add", type=int, metavar="N", help="append the top N untracked links to the checklist")
    ap.add_argument("--match", metavar="REGEX", help="with --add: only links whose URL or label matches")
    args = ap.parse_args()

    converted = {norm(u) for md in OUT.glob("*.md") if (u := read_front_matter(md).get("source_url"))}
    on_list = {norm(u) for _, _, u in checklist()}
    broken = {norm(u) for u in broken_links()}
    ignore = set(read_list(IGNORE))
    skip = [re.compile(p, re.I) for p in read_list(SKIP_FILE)]

    links: dict[str, dict] = {}
    cites: dict[str, set[str]] = defaultdict(set)
    names: dict[str, Counter] = defaultdict(Counter)
    for md in sorted(OUT.glob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace").split("\n---\n", 1)[-1]
        labelled = dict((u, l) for l, u in re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)", text))
        for raw in set(re.findall(r"https?://[^\s)\]\"'<>|]+", text)):
            url = clean(raw)
            host = urlparse(url).netloc.lower()
            if not tracked_host(host) or any(s in url.lower() for s in NOISE) \
                    or urlparse(url).path in ("", "/"):
                continue
            e = links.setdefault(norm(url), {"url": url, "label": "", "found_in": set()})
            label = re.sub(r"</?u>|\*+|(?<!\w)_+|_+(?!\w)", "", labelled.get(raw, ""))
            e["label"] = e["label"] or re.sub(r"\s+", " ", label).strip()
            e["found_in"].add(md.stem)
        for c in CITATION.findall(text):
            if re.fullmatch(r"\d{4}\.\d+[A-Z]?", c):  # bare numbers like 2024.10 are too noisy
                continue
            # Group spellings of the same document ("Order 1800.66" == "FAA Order 1800.66").
            m = re.search(r"\d{4}\.\d{1,3}[A-Z]?|FAA-\w+-\d{3}[A-Z]?|AC\s+\d{2,3}-\d{1,3}[A-Z]?", c)
            key = re.sub(r"\s+", " ", m.group(0))
            cites[key].add(md.stem)
            names[key][re.sub(r"\s+", " ", c.strip())] += 1

    def status(key: str, e: dict) -> str:
        if key in converted:
            return "converted"
        if key in broken:
            return "broken"
        if key in on_list:
            return "on checklist"
        if any(p.search(e["url"]) for p in skip):
            return "skipped"
        if e["found_in"] <= ignore:
            return "ignored source"
        if re.search(r"acquisitionmanagementpolicy\d", key):
            return "in full AMS"
        if other_network(urlparse(e["url"]).netloc.lower()):
            return "other network"
        return "untracked"

    rows = []
    for key, e in links.items():
        rows.append({"kind": "link", "ref": e["url"], "label": e["label"], "status": status(key, e),
                     "count": len(e["found_in"]), "found_in": "; ".join(sorted(e["found_in"]))})
    for c, files in cites.items():
        rows.append({"kind": "citation", "ref": names[c].most_common(1)[0][0], "label": "", "status": "cited",
                     "count": len(files), "found_in": "; ".join(sorted(files))})
    rows.sort(key=lambda r: (r["kind"], r["status"], -r["count"], r["ref"]))

    if args.add:
        added = add_to_checklist(rows, args.add, args.match)
        print(f"Added {added} links to {CHECKLIST.name}")
        for r in rows:  # reflect the additions in this report
            if r["status"] == "untracked" and norm(r["ref"]) in {norm(u) for _, _, u in checklist()}:
                r["status"] = "on checklist"

    with (CURATED / "references.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, ["kind", "ref", "label", "status", "count", "found_in"])
        w.writeheader()
        w.writerows(rows)

    by_status = defaultdict(list)
    for r in rows:
        by_status[r["status"]].append(r)
    lines = ["# References found in converted documents", "",
             "Generated by `references.py`. Full data: `curated/references.csv`.", ""]
    lines += [f"- {s}: {len(by_status[s])} links" for s in STATUSES]
    lines += [f"- cited orders/standards: {len(by_status['cited'])}", ""]
    lines += ["## Untracked links (most-cited first)", ""]
    for r in by_status["untracked"]:
        label = r["label"] or Path(urlparse(r["ref"]).path).name or r["ref"]
        lines.append(f"- [ ] [{label}]({r['ref']}) — cited by {r['count']}: {r['found_in'][:150]}")
    lines += ["", "## Other-network links (most-cited first)", ""]
    for r in by_status["other network"]:
        lines.append(f"- [{r['label'] or r['ref']}]({r['ref']}) — cited by {r['count']}: {r['found_in'][:150]}")
    lines += ["", "## Cited orders & standards (most-cited first)", ""]
    for r in sorted(by_status["cited"], key=lambda r: -r["count"]):
        lines.append(f"- {r['ref']} — cited by {r['count']}: {r['found_in'][:150]}")
    (CURATED / "references.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for s in STATUSES + ("cited",):
        print(f"  {s:<15} {len(by_status[s])}")
    print("Wrote curated/references.csv and curated/references.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
