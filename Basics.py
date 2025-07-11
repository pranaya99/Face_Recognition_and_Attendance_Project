import cv2
import numpy as np

import face_recognition

imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.png')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Bill_Gates.png')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodedElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodedTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1], faceLocTest[2]),(255,0,255),2)


results = face_recognition.compare_faces([encodedElon],encodedTest)
faceDis = face_recognition.face_distance([encodedElon],encodedTest)
#lower the distance lower the match is
print(results, faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)


cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)

cv2.waitKey(0)