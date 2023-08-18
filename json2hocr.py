import json
import sys

def json_to_hocr(json_data):
    hocr_markup = []
    # Add hOCR header
    hocr_markup.append("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="$lang" lang="$lang">
  <head>
        <title>Generated hOCR</title>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    </head>
    <body>
    """)

    pages = json_data.get("pages", [])
    for page in pages:
        page_idx = page.get("page_idx", 0)
        dimensions = page.get("dimensions", [0, 0])
        width, height = dimensions

        hocr_markup.append(f"<div class='ocr_page' id='page_{page_idx}' title='image {page_idx}; bbox 0 0 {width} {height}'>")

        blocks = page.get("blocks", [])
        for block in blocks:
            block_geometry = block.get("geometry", [])
            bbox = [int(coord * width) for coord in block_geometry[0]] + [int(coord * height) for coord in block_geometry[1]]
            hocr_markup.append(f"<div class='ocr_carea' id='block_{page_idx}_{bbox[0]}_{bbox[1]}' title='bbox {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}'>")

            lines = block.get("lines", [])
            for line in lines:
                line_geometry = line.get("geometry", [])
                line_bbox = [int(coord * width) for coord in line_geometry[0]] + [int(coord * height) for coord in line_geometry[1]]
                hocr_markup.append(f"<span class='ocr_line' id='line_{page_idx}_{line_bbox[0]}_{line_bbox[1]}' title='bbox {line_bbox[0]} {line_bbox[1]} {line_bbox[2]} {line_bbox[3]}'>")

                words = line.get("words", [])
                for word in words:
                    word_value = word.get("value", "")
                    word_geometry = word.get("geometry", [])
                    word_bbox = [int(coord * width) for coord in word_geometry[0]] + [int(coord * height) for coord in word_geometry[1]]
                    hocr_markup.append(f"<span class='ocrx_word' id='word_{page_idx}_{word_bbox[0]}_{word_bbox[1]}' title='bbox {word_bbox[0]} {word_bbox[1]} {word_bbox[2]} {word_bbox[3]}'>{word_value}</span>")

                hocr_markup.append("</span>")

            hocr_markup.append("</div>")

        hocr_markup.append("</div>")

    # Add hOCR footer
    hocr_markup.append("""
    </body>
    </html>
    """)

    return "\n".join(hocr_markup)

# JSON file path
json_file_path = sys.argv[1]

# Read JSON data from the file
with open(json_file_path, 'r') as json_file:
    sample_json = json.load(json_file)

# Convert JSON to hOCR markup
hocr_output = json_to_hocr(sample_json)
print(hocr_output)
