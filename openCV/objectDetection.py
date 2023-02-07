import cv2
import os
import imutils
data=  'positive'
dataPath= os.path.dirname(__file__)
objectPath=os.path.join(dataPath,'object',data)
print(objectPath)
if not os.path.exists(objectPath):
    print("Folder was created: ",objectPath)
    os.makedirs(objectPath)

cap= cv2.VideoCapture(0)
x1,y1= 150,80
x2,y2= 450,398
count=0
while True:
    ret, frame= cap.read()#CAMARA ACTIVADA, IMAGEN
    if ret ==False:break
    auxFrame= frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto=auxFrame[y1:y2,x1:x2]
    objeto=imutils.resize(objeto,width=38)

    k= cv2.waitKey(1)
    if k==ord('s'):
        cv2.imwrite(objectPath+f'/objeto_{count}.jpg', objeto)
        print(f"Imagen guardada: objeto_{count}.jpg")
        count+=1

    cv2.imshow('Frame',frame)
    cv2.imshow('Objeto',objeto)