#!/usr/bin/env python
# coding: utf-8

import cv2                                      #import the opencv package
img=cv2.imread('Jellyfish.jpg',0)               #read the image using this function
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)                                      #printing the matrix of image in grayscale
cv2.imshow('image',gray)                         #displaying the grayscale image in a new window named 'image'
cv2.waitKey(6000)                               #the window will appear for 6s
cv2.destroyAllWindows()                         #destroys the window
