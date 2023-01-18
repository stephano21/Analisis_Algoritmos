import cv2
import numpy as np
faceClassif = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("faces.jpeg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces= faceClassif.detectMultiScale(gray,
scaleFactor=1.1,
minNeighbors=5,
minSize=(30,30),
maxSize=(200,200))
c=0
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    c+=1
print('numero de caras:',c)
cv2.imshow("image",image)


if cv2.waitKey(0) & 0xFF==ord('q'):
    cv2.destroyAllWindows()
    exit()