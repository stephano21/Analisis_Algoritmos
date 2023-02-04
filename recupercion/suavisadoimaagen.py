import cv2
import numpy as np

# Carga la imagen
img = cv2.imread('img.jpeg')

# Separa los canales de color
b, g, r = cv2.split(img)

# Aplica el suavizado a cada canal de color
kernel = np.ones((5, 5), np.float32) / 25
b = cv2.filter2D(b, -1, kernel)
g = cv2.filter2D(g, -1, kernel)
r = cv2.filter2D(r, -1, kernel)

# Combinar los canales de color
img_smooth = cv2.merge((b, g, r))

# Guarda la imagen resultante
cv2.imwrite('image_smooth.png', img_smooth)
