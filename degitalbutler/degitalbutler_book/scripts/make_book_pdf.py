# -*- coding: utf-8 -*-
"""
Digital Butler Book – AI秘書書籍出版計画 / 日本語版
Python 3.13 / ReportLab 4.2+
"""
import os
from reportlab.lib.pagesizes import A5, portrait
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from markdown import markdown
from utils.style_config import chapter_title_style, body_text_style, header_style

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "outputs", "digital_butler_book.pdf")
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

def header(canvas, doc):
    canvas.saveState()
    canvas.setFont("HeiseiKakuGo-W5", 7)
    canvas.setFillColorRGB(0.69, 0.54, 0.24)  # gold
    canvas.drawCentredString(A5[0]/2, A5[1]-15, "Digital Butler Book – AI秘書の哲学")
    canvas.restoreState()

def build_story():
    story = []
    files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md")])
    if not files:
        story.append(Paragraph("準備中 / Coming Soon", chapter_title_style))
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph("Obsidianで章ファイルを作成してから再ビルドしてください。", body_text_style))
        return story
    for file in files:
        chapter_title = file.replace("_", " ").replace(".md", "")
        with open(os.path.join(CHAPTERS_DIR, file), "r", encoding="utf-8") as f:
            html = markdown(f.read())
        story.append(Paragraph(chapter_title, chapter_title_style))
        story.append(Spacer(1, 0.2*cm))
        story.append(Paragraph(html, body_text_style))
        story.append(PageBreak())
    return story

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=portrait(A5),
        topMargin=1.5*cm, bottomMargin=1.5*cm,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
    )
    story = build_story()
    doc.build(story, onFirstPage=header, onLaterPages=header)
    print(f"✅ PDF: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
