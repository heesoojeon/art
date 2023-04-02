import cv2
import time
import os

def get_files(path):
    for root, subdirs, files in os.walk(path):
        
        list_files = []
        
        if len(files) >0:
            for f in files:
                fullpath = root +'/'+f
                list_files.append(fullpath)
                
    return list_files

image_files = get_files('C:\Users\user\Desktop')

img = cv2.imread(image_files[0])
height,width,channel = img.shape
fps = 25

fource = cv2.VedeoWriter_fource(*'mp4v')
BASE_DIR = os.path.dirname(os.path.abspath(_file))
writer = cv2.VideoWriter(BASE_DIR + '/'+ 'output.mp4',fourcc, fps, (width,height))  

for file in image_files:
    img = cv2.imread(file)
    writer.write(img)
    cv2.imshow("Color", img)
    
    #esc키 누르면 중지
    if cv2.waitKey(25) == 27:
        break
writer.release()
cv2.destroyAllWindows()             
        