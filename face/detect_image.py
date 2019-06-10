import cv2
import sys
import pickle

imagePath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)) #faceCascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))

print('Found ' + format(len(faces)) + 'faces!')

for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    #roi_color = frame[y:y+h, x:x+w]
    id_, conf = recognizer.predict(roi_gray)
    print(conf)
    if conf > 40:
        # print(id_)
        # print(labels[id_])
        font = cv2.FONT_HERSHEY_SIMPLEX
        name = labels[id_]
        color = (0, 255, 0)
        stroke = 2
       # cv2.putText(image, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

    color = (0,255,0)
    stroke = 2
    end_cord_x = x + w
    end_cord_y = y + h
    cv2.rectangle(image, (x,y),(end_cord_x,end_cord_y), color, stroke)




# for(x,y,w,h) in faces:
#     cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
