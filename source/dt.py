"""DingThats glyph toolkit: tiny vector DSL + font builder (OTF/TTF/WOFF2/SVG)."""
import math, os
from pathops import Path, PathOp, op
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.misc.transform import Transform
from fontTools.fontBuilder import FontBuilder

K = 0.5522847498


class S:
    """A filled shape. + union, - difference, & intersect."""
    def __init__(self, p=None):
        self.p = p if p is not None else Path()

    def _op(a, b, o):
        return S(op(a.p, b.p, o, fix_winding=True, clockwise=False))
    def __add__(a, b): return a._op(b, PathOp.UNION)
    def __sub__(a, b): return a._op(b, PathOp.DIFFERENCE)
    def __and__(a, b): return a._op(b, PathOp.INTERSECTION)
    def __xor__(a, b): return a._op(b, PathOp.XOR)

    def tf(self, t):
        q = Path()
        self.p.draw(TransformPen(q.getPen(), t))
        return S(q) + S()  # renormalise winding
    def move(self, dx, dy): return self.tf(Transform(1, 0, 0, 1, dx, dy))
    def rot(self, deg, cx=400, cy=400):
        return self.tf(Transform().translate(cx, cy).rotate(math.radians(deg)).translate(-cx, -cy))
    def scale(self, sx, sy=None, cx=400, cy=400):
        sy = sx if sy is None else sy
        return self.tf(Transform().translate(cx, cy).scale(sx, sy).translate(-cx, -cy))
    def flipx(self, cx=400): return self.scale(-1, 1, cx, 0)
    def flipy(self, cy=400): return self.scale(1, -1, 0, cy)
    def draw(self, pen): self.p.draw(pen)
    def bounds(self):
        bp = BoundsPen(None); self.p.draw(bp); return bp.bounds


def U(*shapes):
    r = S()
    for s in shapes:
        r = r + s
    return r


def poly(pts):
    p = Path(); pen = p.getPen()
    pen.moveTo(tuple(pts[0]))
    for q in pts[1:]:
        pen.lineTo(tuple(q))
    pen.closePath()
    return S(p) + S()


def ell(cx, cy, rx, ry):
    p = Path(); pen = p.getPen()
    kx, ky = rx * K, ry * K
    pen.moveTo((cx + rx, cy))
    pen.curveTo((cx + rx, cy + ky), (cx + kx, cy + ry), (cx, cy + ry))
    pen.curveTo((cx - kx, cy + ry), (cx - rx, cy + ky), (cx - rx, cy))
    pen.curveTo((cx - rx, cy - ky), (cx - kx, cy - ry), (cx, cy - ry))
    pen.curveTo((cx + kx, cy - ry), (cx + rx, cy - ky), (cx + rx, cy))
    pen.closePath()
    return S(p) + S()


def circ(cx, cy, r): return ell(cx, cy, r, r)


def rect(x, y, w, h, r=0):
    if w < 0: x, w = x + w, -w
    if h < 0: y, h = y + h, -h
    if r <= 0:
        return poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])
    r = min(r, w / 2, h / 2)
    p = Path(); pen = p.getPen(); k = r * (1 - K)
    pen.moveTo((x + r, y))
    pen.lineTo((x + w - r, y))
    pen.curveTo((x + w - k, y), (x + w, y + k), (x + w, y + r))
    pen.lineTo((x + w, y + h - r))
    pen.curveTo((x + w, y + h - k), (x + w - k, y + h), (x + w - r, y + h))
    pen.lineTo((x + r, y + h))
    pen.curveTo((x + k, y + h), (x, y + h - k), (x, y + h - r))
    pen.lineTo((x, y + r))
    pen.curveTo((x, y + k), (x + k, y), (x + r, y))
    pen.closePath()
    return S(p) + S()


def box(x0, y0, x1, y1, r=0):
    return rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0), r)


def line(x1, y1, x2, y2, w, cap=False):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L * w / 2, dx / L * w / 2
    s = poly([(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)])
    if cap:
        s = s + circ(x1, y1, w / 2) + circ(x2, y2, w / 2)
    return s


def pline(pts, w, cap=True):
    """Polyline with round joins (cap=True) for check marks, etc."""
    s = S()
    for a, b in zip(pts, pts[1:]):
        s = s + line(a[0], a[1], b[0], b[1], w, cap)
    return s


def ring(cx, cy, r, w): return circ(cx, cy, r) - circ(cx, cy, r - w)


def wedge(cx, cy, R, a0, a1):
    pts = [(cx, cy)]
    n = max(2, int(abs(a1 - a0) / 30) + 2)
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    return poly(pts)


def arc(cx, cy, r, w, a0, a1, cap=False):
    """Stroked arc, r = centre radius of stroke, angles ccw from +x in degrees."""
    s = (circ(cx, cy, r + w / 2) - circ(cx, cy, r - w / 2)) & wedge(cx, cy, r * 3, a0, a1)
    if cap:
        for a in (a0, a1):
            t = math.radians(a)
            s = s + circ(cx + r * math.cos(t), cy + r * math.sin(t), w / 2)
    return s


def ngon(cx, cy, r, n, a=90):
    return poly([(cx + r * math.cos(math.radians(a + 360 * i / n)),
                  cy + r * math.sin(math.radians(a + 360 * i / n))) for i in range(n)])


def star(cx, cy, ro, ri, n, a=90):
    pts = []
    for i in range(2 * n):
        r = ro if i % 2 == 0 else ri
        t = math.radians(a + 180 * i / n)
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    return poly(pts)


def at(s, a, cx, cy):
    """point on circle helper"""
    return (cx + s * math.cos(math.radians(a)), cy + s * math.sin(math.radians(a)))


# ---------------------------------------------------------------- font build

class GlyphSet:
    def __init__(self, adv, offset=(0, 0)):
        self.adv = adv
        self.offset = offset
        self.glyphs = []      # (name, unicodes, shape, adv, label)
        self.names = set()

    def add(self, name, keys, unis, shape, label=None, adv=None):
        assert name not in self.names, name
        self.names.add(name)
        cps = [ord(k) for k in keys] + list(unis)
        if self.offset != (0, 0) and shape is not None:
            shape = shape.move(*self.offset)
        self.glyphs.append(dict(name=name, unis=cps, shape=shape,
                                adv=adv or self.adv, label=label or name, keys=keys))


def _notdef(adv):
    m = 60
    return rect(m, -100, adv - 2 * m, 800) - rect(m + 50, -50, adv - 2 * m - 100, 700)


def build(gs, family, psbase, outdir, mono=False, version="1.000"):
    os.makedirs(outdir, exist_ok=True)
    order = [".notdef", "space"] + [g["name"] for g in gs.glyphs]
    cmap = {0x20: "space", 0xA0: "space"}
    shapes = {".notdef": _notdef(gs.adv), "space": None}
    advs = {".notdef": gs.adv, "space": gs.adv}
    for g in gs.glyphs:
        shapes[g["name"]] = g["shape"]
        advs[g["name"]] = g["adv"]
        for u in g["unis"]:
            assert u not in cmap, (hex(u), g["name"], cmap.get(u))
            cmap[u] = g["name"]

    lic = ("This Font Software is licensed under the SIL Open Font License, Version 1.1. "
           "This license is available with a FAQ at: https://openfontlicense.org")
    names = dict(
        copyright="Copyright 2026 The DingThats Project Authors (https://dingthat.com)",
        familyName=family, styleName="Regular",
        uniqueFontIdentifier=f"{version};DING;{psbase}-Regular",
        fullName=f"{family} Regular", psName=f"{psbase}-Regular",
        version=f"Version {version}", manufacturer="DingThats Project",
        designer="DingThats Project", vendorURL="https://dingthat.com",
        designerURL="https://dingthat.com", licenseDescription=lic,
        licenseInfoURL="https://openfontlicense.org",
    )
    out = {}
    for flavour in ("otf", "ttf"):
        tt = flavour == "ttf"
        fb = FontBuilder(1000, isTTF=tt)
        fb.setupGlyphOrder(order)
        fb.setupCharacterMap(cmap)
        metrics, data = {}, {}
        for n in order:
            s = shapes[n]
            if tt:
                pen = TTGlyphPen(None)
                if s is not None:
                    s.draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
                data[n] = pen.glyph()
            else:
                pen = T2CharStringPen(advs[n], None)
                if s is not None:
                    s.draw(pen)
                data[n] = pen.getCharString()
            b = s.bounds() if s is not None else None
            metrics[n] = (advs[n], int(round(b[0])) if b else 0)
        if tt:
            fb.setupGlyf(data)
        else:
            fb.setupCFF(f"{psbase}-Regular", {"FullName": f"{family} Regular",
                        "isFixedPitch": mono}, data, {})
        fb.setupHorizontalMetrics(metrics)
        fb.setupHorizontalHeader(ascent=800, descent=-200, lineGap=0)
        fb.setupNameTable(names)
        fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, sTypoLineGap=0,
                    usWinAscent=800, usWinDescent=200, achVendID="DING", fsType=0,
                    version=4, sxHeight=500, sCapHeight=700, fsSelection=0x40 | 0x80)
        fb.setupPost(isFixedPitch=1 if mono else 0)
        path = os.path.join(outdir, f"{psbase}-Regular.{flavour}")
        fb.save(path)
        out[flavour] = path
        if tt:
            fb.font.flavor = "woff2"
            w2 = os.path.join(outdir, f"{psbase}-Regular.woff2")
            fb.font.save(w2)
            out["woff2"] = w2
    return out


def export_svgs(gs, outdir):
    os.makedirs(outdir, exist_ok=True)
    for g in gs.glyphs:
        if g["shape"] is None:
            continue
        pen = SVGPathPen(None)
        g["shape"].draw(pen)
        d = pen.getCommands()
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -800 {g["adv"]} 1000" '
               f'width="{g["adv"]}" height="1000">\n'
               f'  <path transform="scale(1,-1)" d="{d}"/>\n</svg>\n')
        with open(os.path.join(outdir, g["name"] + ".svg"), "w") as f:
            f.write(svg)


def heart(cx, cy, a):
    """Heart of overall width ~1.707a, visually centred on (cx, cy)."""
    cy = cy - 0.0735 * a
    h = a / math.sqrt(2)
    d = poly([(cx, cy + h), (cx + h, cy), (cx, cy - h), (cx - h, cy)])
    return d + circ(cx - h / 2, cy + h / 2, a / 2) + circ(cx + h / 2, cy + h / 2, a / 2)


def tri(cx, cy, r, a=90):
    return ngon(cx, cy, r, 3, a)


def arrow(cx, cy, length, shaft, head_w, head_l, angle=90):
    """Solid arrow centred on (cx,cy) pointing at `angle` degrees."""
    x0 = cx - length / 2; x1 = cx + length / 2
    s = rect(x0, cy - shaft / 2, length - head_l + 2, shaft) + \
        poly([(x1 - head_l, cy - head_w / 2), (x1, cy), (x1 - head_l, cy + head_w / 2)])
    return s.rot(angle, cx, cy) if angle else s
