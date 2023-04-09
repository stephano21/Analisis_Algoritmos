import cv2
import numpy as np

imagen=cv2.imread("monedas.jpg")
imagen_gris=cv2.imread("monedas.jpg",0)
contornos=cv2.Canny(imagen_gris,100,400)
bordes,jerarquia=cv2.findContours(contornos,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,bordes,-1,(255,0,0),2)

intensidad_maxima = np.amax(imagen_gris)
intensidad_media = np.mean(imagen_gris)

print("La intensidad máxima del canal gris es:", intensidad_maxima)
print("La intensidad media del canal gris es:", intensidad_media)
cv2.imshow("Contornos",imagen)
cv2.waitKey(0)
