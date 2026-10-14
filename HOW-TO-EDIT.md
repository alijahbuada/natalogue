# How to update natalogue

Hi Nat! Everything on your site lives in plain text files in this folder. You can change any of them right here on GitHub, in your browser. No coding, no installing anything.

**The basic move, for every change:**

1. Open the file on github.com.
2. Click the **pencil icon** (top right of the file) to edit.
3. Make your change.
4. Click the green **Commit changes** button, then **Commit changes** again.
5. Wait about a minute, then refresh your site.

If something looks broken after a change, don't worry. Every version is saved, so nothing is ever lost. Text Alijah and it can be rolled back in seconds.

---

## Write a new entry

1. Open the **`templates`** folder and click **`new-entry.md`**.
2. Click the **copy icon** (two overlapping squares, top right) to copy everything in it.
3. Go back to the main page of the repo and open the **`_entries`** folder.
4. Click **Add file → Create new file**.
5. Name the file with lowercase words and dashes, ending in `.md`. For example: `learning-to-rest.md`. The name becomes the web address, like `/entries/learning-to-rest/`.
6. Paste what you copied, then fill it in:
   - `title:` your entry's title
   - `date:` today's date, written year-month-day: `2026-10-20`
   - `summary:` and `listening:` are optional. Delete those lines if you don't want them.
   - Write your entry under the second `---` line.
7. **Commit changes.**

Entries are numbered automatically as rows (row 1, row 2...) in date order.

**Keep the lines between the two `---` marks exactly as they are shaped**: one setting per line, a colon, then a space. If a title has a colon in it, wrap the whole title in quotes: `title: "rows: a beginning"`.

### Formatting cheat sheet

| you type | you get |
| --- | --- |
| a blank line between paragraphs | a new paragraph |
| `*slanted*` | *slanted* |
| `**bold**` | **bold** |
| `## a heading` | a smaller heading in pixel type |
| `- item` | a list |
| `> a quote` | a quote with a pink edge |
| `[words](https://link.com)` | a link |
| `---` on its own line | a crochet-chain divider |

### Edit or delete an entry

Open it in `_entries`, then use the pencil to edit. To delete, click the **three dots (…)** at the top right and choose **Delete file**.

---

## Update your shelves

Open **`_data/shelves.yml`**. There are two lists: `currently` and `favorites`. Each item looks like this:

```yaml
  - title: the name of the thing
    type: book
    by: the author
    progress: page 112
    note: a line in your own words
```

- **type** can be `book`, `show`, `film`, `music`, `game`, `podcast`, or `other`. It picks the little pixel icon.
- Only **title** is required. Delete any other line you don't need.
- **progress** is for things you're in the middle of: "ep 4 of 12", "page 90", "halfway".
- To move something from currently to favorites, cut its lines and paste them under `favorites:`.

The one rule: **spacing matters here.** Each item starts with two spaces, a dash, and a space. The lines under it start with four spaces. Copy an existing item and change the words, and you'll always get it right.

---

## Change your about page

Open **`about.md`**. Write anything you want under the second `---` line. Delete the italic note at the top when you're done.

---

## Add your playlist

1. In Spotify, open your playlist, then **Share → Copy link to playlist**.
2. Open **`_config.yml`** and find the line `playlist_url: ""`.
3. Paste the link between the quotes: `playlist_url: "https://open.spotify.com/playlist/..."`
4. **Commit changes.** It'll show up on the listening page, and it updates itself whenever you add songs in Spotify.

---

## Change your links, tagline, or the lace words

All in **`_config.yml`**. Look for the lines marked `# edit me`.

- **tagline**: the line under the big title on the homepage
- **lace_words**: the words worked into the lace at the bottom of every page
- **links**: your Instagram, Goodreads, and anything else. To add one, copy a block of three lines (`label`, `handle`, `url`) and change them.

---

## Turn on the art gallery

1. Open the folder **`assets/img/gallery`** and click **Add file → Upload files**. Drag in your photos. (JPG or PNG. Square-ish photos look best.)
2. Open **`_data/gallery.yml`**, delete the `[]` line, and add each piece:

```yaml
- image: granny-square-blanket.jpg
  title: granny square blanket
  note: six weeks, two skeins short
  alt: a blue and white blanket draped over a chair
```

   `image` must match the photo's file name exactly, including `.jpg` or `.png`. `alt` describes the photo for people using screen readers.

3. In **`_config.yml`**, change `show_gallery: false` to `show_gallery: true`.

"gallery" will appear in the menu.
