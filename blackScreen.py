import cv2
import time
import numpy as np
  
cap = cv2.VideoCapture(0) 
time.sleep(2)

image = cv2.imread() 
  
while(cap.isOpened()): 
    ret, frame = cap.read() 

    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    cv2.waitKey(1)

  
cap.release() 
cv2.destroyAllWindows() 
