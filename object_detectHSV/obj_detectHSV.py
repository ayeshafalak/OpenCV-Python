import numpy as np
import cv2
def nothing(x):
    pass
while True:
    frame=cv2.imread('Jellyfish.jpg')
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lb=np.array([110,50,50])
    ub=np.array([130,255,255])
    mask=cv2.inRange(hsv,lb,ub)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroAllWindows()
