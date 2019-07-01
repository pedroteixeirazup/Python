######## Face Train  #########
#
# Author: Pedro Henrique Faria Teixeira
# Date: 01/07/19
# Description: 
# This program uses OpenCv and Cascade Classifier file to train faces on 
# images and store the results on yml file to be used for another program to detect face.

# Import packages
import cv2
import os
from PIL import Image
import numpy as np
import pickle

#Get the current directory where the program is saved and the path to the image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

#Choose the Cascade Classifier file to detect the faces 
face_cascade = cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
current_id = 0
label_ids = {} #indentifier of a image
y_labels = []
x_train = []

#Join in the path of all images stored on directory and apply
#the cascade classifier to detect the params of a face and generate statistics of 
#faces detecteds in images,  which is stored in a array to transform on a yml file
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg") :
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()

            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            
            id_ = label_ids[label]
            print(label_ids)
            pil_image = Image.open(path).convert("L") 
            image_array = np.array(pil_image, "uint8")
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors = 5)

            for(x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

#When all images is trained, store the result of the label_ids in the labels.pickle,
#and the array with all statistics in the trainner.yml
with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
