from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from textwrap import wrap

def save_story_to_pdf(title: str, story: str, filename: str = "story.pdf"):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER
    margin = 50
    y = height - margin

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, title)
    y -= 30

    # Texto de la historia
    c.setFont("Helvetica", 12)
    line_height = 14
    wrapped_lines = []

    for paragraph in story.split("\n"):
        wrapped_lines.extend(wrap(paragraph, 95))
        wrapped_lines.append("")

    for line in wrapped_lines:
        if y < margin:
            c.showPage()
            y = height - margin
            c.setFont("Helvetica", 12)
        c.drawString(margin, y, line)
        y -= line_height

    c.save()
    print(f"✅ Story saved to: {filename}")
