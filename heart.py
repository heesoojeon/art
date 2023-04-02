import cv2
import turtle
import os


def findnearpixel(s, pixels, visited):
    visited[s]=True
    x0=pixels[s][0]
    y0=pixels[s][1]
    mindist=10000000
    result=s
    for p in range(len(pixels)):
        x1 = pixels[p][0]
        y1 = pixels[p][1]
        dist=(x0-x1)**2+(y0-y1)**2
        if (visited[p]==False and dist < mindist):
            mindist=dist
            result=p
    return result
            
def getx(x,w):
    return x-(w//2)

def gety(y,h):  
    return -(y-(h//2))

# 정렬
def sortpixels(pixels):
    visited=[False]*len(pixels)
    result=[]
    
    s=0
    result.append([pixels[0][0],pixels[0][1]])
    for i in range(len(pixels)-1):
        print(i)
        near = findnearpixel(s, pixels, visited)
        result.append([pixels[near][0], pixels[near][1]])
        s=near
    return result
        
        
        
        
def draw(maskfile,colorfile):
    mask = cv2.imread(maskfile)
    image = cv2.imread(colorfile)

    cv2.imshow('mask', mask)
    cv2.imshow('image', image)
    h,w,_= mask.shape
    print(h,w)


    #그림의 점을 탐색
    pixels=[]
    for y in range(0,h,4):
        for x in range(0,w,4):
            if(mask[y,x][0]!=255):
    #            print(y,x,img[y,x])
                pixels.append([y,x])

    turtle.shape("square")
    turtle.colormode(255)
    result=sortpixels(pixels)

    turtle.penup()

    for p in result:
        turtle.goto(getx(p[1],w),gety(p[0],h))
        c=tuple(image[p[0], p[1]])
        turtle.color(c[2], c[1], c[0])
        turtle.stamp()


os.chdir(r"C://Users/user/Desktop")
draw(r"heart.PNG","flower.JPG")
draw(r"heart1.PNG","C://Users/user/Desktop/microworld.JPG")
        

cv2.waitKey(0)  
cv2.destroyAllWindows()
