import turtle
import random

def drunken_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
    
def drunken_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def drunken_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(drunken_up,'w')
turtle.onkey(drunken_left,'a')
turtle.onkey(drunken_down,'s')
turtle.onkey(drunken_right,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
