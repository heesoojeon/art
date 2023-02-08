import cv2

art = '작업블라썸.jpg'
image = cv2.imread(art)

panel = np.zeros([100,400],np.unit8)
cv2.namedWindow('panel')

def nothing(x):
    pass

cv2.createTrackbar('FX','panel',1,100,nothing)
cv2.createTrackbar('FY','panel',1,100,nothing)
