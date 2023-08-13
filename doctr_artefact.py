import os 
os.environ["USE_TORCH"] = "1"

import argparse
import logging
import numpy as np

import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import torch

from doctr.io.image import read_img_as_tensor
from doctr.models import obj_detection

# Detected classes
CLASSES = ["__background__", "QR Code", "Barcode", "Logo", "Photo"]

# Color map for each class