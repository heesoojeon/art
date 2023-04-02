import cv2
import turtle
import random

def getx(x):
    global width,height
    return (x-(width/2))*3   ##########
def gety(y):
    global width,height
    return (-y+(height/2))*3   ##########
def getpoint():
    global width,height
    global points,pcount
    if(pcount==width//5*height//5):   ##########
        return -1,-1
    while True:
        x=random.randint(0,width//5-1)   ##########
        y=random.randint(0,height//5-1)  ##########
        if(not points[y][x]):
            points[y][x]=True
            pcount+=1
            return x*5,y*5  ##########
def draw():
    global width,height
    global points,pcount
    wn = turtle.Screen()
    wn.setup(1000,1000)
    turtle.title("haruki")
    turtle.colormode(255)
    turtle.penup()
    turtle.shape('square')
    turtle.turtlesize(1)
    turtle.speed(10)

    image = cv2.imread('haruki.jpg')
    #cv2.imshow('image', image)
    height,width,_= image.shape

    print(image.shape)
    print(height,width)

    points=[[False]*(width//5) for _ in range(height//5)]  ##########
    pcount=0

        
            
    while True:
        x,y=getpoint()
        if(x==-1):
            break
        turtle.goto(getx(x),gety(y))
        c=list(image[y,x])
        turtle.color(c[2], c[1], c[0])
        turtle.stamp()
