import cv2
import numpy as np

height = 500
width = 500

image = np.zeros((height, width, 3), dtype=np.uint8)
image[:] = (0, 0, 255) #custom color code BGR in this case is RED B=0, G=0, R=255
print(image)
cv2.imshow("red image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()