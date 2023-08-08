from bs4 import BeautifulSoup
from docx import Document
import sys

def xml_to_docx():
    # Read the XML file
    with open(sys.argv[1], "r", encoding="utf-8") as xml_file:
        soup = BeautifulSoup(xml_file,"xml")
    
    # Create a new Docx document
    doc = Document()

    # Find all p tags with class ocr_par
    par_tags = soup.find_all("p", class_="ocr_par")

    for par_tag in par_tags:
        # find all span tags with class ocr_line
        line_spans = par_tag.find_all('span', class_='ocr_line')

        # Extract all line_span (ocr_line)
        paragraph_text = []
        for line_span in line_spans:
            # Find all the span tags with class ocrx_word which is our text
            word_spans = line_span.find_all("span", class_="ocrx_word")

            # Extract text from each word span
            line_words = []
            for word_span in word_spans:
                word_text = word_span.get_text().strip()
                line_words.append(word_text)
            
            # Concat the words to form the line
            line = " ".join(" ".join(line_words).split())
            paragraph_text.append(line)
        
        # Concat the lines to form the paragraph
        paragraph = " ".join(paragraph_text)
        doc.add_paragraph(paragraph)

    # Save the Docx document
    output_file = sys.argv[2]
    doc.save(output_file+'.docx')

xml_to_docx()