

import cv2
import numpy as np

file_name = '작업 블라썸.jpg'
image = cv2.imread(file_name)

panel = np.zeros([100,400], np.uint8)
cv2.namedWindow('panel')


