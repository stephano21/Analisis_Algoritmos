import cv2
from matplotlib import pyplot as plt
import numpy as np
imagen=cv2.imread("monedas.jpg")
imagen_gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
bordes=cv2.Canny(imagen_gris,200,500)
contours,hierearchy =cv2.findContours(bordes,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Numero de carta es:",len(contours))
cv2.drawContours(imagen,contours,-1,(0,255,0),3)

cv2.imwrite("c:/Users/Administrador/Pictures/Algoritmos/img.jpg",bordes)#guardar una imagen con open cv
cv2.imshow("Oricinal",imagen)
cv2.imshow("Griss",imagen_gris)
cv2.imshow("Bordes",bordes)
cv2.waitKey(0)