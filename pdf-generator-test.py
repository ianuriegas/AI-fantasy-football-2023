from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a new PDF document
pdf_filename = "styled_document.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Define custom styles
styles = getSampleStyleSheet()
custom_style = ParagraphStyle(name="CustomStyle",
                              fontSize=14,
                              textColor=colors.red,
                              leading=16)

# Content for the PDF
content = []
content.append(Paragraph("Styled PDF Example", styles['Title']))
content.append(Paragraph("This is a paragraph with custom styling.", custom_style))
content.append(Paragraph("This is another paragraph with default styling.", styles['Normal']))

# Build the PDF document with the content
doc.build(content)
