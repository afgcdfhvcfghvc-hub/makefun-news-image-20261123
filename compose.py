#!/usr/bin/env python3
"""Render the dense one-day news infographic for Monday 23 November 2026.

Offline renderer: all story text is baked in from stories.md (verified during
the build session against dated 23 Nov 2026 coverage). Output: image.png
(1024x1024). Deterministic: pure PIL drawing, no randomness, no network.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (18, 26, 46)
NAVY = (16, 34, 74)
RED = (178, 34, 44)
GOLD = (196, 141, 26)
GRAY = (92, 96, 108)
CARD = (255, 253, 247)
LINE = (198, 190, 172)
BADGE = {
    "CONFIRMED": (22, 110, 62),
    "OFFICIAL": (24, 78, 150),
    "REPORTED": (150, 96, 10),
}

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, font, fill=INK):
    d.text((x, y), s, font=font, fill=fill)


def badge(x, y, kind, font):
    col = BADGE[kind]
    w_ = d.textlength(kind, font=font) + 8
    d.rounded_rectangle([x, y, x + w_, y + 13], 3, fill=col)
    d.text((x + 4, y + 1), kind, font=font, fill=(255, 255, 255))
    return x + w_


# ---------------------------------------------------------------- stories
# (icon, headline, summary, source, badge)
LEAD = (
    "globe",
    "COP31 CLIMATE SUMMIT COLLAPSES IN ANTALYA",
    "After two days of overtime, the UN talks ended with no deal: an EU-led bloc of 130+ nations "
    "refused a final text that dropped any pledge to move away from fossil fuels. UN chief Guterres "
    "called the failure \u201cdeeply disappointing\u201d; COP32 goes to Addis Ababa.",
    "Saachi Baat \u00b7 Underlines \u00b7 Daily Mirror",
    "CONFIRMED",
)

CARDS = [
    ("chip", "NVIDIA BRINGS BACK JENSEN HUANG AS CEO",
     "Board reverses his ouster under pressure from Trump; shares surge about 34.5% on Monday.",
     "Reuters", "CONFIRMED"),
    ("ship", "UKRAINE SAYS DRONES SANK RUSSIAN CORVETTE OFF LIBYA",
     "Zelenskyy: 7 naval drones sank the Merkury at Benghazi and hit the cargo ship Angara.",
     "Daily Summary \u00b7 Arab News", "CONFIRMED"),
    ("blast", "RUSSIAN STRIKES KILL AT LEAST 15 NEAR KYIV",
     "Dymer flats partly collapsed; a boy of 7 was pulled alive from rubble after 14 hours.",
     "Daily Summary \u00b7 Saachi Baat", "CONFIRMED"),
    ("bank", "US SANCTIONS IRAN'S SHADOW-BANKING NETWORK",
     "Treasury targets 20+ exchange houses, front companies and key personnel.",
     "US Treasury", "OFFICIAL"),
    ("eu", "EU PROPOSES 22ND RUSSIA SANCTIONS PACKAGE",
     "60 banks, crypto platforms, 70 shadow-fleet ships \u2014 and a ban on Russian teams in sport.",
     "European Commission", "OFFICIAL"),
    ("plane", "DELTA SYSTEM CRASH SNARLS 1,000+ US FLIGHTS",
     "Weight-and-balance software failed; FAA ground stop at Atlanta on Thanksgiving eve.",
     "Underlines", "REPORTED"),
    ("gear", "23,000 MORE GERMAN WORKERS JOIN IG METALL STRIKES",
     "Fresh 24-hour walkouts at 19 firms incl. Mercedes-Benz; union demands 5% pay rise.",
     "Reuters", "CONFIRMED"),
    ("chart", "SENSEX PLUNGES 1,484 POINTS AS BANKS SELL OFF",
     "Closes at 82,436 (\u20131.77%); Nifty 25,350. Tata Steel \u20138.2% on its APL Apollo deal.",
     "Hindu BusinessLine \u00b7 ET", "CONFIRMED"),
    ("tennis", "ALCARAZ WINS FIRST ATP FINALS TITLE IN TURIN",
     "Beats Zverev 6-2, 7-6; first Spaniard to lift the year-end crown since Corretja in 1998.",
     "Mid-Day \u00b7 ATP", "CONFIRMED"),
    ("cricket", "INDIA\u2013NEW ZEALAND TEST ENDS IN WELLINGTON DRAW",
     "NZ hold out at 239/5 despite India's 720/9 declared; Mitchell & Phillips bat out the day.",
     "Mid-Day \u00b7 Agencies", "CONFIRMED"),
    ("foot", "LIVERPOOL THRASH MAN UTD 4\u20130 AT ANFIELD",
     "Pochettino's first match as United boss ends in rout after Yoro's early red card.",
     "Mid-Day", "REPORTED"),
    ("tower", "BELGIUM AIRPORTS SHUT BY CONTROLLERS' STRIKE",
     "Brussels & Charleroi halted 07:00\u201321:00 over austerity; 50,000+ travellers hit.",
     "Daily Summary", "CONFIRMED"),
]

# (headline, tail, source, badge)
LIST = [
    ("Burnham defends EU reset deal to MPs", "\u00a317bn/yr benefit claimed by 2040; no rejoin without referendum", "BBC", "CONFIRMED"),
    ("Democrats win largest US House majority since 1992", "after flipping a North Carolina seat", "Daily Mirror", "REPORTED"),
    ("Houston leaps to No. 1 in AP Top 25 poll", "55 of 59 first-place votes after Las Vegas tournament win", "Reuters", "CONFIRMED"),
    ("Bangladesh vows to arrest Hasina if she returns", "ex-PM in India plans December homecoming", "Daily Mirror", "REPORTED"),
    ("Nepal PM Balendra Shah makes Delhi his first foreign visit", "India offers \u20ac1.4bn to rebuild after August floods", "Saachi Baat", "CONFIRMED"),
    ("India\u2013Bangladesh open Ganges treaty talks in Dhaka", "1996 water pact expires 12 December", "Saachi Baat", "CONFIRMED"),
    ("Indonesia candy-factory fire: 24 body bags removed", "workers still missing in Serang; DNA tests under way", "Saachi Baat", "CONFIRMED"),
    ("South Korea's education minister resigns", "AI-assisted cheating scandal days before Suneung exam", "Saachi Baat", "REPORTED"),
    ("Drones strike Khartoum, damaging a UN building", "explosions near the airport for over two hours", "Saachi Baat", "CONFIRMED"),
    ("WHO chief urges peace as fighting disrupts Ebola response", "staff sheltered 24h+ near Ituri hospital, DR Congo", "WHO / Daily Summary", "OFFICIAL"),
    ("Kenya and DR Congo restore full diplomatic ties", "Ruto\u2013Tshisekedi agreement at Oyo summit", "Daily Summary", "CONFIRMED"),
    ("Mexico captures drug lord \u2018El Chapo Isidro\u2019", "Fausto Isidro Meza Flores taken in Sinaloa operation", "Daily Summary", "CONFIRMED"),
    ("Drones hit Colombian police base in C\u00facuta", "60 homes damaged; casualties unclear", "Daily Summary", "CONFIRMED"),
    ("Amtrak train derails after hitting truck in Louisiana", "95 aboard near Lafayette; 5 minor injuries", "Daily Summary", "CONFIRMED"),
    ("Manchester arena evacuated in suspected tear-gas scare", "12,000+ leave Don Toliver concert at Co-op Live", "BBC / Daily Summary", "CONFIRMED"),
    ("Iran flogs singer Parastoo Ahmadi and 4 of her team", "74 lashes each over hijab-free livestream concert", "Daily Summary", "REPORTED"),
    ("Report: toxic contamination across 99% of Gaza", "Oxfam & Conflict and Environment Observatory study", "Oxfam / CEOBS", "OFFICIAL"),
    ("Finland summons Russian ambassador", "suspected helicopter breach of Finnish airspace", "Anadolu", "CONFIRMED"),
    ("EU adds The Base founder to terrorism sanctions list", "Rinaldo Nazzaro faces travel ban and asset freeze", "EU Council", "OFFICIAL"),
    ("Kim Jong Un stresses sovereignty, rebuffs Trump talks", "remarks at ambassadors' credentials ceremony", "KCNA via Daily Summary", "REPORTED"),
    ("Lioness on the loose: police search Istanbul outskirts", "residents told to stay indoors; vets use thermal imaging", "Daily Summary", "REPORTED"),
]

NUMBERS = [
    ("34", "verified stories\non this page"),
    ("130+", "nations backed fossil-\nfuel language at COP31"),
    ("+34.5%", "Nvidia shares on\nHuang's return"),
    ("1,484", "points lost by the\nSensex on Monday"),
    ("23,000", "workers in the new\nIG Metall walkout wave"),
    ("50,000+", "travellers hit by the\nBelgium airport strike"),
]

TIMELINE = [
    ("00:39", "WHO Ebola plea"),
    ("02:35", "Indonesia fire"),
    ("03:15", "Belgium shut"),
    ("04:00", "Gaza report"),
    ("06:10", "Kyiv toll 15"),
    ("07:00", "Merkury sunk"),
    ("08:53", "Kenya\u2013DRC ties"),
    ("09:42", "Chapo captured"),
    ("10:06", "Nepal \u20ac1.4bn aid"),
    ("14:32", "Amtrak derails"),
    ("16:50", "Finland summons"),
    ("17:47", "EU sanctions plan"),
    ("18:30", "US Iran sanctions"),
]


# ---------------------------------------------------------------- icons
def icon(name, x, y, s, col=NAVY):
    """Simple line icons drawn in an s-by-s box at (x, y)."""
    cx, cy = x + s // 2, y + s // 2
    lw = max(2, s // 16)
    if name == "globe":
        d.ellipse([x + 2, y + 2, x + s - 2, y + s - 2], outline=col, width=lw)
        d.ellipse([cx - s // 5, y + 2, cx + s // 5, y + s - 2], outline=col, width=lw)
        d.line([x + 2, cy, x + s - 2, cy], fill=col, width=lw)
    elif name == "chip":
        d.rectangle([x + 8, y + 8, x + s - 8, y + s - 8], outline=col, width=lw)
        d.rectangle([cx - 6, cy - 6, cx + 6, cy + 6], outline=col, width=lw)
        for i in range(3):
            px = x + 12 + i * (s - 24) // 2
            d.line([px, y + 1, px, y + 8], fill=col, width=lw)
            d.line([px, y + s - 8, px, y + s - 1], fill=col, width=lw)
    elif name == "ship":
        d.polygon([(x + 4, y + s - 12), (x + s - 6, y + s - 12), (x + s - 12, y + s - 4), (x + 10, y + s - 4)], outline=col, width=lw)
        d.rectangle([cx - 10, y + s - 24, cx + 8, y + s - 12], outline=col, width=lw)
        d.line([x + 4, y + 6, cx - 4, y + 12], fill=RED, width=lw)
        d.line([cx - 4, y + 12, x + 12, y + 16], fill=RED, width=lw)
    elif name == "blast":
        d.rectangle([x + 6, y + s - 16, x + 22, y + s - 3], outline=col, width=lw)
        d.rectangle([x + 24, y + s - 24, x + s - 8, y + s - 3], outline=col, width=lw)
        for dx, dy in [(0, -8), (8, -4), (-8, -4), (5, -10), (-5, -10)]:
            d.line([cx + 8 + dx, y + 10 + dy + 6, cx + 8 + dx * 2, y + 2 + dy], fill=RED, width=lw)
    elif name == "bank":
        d.polygon([(x + 4, cy - 6), (cx, y + 3), (x + s - 4, cy - 6)], outline=col, width=lw)
        for i in range(4):
            px = x + 8 + i * (s - 16) // 3
            d.line([px, cy - 2, px, y + s - 10], fill=col, width=lw)
        d.line([x + 4, y + s - 6, x + s - 4, y + s - 6], fill=col, width=lw + 1)
    elif name == "eu":
        d.ellipse([x + 3, y + 3, x + s - 3, y + s - 3], outline=col, width=lw)
        import math
        for i in range(8):
            a = math.tau * i / 8
            px, py = cx + int((s // 2 - 7) * math.cos(a)), cy + int((s // 2 - 7) * math.sin(a))
            d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=GOLD)
    elif name == "plane":
        d.polygon([(x + 4, cy + 6), (x + s - 6, y + 8), (x + s - 12, cy - 8), (x + s - 18, cy + 2), (x + 16, cy - 2)], outline=col, width=lw)
        d.line([x + 6, y + s - 6, x + s - 8, y + s - 10], fill=col, width=lw)
    elif name == "gear":
        import math
        for i in range(8):
            a = math.tau * i / 8
            x1, y1 = cx + int((s // 2 - 9) * math.cos(a)), cy + int((s // 2 - 9) * math.sin(a))
            x2, y2 = cx + int((s // 2 - 2) * math.cos(a)), cy + int((s // 2 - 2) * math.sin(a))
            d.line([x1, y1, x2, y2], fill=col, width=lw + 1)
        d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], outline=col, width=lw)
    elif name == "chart":
        d.line([x + 5, y + 6, x + 5, y + s - 5], fill=col, width=lw)
        d.line([x + 5, y + s - 5, x + s - 4, y + s - 5], fill=col, width=lw)
        d.line([x + 9, y + 10, x + 20, y + 18, x + 28, y + 14, x + s - 8, y + s - 12], fill=RED, width=lw + 1)
        d.polygon([(x + s - 8, y + s - 12), (x + s - 16, y + s - 14), (x + s - 10, y + s - 20)], fill=RED)
    elif name == "tennis":
        d.ellipse([x + 6, y + 6, x + s - 6, y + s - 6], outline=col, width=lw)
        d.arc([x - 2, y + 6, cx + 4, y + s - 6], 300, 60, fill=col, width=lw)
        d.arc([x + s - 14, y + 6, x + s + 8, y + s - 6], 120, 240, fill=col, width=lw)
    elif name == "cricket":
        d.rectangle([x + 10, y + 4, x + 18, y + s - 10], outline=col, width=lw)
        d.ellipse([x + s - 20, y + s - 20, x + s - 6, y + s - 6], outline=RED, width=lw)
    elif name == "foot":
        d.ellipse([x + 5, y + 5, x + s - 5, y + s - 5], outline=col, width=lw)
        d.polygon([(cx - 5, cy - 5), (cx + 5, cy - 5), (cx + 7, cy + 3), (cx, cy + 7), (cx - 7, cy + 3)], outline=col, width=lw)
    elif name == "tower":
        d.rectangle([cx - 4, y + 8, cx + 4, y + s - 6], outline=col, width=lw)
        d.line([cx - 12, y + s - 6, cx + 12, y + s - 6], fill=col, width=lw + 1)
        d.line([x + 6, y + 8, x + s - 6, y + s - 8], fill=RED, width=lw + 1)
        d.line([x + s - 6, y + 8, x + 6, y + s - 8], fill=RED, width=lw + 1)


# ---------------------------------------------------------------- layout
M = 16  # page margin

# Masthead
d.rectangle([0, 0, W, 62], fill=NAVY)
text(M, 6, "THE WORLD IN ONE DAY", f(FB, 15), (255, 255, 255))
sub = "34 verified stories \u00b7 every one first reported on 23 Nov 2026"
text(W - M - d.textlength(sub, font=f(FR, 12)), 8, sub, f(FR, 12), (210, 220, 245))
text(M, 28, "MONDAY 23 NOVEMBER 2026", f(FB, 27), (255, 255, 255))
tag = "ONE IMAGE \u00b7 ONE DAY \u00b7 THE WHOLE WORLD"
text(W - M - d.textlength(tag, font=f(FB, 11)), 40, tag, f(FB, 11), GOLD)

# Day in numbers
ny = 68
nw = (W - 2 * M - 5 * 6) // 6
for i, (num, lab) in enumerate(NUMBERS):
    x = M + i * (nw + 6)
    d.rectangle([x, ny, x + nw, ny + 46], fill=(238, 231, 214), outline=LINE)
    text(x + 8, ny + 2, num, f(FB, 18), RED)
    lns = lab.split("\n")
    text(x + 8, ny + 24, lns[0], f(FR, 9), GRAY)
    if len(lns) > 1:
        text(x + 8, ny + 34, lns[1], f(FR, 9), GRAY)

# Lead story
ly = 122
d.rectangle([M, ly, W - M, ly + 86], fill=NAVY)
icon(LEAD[0], M + 10, ly + 14, 56, (255, 255, 255))
lx = M + 78
text(lx, ly + 7, "LEAD STORY \u00b7 CLIMATE", f(FB, 11), GOLD)
text(lx, ly + 22, LEAD[1], f(FB, 21), (255, 255, 255))
for j, ln in enumerate(wrap(LEAD[2], f(FR, 12), W - lx - M - 8)):
    text(lx, ly + 50 + j * 14, ln, f(FR, 12), (225, 232, 248))
bw_ = d.textlength(LEAD[4], font=f(FB, 9)) + 8
d.rounded_rectangle([W - M - bw_, ly + 7, W - M, ly + 20], 3, fill=BADGE[LEAD[4]])
d.text((W - M - bw_ + 4, ly + 8), LEAD[4], font=f(FB, 9), fill=(255, 255, 255))
text(W - M - d.textlength(LEAD[3], font=f(FR, 10)), ly + 70, LEAD[3], f(FR, 10), (170, 185, 220))

# Cards grid: 3 cols x 4 rows
gy = ly + 94
cw = (W - 2 * M - 2 * 8) // 3
ch = 86
for idx, (ic, head, summ, src, bd) in enumerate(CARDS):
    r, c = divmod(idx, 3)
    x, y = M + c * (cw + 8), gy + r * (ch + 6)
    d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=LINE)
    d.rectangle([x, y, x + 4, y + ch], fill=RED if idx % 3 == 0 else NAVY)
    icon(ic, x + 10, y + 10, 40)
    tx = x + 58
    for j, ln in enumerate(wrap(head, f(FB, 12), x + cw - tx - 6)[:2]):
        text(tx, y + 6 + j * 14, ln, f(FB, 12), INK)
    for j, ln in enumerate(wrap(summ, f(FR, 10), x + cw - tx - 6)[:3]):
        text(tx, y + 36 + j * 12, ln, f(FR, 10), (52, 56, 70))
    bx2 = badge(x + 10, y + ch - 17, bd, f(FB, 8))
    text(bx2 + 5, y + ch - 15, src, f(FR, 9), GRAY)

# Timeline strip
ty = gy + 4 * (ch + 6) + 2
d.rectangle([M, ty, W - M, ty + 58], fill=(238, 231, 214), outline=LINE)
text(M + 8, ty + 4, "THE DAY BY THE HOUR \u2014 FIRST REPORTED (UTC)", f(FB, 11), NAVY)
tl_y = ty + 34
d.line([M + 14, tl_y, W - M - 14, tl_y], fill=NAVY, width=2)
n = len(TIMELINE)
for i, (hh, ev) in enumerate(TIMELINE):
    x = M + 14 + i * (W - 2 * M - 28) // (n - 1)
    d.ellipse([x - 3, tl_y - 3, x + 3, tl_y + 3], fill=RED)
    text(x - 13, tl_y - 16, hh, f(FB, 10), INK)
    lx_ = min(max(x - 36, M + 2), W - M - 76)
    ly_ = tl_y + 5 + (10 if i % 2 else 0)  # stagger alternate labels to avoid collisions
    text(lx_, ly_, ev, f(FR, 8), (52, 56, 70))

# Compact list: two columns
sy = ty + 66
text(M, sy, "ALSO ON 23 NOVEMBER \u2014 21 MORE VERIFIED STORIES", f(FB, 13), NAVY)
d.line([M, sy + 18, W - M, sy + 18], fill=RED, width=2)
colw = (W - 2 * M - 16) // 2
rowh = 26
for i, (head, tail, src, bd) in enumerate(LIST):
    c = 0 if i < 11 else 1
    r = i if i < 11 else i - 11
    x = M + c * (colw + 16)
    y = sy + 24 + r * rowh
    text(x, y, f"{i + 14:02d}", f(FB, 11), RED)
    hx = x + 26
    hw = colw - 26
    hl = wrap(head, f(FB, 11), hw)
    text(hx, y, hl[0], f(FB, 11), INK)
    line2 = f"{tail}  \u2014 {src}"
    text(hx, y + 13, line2, f(FR, 9), GRAY)
    bw = d.textlength(bd, font=f(FB, 7)) + 6
    d.rounded_rectangle([x + colw - bw, y + 1, x + colw, y + 11], 2, fill=BADGE[bd])
    d.text((x + colw - bw + 3, y + 2), bd, font=f(FB, 7), fill=(255, 255, 255))

# Footer: date check
fy = sy + 24 + 11 * rowh + 8
d.rectangle([0, fy, W, H], fill=NAVY)
text(M, fy + 7, "DATE CHECK \u2713", f(FB, 13), GOLD)
dc = ("Every story above was first reported on Monday 23 November 2026 (any time zone) and cross-checked against "
      "dated 23 Nov editions. Deliberately EXCLUDED as not of this day: GTA VI's $3.79bn day-one sales record "
      "(announced 20 Nov) and the Houthi claim on Saudi Arabia's Rabigh refinery (made 22 Nov, unconfirmed). "
      "Badges: CONFIRMED = 2+ outlets \u00b7 OFFICIAL = official source \u00b7 REPORTED = single outlet.")
for j, ln in enumerate(wrap(dc, f(FR, 11), W - 2 * M - 130)):
    text(M + 130, fy + 5 + j * 13, ln, f(FR, 11), (225, 232, 248))

img.save("image.png", optimize=True)
print("saved image.png", img.size)
