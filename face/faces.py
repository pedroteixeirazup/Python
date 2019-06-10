import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('./cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('./cascades/data/haarcascade_smile.xml')


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

#for button
img_counter = 0
img_roi = 0
while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w] #([ycor_start, ycord_end])
        roi_color = frame[y:y+h, x:x+w]
        img_roi = roi_color

        #recognize?
        id_, conf = recognizer.predict(roi_gray)
        if conf>=45: # and conf <=105: 55 105
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            

        img_item = "pedro3.png"
        #cv2.imwrite(img_item, roi_color)

        color=(255,0,0) #BGR
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y),(end_cord_x,end_cord_y), color, stroke)
        # subitems = eye_cascade.detectMultiScale(roi_gray)
        # for(ex,ey,ew,eh) in subitems:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    cv2.imshow('frame', frame)
    #button for screen shot
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img_roi)
        print("{} written!".format(img_name))
        img_counter += 1
    

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
