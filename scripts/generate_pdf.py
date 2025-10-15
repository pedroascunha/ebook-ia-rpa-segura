# Gera PDF A4 a partir de chapters/*.md e assets/capa.png
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from pathlib import Path

TITLE = "IA e RPA: O Futuro da Automação Inteligente e seus Impactos na Carreira"
SUBTITLE = "Como Inteligência Artificial e RPA estão transformando o trabalho e criando novas oportunidades"
AUTHOR = "por Pedro Cunha"
FOOTER = "Pedro Cunha – IA & RPA Segura"

ROOT = Path(__file__).resolve().parents[1]
CH_DIR = ROOT / "chapters"
OUT_PDF = ROOT / "ebook-ia-rpa-futuro-automacao.pdf"
CAPA = ROOT / "assets" / "capa.png"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="H1", parent=styles["Heading1"], textColor=colors.HexColor("#1546C6")))
styles.add(ParagraphStyle(name="Body", parent=styles["Normal"], leading=16))
styles.add(ParagraphStyle(name="Sub", parent=styles["Heading2"], textColor=colors.HexColor("#189956")))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#0a3a2a"))
    canvas.drawRightString(A4[0]-1.5*cm, 1*cm, FOOTER)
    canvas.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(str(OUT_PDF), pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    story = []
    if CAPA.exists():
        story.append(Image(str(CAPA), width=16*cm, height=16*cm))
        story.append(Spacer(1, 0.8*cm))

    story.append(Paragraph(f"<b>IA e RPA: O Futuro da Automação Inteligente e seus Impactos na Carreira</b>", styles["H1"]))
    story.append(Paragraph(SUBTITLE, styles["Sub"]))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(AUTHOR, styles["Body"]))
    story.append(PageBreak())

    files = sorted(CH_DIR.glob("*.md"))
    for f in files:
        text = f.read_text(encoding="utf-8")
        for block in text.split("\n\n"):
            block = block.strip()
            if not block:
                story.append(Spacer(1, 0.3*cm))
                continue
            if block.startswith("# "):
                story.append(Paragraph(block[2:], styles["H1"]))
            elif block.startswith("## "):
                story.append(Paragraph(block[3:], styles["Sub"]))
            else:
                story.append(Paragraph(block.replace("\n", "<br/>"), styles["Body"]))
            story.append(Spacer(1, 0.3*cm))
        story.append(PageBreak())

    doc.build(story, onFirstPage=footer, onLaterPages=footer)

if __name__ == "__main__":
    build_pdf()
