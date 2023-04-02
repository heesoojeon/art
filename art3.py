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
    
<<<<<<< HEAD
cv2.imshow("camu_cat.mp4")
print ("안녕하세요")
=======
    print('Frames per second : ', fps,'FPS')
    print('Frame count : ', f_count )
    print('Frame width : ', f_width)
    print('Frame height : ', f_height)



def mosaic(img):
    rate=50
    w,h=rate,rate
    for y in range(0,f_height-h,h):    
        for x in range(0,f_width-w,w):
            roi = img[y:y+h, x:x+w]   # 관심영역 지정
            roi = cv2.resize(roi, (w//rate, h//rate)) # 1/rate 비율로 축소
            # 원래 크기로 확대
            roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
            img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용

        
while Vid.isOpened():
    ret, frame = Vid.read()
    if ret:
        # width = frame.shape[1]
        # height = frame.shape[0]
        # print('Frame width : ', width)
        # print('Frame height : ', height)
        
        # width = frame.shape[1] //2
        # height = frame.shape[0]//2
        # dim = (width, height)
        # resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        mosaic(frame)
        #re_frame = cv2.resize(frame, (f_width//rate,f_height//rate))
        #re_frame = cv2.resize(re_frame, (f_width,f_height),interpolation = None)
        cv2.imshow('camu_cat', frame)
        key = cv2.waitKey(10)
        
        if key == ord('q'):
            break
    else: break
>>>>>>> b5f884d868001cb0c8dcc6f8da6f9eb3faec7db5
    
Vid.release()
cv2.destroyAllWindows()    



