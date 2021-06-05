import cv2

imagen = cv2.imread('OpenCV_Logo.png') # una coma y un 0 y lo muestra con escala de grises
cv2.imshow('prueba de imagen', imagen)
cv2.waitKey(1000) # si se pone un 0 hay que pulsar un boton para que se cierre, si no, esperar 1 seg
cv2.destroyAllWindows()