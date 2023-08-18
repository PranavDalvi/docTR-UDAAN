import json
from PIL import Image, ImageDraw

# Load your JSON OCR data here
with open('./Output/sic_test_4.json', 'r') as json_file:
    ocr_data = json.load(json_file)

# Create a new image canvas with white background
image_width, image_height = ocr_data['pages'][0]['dimensions']
image = Image.new('RGB', (image_width, image_height), 'white')
draw = ImageDraw.Draw(image)

# Loop through the blocks, lines, and words to draw them on the image
for block in ocr_data['pages'][0]['blocks']:
    for line in block['lines']:
        for word in line['words']:
            bbox = word['geometry']
            bbox_pixels = [
                (int(image_width * bbox[0][0]), int(image_height * bbox[0][1])),
                (int(image_width * bbox[1][0]), int(image_height * bbox[1][1]))
            ]
            draw.rectangle(bbox_pixels, outline='red')  # Draw bounding box
            draw.text((bbox_pixels[0][0], bbox_pixels[0][1]), word['value'], fill='blue')  # Draw text

# Save or display the image
image.save('output_image.png')
# image.show()
