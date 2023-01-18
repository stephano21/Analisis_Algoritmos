import cv2
import numpy as np


def eye(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


    bordes = cv2.Canny(imagen_gris, 200, 500)
    contours, hierearchy = cv2.findContours(
        bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    circles = cv2.HoughCircles(bordes, cv2.HOUGH_GRADIENT, 30, 50,
                            param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    c = 0
    for i in circles[0, :]:
        # dibujar circulo
        cv2.circle(bordes, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # dibujar centro
        cv2.circle(bordes, (i[0], i[1]), 2, (0, 0, 255), 3)
        c += 1

    bordes = cv2.Canny(imagen_gris, 100, 400)
    contours, hierearchy = cv2.findContours(
        bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("Numero de ojos:", c)
    cv2.drawContours(imagen, contours, -1, (0, 255, 0), 3)


    # cv2.imshow("original",redimencionar)
    cv2.imshow("Griss", bordes)
    cv2.imshow("xd", imagen)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


cap=cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame= cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceClassif.detectMultiScale(gray,1.3,5)
    auxFrame= frame.copy()
    for (x,y,w,h) in faces:
        rostro=auxFrame[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        eye(rostro)
    cv2.imshow('Frame',frame)