"""Build all fonts, then assemble the release folder + zip."""
import os, shutil, base64, json, unicodedata
import gui, shapes, objects, preview
from dt import build, export_svgs

V = "1.000"
DIST = f"dist/DingThats-{V}"
shutil.rmtree("dist", ignore_errors=True)
FAMS = [("gui", "DingThats GUI", "DingThatsGUI", gui.gs, True),
        ("shapes", "DingThats Shapes", "DingThatsShapes", shapes.gs, False),
        ("objects", "DingThats Objects", "DingThatsObjects", objects.gs, False)]

OFL = open("OFL_body.txt").read()


def uname(cp):
    try:
        return unicodedata.name(chr(cp)).title()
    except ValueError:
        return "Private Use" if 0xE000 <= cp <= 0xF8FF else ""


readme = [f"# DingThats fonts v{V}\n",
          "Three free, open-source dingbat fonts from [dingthat.com](https://dingthat.com).\n",
          "| Font | What's in it | Glyphs |", "|---|---|---|"]
data = {}
for slug, fam, ps, gs, mono in FAMS:
    out = build(gs, fam, ps, f"{DIST}/fonts/{slug}", mono=mono, version=V)
    export_svgs(gs, f"{DIST}/svg/{slug}")
    os.makedirs(f"{DIST}/specimens", exist_ok=True)
    preview.specimen(gs, out["ttf"], f"{DIST}/specimens/{ps}-specimen.png", fam)
    data[slug] = dict(family=fam, ps=ps, mono=mono,
                      woff2=base64.b64encode(open(out["woff2"], "rb").read()).decode(),
                      glyphs=[dict(n=g["name"], k=g["keys"], u=g["unis"], l=g["label"]) for g in gs.glyphs])
desc = {"gui": "Box drawing (single, double, mixed, rounded), shade blocks, classic PC symbols, GUI widgets. Monospaced; box characters tile seamlessly.",
        "shapes": "Arrows, triangles, squares, circles, stars, checks, crosses, media controls and UI symbols.",
        "objects": "Buildings, vehicles and transport, office and everyday objects, weather."}
for slug, fam, ps, gs, mono in FAMS:
    readme.append(f"| **{fam}** | {desc[slug]} | {len(gs.glyphs)} |")
readme += ["", "## How to type them", "",
           "Every glyph sits on a keyboard key (shown below), and where a matching Unicode symbol exists it is *also* mapped there, "
           "so text like `┌──┐`, `★`, `✈` renders correctly too. Glyphs without a standard code point live in the Private Use Area.", "",
           "**GUI:** box drawing is laid out as a 3×3 grid on the keyboard — `q w e / a s d / z x c` is single line "
           "`┌┬┐ / ├┼┤ / └┴┘`, `r` = `─`, `f` = `│`. Shift gives the double-line set. `t y u / g h j / b n m` (and shifted) are the "
           "mixed single/double sets, `i o / k l` are rounded corners.", "",
           "**Shapes:** heavy arrows follow the numeric keypad (`8` up, `2` down, `4` left, `6` right, `7 9 1 3` diagonals).", "",
           "## Files", "",
           "- `fonts/<family>/*.otf` – desktop (CFF outlines)",
           "- `fonts/<family>/*.ttf` – desktop / apps (TrueType outlines)",
           "- `fonts/<family>/*.woff2` – web",
           "- `svg/<family>/*.svg` – every glyph as a standalone SVG",
           "- `specimens/*.png` – glyph charts", "- `specimen.html` – interactive specimen + type tester (open in a browser)",
           "- `source/` – the Python that draws and compiles everything (`python3 package.py`, needs `fonttools skia-pathops brotli pillow`)", "",
           "## Web use", "", "```css",
           "@font-face { font-family: 'DingThats Objects'; src: url('DingThatsObjects-Regular.woff2') format('woff2'); }",
           ".icon { font-family: 'DingThats Objects'; }", "```", "",
           "```html", "<span class=\"icon\">h</span> Home  <span class=\"icon\">e</span> Contact", "```", "",
           "For accessibility, add `aria-hidden=\"true\"` to decorative icons and give meaningful ones an `aria-label`.", "",
           "## License", "",
           "Copyright 2026 The DingThats Project Authors (https://dingthat.com). "
           "Licensed under the SIL Open Font License 1.1 — see `OFL.txt`. Free to use, embed, modify and redistribute; "
           "the fonts may not be sold on their own.", ""]
for slug, fam, ps, gs, mono in FAMS:
    readme += [f"## {fam} — character map", "", "| Key | Glyph | Also mapped to |", "|---|---|---|"]
    for g in gs.glyphs:
        k = g["keys"]
        kk = "`" + k.replace("|", "\\|").replace("`", "\\`") + "`" if k else "—"
        if k == "`":
            kk = "`` ` ``"
        extra = ", ".join(f"U+{u:04X} {uname(u)}" for u in g["unis"][len(k):])
        readme.append(f"| {kk} | {g['label']} | {extra} |")
    readme.append("")

open(f"{DIST}/README.md", "w").write("\n".join(readme))
open(f"{DIST}/OFL.txt", "w").write(
    "Copyright 2026 The DingThats Project Authors (https://dingthat.com)\n\n" + OFL)
os.makedirs(f"{DIST}/source", exist_ok=True)
for f in ("dt.py", "gui.py", "shapes.py", "objects.py", "preview.py", "package.py", "OFL_body.txt", "specimen_template.html"):
    shutil.copy(f, f"{DIST}/source/")
json.dump(data, open("build/data.json", "w"))
# standalone specimen (fonts embedded so it works by double-clicking)
tpl = open("specimen_template.html").read()
open(f"{DIST}/specimen.html", "w").write(
    "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
    + tpl.replace("/*DATA*/null", json.dumps(data)) + "</html>")
shutil.make_archive(DIST, "zip", "dist", f"DingThats-{V}")
print("ok", DIST)
