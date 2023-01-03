import cv2
import numpy as np

imagen= cv2.imread("img.jpeg")
redimencionar=cv2.resize(imagen ,(800,500))
imagen_gris=cv2.cvtColor(redimencionar,cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=10)#clipLimit= de 0 a 40 luego de eso se pierde el contraste
imagen_final=clahe.apply(imagen_gris)

cv2.imshow("original",redimencionar)
cv2.imshow("Griss",imagen_gris)
cv2.imshow("Sobreajuste de contraste",imagen_final)
cv2.waitKey(0)