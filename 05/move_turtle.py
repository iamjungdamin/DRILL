import turtle

def move_turtle(degree, distance = 50):
    turtle.setheading(degree)
    turtle.forward(distance)
    turtle.stamp()

def move_up():
    move_turtle(90)
    
def move_down():
    move_turtle(270)

def move_left():
    move_turtle(180)

def move_right():
    move_turtle(0)

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.stamp()

turtle.onkey(move_up,'w')
turtle.onkey(move_left,'a')
turtle.onkey(move_down,'s')
turtle.onkey(move_right,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
turtle.mainloop()