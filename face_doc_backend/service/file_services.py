######## File Services #########
#
# Author: Pedro Henrique Faria Teixeira
# Date: 01/07/19
# Description: 
# This program is a simple script to decode and encode images to base64, and normalize the string of the base64 and the confiance

#IMPORT PACKAGES
import base64
from PIL import Image
from io import BytesIO
import cv2
import matplotlib.pyplot as plt


#ENCONDING IMAGE TO BASE 64
def encoding_to_64(file):
    image = open(file,'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    print(image_64_encode)
    return image_64_encode


#DECODE MAGE TO FILE
def decode_to_image(base64_string):
    base64_splited = base64_string.split(',',1)[1]
    image = Image.open(BytesIO(base64.b64decode(base64_splited)))
    image.save('out.jpg','JPEG',quality=80, optimize=True, progressive=True)
    plt.figure()
    plt.imshow(image)
    plt.show()

#NOMALIZE THE CONFIANCE OF A FACE DETECTED
def normalize_conf(conf):
    for x in range(len(conf)):
            if conf[x] > 100:
                conf[x] = 100.00
    return conf
