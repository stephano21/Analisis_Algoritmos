import cv2
import numpy as np
import os
dataPath= os.path.dirname(__file__)
dataPath=os.path.join(dataPath,'data')
peoplelist=os.listdir(dataPath)
print(peoplelist)
face_recognizer=cv2.face.EigenFaceRecognizer_create()

#read the model
face_recognizer.read('modeloEigenFace.xml')
cap=cv2.VideoCapture(2)
faceClassifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
while True:
    ret, frame=cap.read()
    if ret ==False:break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame=gray.copy()

    faces=faceClassifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h)in faces:
        rostro=auxFrame[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        result=face_recognizer.predict(rostro)

        cv2.putText(frame,f"{result}",(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        print(result)
        if result[1]<6100:
            cv2.putText(frame,f"{peoplelist[result[0]]}",(x,y-25),1,1.3,(255,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        else:
            cv2.putText(frame,f"Desconocido",(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

            
    cv2.imshow("Frame",frame)
    k= cv2.waitKey(1)
    if k & 0xFF==ord('q'):break
cap.release()
#cap.destroyAllWIndows()