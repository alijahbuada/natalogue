"""Regenerates the hand-drawn-in-code SVG includes for Natalogue.

Run from the repo root:  python3 tools/make_svgs.py
Outputs:
  _includes/wordmark.svg   stitched pixel "natalogue" on its foundation chain
  _includes/icons/*.svg    8x8 pixel icons for shelf media types
  _includes/lace.html      lace trim with words worked into it (footer)
Nat never needs to run this; it's here so the art can be tweaked later.
"""
import math
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "_includes")

# ---------------------------------------------------------------- wordmark
GLYPHS = {
    "n": [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#", ".....", "....."],
    "a": [".....", ".....", ".###.", "....#", ".####", "#...#", ".####", ".....", "....."],
    "t": [".#...", ".#...", "####.", ".#...", ".#...", ".#..#", "..##.", ".....", "....."],
    "l": [".##..", "..#..", "..#..", "..#..", "..#..", "..#..", ".###.", ".....", "....."],
    "o": [".....", ".....", ".###.", "#...#", "#...#", "#...#", ".###.", ".....", "....."],
    "g": [".....", ".....", ".####", "#...#", "#...#", ".####", "....#", "....#", ".###."],
    "u": [".....", ".....", "#...#", "#...#", "#...#", "#..##", ".##.#", ".....", "....."],
    "e": [".....", ".....", ".###.", "#...#", "#####", "#....", ".###.", ".....", "....."],
}

CELL = 16          # matches the paper's minor grid
ROWS = 9
CHAIN_ROW = 10     # foundation chain sits one empty row below the letters


def wordmark(word="natalogue"):
    rnd = random.Random(7)
    cols = len(word) * 6 - 1
    w, h = cols * CELL, (CHAIN_ROW + 1) * CELL
    parts = [
        f'<svg class="wordmark" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-labelledby="wm-title" xmlns="http://www.w3.org/2000/svg">',
        '<title id="wm-title">natalogue</title>',
    ]

    # foundation chain: worked first, left to right
    parts.append('<g class="chain" filter="url(#crayon)">')
    cy = CHAIN_ROW * CELL + CELL / 2
    n_chain = cols
    for i in range(n_chain):
        cx = i * CELL + CELL / 2
        rot = rnd.uniform(-6, 6)
        parts.append(
            f'<ellipse class="st" style="--d:{i * 14}ms" cx="{cx:.1f}" cy="{cy:.1f}" '
            f'rx="6.6" ry="3.6" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})"/>'
        )
    parts.append("</g>")
    chain_ms = n_chain * 14 + 120

    # letters: rows worked bottom-up, the way crochet grows from its base
    parts.append('<g class="stitches" filter="url(#crayon)">')
    for li, ch in enumerate(word):
        g = GLYPHS[ch]
        for r in range(ROWS):
            for c in range(5):
                if g[r][c] != "#":
                    continue
                col = li * 6 + c
                x, y = col * CELL, r * CELL
                cx, cy = x + CELL / 2, y + CELL / 2
                delay = chain_ms + (ROWS - 1 - r) * 110 + col * 5
                j = rnd.uniform(-4, 4)
                # one "V" stitch = two tilted loops meeting at the bottom
                parts.append(
                    f'<g class="st" style="--d:{delay}ms">'
                    f'<ellipse cx="{cx - 2.9:.1f}" cy="{cy - 0.6:.1f}" rx="2.7" ry="6.1" '
                    f'transform="rotate({-27 + j:.1f} {cx - 2.9:.1f} {cy - 0.6:.1f})"/>'
                    f'<ellipse cx="{cx + 2.9:.1f}" cy="{cy - 0.6:.1f}" rx="2.7" ry="6.1" '
                    f'transform="rotate({27 + j:.1f} {cx + 2.9:.1f} {cy - 0.6:.1f})"/>'
                    "</g>"
                )
    parts.append("</g></svg>")
    return "".join(parts)


# ---------------------------------------------------------------- icons
ICONS = {
    "book": ["..#####.", ".#....##", ".#.##.##", ".#....##", ".#.##.##", ".#....##", ".######.", "..######"],
    "show": [".#...#..", "..#.#...", "########", "#......#", "#......#", "#......#", "########", ".#....#."],
    "film": ["########", "#.#..#.#", "########", "#......#", "#......#", "########", "#.#..#.#", "########"],
    "music": ["....###.", "....#.##", "....#..#", "....#...", "....#...", "..###...", ".####...", "..##...."],
    "game": ["........", ".######.", "#.#####.", "...###.#", "#.######", "########", ".##..##.", "........"],
    "podcast": ["...##...", "..####..", "..####..", "..####..", "#.####.#", ".#.##.#.", "..####..", "...##..."],
    "other": [".##..##.", "########", "########", "########", ".######.", "..####..", "...##...", "........"],
}


def icon(rows):
    rects = []
    for y, row in enumerate(rows):
        x = 0
        while x < 8:
            if row[x] == "#":
                start = x
                while x < 8 and row[x] == "#":
                    x += 1
                rects.append(f'<rect x="{start}" y="{y}" width="{x - start}" height="1"/>')
            else:
                x += 1
    return (
        '<svg class="px-icon" viewBox="0 0 8 8" aria-hidden="true" '
        'shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">'
        + "".join(rects)
        + "</svg>"
    )


# ---------------------------------------------------------------- lace
def lace():
    W, H, S = 2400, 88, 64          # width, height, scallop width
    band = 44                        # depth of the straight ribbon part
    r = S / 2
    # straight ribbon, then a row of round scallops along the bottom
    d = [f"M0 0 H{W} V{band}"]
    x = W
    while x > 0:
        d.append(f"A{r} {r} 0 0 1 {x - S} {band}")
        x -= S
    d.append("Z")
    edge = " ".join(d)
    eyelets = "".join(f'<circle cx="{i * 16 + 8}" cy="10" r="3"/>' for i in range(W // 16))
    scallop_holes = []
    for i in range(W // S):
        cx = i * S + r
        scallop_holes.append(f'<circle cx="{cx}" cy="{band + 13}" r="4.5"/>')
        scallop_holes.append(f'<circle cx="{cx - 14}" cy="{band + 6}" r="2"/>')
        scallop_holes.append(f'<circle cx="{cx + 14}" cy="{band + 6}" r="2"/>')
    picots = "".join(
        f'<circle class="picot" cx="{i * S}" cy="{band + 4}" r="2.6"/>' for i in range(1, W // S)
    )
    return (
        '<div class="lace" aria-hidden="true">'
        f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMinYMin slice" '
        'xmlns="http://www.w3.org/2000/svg">'
        f'<path class="lace-body" d="{edge}"/>'
        f'<path class="lace-rule" d="M0 19.5 H{W} M0 40.5 H{W}"/>'
        f'<g class="lace-holes">{eyelets}{"".join(scallop_holes)}</g>'
        f'<g class="lace-picots">{picots}</g>'
        '<text class="lace-words" x="10" y="34">'
        "{% for i in (1..14) %}{{ site.data.settings.lace_words }} &#10047; {% endfor %}"
        "</text>"
        "</svg></div>\n"
    )


def main():
    os.makedirs(os.path.join(INC, "icons"), exist_ok=True)
    with open(os.path.join(INC, "wordmark.svg"), "w") as f:
        f.write(wordmark() + "\n")
    for name, rows in ICONS.items():
        with open(os.path.join(INC, "icons", f"{name}.svg"), "w") as f:
            f.write(icon(rows) + "\n")
    with open(os.path.join(INC, "lace.html"), "w") as f:
        f.write(lace())
    print("wrote wordmark, icons, lace")


if __name__ == "__main__":
    main()
