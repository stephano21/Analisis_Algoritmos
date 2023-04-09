import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("image.jpg")
redimencionar=cv2.resize(image,(500,500))
color=['r','g','b']
for index,color_ob in enumerate (color):
    histograma= cv2.calcHist([redimencionar],[index],None,[256],[0,256])
    print(histograma)
    plt.plot(histograma,color=color_ob)
    plt.xlim([0,255])
    
plt.show()
#cv2.imshow("original",redimencionar)
cv2.waitKey(0)