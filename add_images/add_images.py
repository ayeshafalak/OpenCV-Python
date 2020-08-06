import numpy as np
import cv2
img1=cv2.imread('Chrysanthemum.jpg')
img2=cv2.imread('Jellyfish.jpg')
img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))
result=cv2.add(img1,img2);
result2=cv2.addWeighted(img1,.2,img2,.8,0);
cv2.imshow('result',result)
cv2.imshow('result2',result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
