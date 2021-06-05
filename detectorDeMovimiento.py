import cv2
import numpy as np

video=cv2.VideoCapture(0) # se puede pasar un video en vez del 0 y así detecta el movimiento en el video
i = 0

while True:
    ret, frame=video.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 15:
        bgGray = gray
    if i > 15:
        dif = cv2.absdiff(gray, bgGray)
        _, th = cv2.threshold(dif, 30, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Contornos correspondientes a las imagens en blanco de la imagen binaria
#        cv2.drawContours(frame, cnts, -1, (00,0,255),2) 
#        cv2.imshow('dif', dif)
        cv2.imshow('th', th)
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 9000:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x,y), (x+w, y+h),(00,0,255),2) 

    cv2.imshow('Frame', frame)

    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
