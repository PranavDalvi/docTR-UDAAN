import json
import os
from pdf2docx import parse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Load JSON data from a file
with open('./Output/test.json', 'r') as json_file:
    json_data = json.load(json_file)



# Create a PDF document
common_output_path = "./Output/"
output_docx = common_output_path + "output.docx"
output_pdf = common_output_path + "output.pdf"
c = canvas.Canvas(output_pdf, pagesize=letter)

# Iterate through the JSON data and add text to PDF
for block in json_data["pages"][0]["blocks"]:
    for line in block["lines"]:
        for word in line["words"]:
            text = word["value"]
            x0, y0 = word["geometry"][0]
            x1, y1 = word["geometry"][1]

            # Convert coordinates to PDF units (assuming 72 dpi)
            x0 *= letter[0]
            y0 = letter[1] - y0 * letter[1]
            x1 *= letter[0]
            y1 = letter[1] - y1 * letter[1]

            # Save the state and set the text position
            c.saveState()
            c.translate(x0, y0)

            # Draw the text
            c.drawString(0, 0, text)

            # Restore the state
            c.restoreState()

# Save the PDF document
c.save()

print(f"PDF created: {output_pdf}")

# convert pdf to docx
parse(output_pdf, output_docx)

os.remove(output_pdf)