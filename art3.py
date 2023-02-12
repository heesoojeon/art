import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

image = cv2.imread("camu_cat.mp4")
cap = cv2.VideoCapture("camu_cat.mp4")
cap.set(1, 2) #2- the second frame of my video
res, frame = cap.read()
cv2.imshow("video", frame)
while True:
    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break
    
cv2.imshow("camu_cat.mp4")
    
