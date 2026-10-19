"""DingThats Shapes — arrows, geometry, checks, crosses, media and UI symbols (solid style).
Glyphs are drawn in a local 0..800 square (centre 400,400) and shifted into the em."""
from dt import *

C = 400
gs = GlyphSet(1000, offset=(100, -100))
PUA = iter(range(0xE100, 0xE200))


def outline(shape, s, cx=C, cy=C):
    return shape - shape.scale(s, s, cx, cy)


def heavy_arrow(angle, length=720):
    return arrow(C, C, length, 230, 620, 330, angle)


def double_arrow(angle):
    s = rect(C - 200, C - 115, 400, 230) + poly([(C - 160, C - 310), (C - 380, C), (C - 160, C + 310)]) + \
        poly([(C + 160, C - 310), (C + 380, C), (C + 160, C + 310)])
    return s.rot(angle, C, C) if angle else s


def chevron(angle, w=120):
    s = pline([(C - 110, C + 250), (C + 140, C), (C - 110, C - 250)], w)
    return s.rot(angle, C, C) if angle else s


def head(x, y, ang, L=220, Wd=230):
    t = poly([(-L * 0.35, -Wd / 2), (L * 0.65, 0), (-L * 0.35, Wd / 2)])
    return t.rot(ang, 0, 0).move(x, y)


def circ_arrow(a0, a1, r=250, w=95):
    s = arc(C, C, r, w, a0, a1)
    t = math.radians(a1)
    return s + head(C + r * math.cos(t), C + r * math.sin(t), a1 + 90)


def thin_double_diag(angle):
    s = line(C - 220, C, C + 220, C, 95) + head(C + 250, C, 0, 260, 280) + head(C - 250, C, 180, 260, 280)
    return s.rot(angle, C, C)


def qmark():
    return arc(C, C + 130, 120, 90, -90, 180) + box(C - 45, C - 70, C + 45, C + 30) + circ(C, C - 175, 55)


def excl():
    return poly([(C - 55, C + 260), (C + 55, C + 260), (C + 40, C - 80), (C - 40, C - 80)]) + circ(C, C - 190, 55)


DISC = circ(C, C, 360)
SQR = rect(70, 70, 660, 660, 90)
TRI_R = poly([(110, 60), (110, 740), (700, 400)])
TRI_U = poly([(60, 110), (740, 110), (400, 700)])
DIAM = poly([(C, 770), (730, C), (C, 30), (70, C)])
HEX = ngon(C, C, 390, 6, 90)
STAR = star(C, 385, 390, 155, 5)
SPARK = star(C, C, 390, 105, 4)
X = line(170, 170, 630, 630, 130, True) + line(170, 630, 630, 170, 130, True)
CHECK = pline([(110, 410), (315, 205), (690, 610)], 135)
PLUS = rect(330, 90, 140, 620, 70) + rect(90, 330, 620, 140, 70)
MINUS = rect(90, 330, 620, 140, 70)

# ---------------------------------------------------------------- lowercase: solid geometry
gs.add("triangleUp", "a", [0x25B2], TRI_U, "triangle up")
gs.add("bullet", "b", [0x2022], circ(C, C, 170), "bullet")
gs.add("circle", "c", [0x25CF], circ(C, C, 345), "circle")
gs.add("diamond", "d", [0x25C6], DIAM, "diamond")
gs.add("ellipse", "e", [0x2B2C], ell(C, C, 380, 230), "ellipse")
gs.add("burst", "f", [0x2738], star(C, C, 395, 205, 8, 90), "burst")
cog = circ(C, C, 280)
for k in range(8):
    cog += rect(C - 65, C, 130, 385, 18).rot(45 * k, C, C)
gs.add("cog", "g", [0x2699], cog - circ(C, C, 120), "cog")
gs.add("heart", "h", [0x2665], heart(C, C, 440), "heart")
gs.add("info", "i", [0x24D8], DISC - circ(C, C + 200, 58) - rect(C - 52, 150, 104, 300, 15), "info")
gs.add("cornerBR", "j", [0x25E2], poly([(70, 70), (730, 70), (730, 730)]), "corner")
gs.add("star", "k", [0x2605], STAR, "star")
gs.add("triangleLeft", "l", [0x25C0], TRI_R.flipx(C), "triangle left")
gs.add("menu", "m", [0x2630], U(*[rect(80, y, 640, 130, 65) for y in (95, 335, 575)]), "menu")
gs.add("octagon", "n", [0x2BC3], ngon(C, C, 385, 8, 22.5), "octagon")
gs.add("ring", "o", [0x25CB], ring(C, C, 345, 95), "ring")
gs.add("pentagon", "p", [0x2B1F], ngon(C, 380, 400, 5, 90), "pentagon")
gs.add("question", "q", [next(PUA)], DISC - qmark(), "question")
gs.add("triangleRight", "r", [0x25B6], TRI_R, "triangle right")
gs.add("square", "s", [0x25A0], rect(90, 90, 620, 620), "square")
gs.add("hexagon", "t", [0x2B22], HEX, "hexagon")
gs.add("power", "u", [0x23FB], arc(C, 370, 270, 100, 125, 415, True) + line(C, C, C, 750, 100, True), "power")
gs.add("check", "v", [0x2713], CHECK, "check")
gs.add("triangleDown", "w", [0x25BC], TRI_U.flipy(C), "triangle down")
gs.add("cross", "x", [0x2715], X, "cross")
gs.add("sparkle", "y", [0x2726], SPARK, "sparkle")
gs.add("bolt", "z", [0x26A1], poly([(430, 790), (150, 350), (365, 350), (285, 10), (650, 470), (435, 470), (580, 790)]), "bolt")

# ---------------------------------------------------------------- uppercase: outlines / status
warn = poly([(30, 70), (770, 70), (400, 740)])
gs.add("warning", "A", [0x26A0], warn - poly([(355, 470), (445, 470), (425, 270), (375, 270)]) - circ(C, 185, 48), "warning")
gs.add("squareInSquare", "B", [0x25A3], outline(rect(70, 70, 660, 660), 0.8) + rect(225, 225, 350, 350), "square in sq")
gs.add("radioOn", "C", [0x25C9], ring(C, C, 360, 80) + circ(C, C, 190), "fisheye")
gs.add("diamondWhite", "D", [0x25C7], DIAM - DIAM.scale(0.68, 0.68), "diamond white")
gs.add("circleMinus", "E", [0x2296], DISC - MINUS.scale(0.75, 0.75), "circle minus")
gs.add("circlePlus", "F", [0x2295], DISC - PLUS.scale(0.75, 0.75), "circle plus")
gs.add("circleCross", "G", [0x2297], DISC - X.scale(0.72, 0.72), "circle cross")
gs.add("heartWhite", "H", [0x2661], heart(C, C, 440) - heart(C, C + 10, 280), "heart white")
gs.add("circleLeftHalf", "I", [0x25D0], ring(C, C, 360, 80) + (circ(C, C, 300) & rect(0, 0, C, 800)), "half left")
gs.add("cornerBL", "J", [0x25E3], poly([(70, 70), (730, 70), (70, 730)]), "corner")
gs.add("starWhite", "K", [0x2606], STAR - STAR.scale(0.58, 0.58, C, 375), "star white")
gs.add("triangleLeftWhite", "L", [0x25C1], (TRI_R - TRI_R.scale(0.55, 0.55, 307, C)).flipx(C), "tri left white")
gs.add("ellipsisH", "M", [0x22EF], circ(130, C, 85) + circ(C, C, 85) + circ(670, C, 85), "ellipsis")
gs.add("prohibited", "N", [0x1F6C7], ring(C, C, 365, 95) + line(C - 245, C + 245, C + 245, C - 245, 95), "prohibited")
gs.add("bullseye", "O", [0x25CE], ring(C, C, 370, 85) + ring(C, C, 215, 85) + circ(C, C, 80), "bullseye")
gs.add("playCircle", "P", [next(PUA)], DISC - poly([(300, 190), (300, 610), (590, 400)]), "play circle")
gs.add("ballotBox", "Q", [0x2610], outline(SQR, 0.76), "ballot box")
gs.add("triangleRightWhite", "R", [0x25B7], TRI_R - TRI_R.scale(0.55, 0.55, 307, C), "tri right white")
gs.add("squareWhite", "S", [0x25A1], outline(rect(90, 90, 620, 620), 0.74), "square white")
gs.add("hexagonWhite", "T", [0x2B21], HEX - HEX.scale(0.7, 0.7), "hexagon white")
gs.add("eject", "U", [0x23CF], poly([(80, 330), (720, 330), (400, 720)]) + rect(80, 90, 640, 140, 20), "eject")
gs.add("ballotCheck", "V", [0x2611], SQR - CHECK.scale(0.66, 0.66), "ballot check")
gs.add("triangleDownWhite", "W", [0x25BD], (TRI_U - TRI_U.scale(0.55, 0.55, C, 307)).flipy(C), "tri down white")
gs.add("ballotX", "X", [0x2612], SQR - X.scale(0.7, 0.7), "ballot x")
gs.add("sparkleWhite", "Y", [0x2727], SPARK - SPARK.scale(0.55, 0.55), "sparkle white")
gs.add("circleRightHalf", "Z", [0x25D1], ring(C, C, 360, 80) + (circ(C, C, 300) & rect(C, 0, C, 800)), "half right")

# ---------------------------------------------------------------- digits: heavy arrows (numpad layout)
for key, uni, ang, lab in [("8", 0x2B06, 90, "up"), ("2", 0x2B07, 270, "down"), ("4", 0x2B05, 180, "left"),
                           ("6", 0x27A1, 0, "right"), ("7", 0x2B09, 135, "up-left"), ("9", 0x2B08, 45, "up-right"),
                           ("1", 0x2B0B, 225, "down-left"), ("3", 0x2B0A, 315, "down-right")]:
    gs.add("arrow" + lab.title().replace("-", ""), key, [uni],
           heavy_arrow(ang, 720 if ang % 90 == 0 else 760).rot(0) if ang else heavy_arrow(0), "arrow " + lab)
gs.add("arrowUpDown", "5", [0x2B0D], double_arrow(90), "arrow up-down")
gs.add("arrowLeftRight", "0", [0x2B0C], double_arrow(0), "arrow left-right")

# ---------------------------------------------------------------- shifted digits: line arrows & chevrons
ccw = circ_arrow(60, 330)
gs.add("undo", "!", [0x21BA], ccw, "undo")
gs.add("chevronDown", "@", [0x2304], chevron(270), "chevron down")
gs.add("redo", "#", [0x21BB], ccw.flipx(C), "redo")
gs.add("chevronLeft", "$", [0x2039], chevron(180), "chevron left")
gs.add("refresh", "%", [0x27F3], circ_arrow(20, 160) + circ_arrow(200, 340), "refresh")
gs.add("chevronRight", "^", [0x203A], chevron(0), "chevron right")
gs.add("expand", "&", [0x2922], thin_double_diag(45), "expand diag")
gs.add("chevronUp", "*", [0x2303], chevron(90), "chevron up")
gs.add("expandAlt", "(", [0x2921], thin_double_diag(135), "diag alt")
swap = line(110, 540, 560, 540, 90) + head(600, 540, 0, 250, 260) + line(240, 260, 690, 260, 90) + head(200, 260, 180, 250, 260)
gs.add("swap", ")", [0x21C4], swap, "swap")

# ---------------------------------------------------------------- punctuation: maths, media, UI
gs.add("plus", "+", [0x2795], PLUS, "plus")
gs.add("minus", "-", [0x2796], MINUS, "minus")
gs.add("equals", "=", [next(PUA)], rect(90, 450, 620, 130, 65) + rect(90, 220, 620, 130, 65), "equals")
gs.add("divide", "/", [0x2797], MINUS + circ(C, 620, 85) + circ(C, 180, 85), "divide")
ast = S()
for a in (0, 60, 120):
    ast += rect(C - 70, 40, 140, 720, 70).rot(a, C, C)
gs.add("asterisk", "\\", [0x2731], ast, "asterisk")
gs.add("skipPrev", "[", [0x23EE], rect(110, 110, 120, 580, 20) + poly([(690, 110), (690, 690), (240, 400)]), "skip prev")
gs.add("skipNext", "]", [0x23ED], (rect(110, 110, 120, 580, 20) + poly([(690, 110), (690, 690), (240, 400)])).flipx(C), "skip next")
ff = poly([(40, 130), (40, 670), (400, 400)]) + poly([(400, 130), (400, 670), (760, 400)])
gs.add("rewind", "{", [0x23EA], ff.flipx(C), "rewind")
gs.add("fastForward", "}", [0x23E9], ff, "fast forward")
gs.add("pause", ";", [0x23F8], rect(140, 90, 180, 620, 30) + rect(480, 90, 180, 620, 30), "pause")
gs.add("stop", ":", [0x23F9], rect(110, 110, 580, 580, 50), "stop")
gs.add("record", "'", [0x23FA], circ(C, C, 300), "record")
gs.add("playPause", '"', [0x23EF], poly([(40, 120), (40, 680), (420, 400)]) + rect(520, 120, 90, 560, 20) + rect(670, 120, 90, 560, 20), "play/pause")
gs.add("triangleLeftSmall", ",", [0x25C2], TRI_R.flipx(C).scale(0.55, 0.55), "small left")
gs.add("triangleRightSmall", ".", [0x25B8], TRI_R.scale(0.55, 0.55), "small right")
dch = pline([(110, 650), (360, 400), (110, 150)], 115) + pline([(420, 650), (670, 400), (420, 150)], 115)
gs.add("doubleChevronLeft", "<", [next(PUA)], dch.flipx(C), "dbl chev left")
gs.add("doubleChevronRight", ">", [next(PUA)], dch, "dbl chev right")
gs.add("exclaimCircle", "?", [next(PUA)], DISC - excl(), "exclaim circle")
gs.add("ellipsisV", "|", [0x22EE], circ(C, 130, 85) + circ(C, C, 85) + circ(C, 670, 85), "ellipsis vert")
gs.add("search", "`", [0x2315], ring(470, 470, 240, 95) + line(140, 140, 300, 300, 120, True), "search")
bs = poly([(30, C), (250, 680), (770, 680), (770, 120), (250, 120)])
gs.add("backspace", "~", [0x232B], bs - (line(380, 260, 640, 540, 85, True) + line(380, 540, 640, 260, 85, True)), "backspace")
ret = box(610, 300, 700, 720) + box(230, 300, 700, 390) + head(180, 345, 180, 300, 330)
gs.add("return", "_", [0x23CE], ret, "return")

if __name__ == "__main__":
    import preview
    out = build(gs, "DingThats Shapes", "DingThatsShapes", "build/fonts")
    export_svgs(gs, "build/svg/shapes")
    preview.specimen(gs, out["ttf"], "build/shapes_specimen.png", "DingThats Shapes")
    print(len(gs.glyphs), out)
