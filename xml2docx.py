# pip install lxml
# pip install beautifulsoup4
# pip install python-docx
# How to run => python3 xml2docx.py input_filename.xml output_filename

from bs4 import BeautifulSoup
from docx import Document
import sys

def xml_to_docx():
    # Read the XML file
    with open(sys.argv[1]) as xml_file:
        soup = BeautifulSoup(xml_file, 'xml')
    
    # Create a new DOCX document
    doc = Document()

    # Find all the <span> tags and extract their text
    span_tags = soup.find_all('span')
    extracted_text = ' '.join(tag.get_text() for tag in span_tags)

    # Add the extracted text to the DOCX document as paragraphs
    doc.add_paragraph(extracted_text)

    # Save the DOCX document to the output file
    output_file = sys.argv[2]
    doc.save(output_file+".docx")

xml_to_docx()