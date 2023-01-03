import cv2
import numpy as np
video= cv2.VideoCapture(0)

while True:
    val,frame=video.read()
    if val==False:break
    print(frame)
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    menor_blue= np.array([110,50,50])
    mayor_blue= np.array([130,255,255])
    mascara=cv2.inRange(hsv,menor_blue,mayor_blue)
    res=cv2.bitwise_and(frame,frame,mask=mascara)



    cv2.imshow("Frame",mascara)
    if cv2.waitKey(1)& 0xff == ord('q'):
        break
    #video.release()