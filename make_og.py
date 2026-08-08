#!/usr/bin/env python3
"""OG 画像を作る。★ 生成した抽象背景 + 本物の文字（PIL 合成）。

SD は文字が描けないので、背景だけ imgen で作り、文字はここで正確に載せる。
= ローカル生成が「デザインファーストでは届かない場所」に価値を足す実例。

    python make_og.py   # /tmp/og_bg.png -> assets/og.jpg (1200x630)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG = Path.home() / "AppData/Local/Temp/og_bg.png"
OUT = Path("assets/og.jpg")
W, H = 1200, 630
FONT = "C:/Windows/Fonts/YuGothB.ttc"

# サイトの配色に合わせる
INK = (232, 238, 245)       # 明るい文字
MUTED = (159, 176, 196)     # 弱い文字
TEAL = (34, 184, 207)       # accent（サイトの teal 系）

img = Image.open(BG).convert("RGB")
# cover: 512x512 を 1200x630 に敷き詰めて中央切り出し
scale = max(W / img.width, H / img.height)
img = img.resize((int(img.width * scale) + 1, int(img.height * scale) + 1),
                 Image.LANCZOS)
left = (img.width - W) // 2
top = (img.height - H) // 2
img = img.crop((left, top, left + W, top + H))
# ★ 文字の可読性のため暗くする。左ほど濃く（文字が左寄せなので）
dark = Image.new("L", (W, H), 0)
dd = ImageDraw.Draw(dark)
for x in range(W):
    a = int(150 * (1 - x / W) + 60)      # 左 210 → 右 60
    dd.line([(x, 0), (x, H)], fill=a)
black = Image.new("RGB", (W, H), (4, 12, 22))
img = Image.composite(black, img, dark)
# ほんの少しぼかして地の崩れ文字（SD の癖）を沈める
img = img.filter(ImageFilter.GaussianBlur(0.6))

d = ImageDraw.Draw(img)
title = ImageFont.truetype(FONT, 108)
tag = ImageFont.truetype(FONT, 33)
small = ImageFont.truetype(FONT, 22)

PAD = 84
# 上部: teal の角モチーフ（サイトの反復する形）
d.line([(PAD, 150), (PAD + 34, 150)], fill=TEAL, width=3)
d.line([(PAD, 150), (PAD, 184)], fill=TEAL, width=3)

d.text((PAD, 210), "basrun", font=title, fill=INK)
d.text((PAD, 356), "マクロを置けない文書を、平文の Basic で動かす",
       font=tag, fill=MUTED)
d.text((PAD, 470), ".xlsx / .pptx / .docx を、Office 無しで機械で処理する。",
       font=small, fill=MUTED)
d.text((PAD, 502), "ソースは平文のまま git に置き、実行時にライブラリへ流し込む。",
       font=small, fill=MUTED)

OUT.parent.mkdir(exist_ok=True)
img.save(OUT, quality=86, optimize=True)
kb = OUT.stat().st_size / 1024
print(f"-> {OUT}  {W}x{H}  {kb:.0f}KB")
