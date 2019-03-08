# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('RyanRun.mp4')
frame_counter=0
x=[]
y=[]

while(cap.isOpened()):
    frame_counter=frame_counter+1
    if frame_counter>1082:
        break
    if frame_counter<=871:
        img1=cap.grab()
    else:       
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
       
        template = cv2.imread('hip.png',0)
        w, h = template.shape[::-1]
        
        method = eval('cv2.TM_CCOEFF_NORMED')
        
        # Apply template Matching
        min_bound,max_bound=60,150
        
        res = cv2.matchTemplate(img[min_bound:max_bound,],template,method)

        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        
        top_left = (max_loc[0],max_loc[1]+min_bound)
        bottom_right = (top_left[0] + w, top_left[1] + h)
        
        x.append(top_left[0])
        y.append(top_left[1])

        
        cv2.rectangle(img,top_left, bottom_right, 255, 2)
    
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

plt.plot(np.array(x),-np.array(y))
plt.ylim([-110,-65])
plt.xlim([0,700])




