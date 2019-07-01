######## Image Detect Face  #########
#
# Author: Pedro Henrique Faria Teixeira
# Date: 01/07/19
# Description: 
# This program uses OpenCv and Cascade Classifier file to identify faces on 
# images and show in a moldure with the faces circled

# Import packages
import cv2
import sys
import pickle

# Function to detect the face
def detect_face(image):
    imagePath = image # Image input from frontend
    faceCascade = cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_alt2.xml') # The cascade classifier used to train on face_train

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml") # Use the trainner.yml statistics trained on face_train to detect faces on images

    labels = {"person_name": 1} # The identifier of the image
    with open("labels.pickle", 'rb') as f: # Open the labels.pickle to read the metrics and apply in the image
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    image = cv2.imread(imagePath) # Read the image
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Convert the image to a RGB format

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)) # Detect the scales of faces in the image, and store in a array how much faces is found

    print('Found ' + format(len(faces)) + 'faces!') # If the image have faces, print how much is found
    confiance =[]
    for (x, y, w, h) in faces: # This for is to apply the recognizer classifier in the image, take the confiance result and draw the box in the image
        roi_gray = gray[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)
        print(conf)
        confiance.append(round(conf,2))

        if conf > 40:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (0, 255, 0)
            stroke = 2
        
        color = (0,255,0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(image, (x,y),(end_cord_x,end_cord_y), color, stroke)

    cv2.imshow("Faces found", image) # When finish the process of detect face and put the box on faces, show in the moldure
    cv2.waitKey(0) # Close button of the moldure to finish the program

    return confiance
    
