# FAA docs → Markdown kit

Turns documents you download (PDF, Word, PowerPoint, Excel, saved web pages)
into `.md` files, and keeps track of what you've downloaded, what's broken, and
what the documents reference that you don't have yet.

Nothing here crawls or logs in to anything. You download in your own browser,
with your own session; the scripts only read files on disk.

**Before you start:** follow your organization's rules for running scripts on
your machine, and for where the converted files may go. Internal documents
often carry handling markings (CUI, SSI, "FAA only"); converted text keeps the
content but not the markings. Don't move output off the network unless you're
authorized to.

## Setup (Windows)

```bat
cd faa-md-kit
py -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

macOS/Linux: `python3 -m venv .venv` and `.venv/bin/pip install -r requirements.txt`.

If `pip install` is blocked, ask IT for the four packages in `requirements.txt`.
Missing packages only disable their file type: no `pymupdf4llm` means PDFs fail
and stay in `inbox/`, while everything else still converts.

Legacy `.doc` files need one of: LibreOffice, or Microsoft Word plus
`pip install pywin32`. Otherwise, open the file in Word, Save As `.docx`, and
drop that in `inbox/`.

## Saving web pages

`curated/save_page_bookmarklet.txt` is **not a script you run**. It's one line of
JavaScript to paste as the URL of a browser bookmark. Open it in Notepad, copy
the whole line, then in Chrome press Ctrl+Shift+O → ⋮ → Add new bookmark, name
it "Save for FAA" and paste the line as the URL. On any page, click the
bookmark: a green banner says what it saved, a red one says what failed, and the
file lands in your Downloads folder.

- It saves the page as rendered, so SharePoint and other script-built pages keep
  their content, and it stamps the source URL inside the file.
- **Managed browsers often block `javascript:` bookmarks.** If clicking does
  nothing at all (no banner), check `chrome://policy` for `URLBlocklist` or
  `JavaScriptBlockedForUrls`. If it's blocked, use Ctrl+S instead.

**Ctrl+S route (works without JavaScript):** press Ctrl+S, set "Save as type" to
**Webpage, Complete** (not "HTML only", which saves the page before its scripts
run and comes out empty on SharePoint-style pages), and save into `inbox\`.
Chrome also creates a `<page name>_files` folder; `convert.py` ignores those
folders. Source URLs: the bookmarklet stamps the URL into the file; a Ctrl+S
file has no stamp, so `convert.py` falls back to the page's own canonical link.
If it prints `(no source URL match)`, the file is already converted and
archived without a URL. To fix it, add this as the first line of the saved
`.html`: `<!-- saved from url=(0000)https://the/page/url -->`, then run
`convert.py --force` (the number in parentheses is ignored).
Last resort for stubborn pages: Ctrl+P → Save as PDF (no source URL; the
checklist matches it by filename if you name it like the link).

## The loop

```bat
.venv\Scripts\python next_batch.py        :: opens a click-to-download page of the next 20 links
   (download into inbox\)
.venv\Scripts\python convert.py           :: inbox\ -> output\md\, originals move to archive\
.venv\Scripts\python status.py            :: ticks the checklist, writes curated\status.md
.venv\Scripts\python references.py        :: what the converted docs cite that you don't have
.venv\Scripts\python references.py --add 20   :: put the top 20 of those on the checklist
```

A link that 404s:

```bat
.venv\Scripts\python status.py --broken https://example.faa.gov/doc.pdf "404"
```

`status.py` then lists which converted documents still point to it.

## Files

| Path | What |
|---|---|
| `curated/downloads.md` | The checklist. Seeded with FAA-network links that public FAST/faa.gov documents cite. Add your own `- [ ] [label](url)` lines anywhere. |
| `curated/status.md` | Converted / downloaded / broken / still to download |
| `curated/references.md` / `.csv` | Links and cited orders/standards found inside converted docs |
| `curated/broken_links.txt` | Links that didn't work |
| `curated/references_skip.txt` | URL patterns to ignore (dead folders, low-value link families) |
| `curated/references_ignore.txt` | Converted pages whose links shouldn't count (big index pages) |
| `output/manifest.csv` | One row per converted file: title, source URL, type, size |
| `settings.py` | Folder locations and which hosts to track |

## Tips

- If a saved page converts as "nearly empty", it was a PDF viewer or a page
  that's just a wrapper for one file. Download the file it points to instead.
- Duplicates (same bytes, even renamed) are detected and left in `inbox/`.
- `convert.py --force` re-converts everything after you change the converter.
