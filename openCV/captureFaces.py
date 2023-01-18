import cv2
import os
import imutils
personName=  'Velez'
dataPath= os.path.dirname(__file__)
personPath=os.path.join(dataPath,'data',personName)
print(personPath)
if not os.path.exists(personPath):
    print("Folder was created: ",personPath)
    os.makedirs(personPath)

cap= cv2.VideoCapture(0)
faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
count=0
while True:
    ret, frame= cap.read()#CAMARA ACTIVADA, IMAGEN
    if ret ==False:break
    frame=imutils.resize(frame,width=240,height=720)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame= frame.copy()

    faces= faceClassif.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),maxSize=(200,200))
    for (x,y,w,h)in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        rostro=auxFrame[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        ruta=personPath+'/rostro_{}.jpg'.format(count)
        cv2.imwrite(ruta,rostro)
        count+=1
    cv2.imshow('Frame',frame)
    k= cv2.waitKey(1)
    if k==27 or count>=300:
        break
