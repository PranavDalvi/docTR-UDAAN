import os
import sys
# Let's pick the desired backend
# os.environ['USE_TF'] = '1'
# pip install "python-doctr[torch]"
# pip install rapidfuzz==2.15.1
os.environ['USE_TORCH'] = '1'

import matplotlib.pyplot as plt

from doctr.io import DocumentFile
# from doctr.models import ocr_predictor
from doctr.models import kie_predictor



# Image File

doc = DocumentFile.from_images(sys.argv[1])
print(f"Number of pages: {len(doc)}")

# Instantiate a pretrained model
# predictor = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
model = kie_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)

# Display the architecture
# print(predictor)

# result = predictor(doc)
result = model(doc)

# result.show(doc)

synthetic_pages = result.synthesize()
# plt.imshow(synthetic_pages[0]); plt.axis('off');plt.show()

#Exporting results

json_export = result.export()
print(json_export)


xml_output = result.export_as_xml()
for output in xml_output:
    xml_bytes_string = output[0]
    xml_element = output[1]

output_file = sys.argv[2]+'.xml'
with open(output_file, 'wb') as file:
    file.write(xml_bytes_string)
