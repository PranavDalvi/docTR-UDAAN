import json
from docx import Document
from docx.shared import Pt

# Load JSON data from a file
with open('./Output/test.json', 'r') as json_file:
    json_data = json.load(json_file)

def docx_converter(json_response):
  doc=Document()
  style=doc.styles['Normal']
  font=style.font
  font.size=Pt(8)
  for pages in json_response['pages']:
        y,x=pages['dimensions']
        prev=0
        prevxl=0
        prevxh=0
        flag=True
        sentence=' '
        for blocks in pages['blocks']:
            for lines in blocks['lines']:
                ((xl,yl),(xh,yh))=lines['geometry']
                if abs(int(yl*y)-prev)>10:
                    if(flag):
                        sentence=""
                        flag=False
                    else:
                        # print(sentence)
                        p=doc.add_paragraph(sentence)
                        if (prevxl+prevxh)/2<x/3:
                            p.alignment=0
                        elif (prevxl+prevxh)/2<2*x/3:
                            p.alignment=1
                        else:
                            p.alignment=2
                        sentence=""
                prev=int(yl*y)
                prevxl=int(xl*x)
                prevxh=int(xh*x)
                
                for words in lines['words']:
                    sentence+=f' {words["value"]}'
  doc.save(f'output_doc.docx')

docx_converter(json_data)