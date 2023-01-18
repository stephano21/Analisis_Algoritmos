import cv2
import numpy as np
video = cv2.VideoCapture(0)#0para agregar camaras del driver
while True:
    val, frame= video.read()
    print(frame)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    menor_blue = np.array([117,33,17])
    mayor_blue = np.array([0,0,0])
    
    mascara = cv2.inRange(hsv,menor_blue,mayor_blue)
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)
    
    #flip = cv2.flip(frame,90)
    #cv2.imshow("espejo", flip)
    if val ==False: break
    cv2.imshow("imagen",frame)
    cv2.imshow("mascara",mascara)
    cv2.imshow("resultado",resultado)
    
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
video.destroyAllWindows()