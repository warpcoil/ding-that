"""DingThats GUI — box drawing, blocks, classic PC symbols and GUI widgets (monospace)."""
from dt import *

W = 600                 # advance (monospace)
CX, CY = 300, 300       # cell centre
X0, X1, Y0, Y1 = 0, 600, -200, 800
LW = 70                 # single line weight
DO, DW = 80, 50         # double line offset / weight
gs = GlyphSet(W)


# ------------------------------------------------------------ box drawing
def arm(d, ext, half):
    if d == "r": return box(CX - ext, CY - half, X1, CY + half)
    if d == "l": return box(X0, CY - half, CX + ext, CY + half)
    if d == "u": return box(CX - half, CY - ext, CX + half, Y1)
    if d == "d": return box(CX - half, Y0, CX + half, CY + ext)


PERP = {"r": "ud", "l": "ud", "u": "lr", "d": "lr"}
OPP = {"r": "l", "l": "r", "u": "d", "d": "u"}


def boxchar(u=0, d=0, l=0, r=0):
    a = dict(u=u, d=d, l=l, r=r)
    thick, thin, single = S(), S(), S()
    for k, v in a.items():
        perps = [a[p] for p in PERP[k]]
        if v == 2:
            if 2 in perps:
                thick += arm(k, DO + DW / 2, DO + DW / 2)
                thin += arm(k, DO - DW / 2, DO - DW / 2)
            else:
                thick += arm(k, LW / 2, DO + DW / 2)
                thin += arm(k, 400, DO - DW / 2)
        elif v == 1:
            if a[OPP[k]]:
                ext = LW / 2
            elif perps.count(2) == 2:
                ext = -(DO - DW / 2)
            elif 2 in perps:
                ext = DO + DW / 2
            else:
                ext = LW / 2
            single += arm(k, ext, LW / 2)
    return (thick - thin) + single


BOX = [
    # key, unicode, u d l r, label
    ("q", 0x250C, (0, 1, 0, 1), "corner tl"), ("w", 0x252C, (0, 1, 1, 1), "tee down"),
    ("e", 0x2510, (0, 1, 1, 0), "corner tr"), ("a", 0x251C, (1, 1, 0, 1), "tee right"),
    ("s", 0x253C, (1, 1, 1, 1), "cross"), ("d", 0x2524, (1, 1, 1, 0), "tee left"),
    ("z", 0x2514, (1, 0, 0, 1), "corner bl"), ("x", 0x2534, (1, 0, 1, 1), "tee up"),
    ("c", 0x2518, (1, 0, 1, 0), "corner br"), ("r", 0x2500, (0, 0, 1, 1), "horizontal"),
    ("f", 0x2502, (1, 1, 0, 0), "vertical"),
    ("Q", 0x2554, (0, 2, 0, 2), "dbl tl"), ("W", 0x2566, (0, 2, 2, 2), "dbl tee dn"),
    ("E", 0x2557, (0, 2, 2, 0), "dbl tr"), ("A", 0x2560, (2, 2, 0, 2), "dbl tee rt"),
    ("S", 0x256C, (2, 2, 2, 2), "dbl cross"), ("D", 0x2563, (2, 2, 2, 0), "dbl tee lt"),
    ("Z", 0x255A, (2, 0, 0, 2), "dbl bl"), ("X", 0x2569, (2, 0, 2, 2), "dbl tee up"),
    ("C", 0x255D, (2, 0, 2, 0), "dbl br"), ("R", 0x2550, (0, 0, 2, 2), "dbl horiz"),
    ("F", 0x2551, (2, 2, 0, 0), "dbl vert"),
    # double horizontal / single vertical
    ("t", 0x2552, (0, 1, 0, 2), "mix tl"), ("y", 0x2564, (0, 1, 2, 2), "mix tee dn"),
    ("u", 0x2555, (0, 1, 2, 0), "mix tr"), ("g", 0x255E, (1, 1, 0, 2), "mix tee rt"),
    ("h", 0x256A, (1, 1, 2, 2), "mix cross"), ("j", 0x2561, (1, 1, 2, 0), "mix tee lt"),
    ("b", 0x2558, (1, 0, 0, 2), "mix bl"), ("n", 0x2567, (1, 0, 2, 2), "mix tee up"),
    ("m", 0x255B, (1, 0, 2, 0), "mix br"),
    # single horizontal / double vertical
    ("T", 0x2553, (0, 2, 0, 1), "mix2 tl"), ("Y", 0x2565, (0, 2, 1, 1), "mix2 tee dn"),
    ("U", 0x2556, (0, 2, 1, 0), "mix2 tr"), ("G", 0x255F, (2, 2, 0, 1), "mix2 tee rt"),
    ("H", 0x256B, (2, 2, 1, 1), "mix2 cross"), ("J", 0x2562, (2, 2, 1, 0), "mix2 tee lt"),
    ("B", 0x2559, (2, 0, 0, 1), "mix2 bl"), ("N", 0x2568, (2, 0, 1, 1), "mix2 tee up"),
    ("M", 0x255C, (2, 0, 1, 0), "mix2 br"),
]
for key, uni, (u, d, l, r), lab in BOX:
    gs.add("box" + "%04X" % uni, key, [uni], boxchar(u, d, l, r), lab)


def rounded(sx, sy):
    """sx,sy = direction of the two arms: (+1,-1) means right & down (╭)."""
    R = 160
    ccx, ccy = CX + sx * R, CY + sy * R
    lo, hi = {(1, -1): (90, 180), (-1, -1): (0, 90), (1, 1): (180, 270), (-1, 1): (270, 360)}[(sx, sy)]
    s = arc(ccx, ccy, R, LW, lo, hi)
    s += box(ccx, CY - LW / 2, X1 if sx > 0 else X0, CY + LW / 2)
    s += box(CX - LW / 2, ccy, CX + LW / 2, Y1 if sy > 0 else Y0)
    return s


gs.add("arcTL", "i", [0x256D], rounded(1, -1), "round tl")
gs.add("arcTR", "o", [0x256E], rounded(-1, -1), "round tr")
gs.add("arcBL", "k", [0x2570], rounded(1, 1), "round bl")
gs.add("arcBR", "l", [0x256F], rounded(-1, 1), "round br")

# ------------------------------------------------------------ blocks
def pattern(pred, n=100):
    s = S()
    for i in range(W // n):
        for j in range(1000 // n):
            if pred(i, j):
                s += rect(i * n, Y0 + j * n, n, n)
    return s


FULL = box(X0, Y0, X1, Y1)
gs.add("shadeLight", "1", [0x2591], pattern(lambda i, j: i % 2 == 0 and j % 2 == 0), "shade light")
gs.add("shadeMedium", "2", [0x2592], pattern(lambda i, j: (i + j) % 2 == 0), "shade medium")
gs.add("shadeDark", "3", [0x2593], FULL - pattern(lambda i, j: i % 2 == 1 and j % 2 == 1), "shade dark")
gs.add("blockFull", "4", [0x2588], FULL, "full block")
gs.add("blockUpper", "5", [0x2580], box(X0, CY, X1, Y1), "upper half")
gs.add("blockLower", "6", [0x2584], box(X0, Y0, X1, CY), "lower half")
gs.add("blockLeft", "7", [0x258C], box(X0, Y0, CX, Y1), "left half")
gs.add("blockRight", "8", [0x2590], box(CX, Y0, X1, Y1), "right half")
gs.add("squareBlack", "9", [0x25A0], rect(CX - 170, CY - 170, 340, 340), "square")
gs.add("squareWhite", "0", [0x25A1], rect(CX - 170, CY - 170, 340, 340) - rect(CX - 120, CY - 120, 240, 240), "square white")
gs.add("squareSmall", "?", [0x25AA], rect(CX - 100, CY - 100, 200, 200), "small square")
gs.add("rectBlack", "", [0x25AC], rect(CX - 260, CY - 80, 520, 160), "black rect")

# ------------------------------------------------------------ classic PC symbols
def face(inv=False):
    eyes = circ(CX - 85, CY + 70, 42) + circ(CX + 85, CY + 70, 42)
    smile = arc(CX, CY + 20, 150, 50, 205, 335, cap=True)
    if inv:
        return circ(CX, CY, 260) - eyes - smile
    return ring(CX, CY, 260, 50) + eyes + smile


def club():
    r = 92
    s = circ(CX, CY + 120, r) + circ(CX - 110, CY - 30, r) + circ(CX + 110, CY - 30, r) + circ(CX, CY + 20, 60)
    return s + poly([(CX - 30, CY + 20), (CX + 30, CY + 20), (CX + 90, CY - 230), (CX - 90, CY - 230)])


def spade():
    h = heart(CX, CY + 10, 240).flipy(CY + 30)
    return h + poly([(CX - 30, CY - 20), (CX + 30, CY - 20), (CX + 90, CY - 240), (CX - 90, CY - 240)])


gs.add("smiley", "!", [0x263A], face(), "smiley")
gs.add("smileyInv", "@", [0x263B], face(True), "smiley inv")
gs.add("heart", "#", [0x2665], heart(CX, CY, 290), "heart")
gs.add("diamond", "$", [0x2666], poly([(CX, CY + 270), (CX + 210, CY), (CX, CY - 270), (CX - 210, CY)]), "diamond")
gs.add("club", "%", [0x2663], club(), "club")
gs.add("spade", "^", [0x2660], spade(), "spade")
gs.add("bullet", "&", [0x2022], circ(CX, CY, 110), "bullet")
gs.add("bulletInv", "*", [0x25D8], FULL - circ(CX, CY, 110), "bullet inv")
gs.add("circleWhite", "(", [0x25CB], ring(CX, CY, 170, 55), "circle")
gs.add("circleInv", ")", [0x25D9], FULL - ring(CX, CY, 170, 55), "circle inv")
gs.add("triUp", "-", [0x25B2], poly([(CX - 240, CY - 180), (CX + 240, CY - 180), (CX, CY + 230)]), "tri up")
gs.add("triDown", "=", [0x25BC], poly([(CX - 240, CY + 180), (CX + 240, CY + 180), (CX, CY - 230)]), "tri down")
gs.add("triLeft", "[", [0x25C4], poly([(CX + 200, CY + 220), (CX + 200, CY - 220), (CX - 230, CY)]), "pointer left")
gs.add("triRight", "]", [0x25BA], poly([(CX - 200, CY + 220), (CX - 200, CY - 220), (CX + 230, CY)]), "pointer right")

# thin arrows (unicode only)
def thin_arrow(angle, double=False):
    s = line(CX, CY - 300, CX, CY + 300, 60) + poly([(CX - 170, CY + 140), (CX, CY + 330), (CX + 170, CY + 140), (CX + 120, CY + 100), (CX, CY + 230), (CX - 120, CY + 100)])
    if double:
        s += s.rot(180, CX, CY)
    return s.rot(angle, CX, CY) if angle else s


gs.add("arrowUp", "", [0x2191], thin_arrow(0), "arrow up")
gs.add("arrowDown", "", [0x2193], thin_arrow(180), "arrow down")
gs.add("arrowLeft", "", [0x2190], thin_arrow(90).scale(0.95, 0.95, CX, CY), "arrow left")
gs.add("arrowRight", "", [0x2192], thin_arrow(-90).scale(0.95, 0.95, CX, CY), "arrow right")
gs.add("arrowUpDown", "", [0x2195], thin_arrow(0, True), "arrow up-down")
gs.add("arrowLeftRight", "", [0x2194], thin_arrow(90, True).scale(0.95, 0.95, CX, CY), "arrow left-right")
gs.add("arrowUpDownBase", "", [0x21A8], thin_arrow(0, True).scale(1, 0.85, CX, CY + 60) + rect(CX - 200, CY - 330, 400, 60), "up-down base")
gs.add("rightAngle", "", [0x221F], box(CX - 220, CY - 200, CX - 160, CY + 220) + box(CX - 220, CY - 200, CX + 220, CY - 140), "right angle")


def note(x, y):
    return ell(x, y, 85, 62).rot(-20, x, y) + box(x + 52, y, x + 102, y + 420)


n1 = note(CX - 60, CY - 180) + poly([(CX + 42, CY + 240), (CX + 42, CY + 170), (CX + 210, CY + 80), (CX + 210, CY + 150)])
gs.add("noteEighth", "", [0x266A], n1, "note")
n2 = note(CX - 140, CY - 180) + note(CX + 100, CY - 120) + poly([(CX - 38, CY + 240), (CX + 202, CY + 300), (CX + 202, CY + 230), (CX - 38, CY + 170)])
gs.add("noteBeamed", "", [0x266B], n2, "notes")
sun = ring(CX, CY, 130, 50)
for k in range(8):
    sun += line(CX, CY + 175, CX, CY + 270, 50).rot(45 * k, CX, CY)
gs.add("sunWhite", "", [0x263C], sun, "sun")
house = poly([(CX - 220, CY - 200), (CX + 220, CY - 200), (CX + 220, CY + 60), (CX, CY + 250), (CX - 220, CY + 60)]) - \
    poly([(CX - 165, CY - 145), (CX + 165, CY - 145), (CX + 165, CY + 35), (CX, CY + 177), (CX - 165, CY + 35)])
gs.add("house", "", [0x2302], house, "house")
male = ring(CX - 50, CY - 60, 150, 50) + line(CX + 50, CY + 40, CX + 210, CY + 200, 50) + \
    poly([(CX + 80, CY + 240), (CX + 250, CY + 240), (CX + 250, CY + 70), (CX + 200, CY + 120), (CX + 200, CY + 190), (CX + 130, CY + 190)])
gs.add("male", "", [0x2642], male, "male")
female = ring(CX, CY + 100, 150, 50) + box(CX - 25, CY - 300, CX + 25, CY - 30) + box(CX - 120, CY - 200, CX + 120, CY - 150)
gs.add("female", "", [0x2640], female, "female")
excl = S()
for x in (CX - 110, CX + 110):
    excl += poly([(x - 55, CY + 280), (x + 55, CY + 280), (x + 30, CY - 120), (x - 30, CY - 120)]) + circ(x, CY - 230, 45)
gs.add("exclamDouble", "", [0x203C], excl, "double excl")
pil = circ(CX - 40, CY + 160, 130) + box(CX - 40, CY + 30, CX + 30, CY + 290) + box(CX - 40, CY + 230, CX + 200, CY + 290) + \
    box(CX + 15, CY - 300, CX + 70, CY + 290) + box(CX + 135, CY - 300, CX + 190, CY + 290)
gs.add("pilcrow", "", [0x00B6], pil, "pilcrow")

# ------------------------------------------------------------ GUI widgets  (PUA U+E000…)
PUA = iter(range(0xE000, 0xE100))


def frame(w=420, h=420, r=50, t=45, cx=CX, cy=CY):
    return rect(cx - w / 2, cy - h / 2, w, h, r) - rect(cx - w / 2 + t, cy - h / 2 + t, w - 2 * t, h - 2 * t, max(r - t, 0))


check = pline([(CX - 120, CY + 5), (CX - 35, CY - 85), (CX + 125, CY + 110)], 60)
gs.add("checkboxOff", "p", [next(PUA)], frame(), "checkbox")
gs.add("checkboxOn", "P", [next(PUA), 0x2611], rect(CX - 210, CY - 210, 420, 420, 50) - check, "checkbox on")
gs.add("checkboxMixed", "~", [next(PUA)], frame() + rect(CX - 120, CY - 32, 240, 64, 20), "checkbox mixed")
gs.add("radioOff", "v", [next(PUA)], ring(CX, CY, 220, 45), "radio")
gs.add("radioOn", "V", [next(PUA)], ring(CX, CY, 220, 45) + circ(CX, CY, 110), "radio on")
pill = rect(CX - 290, CY - 160, 580, 320, 160)
gs.add("toggleOff", "I", [next(PUA)], (pill - rect(CX - 245, CY - 115, 490, 230, 115)) + circ(CX - 130, CY, 95), "toggle off")
gs.add("toggleOn", "O", [next(PUA)], pill - circ(CX + 130, CY, 105), "toggle on")
gs.add("progressEmpty", "_", [next(PUA)], box(X0, CY - 160, X1, CY - 115) + box(X0, CY + 115, X1, CY + 160), "progress empty")
gs.add("progressFull", "+", [next(PUA)], box(X0, CY - 160, X1, CY - 115) + box(X0, CY + 115, X1, CY + 160) + box(X0, CY - 85, X1, CY + 85), "progress full")
gs.add("progressCapL", "K", [next(PUA)], box(CX - 40, CY - 160, X1, CY - 115) + box(CX - 40, CY + 115, X1, CY + 160) + box(CX - 40, CY - 160, CX + 5, CY + 160), "progress L cap")
gs.add("progressCapR", "L", [next(PUA)], box(X0, CY - 160, CX + 40, CY - 115) + box(X0, CY + 115, CX + 40, CY + 160) + box(CX - 5, CY - 160, CX + 40, CY + 160), "progress R cap")
xmark = line(CX - 100, CY - 100, CX + 100, CY + 100, 55, True) + line(CX - 100, CY + 100, CX + 100, CY - 100, 55, True)
gs.add("winClose", ";", [next(PUA)], frame() + xmark, "close")
gs.add("winMaximize", ":", [next(PUA)], frame() + frame(220, 200, 0, 35, CX, CY - 10) + box(CX - 110, CY + 50, CX + 110, CY + 90), "maximize")
gs.add("winMinimize", "'", [next(PUA)], frame() + box(CX - 110, CY - 110, CX + 110, CY - 60), "minimize")
gs.add("winRestore", '"', [next(PUA)], frame() + frame(170, 150, 0, 32, CX - 25, CY - 35) +
       (box(CX - 60, CY + 50, CX + 125, CY + 125) - box(CX - 28, CY + 40, CX + 93, CY + 93)) + box(CX + 93, CY - 20, CX + 125, CY + 125), "restore")
gs.add("pointer", ",", [next(PUA)], poly([(CX - 150, CY + 300), (CX - 150, CY - 170), (CX - 45, CY - 70), (CX + 30, CY - 250),
                                          (CX + 110, CY - 215), (CX + 35, CY - 40), (CX + 180, CY - 40)]), "pointer")
gs.add("ibeam", ".", [next(PUA)], box(CX - 25, CY - 260, CX + 25, CY + 260) + rect(CX - 120, CY + 230, 240, 50, 25) + rect(CX - 120, CY - 280, 240, 50, 25), "text cursor")
hg = rect(CX - 180, CY + 250, 360, 50, 20) + rect(CX - 180, CY - 300, 360, 50, 20) + \
    (poly([(CX - 140, CY + 250), (CX + 140, CY + 250), (CX + 140, CY + 210), (CX + 30, CY), (CX + 140, CY - 210), (CX + 140, CY - 250),
           (CX - 140, CY - 250), (CX - 140, CY - 210), (CX - 30, CY), (CX - 140, CY + 210)]) -
     poly([(CX - 95, CY + 210), (CX + 95, CY + 210), (CX + 95, CY + 195), (CX, CY + 50), (CX - 95, CY + 195)]) -
     poly([(CX - 95, CY - 210), (CX + 95, CY - 210), (CX + 95, CY - 195), (CX + 10, CY - 80), (CX - 10, CY - 80), (CX - 95, CY - 195)])) + \
    poly([(CX - 70, CY - 205), (CX + 70, CY - 205), (CX, CY - 110)])
gs.add("hourglass", "/", [next(PUA), 0x231B], hg, "hourglass")


def scrollbtn(angle):
    t = poly([(CX - 110, CY - 60), (CX + 110, CY - 60), (CX, CY + 80)])
    return frame() + (t.rot(angle, CX, CY) if angle else t)


gs.add("scrollLeft", "<", [next(PUA)], scrollbtn(90), "scroll left")
gs.add("scrollRight", ">", [next(PUA)], scrollbtn(-90), "scroll right")
gs.add("scrollUp", "{", [next(PUA)], scrollbtn(0), "scroll up")
gs.add("scrollDown", "}", [next(PUA)], scrollbtn(180), "scroll down")
gs.add("menu", "\\", [next(PUA)], U(*[rect(CX - 210, CY + dy - 30, 420, 60, 30) for dy in (-150, 0, 150)]), "menu")
gs.add("dropdown", "|", [next(PUA)], frame() + poly([(CX - 110, CY + 50), (CX + 110, CY + 50), (CX, CY - 70)]), "dropdown")
grip = S()
for k in (0, 1, 2):
    o = 130 * k
    grip += line(CX + 240 - o, CY - 240, CX + 240, CY - 240 + o, 50, True) if k else circ(CX + 225, CY - 225, 30)
gs.add("resizeGrip", "`", [next(PUA)], grip, "resize grip")

if __name__ == "__main__":
    import preview
    out = build(gs, "DingThats GUI", "DingThatsGUI", "build/fonts", mono=True)
    export_svgs(gs, "build/svg/gui")
    preview.specimen(gs, out["ttf"], "build/gui_specimen.png", "DingThats GUI")
    preview.tile_test(out["ttf"], "build/gui_tile.png", [
        "QRRRRWRRRRE  qrrrwrrre  iro  trrrrytrru",
        "F    F    F  f   f   f  f f  f    f    f",
        "ARRRRSRRRRD  asrrsrrsd  krl  grrrrhrrrj",
        "F 1234F5678  f   f   f       f    f    f",
        "ZRRRRXRRRRC  zrrrxrrrc  KL   brrrrnrrrm",
        "K____+++++L  p v I O ; : ' \" , . / < > { } \\ | `",
    ])
    print(out)
