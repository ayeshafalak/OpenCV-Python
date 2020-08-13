  ## Importing the useful libraries ##
import cv2
import numpy as np

## Setting up the parameters for webcam ##

width = 640
height = 480
cap = cv2.VideoCapture(1)
cap.set(3, width)  # setting width
cap.set(4, height)  # setting height
cap.set(10,130) # setting brightness


## Initializing some variables ##

myColors = [[4, 168, 80, 10, 255, 178], ## orange
            [132, 27, 31, 143, 255, 198]  ## purple
            ]

myColorVals = [[51,153,255],          ## BGR
               [255,0,255]
                 ]


myPoints = [] ## [x. y, colorId]

## Find Color function ##

def findColor(img,myColors, myColorVals):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(str(color[0]), mask)
        x,y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorVals[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints
        
 ## Function for getting contours ##

def getContours(img):
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        x,y,w,h = 0,0,0,0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            print(area)
            if area > 700:
                #cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x, y, w, h = cv2.boundingRect(approx)
        return x + w//2, y


def Draw(myPoints, myColorVals):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 10, myColorVals[point[2]], cv2.FILLED)
        



while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorVals)
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)
            
    if len(newPoints) !=0:
        Draw(myPoints, myColorVals)
    
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
    
