#!/usr/bin/env python3
"""Render THE WORLD DAILY front page for Thursday 26 November 2026.

Draws a 1024x1024 newspaper poster of the day's real world news with Pillow.
Deterministic: no timestamps, no randomness, fixed fonts and layout.
Run: python3 draw.py  -> writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
GREY = (90, 86, 78)
RULE = (60, 58, 52)
BLUE = (24, 62, 110)
TEAL = (14, 94, 84)
GOLD = (176, 128, 24)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, word by word."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, leading, color=INK):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def hline(draw, x0, x1, y, width=2, color=RULE):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def draw_refinery(draw, x, y, w, h):
    """Stylised oil refinery at dusk with a rising price arrow."""
    # sky
    draw.rectangle([x, y, x + w, y + h], fill=(30, 38, 58))
    # sun / glow
    draw.ellipse([x + w - 78, y + 14, x + w - 28, y + 64], fill=(232, 148, 52))
    # ground
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(16, 20, 30))
    # tanks
    draw.rectangle([x + 18, y + h - 92, x + 78, y + h - 26], fill=(74, 88, 110))
    draw.rectangle([x + 18, y + h - 100, x + 78, y + h - 92], fill=(96, 110, 134))
    # distillation towers
    for tx, th in ((96, 128), (128, 148), (168, 118)):
        top = y + h - 26 - th
        draw.rectangle([x + tx, top, x + tx + 22, y + h - 26],
                       fill=(58, 70, 92))
        draw.polygon([(x + tx, top), (x + tx + 11, top - 14),
                      (x + tx + 22, top)], fill=(58, 70, 92))
    # flame on the flare stack only (tower flames clashed with the price label)
    # flare stack
    draw.rectangle([x + 210, y + h - 150, x + 222, y + h - 26], fill=(58, 70, 92))
    f2 = y + h - 150
    draw.polygon([(x + 205, f2), (x + 216, f2 - 20),
                  (x + 227, f2)], fill=(255, 176, 32))
    # rising price arrow (red, over the sky)
    pts = [(x + 14, y + h - 60), (x + 90, y + h - 96),
           (x + 150, y + h - 78), (x + 225, y + h - 128),
           (x + 300, y + h - 150)]
    draw.line(pts, fill=(232, 64, 48), width=7, joint="curve")
    draw.polygon([(x + 300, y + h - 150), (x + 272, y + h - 150),
                  (x + 300, y + h - 124)], fill=(232, 64, 48))
    draw.text((x + 14, y + 10), "BRENT $94.61", font=font(SANS_B, 26),
              fill=(255, 255, 255))
    draw.text((x + 14, y + 42), "+3.5% on the day", font=font(SANS, 22),
              fill=(214, 214, 214))


STORIES = [
    ("TRADE", RED, "US proposes new tariffs on 14 partners",
     "Washington proposed tariffs of up to 15% on 14 partners to fight "
     "factory overcapacity."),
    ("SECURITY", DARKRED, "Kim orders wider tactical nuclear deployment",
     "Kim Jong Un said North Korea should deploy tactical nuclear weapons "
     "across more domains."),
    ("MIDDLE EAST", BLUE, "Israeli strike kills senior Hamas official in Gaza",
     "Israel killed Hamas colonel Mohammad Abuelouf, his wife and two "
     "children. The ceasefire is strained."),
    ("ASIA", TEAL, "Nine dead, 17 trapped in Indonesia mine flood",
     "Floodwater swept into an unauthorised gold mine in Bogor, West Java. "
     "Nine dead, 17 still trapped."),
    ("AFRICA", DARKRED, "Sudan drone strikes kill 19 civilians",
     "Drone strikes in Sudan's Blue Nile state killed 19 civilians, "
     "reports said."),
    ("EUROPE", BLUE, "Ukraine hits Russian air base; five planes damaged",
     "Ukraine said it struck a major Russian air base, damaging five "
     "aircraft."),
    ("INDIA", GOLD, "India marks Constitution Day, 18 years since 26/11",
     "India marked 77 years of its Constitution and 18 years since the "
     "2008 Mumbai attacks."),
    ("SPORT", TEAL, "Chess title match opens in Geneva",
     "World champion D Gukesh faces Javokhir Sindarov for the title. "
     "The opener was drawn."),
]


def story_block(draw, x, y, w, tag, color, head, body):
    draw.text((x, y), tag, font=font(SANS_B, 16), fill=color)
    y += 22
    y = para(draw, x, y, head, font(SERIF_B, 23), w, 27)
    y += 2
    y = para(draw, x, y, body, font(SANS, 18), w, 23, color=(38, 36, 32))
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36
    rx = W - mx

    # --- top dateline bar ---
    d.text((mx, 14), "THURSDAY, 26 NOVEMBER 2026", font=font(SANS_B, 19), fill=INK)
    d.text((rx, 14), "No. 330  •  WORLD EDITION", font=font(SANS, 19),
           fill=GREY, anchor="ra")
    hline(d, mx, rx, 44, 2)

    # --- masthead (scaled to fit the page width) ---
    msize = 96
    while True:
        mast = font(SERIF_B, msize)
        if d.textlength("THE WORLD DAILY", font=mast) <= rx - mx:
            break
        msize -= 2
    d.text((W // 2, 52), "THE WORLD DAILY", font=mast, fill=INK, anchor="ma")
    hline(d, mx, rx, 158, 4)
    hline(d, mx, rx, 164, 1)
    d.text((W // 2, 172), "ONE DAY'S WORLD NEWS  —  THURSDAY 26 NOVEMBER 2026",
           font=font(SANS_B, 20), fill=RED, anchor="ma")
    hline(d, mx, rx, 202, 1)

    # --- lead story ---
    ly = 214
    d.text((mx, ly), "MIDDLE EAST  •  ENERGY", font=font(SANS_B, 18), fill=RED)
    ly += 26
    # fixed two-line headline (no wrap surprises)
    lead_f = font(SERIF_B, 34)
    d.text((mx, ly), "Houthis claim strike on Saudi", font=lead_f, fill=INK)
    ly += 46
    d.text((mx, ly), "refinery as oil tops $94", font=lead_f, fill=INK)
    ly += 46
    ly += 6
    ly = para(d, mx, ly,
              "Yemen's Houthis said they attacked Saudi Arabia's Ras Tanura "
              "refinery and Riyadh's financial district, sending Brent crude "
              "up 3.5% to $94.61 a barrel.",
              font(SANS, 20), 580, 27, color=(38, 36, 32))
    # illustration panel, right of lead text
    draw_refinery(d, 636, 214, 352, 210)
    d.text((636, 430), "Ras Tanura refinery, Saudi Arabia.  Photo: illustration.",
           font=font(SANS, 15), fill=GREY)
    hline(d, mx, rx, 456, 2)

    # --- grid of eight stories, 2 columns x 4 rows ---
    col_w = (rx - mx - 28) // 2
    row_h = 118
    gy = 470
    for i, (tag, color, head, body) in enumerate(STORIES):
        cx = mx + (i % 2) * (col_w + 28)
        cy = gy + (i // 2) * row_h
        story_block(d, cx, cy, col_w, tag, color, head, body)
        if i % 2 == 0:
            d.line([(mx + col_w + 14, cy + 4), (mx + col_w + 14, cy + row_h - 12)],
                   fill=(200, 194, 182), width=1)

    # --- footer ---
    fy = 962
    hline(d, mx, rx, fy, 2)
    d.text((W // 2, fy + 10),
           "Sources: Reuters, AP, CNN, KCNA.  All stories happened or were first",
           font=font(SANS, 16), fill=GREY, anchor="ma")
    d.text((W // 2, fy + 30),
           "reported on Thursday 26 November 2026.  THE WORLD DAILY  •  Page 1",
           font=font(SANS, 16), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
