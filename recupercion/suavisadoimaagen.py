import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carga la imagen
img = cv2.imread('img.jpeg')

#crear histograma
resize=cv2.resize(cv2.imread('img.jpeg',0),(500,500))
color=['r','g','b']
for index,color_ob in enumerate (color):
    histograma= cv2.calcHist([resize],[index],None,[256],[0,256])
    plt.plot(histograma,color=color_ob)
    plt.xlim([0,255])
    
plt.show()
# Separa los canales de color
b, g, r = cv2.split(img)
enfoque=[[0,-1,0],[-1,5,-1],[0,-1,0]]
desenfoque=np.ones((3,3))
# Aplica el suavizado a cada canal de color
base = np.array(enfoque)
b = cv2.filter2D(b, -1, base)
g = cv2.filter2D(g, -1, base)
r = cv2.filter2D(r, -1, base)

# Combinar los canales de color
img_enfoque = cv2.merge((b, g, r))
base = np.array(desenfoque)
b = cv2.filter2D(b, -1, base)
g = cv2.filter2D(g, -1, base)
r = cv2.filter2D(r, -1, base)

img_desenfoque = cv2.merge((b, g, r))

# Guarda la imagen resultante
cv2.imshow('Enfoque', img_enfoque)
cv2.imshow('Desenfoque', img_desenfoque)
cv2.waitKey(0)
