import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_mouth.xml')
face_cascade=cv2.CascadeClassifier('./cascade_files/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
    frame = cv2.flip(frame,1)
    #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    frame=cv2.resize(frame,(750,512))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mask_detect = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    face_detect = face_cascade.detectMultiScale(gray, 1.1,5)
    
    if len(face_detect)>0:
  
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
     
            if len(mask_detect)>0:
                 cv2.putText(frame,"No Mask",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            
            else:
          
                 for (x,y,w,h) in face_detect:
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
                    cv2.putText(frame,"Mask",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                    
    else:
        cv2.putText(frame,"Checking..",(280,260),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

                    
       
    cv2.imshow('Mask Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
