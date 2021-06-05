import cv2

captura=cv2.VideoCapture(0) # grabar por primera vez
#captura=cv2.VideoCapture('videoSalida.avi') # si ya lo he grabado antes se puede ver el video
#salida=cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480)) # Variable para guardar el video

while(captura.isOpened()):
    ret, imagen=captura.read()
    if ret == True:
        cv2.imshow('video', imagen)
 #       salida.write(imagen) # para guardar las imagenes de video
        if cv2.waitKey(50) & 0xFF == ord('s'):
            break
    else: break

captura.release()
#salida.release() # finaliza la grabacion del video
cv2.destroyAllWindows()