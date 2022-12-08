#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
while(True):
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (640,480))
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print(type(fgmask))
        print(fgmask.shape)
        print(fgmask[0:10,0:10])
        break # 'ESC' key is pressed
cap.release()
cv2.destroyAllWindows()
