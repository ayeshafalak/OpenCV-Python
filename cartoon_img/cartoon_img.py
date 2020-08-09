import cv2
import numpy as np
img=cv2.imread("Tulips.jpg",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.bilateralFilter(gray,-1,10,1)
gray=cv2.GaussianBlur(gray,(5,5),0)

edges=cv2.Laplacian(gray,-1,ksize=5)
_,mask=cv2.threshold(edges,35,255,cv2.THRESH_BINARY_INV)

for i in range(30):
    mask=cv2.medianBlur(mask,3)

mask=cv2.resize(mask,(512,512))
kernal=np.ones((2,2),np.uint8)
mask=cv2.dilate(mask,kernal,iterations=1)
mask=cv2.erode(mask,kernal,iterations=1)

r,g,b=cv2.split(img)
img=cv2.resize(img,(512,512))
r=cv2.resize(r,(512,512))
g=cv2.resize(g,(512,512))
b=cv2.resize(b,(512,512))

rf=cv2.bitwise_and(mask,r)
gf=cv2.bitwise_and(mask,g)
bf=cv2.bitwise_and(mask,b)

maskf=cv2.merge((rf,gf,bf))
maskf=cv2.resize(maskf,(512,512))

cv2.imshow('Original Image',img)
cv2.imshow('Cartoon Image',maskf)


cv2.waitKey(0)
cv2.destroyAllWindows()
