import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

Vid = cv2.VideoCapture('camu_cat.mp4')

if Vid.isOpened():
    fps = Vid.get(cv2.CAP_PROP_FPS)
    f_count = Vid.get(cv2.CAP_PROP_FRAME_COUNT)
    f_width = int(Vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    f_height = int(Vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
cv2.imshow("camu_cat.mp4")
print ("안녕하세요")
    
Vid.release()
cv2.destroyAllWindows()    



