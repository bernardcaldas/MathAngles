import cv2
import math

image = cv2.imread('90-degrees.png')
pointsList = []

def mouseClick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y), 3, (0,0,255), -1)
        pointsList.append([x,y])
        print(pointsList)

def getAngle(a,b,c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0],) - math.atan2(a[1]-b[1], a[0]-b[0]))

    if ang < 0:
        #ang + 360
        print(f'the value of the angle is {ang}, + 360 in this case')
    else:
        print(f'the value of the angle is {ang}.')    
    #return ang + 360 if ang < 0 else ang

while True:

    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        print( 'there are 3 elements')
        a,b,c = pointsList
        pointsList.clear()
        print('valor de a,b,c')
        print(a,b,c)
        getAngle(a,b,c)


    cv2.imshow('imagem', image)
    cv2.setMouseCallback('imagem', mouseClick)
    c = cv2.waitKey(1)
    if c == 27:
        break
        

cv2.destroyAllWindows()