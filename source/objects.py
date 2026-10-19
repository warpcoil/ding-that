"""DingThats Objects — buildings, transport and everyday objects (solid style).
Drawn in a local 0..800 square (centre 400,400), shifted into the em."""
from dt import *

C = 400
gs = GlyphSet(1000, offset=(100, -100))
TOP = rect(-100, 0, 1000, 1000)


def above(y): return rect(-100, y, 1000, 1000)
def below(y): return rect(-100, y - 1000, 1000, 1000)


def wheel(x, y, r=95, gap=28, hub=38):
    """returns (cutout, wheel) so callers can do body - cut + whl"""
    return circ(x, y, r + gap), circ(x, y, r) - circ(x, y, hub)


def person(cx, s=1.0):
    head = circ(cx, 590, 150)
    body = ell(cx, 40, 290, 360) & above(40)
    return (head + body).scale(s, s, cx, 40)


def tri_tip(x, y, w=90, h=120):
    return poly([(x - w / 2, y - h / 3), (x + w / 2, y - h / 3), (x, y + h * 2 / 3)])


# ---------------------------------------------------------------- lowercase
plane = rect(355, 40, 90, 720, 45) + poly([(400, 560), (770, 340), (770, 260), (400, 400), (30, 260), (30, 340)]) + \
    poly([(400, 200), (580, 90), (580, 40), (400, 100), (220, 40), (220, 90)]) + ell(C, 640, 45, 150)
gs.add("airplane", "a", [0x2708], plane.rot(-45), "airplane")

bus = rect(30, 120, 740, 560, 70)
for i in range(4):
    bus -= rect(85 + i * 140, 420, 105, 190, 18)
bus -= rect(650, 230, 70, 380, 18)
cut1, w1 = wheel(190, 120); cut2, w2 = wheel(560, 120)
gs.add("bus", "b", [0x1F68C], bus - cut1 - cut2 + w1 + w2 + rect(30, 280, 740, 30) - rect(30, 330, 600, 30), "bus")


def car(taxi=False):
    body = rect(30, 160, 740, 200, 70) + poly([(190, 340), (290, 560), (530, 560), (650, 340)])
    body -= poly([(270, 390), (330, 515), (390, 515), (390, 390)]) + poly([(430, 390), (430, 515), (510, 515), (590, 390)])
    c1, a = wheel(200, 160); c2, b = wheel(600, 160)
    body = body - c1 - c2 + a + b
    body -= rect(80, 280, 60, 35, 15) if False else S()
    if taxi:
        body += rect(330, 585, 140, 80, 15)
    return body


gs.add("car", "c", [0x1F697], car(), "car")
doc = poly([(140, 40), (660, 40), (660, 540), (440, 760), (140, 760)])
doc -= poly([(410, 790), (410, 510), (690, 510)]).scale(1, 1) + S()
doc = doc - poly([(395, 800), (395, 495), (700, 495), (700, 800)]) + poly([(440, 760), (440, 540), (660, 540)])
doc = poly([(140, 40), (660, 40), (660, 520), (420, 760), (140, 760)]) - poly([(390, 790), (390, 490), (690, 490)]) + \
    poly([(420, 760), (420, 520), (660, 520)]).scale(0.88, 0.88, 500, 600)
for y in (380, 270, 160):
    doc -= rect(220, y, 360, 50, 25)
gs.add("document", "d", [0x1F4C4], doc, "document")
env = rect(40, 130, 720, 540, 50) - pline([(120, 590), (400, 350), (680, 590)], 55)
gs.add("envelope", "e", [0x2709], env, "envelope")
fac = rect(40, 40, 720, 340)
for x in (40, 270, 500):
    fac += poly([(x, 370), (x, 560), (x + 230, 370)])
fac += rect(610, 370, 100, 390)
for x in (110, 300, 490):
    fac -= rect(x, 190, 110, 110)
fac -= rect(620, 40, 90, 170)
gs.add("factory", "f", [0x1F3ED], fac, "factory")
pump = rect(110, 40, 400, 120, 20) + rect(150, 100, 320, 660, 50) - rect(210, 480, 200, 190, 20)
pump += pline([(470, 620), (660, 620), (660, 300), (600, 240)], 55) + rect(560, 160, 80, 110, 20)
gs.add("fuelPump", "g", [0x26FD], pump, "fuel pump")
house = rect(150, 40, 500, 400) + poly([(30, 400), (400, 750), (770, 400)]) + rect(570, 560, 90, 170)
house -= rect(345, 40, 110, 200, 15) + rect(205, 240, 100, 100) + rect(495, 240, 100, 100)
gs.add("house", "h", [0x1F3E0], house, "house")
bulb = circ(C, 510, 255) + poly([(250, 350), (550, 350), (500, 230), (300, 230)])
bulb -= arc(C, 510, 170, 45, 105, 165, True)
bulb += rect(295, 160, 210, 50, 25) + rect(305, 95, 190, 50, 25) + rect(350, 35, 100, 45, 22)
gs.add("lightbulb", "i", [0x1F4A1], bulb, "lightbulb")
anc = ring(C, 680, 80, 45) + rect(365, 120, 70, 530) + rect(230, 530, 340, 65, 32)
anc += arc(C, 360, 270, 65, 195, 345)
anc += tri_tip(*at(270, 195, C, 360), 120, 160) + tri_tip(*at(270, 345, C, 360), 120, 160)
gs.add("anchor", "j", [0x2693], anc, "anchor")
key = ring(220, C, 170, 90) + rect(370, 355, 400, 90, 20) + rect(600, 250, 60, 140, 10) + rect(700, 250, 60, 140, 10)
gs.add("key", "k", [0x1F511], key, "key")
lock = rect(130, 40, 540, 420, 60) - circ(C, 270, 60) - poly([(368, 260), (432, 260), (455, 120), (345, 120)])
lock += arc(C, 470, 180, 75, 0, 180) + rect(182, 440, 75, 40) + rect(543, 440, 75, 40)
gs.add("lock", "l", [0x1F512], lock, "lock")
pin = circ(C, 510, 255) + poly([(185, 375), (615, 375), (C, 30)]) - circ(C, 510, 105)
gs.add("mapPin", "m", [0x1F4CD], pin, "map pin")
bell = (circ(C, 470, 220) & above(470)) + poly([(180, 470), (620, 470), (670, 230), (130, 230)])
bell += rect(60, 170, 680, 80, 40) + circ(C, 110, 75) + circ(C, 705, 55)
gs.add("bell", "n", [0x1F514], bell, "bell")
off = rect(180, 40, 440, 680) + rect(360, 720, 80, 60)
for r in range(5):
    for c in range(3):
        off -= rect(230 + c * 125, 230 + r * 95, 90, 60)
off -= rect(340, 40, 120, 150)
gs.add("office", "o", [0x1F3E2], off, "office")
gs.add("person", "p", [0x1F464], person(C), "person")
front = person(310, 0.9)
back = person(530, 0.78).move(0, 60) - person(310, 0.9).scale(1.1, 1.1, 310, 40)
gs.add("people", "q", [0x1F465], front + back, "people")
rk = ell(C, 470, 125, 310) + poly([(290, 380), (160, 170), (160, 90), (300, 200)]) + poly([(510, 380), (640, 170), (640, 90), (500, 200)])
rk -= circ(C, 520, 55)
rk += poly([(340, 140), (C, 10), (460, 140)])
gs.add("rocket", "r", [0x1F680], rk.rot(-35, C, C).scale(0.95, 0.95), "rocket")
shop = rect(90, 40, 620, 430) + rect(40, 480, 720, 150) + rect(90, 640, 620, 110, 15)
for x in (100, 260, 420, 580):
    shop -= circ(x + 80, 480, 80) & below(480) if False else S()
for x in (180, 340, 500):
    shop -= rect(x - 10, 480, 50, 150)
shop -= rect(140, 180, 280, 210, 15) + rect(480, 40, 170, 330, 15)
gs.add("shop", "s", [0x1F3EA], shop, "shop")
tr = rect(170, 120, 460, 640, 130) - rect(240, 450, 320, 210, 40) - circ(285, 260, 45) - circ(515, 260, 45) - rect(330, 330, 140, 40, 20)
tr += line(270, 120, 170, 20, 55, True) + line(530, 120, 630, 20, 55, True)
gs.add("train", "t", [0x1F686], tr, "train")
umb = (circ(C, 400, 370) & above(400))
for x in (160, 400, 640):
    umb -= circ(x, 400, 75)
umb += rect(375, 140, 50, 600) + arc(305, 145, 95, 50, 180, 360, True)
gs.add("umbrella", "u", [0x2602], umb, "umbrella")
truck = rect(30, 170, 470, 520, 20) + rect(520, 170, 250, 330, 50) - poly([(600, 330), (600, 450), (700, 450), (740, 330)])
c1, a = wheel(170, 165); c2, b = wheel(640, 165)
gs.add("truck", "v", [0x1F69A], truck - c1 - c2 + a + b, "truck")
glob = circ(C, C, 360) - (ell(C, C, 170, 360) - ell(C, C, 125, 330)) - rect(40, 380, 720, 40) - rect(380, 40, 40, 720)
glob -= rect(40, 570, 720, 35) + rect(40, 195, 720, 35)
gs.add("globe", "w", [0x1F310], glob, "globe")
gs.add("taxi", "x", [0x1F695], car(True), "taxi")
bk = ring(180, 220, 150, 50) + ring(620, 220, 150, 50)
pts = dict(rh=(180, 220), bb=(380, 220), st=(320, 480), hd=(570, 480), fh=(620, 220))
for a, b in [("rh", "bb"), ("bb", "st"), ("st", "rh"), ("bb", "hd"), ("st", "hd"), ("hd", "fh")]:
    bk += line(*pts[a], *pts[b], 45, True)
bk += rect(240, 490, 150, 45, 22) + line(570, 480, 540, 590, 45, True) + line(500, 590, 640, 590, 45, True)
gs.add("bicycle", "y", [0x1F6B2], bk, "bicycle")
cart = poly([(160, 620), (740, 620), (660, 300), (230, 300)]) + pline([(40, 700), (150, 700), (250, 230), (660, 230)], 50)
cart -= rect(340, 340, 35, 240) + rect(500, 340, 35, 240)
cart += circ(290, 120, 65) + circ(600, 120, 65)
gs.add("cart", "z", [0x1F6D2], cart, "cart")

# ---------------------------------------------------------------- uppercase
alarm = ring(C, 380, 300, 75) + line(C, 380, C, 560, 50, True) + line(C, 380, 510, 320, 50, True)
alarm += (circ(170, 660, 105) - circ(C, 380, 330)) + (circ(630, 660, 105) - circ(C, 380, 330))
alarm += line(220, 140, 140, 40, 55, True) + line(580, 140, 660, 40, 55, True)
gs.add("alarmClock", "A", [0x23F0], alarm, "alarm clock")
bank = poly([(40, 570), (760, 570), (C, 770)]) - circ(C, 650, 40) + rect(80, 500, 640, 60) + rect(50, 40, 700, 80) + rect(90, 120, 620, 40)
for x in (120, 270, 440, 590):
    bank += rect(x, 160, 90, 340)
gs.add("bank", "B", [0x1F3E6], bank, "bank")
cal = rect(70, 50, 660, 620, 50) - rect(125, 105, 550, 420, 15)
for r in range(3):
    for c in range(4):
        cal += rect(165 + c * 125, 135 + r * 125, 90, 90, 10)
cal = cal - rect(195, 600, 110, 180, 40) - rect(495, 600, 110, 180, 40) + rect(215, 610, 70, 160, 35) + rect(515, 610, 70, 160, 35)
gs.add("calendar", "C", [0x1F4C5], cal, "calendar")
mon = rect(30, 230, 740, 490, 40) - rect(90, 290, 620, 370, 10) + poly([(340, 230), (460, 230), (490, 110), (310, 110)]) + rect(200, 60, 400, 60, 30)
gs.add("desktop", "D", [0x1F5A5], mon, "desktop")
sch = rect(80, 40, 640, 400) + poly([(30, 420), (C, 610), (770, 420)]) + rect(320, 560, 160, 140) + poly([(300, 690), (500, 690), (C, 790)])
sch -= (rect(345, 40, 110, 180) + circ(C, 220, 55)) + circ(C, 470, 50)
for x in (140, 240, 500, 600):
    sch -= rect(x, 240, 60, 110, 10)
gs.add("school", "E", [0x1F3EB], sch, "school")
fold = poly([(50, 90), (50, 700), (300, 700), (370, 620), (750, 620), (750, 90)]) - rect(50, 500, 700, 40)
gs.add("folder", "F", [0x1F4C1], fold, "folder")
gift = rect(110, 40, 580, 400) + rect(70, 460, 660, 140) - rect(345, 40, 25, 560) - rect(430, 40, 25, 560)
bow = (ell(290, 680, 120, 70) - ell(290, 680, 65, 25)).rot(20, 290, 680) + (ell(510, 680, 120, 70) - ell(510, 680, 65, 25)).rot(-20, 510, 680)
gs.add("gift", "G", [0x1F381], gift + bow + circ(C, 640, 45), "gift")
hosp = rect(90, 40, 620, 620) + rect(260, 660, 280, 80) - rect(320, 40, 160, 200, 15)
hosp -= rect(340, 300, 120, 300) + rect(250, 390, 300, 120)
gs.add("hospital", "H", [0x1F3E5], hosp, "hospital")
cam = rect(30, 110, 740, 480, 60) + poly([(240, 570), (300, 690), (500, 690), (560, 570)])
cam = cam - circ(C, 340, 185) + circ(C, 340, 120) - rect(610, 480, 90, 50, 15)
gs.add("camera", "I", [0x1F4F7], cam, "camera")
case = rect(50, 70, 700, 480, 50) + (rect(260, 520, 280, 190, 60) - rect(320, 520, 160, 130, 25))
case = case - rect(50, 330, 700, 40) - rect(345, 280, 110, 130, 15) + rect(370, 295, 60, 100, 10)
gs.add("briefcase", "J", [0x1F4BC], case, "briefcase")
kb = rect(20, 170, 760, 460, 45)
for r, (n, x0) in enumerate([(9, 75), (8, 115), (9, 75)]):
    for c in range(n):
        kb -= rect(x0 + c * 75 + 0, 470 - r * 95, 55, 65, 10)
kb -= rect(190, 210, 420, 60, 10)
gs.add("keyboard", "K", [0x2328], kb, "keyboard")
lap = rect(130, 230, 540, 470, 30) - rect(185, 285, 430, 360, 8) + rect(30, 140, 740, 70, 35) - rect(330, 175, 140, 35, 15)
gs.add("laptop", "L", [0x1F4BB], lap, "laptop")
mob = rect(230, 30, 340, 740, 60) - rect(270, 160, 260, 520, 10) - rect(350, 705, 100, 25, 12) - circ(C, 95, 35)
gs.add("mobile", "M", [0x1F4F1], mob, "mobile")
CLOUD = circ(230, 350, 160) + circ(440, 450, 230) + circ(620, 360, 150) + rect(230, 190, 390, 200)
CLOUD = CLOUD.move(0, 10)
gs.add("cloud", "N", [0x2601], CLOUD, "cloud")
clk = circ(C, C, 365) - line(C, C, C, 640, 60, True) - line(C, C, 570, 320, 60, True)
for k in range(12):
    clk -= circ(*at(305, 30 * k, C, C), 22 if k % 3 else 32)
gs.add("clock", "O", [0x1F552], clk, "clock")
prn = rect(30, 190, 740, 330, 50) - rect(170, 30, 460, 300) + rect(200, 40, 400, 260) - rect(250, 100, 300, 30) - rect(250, 170, 300, 30)
prn = prn + rect(210, 545, 380, 215, 10) - circ(660, 440, 32)
gs.add("printer", "P", [0x1F5A8], prn, "printer")
bag = poly([(110, 40), (690, 40), (640, 530), (160, 530)]) + arc(C, 530, 150, 55, 0, 180) + rect(222, 500, 56, 30) + rect(522, 500, 56, 30)
gs.add("shoppingBag", "Q", [0x1F6CD], bag - circ(C, 330, 0.1), "shopping bag")
fork = rect(165, 430, 40, 340, 20) + rect(240, 430, 40, 340, 20) + rect(315, 430, 40, 340, 20) + rect(165, 400, 190, 110, 50) + rect(225, 40, 70, 420, 35)
knife = (ell(560, 560, 100, 230) & rect(460, 330, 100, 500)) + rect(490, 40, 70, 320, 35)
gs.add("restaurant", "R", [0x1F374], fork + knife.move(30, 0), "restaurant")
sun = circ(C, C, 185)
for k in range(8):
    sun += rect(C - 38, C + 240, 76, 150, 38).rot(45 * k, C, C)
gs.add("sun", "S", [0x2600], sun, "sun")
tl = rect(260, 150, 280, 620, 70) - ring(C, 645, 85, 30) - ring(C, 460, 85, 30) - ring(C, 275, 85, 30) - circ(C, 645, 60) + rect(370, 20, 60, 140)
gs.add("trafficLight", "T", [0x1F6A6], tl, "traffic light")
trash = poly([(180, 40), (620, 40), (660, 580), (140, 580)]) + rect(110, 610, 580, 70, 25) + (rect(310, 670, 180, 90, 30) - rect(355, 670, 90, 45))
for x in (270, 380, 490):
    trash -= rect(x, 110, 40, 400, 20)
gs.add("trash", "U", [0x1F5D1], trash, "trash")
tent = poly([(30, 50), (770, 50), (C, 690)]) - poly([(290, 50), (510, 50), (C, 360)]) + line(C, 680, C, 780, 40, True)
gs.add("tent", "V", [0x26FA], tent, "tent")
sun2 = circ(520, 560, 135)
for k in range(8):
    sun2 += rect(500, 560 + 175, 40, 75, 20).rot(45 * k, 520, 560)
cl2 = CLOUD.scale(0.78, 0.78, 360, 200).move(-40, 0)
gs.add("partlyCloudy", "W", [0x26C5], (sun2 - cl2.scale(1.1, 1.12, 330, 260)) + cl2, "partly cloudy")
ph = poly([(150, 40), (650, 40), (590, 400), (210, 400)]) - ring(C, 210, 105, 35) + rect(320, 390, 160, 70)
ph += arc(C, 300, 300, 120, 30, 150) + rect(40, 410, 210, 150, 55) + rect(550, 410, 210, 150, 55)
gs.add("telephone", "X", [0x260E], ph, "telephone")
boat = poly([(40, 170), (760, 170), (640, 40), (160, 40)]) + rect(385, 170, 30, 610) + poly([(440, 220), (440, 770), (730, 220)]) + poly([(360, 260), (360, 640), (110, 260)])
gs.add("sailboat", "Y", [0x26F5], boat, "sailboat")
gs.add("moon", "Z", [0x1F319], circ(C, C, 350) - circ(570, 520, 290), "moon")

# ---------------------------------------------------------------- digits
tree = circ(C, 530, 220) + circ(260, 420, 155) + circ(540, 420, 155) + circ(C, 360, 150) + rect(355, 40, 90, 300, 10)
gs.add("tree", "1", [0x1F333], tree, "tree")
cas = rect(200, 40, 400, 450) + rect(50, 40, 190, 600) + rect(560, 40, 190, 600)
for x in (50, 120, 190, 560, 630, 700):
    cas += rect(x, 630, 50, 80)
for x in (240, 320, 400, 480):
    cas += rect(x + 15, 480, 45, 70)
cas -= rect(325, 40, 150, 170) + circ(C, 210, 75) + rect(120, 430, 50, 100, 25) + rect(630, 430, 50, 100, 25)
gs.add("castle", "2", [0x1F3F0], cas, "castle")
ship = poly([(30, 270), (770, 270), (650, 50), (150, 50)]) + rect(200, 290, 400, 150) + rect(290, 460, 90, 210) + rect(430, 460, 90, 210)
for x in (230, 330, 430, 530):
    ship -= circ(x, 170, 32)
ship -= rect(250, 350, 300, 40)
gs.add("ship", "3", [0x1F6A2], ship, "ship")
tram = rect(140, 110, 520, 520, 60) - rect(195, 360, 180, 190, 15) - rect(425, 360, 180, 190, 15) - rect(320, 180, 160, 30, 15)
tram += pline([(C, 630), (290, 710), (C, 780)], 35, True) + rect(60, 765, 680, 30, 15) + rect(190, 40, 90, 90, 20) + rect(520, 40, 90, 90, 20)
gs.add("tram", "4", [0x1F68B], tram, "tram")
br = rect(20, 240, 760, 60) + rect(180, 60, 70, 660) + rect(550, 60, 70, 660)
cab = S()
pts = [(215 + (585 - 215) * i / 20, 0) for i in range(21)]
pts = [(x, 330 + 390 * ((x - 400) / 185) ** 2) for x, _ in pts]
cab += pline(pts, 30, True)
cab += pline([(215, 715), (110, 600), (20, 300)], 30, True) + pline([(585, 715), (690, 600), (780, 300)], 30, True)
for x in (290, 340, 400, 460, 510):
    yy = 330 + 390 * ((x - 400) / 185) ** 2
    cab += rect(x - 10, 290, 20, yy - 290)
gs.add("bridge", "5", [0x1F309], br + cab, "bridge")
bat = rect(40, 200, 660, 400, 50) - rect(95, 255, 550, 290, 20) + rect(700, 320, 70, 160, 20)
bat += rect(130, 290, 140, 220, 10) + rect(300, 290, 140, 220, 10)
gs.add("battery", "6", [0x1F50B], bat, "battery")
pk = rect(270, 160, 110, 480) + (rect(270, 370, 330, 270, 135) - rect(380, 460, 135, 90, 45)) + rect(270, 370, 150, 270)
gs.add("parking", "7", [0x1F17F], rect(50, 50, 700, 700, 100) - pk, "parking")
stop = rect(370, 30, 60, 470) + circ(C, 590, 190) - rect(300, 520, 200, 150, 25) + rect(320, 585, 160, 50) + circ(345, 500, 0.1)
gs.add("busStop", "8", [0x1F68F], stop, "bus stop")
wr = line(170, 170, 520, 520, 110, True) + circ(580, 580, 170)
wr -= rect(580 - 60, 580, 120, 300).rot(-45, 580, 580) + circ(170, 170, 30)
gs.add("wrench", "9", [0x1F527], wr, "wrench")
wave = [(190 + 520 * i / 24, 760 - 40 * math.sin(math.pi * 2 * i / 24)) for i in range(25)]
flag = rect(130, 30, 60, 750, 20) + poly(wave + [(p[0], p[1] - 330) for p in reversed(wave)])
gs.add("flag", "0", [0x2691], flag, "flag")

if __name__ == "__main__":
    import preview
    out = build(gs, "DingThats Objects", "DingThatsObjects", "build/fonts")
    export_svgs(gs, "build/svg/objects")
    preview.specimen(gs, out["ttf"], "build/objects_specimen.png", "DingThats Objects")
    print(len(gs.glyphs), out)
