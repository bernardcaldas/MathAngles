import cv2
import math

image = cv2.imread('angles.png')

cv2.imshow('imagem', image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()

