import cv2
import numpy as np
img=cv2.imread("Jellyfish.jpg")
gray=cv2.imread("Jellyfish.jpg",0)
_,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,thresh2=cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
thresh3=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Image',img)
cv2.imshow('Thresh1',thresh1)
cv2.imshow('Thresh2',thresh2)
cv2.imshow('Thresh3',thresh3)
cv2.waitKey(0)
cv2.destryAllWindows()
