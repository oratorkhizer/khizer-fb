#!/usr/bin/env python3
"""Branded Facebook post-graphic engine for Dr. Khizer."""
from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1080
# palette
TEAL   = (31, 92, 110)
TEAL2  = (46, 139, 158)
DARK   = (28, 46, 54)
BG     = (246, 250, 251)
SOFT   = (228, 240, 242)
AMBER  = (244, 162, 0)
REDBG  = (250, 232, 230)
RED    = (176, 0, 32)
WHITE  = (255, 255, 255)
GREY   = (110, 122, 128)
GREENL = (232, 244, 238)
GREEN  = (30, 122, 90)

FD = "/usr/share/fonts/truetype/dejavu"
def F(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)
# font shortcuts
def bold(s):  return F("DejaVuSans-Bold.ttf", s)
def reg(s):   return F("DejaVuSans.ttf", s)
def serif(s): return F("DejaVuSerif.ttf", s)
def serifb(s):return F("DejaVuSerif-Bold.ttf", s)

def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= max_w:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def draw_text_block(draw, text, font, x, y, max_w, fill, line_gap=10, center=False, cx=None):
    lines = wrap(draw, text, font, max_w)
    asc, desc = font.getmetrics()
    lh = asc + desc + line_gap
    for ln in lines:
        if center:
            tw = draw.textlength(ln, font=font)
            draw.text((cx - tw/2, y), ln, font=font, fill=fill)
        else:
            draw.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def accent_rgb(name):
    return {"teal":TEAL, "red":RED, "amber":AMBER, "green":GREEN}.get(name, TEAL)

def header(img, draw, kicker, accent):
    ac = accent_rgb(accent)
    # top band
    draw.rectangle([0,0,W,150], fill=ac)
    # small medical motif: plus in a circle
    cx, cy, r = 78, 75, 30
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], outline=WHITE, width=5)
    draw.rectangle([cx-14,cy-5,cx+14,cy+5], fill=WHITE)
    draw.rectangle([cx-5,cy-14,cx+5,cy+14], fill=WHITE)
    # kicker text (letter-spaced)
    f = bold(38)
    txt = "  ".join(list(kicker)) if len(kicker) <= 16 else kicker
    draw.text((132, 52), kicker.upper(), font=bold(40), fill=WHITE)

def footer(img, draw):
    draw.rectangle([0,H-92,W,H], fill=DARK)
    left = "Dr Khizer Hussain Junaidy"
    right = "Caspian Healthcare"
    # auto-fit both so they never overlap
    lf, rf = bold(28), reg(27)
    while draw.textlength(left, font=lf) + draw.textlength(right, font=rf) + 90 > W-100:
        lf = bold(lf.size-1); rf = reg(rf.size-1)
    ly = H-46 - (lf.getmetrics()[0]//2)
    draw.text((55, H-62), left, font=lf, fill=WHITE)
    # small amber tick before hospital name
    rw = draw.textlength(right, font=rf)
    dot_x = W-55-rw-24
    draw.ellipse([dot_x, H-56, dot_x+12, H-44], fill=AMBER)
    draw.text((W-55-rw, H-61), right, font=rf, fill=(205,217,221))

def base(kicker, accent):
    img = Image.new("RGB", (W,H), BG)
    d = ImageDraw.Draw(img)
    # subtle corner accent
    header(img, d, kicker, accent)
    footer(img, d)
    return img, d

def render(spec, out):
    layout = spec["layout"]
    accent = spec.get("accent","teal")
    ac = accent_rgb(accent)
    img, d = base(spec["kicker"], accent)

    if layout == "myth":
        # MYTH box
        y = 210
        draw_text_block(d, "MYTH", bold(34), 60, y, W-120, RED);
        y += 54
        # red rounded box
        mlines = wrap(d, spec["myth"], bold(46), W-180)
        box_h = 40 + len(mlines)*66 + 20
        d.rounded_rectangle([60,y,W-60,y+box_h], radius=28, fill=REDBG)
        yy = y+34
        for ln in mlines:
            d.text((100, yy), ln, font=bold(46), fill=(120,20,30)); yy += 66
        y += box_h + 46
        # FACT
        draw_text_block(d, "THE FACT", bold(34), 60, y, W-120, TEAL); y += 54
        flines = wrap(d, spec["fact"], reg(40), W-180)
        box_h2 = 34 + len(flines)*58 + 20
        d.rounded_rectangle([60,y,W-60,y+box_h2], radius=28, fill=SOFT)
        yy = y+30
        for ln in flines:
            d.text((100, yy), ln, font=reg(40), fill=DARK); yy += 58

    elif layout == "list":
        y = 200
        # headline
        y = draw_text_block(d, spec["headline"], bold(54), 60, y, W-120, DARK, line_gap=6)
        y += 26
        lines = spec["lines"]
        chip = ac
        for i, item in enumerate(lines, 1):
            # number/check chip
            d.rounded_rectangle([60, y+4, 116, y+60], radius=14, fill=chip)
            num = str(i)
            nf = bold(36)
            nw = d.textlength(num, font=nf)
            d.text((88-nw/2, y+12), num, font=nf, fill=WHITE)
            # item text
            end_y = draw_text_block(d, item, reg(38), 140, y+6, W-200, DARK, line_gap=6)
            y = max(end_y, y+72) + 14

    elif layout == "quote":
        # big quotation mark
        d.text((60, 176), "“", font=serifb(200), fill=(ac[0],ac[1],ac[2]))
        q = spec["quote"]
        f = serif(54)
        lines = wrap(d, q, f, W-160)
        total_h = len(lines)*78
        y = max(360, (H-total_h)//2 - 30)
        for ln in lines:
            tw = d.textlength(ln, font=f)
            d.text((W/2 - tw/2, y), ln, font=f, fill=DARK); y += 78
        y += 24
        attrib = spec.get("attrib","— Dr. Khizer")
        af = bold(34)
        tw = d.textlength(attrib, font=af)
        d.text((W/2 - tw/2, y), attrib, font=af, fill=TEAL2)

    img.save(out, "PNG")
    return out

if __name__ == "__main__":
    samples = [
        {"layout":"myth","kicker":"Myth vs Fact","accent":"teal",
         "myth":"“Diabetes is caused by eating too much sugar.”",
         "fact":"Type 2 diabetes is mainly about how the body handles insulin over years — genetics, weight, activity and sleep. Sugar is one piece, not the whole story."},
        {"layout":"list","kicker":"Warning Signs","accent":"red",
         "headline":"5 signs a parent’s diabetes is NOT under control",
         "lines":["Waking 2–3 times at night to pass urine",
                  "Unusual thirst or a dry mouth",
                  "Tiredness or sleepiness after meals",
                  "Slow-healing cuts, or tingling feet",
                  "Blurred vision that comes and goes"]},
        {"layout":"quote","kicker":"For the Caregiver","accent":"amber",
         "quote":"You can’t pour from an empty cup. An exhausted caregiver can’t give good care.",
         "attrib":"— Dr. Khizer"},
    ]
    os.makedirs("samples", exist_ok=True)
    for i,s in enumerate(samples,1):
        render(s, f"samples/sample_{i}.png")
    print("samples rendered")
