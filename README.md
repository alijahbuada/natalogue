# natalogue

Nat's site: entries, shelves, a playlist, links, and a gallery that stays hidden until she has photos. Built with Jekyll for GitHub Pages, with no plugins or build step, so GitHub builds it on every commit.

**Nat, start here → [HOW-TO-EDIT.md](HOW-TO-EDIT.md)**

## Going live

1. Create a GitHub repo and upload everything in this folder.
   - If the repo is named `<username>.github.io`, the site lives at `https://<username>.github.io`.
   - Any other name (like `natalogue`) lives at `https://<username>.github.io/natalogue`. In that case, set `baseurl: /natalogue` in `_config.yml`.
2. Repo **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main` / `(root)`.
3. Set `url:` in `_config.yml` to the live address.
4. Add Nat as a collaborator (**Settings → Collaborators**) so she can edit, or transfer the repo to her account.
5. Check the Goodreads link in `_config.yml` resolves to her profile. If the short `goodreads.com/natalihn` form doesn't work, use the full profile URL.

## What's where

| path | what it is |
| --- | --- |
| `_config.yml` | site name, tagline, lace words, playlist link, gallery switch, links |
| `_entries/` | one Markdown file per entry; numbered as rows by date |
| `_data/shelves.yml` | currently consuming + favorites |
| `_data/gallery.yml` | gallery pieces (images go in `assets/img/gallery/`) |
| `_data/nav.yml` | menu order |
| `about.md` | about page |
| `templates/new-entry.md` | copy-paste starter for entries (excluded from the site) |
| `assets/css/style.css` | all styling |
| `_includes/wordmark.svg`, `lace.html`, `icons/` | generated art; regenerate with `python3 tools/make_svgs.py` |

## Design notes

- Everything sits on a 16px engineering-paper grid (heavier line every 5 squares). Body text runs on 32px lines, two squares per line, and the page column snaps its left edge to the grid.
- The wordmark is pixel type made of crochet "V" stitches, sitting on a pink foundation chain. On the homepage it's worked in once on load: chain first, then rows from the bottom up. Reduced-motion users see it finished.
- Crayon/oil-pastel grain is an SVG filter (`_includes/textures.svg`), used on the wordmark and the active menu scribble.
- The footer trim is lace with `lace_words` worked into the ribbon.
- Fonts: Pixelify Sans (headings, menu) and Newsreader (reading text), from Google Fonts.

## Preview locally (optional)

```
bundle install
bundle exec jekyll serve
```
