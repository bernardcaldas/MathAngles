import cv2
import math

image = cv2.imread('angles.png')
pointsList = []

def mouseClick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y), 3, (0,0,255), -1)
        pointsList.append([x,y])
        print(pointsList)

def getAngle(a,b,c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0],) - math.atan2(a[1]-b[1], a[0]-b[0]))

    if ang < 0:
        ang + 360
        
        print(f'the value of the angle is {ang}, + 360 in this case')
    else:
        print(f'the value of the angle is {ang}.')    
    #return ang + 360 if ang < 0 else ang
    cv2.putText(image,str(("{:.2f}".format(ang))),(b[0]+10,b[1]+20), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)

while True:

    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        print( 'there are 3 elements')
        a,b,c = pointsList
        cv2.line(image, a,b,(0,0,0),1,cv2.LINE_AA )
        cv2.line(image, b,c,(0,0,0),1,cv2.LINE_AA )
        
        pointsList.clear()
        getAngle(a,b,c)
        


    cv2.imshow('imagem', image)
    cv2.setMouseCallback('imagem', mouseClick)
    c = cv2.waitKey(1)
    if c == 27:
        break
        

cv2.destroyAllWindows()