"""Render a specimen grid PNG from a built TTF + glyph list."""
from PIL import Image, ImageDraw, ImageFont

LBL = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def specimen(gs, ttf, out, title, cols=12, cell=110, size=64):
    rows = (len(gs.glyphs) + cols - 1) // cols
    W, H = cols * cell + 40, rows * cell + 90
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(ttf, size)
    try:
        lf = ImageFont.truetype(LBL, 13); tf = ImageFont.truetype(LBL, 24)
    except OSError:
        lf = tf = ImageFont.load_default()
    d.text((20, 20), title, fill="black", font=tf)
    for i, g in enumerate(gs.glyphs):
        x = 20 + (i % cols) * cell
        y = 70 + (i // cols) * cell
        d.rectangle([x, y, x + cell - 6, y + cell - 6], outline="#ddd")
        ch = chr(g["unis"][0])
        d.text((x + (cell - 6) / 2, y + 48), ch, font=f, fill="black", anchor="mm")
        key = g["keys"] or "U+%04X" % g["unis"][0]
        if key == " ":
            key = "space"
        d.text((x + 4, y + cell - 24), key + "  " + g["label"][:11], font=lf, fill="#c33")
    im.save(out)
    return out


def tile_test(ttf, out, lines, size=48):
    """Render lines of text to check box-drawing tiling."""
    f = ImageFont.truetype(ttf, size)
    W = max(len(l) for l in lines) * int(size * 0.6) + 40
    H = len(lines) * size + 40
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        d.text((20, 20 + i * size), l, font=f, fill="black")
    im.save(out)
