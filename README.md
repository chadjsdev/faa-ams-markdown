# FAA AMS / Systems Engineering → Markdown

Public FAA acquisition and systems engineering documents converted to Markdown
for use as an AI knowledge base (e.g. a Claude Project), plus the scripts that
track and convert them.

All source material is publicly available from fast.faa.gov, faa.gov and
transportation.gov. Every converted file records its `source_url` in its front
matter; check the source for the current version before relying on it.

## What's here

| Path | What |
|---|---|
| `output/fast/` | ~200 converted `.md` files: AMS Policy (full, sections, appendices), FAST lifecycle and Engineering & Management Practices pages, templates and guidance (CRD, ISPD, PMP, PRD, T&E, V&V, ILS, EVM, business cases, SOWs, DIDs), NAS EA roadmaps, CIP, budget justifications, Tech Center, AIT, research plans |
| `output/manifest.csv` | One row per converted file: title, source URL, type, size |
| `curated/fast_downloads.md` | The download checklist: `[x]` converted, `[!]` broken, `[ ]` to do |
| `curated/status.md` | Status report by group |
| `curated/broken_links.txt` | Links that 404'd, with notes and replacements |
| `curated/references.md` / `.csv` | Links and cited orders/standards found inside the documents |
| `dist/faa-md-kit.zip` | Portable copy of the scripts with an empty workspace, for use on another machine |

## Why downloads are manual

- **fast.faa.gov** robots.txt disallows all crawlers (`User-agent: * / Disallow: /`).
- **www.faa.gov** allows crawling, but its CDN returns 403 to self-identified bots.
- **sep.faa.gov** (NAS Systems Engineering Portal, home of the SEM) is FAA-internal.

So documents are downloaded by hand in a browser and the scripts handle
everything after that. `crawl.py` (a polite, robots-respecting crawler for
www.faa.gov) is kept for reference but is blocked in practice.

## Setup

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Legacy `.doc` files use macOS `textutil`, LibreOffice, or Microsoft Word via
pywin32 (Windows), whichever is available.

## The loop

```sh
.venv/bin/python next_batch.py          # click-to-download page of the next 20 checklist items
#   ...download into inbox/...
.venv/bin/python convert.py             # inbox/ -> output/fast/, originals move to archive/
.venv/bin/python status.py              # tick the checklist, write curated/status.md
.venv/bin/python references.py          # what the documents cite that isn't downloaded yet
.venv/bin/python references.py --add 20 # put the top 20 of those on the checklist
.venv/bin/python status.py --broken URL "404"   # record a dead link
```

### Saving web pages

Make a bookmark whose URL is the contents of `curated/save_page_bookmarklet.txt`.
Clicking it on a page downloads `<page-name>.html` with the source URL stamped
inside; on a PDF it downloads the real PDF.

### Converter behavior

- PDF via pymupdf4llm; DOCX/PPTX/XLSX via markitdown; HTML via BeautifulSoup +
  markdownify, extracting the main content (`article`, `main`, FAST's
  `div.mainColumn`) and keeping icon-only download links.
- Source URLs come from matching filenames to checklist links (skipping broken
  ones, so a file from a replacement source gets the working URL), or from the
  bookmarklet's stamp.
- Byte-identical duplicates (even renamed) and near-empty saved pages are
  rejected and left in `inbox/`.

### Reference tracking

`references.py` scans every converted `.md` for links and for cited orders and
standards ("FAA Order 1800.66", "FAA-STD-067"). Each link is marked converted /
on checklist / broken / skipped / ignored source / other network / untracked.

- `curated/references_skip.txt`: URL patterns to ignore (dead folders,
  flowcharts, facilities SOW templates, old CIPs…)
- `curated/references_ignore.txt`: converted pages whose links shouldn't count
  (e.g. REDAC's ~2,000 meeting-minute links)

## Settings and the portable kit

Folder locations and which hosts to track live in `settings.py`.
`make_kit.py` builds `dist/faa-md-kit.zip`: the same scripts with their own
settings, an empty workspace, and a starter checklist of FAA-network links
(sep.faa.gov, employees.faa.gov, …) cited by these public documents. See
`KIT_README.md`, which ships inside the kit as its README.
