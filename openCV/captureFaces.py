import cv2
import os
import imutils
personName=  'Stephano'
dataPath= os.path.dirname(__file__)
personPath=os.path.join(dataPath,personName)
if not os.path.exists(personPath):
    print("Folder was created: ",personPath)
    os.makedirs(personPath)

cap= cv2.VideoCapture("stephano.mp4")
faceClassif=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
count=0
while True:
    ret, frame= cap.read()
    if ret ==False:break
    frame=imutils.resize(frame,width=640)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame= frame.copy()

    k= cv2.waitKey(1)
    if k==27 or count>=300:
        break