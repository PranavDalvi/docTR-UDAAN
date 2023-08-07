import os
import sys
# Let's pick the desired backend
# os.environ['USE_TF'] = '1'
# pip install "python-doctr[torch]"
# pip install rapidfuzz==2.15.1
os.environ['USE_TORCH'] = '1'

import matplotlib.pyplot as plt

from doctr.io import DocumentFile
from doctr.models import ocr_predictor



# PDF File
doc = DocumentFile.from_pdf(sys.argv[1])
print(f"Number of pages: {len(doc)}")

# Instantiate a pretrained model
predictor = ocr_predictor(pretrained=True)

# Display the architecture
# print(predictor)

result = predictor(doc)

# result.show(doc)

synthetic_pages = result.synthesize()
# plt.imshow(synthetic_pages[0]); plt.axis('off');plt.show()

#Exporting results

# json_export = result.export()
# print(json_export)


xml_output = result.export_as_xml()
# print(xml_output[0][0])

output_file = sys.argv[2]+'.xml'
with open(output_file, 'wb') as file:
    file.write(xml_output[0][0])
