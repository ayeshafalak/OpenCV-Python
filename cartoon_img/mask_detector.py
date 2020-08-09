#!/usr/bin/env python
# coding: utf-8

# In[29]:


import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_mouth.xml')

  
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth_detect = mouth_cascade.detectMultiScale(gray, 1.7, 11)
  
    for (x,y,w,h) in mouth_detect:
        y = int(y - 0.15*h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
        break
            
            
            
            
    if len(mouth_detect)>0:
             cv2.putText(frame,"No Mask",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    else:
             cv2.putText(frame,"Mask",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        
       
        
        
   
  
        
            

    cv2.imshow('Mouth Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




