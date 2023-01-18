import cv2
import numpy as np

# Iniciar la captura de video
cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    # Leer el siguiente frame
    ret, frame = cap.read()

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Utilizar un algoritmo de detección de rostros (por ejemplo, utilizando dlib) para detectar rostros en el frame
    # Aquí se asume que se ha importado dlib y se ha cargado un modelo de detección de rostros
    faces=faceClassif.detectMultiScale(gray,1.3,5)
    # Para cada rostro detectado
    for face in faces:
        # Obtener las coordenadas del rostro
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Dibujar un rectángulo alrededor del rostro
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Obtener la región de interés del rostro
        roi = gray[y:y + h, x:x + w]

        # Utilizar un algoritmo para detectar los contornos de los ojos en la región de interés (por ejemplo, utilizando HoughCircles)
        circles = cv2.HoughCircles(roi, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

        # Asegurarse de que se hayan detectado al menos dos círculos (un círculo para cada ojo)
        if circles is not None and circles.shape[1] >= 2:
            circles = np.round(circles[0, :]).astype("int")

            # Para cada círculo detectado
            for (x_c, y_c, r) in circles:
                # Dibujar un círculo alrededor del ojo
                cv2.circle(roi, (x_c, y_c), r, (0, 255, 0), 2)

    # Mostrar el frame resultante
    cv2.imshow("Video", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar la captura de video y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
