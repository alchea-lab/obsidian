# -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER

COLOR_GOLD = colors.HexColor("#B08A3E")
COLOR_BLACK = colors.HexColor("#1B1B1B")

chapter_title_style = ParagraphStyle(
    "ChapterTitle",
    fontName="HeiseiKakuGo-W5",  # 日本語OK（内蔵CIDフォント）
    fontSize=16,
    leading=20,
    textColor=COLOR_GOLD,
    alignment=TA_LEFT,
    spaceAfter=8,
    underlineWidth=0.5,
)
body_text_style = ParagraphStyle(
    "BodyText",
    fontName="HeiseiKakuGo-W5",
    fontSize=9,
    leading=13,
    textColor=COLOR_BLACK,
    alignment=TA_JUSTIFY,
    spaceAfter=6,
)
header_style = ParagraphStyle(
    "Header",
    fontName="HeiseiKakuGo-W5",
    fontSize=7,
    textColor=COLOR_GOLD,
    alignment=TA_CENTER,
)
