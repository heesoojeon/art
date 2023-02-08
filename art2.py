import cv2
import numpy

art = '작업블라썸.jpg'
image = cv2.imread(art)

panel = numpy.zeros([100,400],numpy.unit8)
cv2.namedWindow('panel')

def nothing(x):
    pass

cv2.createTrackbar('FX','panel',1,100,nothing)
cv2.createTrackbar('FY','panel',1,100,nothing)
