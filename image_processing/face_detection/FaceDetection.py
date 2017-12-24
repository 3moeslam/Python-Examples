'''
Created on Dec 3, 2017

@author: Eslam Ahmad- Twitter @3moeslam
@version: 1

'''
import cv2

cam = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while True:
    ret , frame = cam.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x+10,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Camera',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()