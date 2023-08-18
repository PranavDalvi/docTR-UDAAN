from pdf2image import convert_from_path
import sys

def extract_pdf_as_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image_path = f"{output_folder}/page_{i + 1}.jpg"
        image.save(image_path, "JPEG")

pdf_path = sys.argv[1]
output_folder = sys.argv[2]

extract_pdf_as_images(pdf_path, output_folder)