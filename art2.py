

import opencv2 as cv2
import numpy as np

print(cv2.__version__)
exit()

print(np.__version__)
exit()
print("설치가 잘 되었습니다.")

file_name = 'work_blossom.jpg'
image = cv2.imread(file_name)

panel = np.zeros([100,400], np.uint8)
cv2.namedWindow('panel')

def nothing(x):
    pass

cv2.createTrackbar('FX', 'panel', 1,100, nothing)
cv2.createTrackbar('FY', 'panel', 1,100, nothing)

return_name = file_name.replace('_','_pixel')




