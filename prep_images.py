import numpy as np
from PIL import ImageOps
from PIL import Image
from matplotlib.pyplot import figure
import os

wid = 1024
hei = 1024

from_path = 'D:/art/wikiart3_cropped/'
to_path = 'D:/art/wikiart3_resized/'

for from_file in os.scandir(from_path):
    print(from_file.name)
    img = Image.open(from_path + '/' + from_file.name)
    img = ImageOps.autocontrast(img, cutoff=1)
    img_resized = img.resize((wid,hei), resample=Image.BILINEAR)
    img_resized.save(to_path + from_file.name)

