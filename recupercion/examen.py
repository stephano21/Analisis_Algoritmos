""" import cv2
image= cv2.imread("img.jpeg")
BLUE, GREEN, RED = cv2.split(image)


cv2.imshow("ROJO",RED)
cv2.imshow("VERDE",GREEN)
cv2.imshow("AZUL",BLUE)
if cv2.waitKey(0) & 0xFF==ord('q'):
    image.release()
 """
#Importar librería cv2
import cv2
import numpy as np

#Crea arreglos que son la base de una imagen
img1 = np.zeros((60,80,1),np.uint8)
img2 = np.ones((6,8,1),np.uint8)
img3 = 200*np.ones((6,8,1),np.uint8)

#Mostrar imagenes
cv2.imshow('imagen-zeros',img1)
cv2.imshow('imagen-ones',img2)
cv2.imshow('imagen-250',img2)

#Cerrar las ventanas con tecla esc
cv2.waitKey(0)
cv2.destroyAllWindows()