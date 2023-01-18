import cv2
import numpy as np
import os
dataPath= os.path.dirname(__file__)
dataPath=os.path.join(dataPath,'data')
peoplelist=os.listdir(dataPath)
print(peoplelist)

labels=[]
FacesData=[]
label=0

for nameDir in peoplelist:
    personPath= dataPath+'/'+nameDir
    for fileName in os.listdir(personPath):
        print(f'rostros:{nameDir}/{fileName}')
        labels.append(label)
        FacesData.append(cv2.imread(personPath+'/'+fileName,0))
        image= cv2.imread(personPath+'/'+fileName,0)
    label+=1

#print(labels)
#print("etiquetas",np.count_nonzero(np.array(labels)==1))
face_recognizer=cv2.face.EigenFaceRecognizer_create()
print("Entrenando...")
#train model
face_recognizer.train(FacesData,np.array(labels))
#create model train
face_recognizer.write('modeloEigenFace.xml')
print('Entrenamiento finalizado!')