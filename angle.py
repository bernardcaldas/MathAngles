import cv2
import math

image = cv2.imread('angles.png')
pointsList = []

def mouseClick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y), 3, (0,0,255), -1)
        pointsList.append([x,y])
        print(pointsList)
    
while True:

    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        print( 'there are 3 elements')
        pointsList.clear()


    cv2.imshow('imagem', image)
    cv2.setMouseCallback('imagem', mouseClick)
    c = cv2.waitKey(1)
    if c == 27:
        break
        

cv2.destroyAllWindows()