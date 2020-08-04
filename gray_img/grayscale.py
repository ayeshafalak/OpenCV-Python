#!/usr/bin/env python
# coding: utf-8

import cv2                                      #import the opencv package
img=cv2.imread('Jellyfish.jpg',0)      #read the image using this function
print(img)                                      #printing the matrix of image in grayscale
cv2.imshow('image',img)                         #displaying the grayscale image in a new window named 'image'
cv2.waitKey(6000)                               #the window will appear for 6s
cv2.destroyAllWindows()                         #destroys the window
