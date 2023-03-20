import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor('white')

# Create a turtle object
pen = turtle.Turtle()

# Set the pen color and size
pen.color('black')
pen.pensize(2)

# Draw a circle of dots
num_dots = 20
radius = 100

for i in range(num_dots):
    # Calculate the angle for the dot
    angle = 2 * math.pi * i / num_dots

    # Calculate the x and y coordinates of the dot
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    # Move the pen to the dot's position
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Draw the dot
    pen.dot(5)

# Hide the turtle
pen.hideturtle()

# Keep the screen open until closed by the user
turtle.done()






