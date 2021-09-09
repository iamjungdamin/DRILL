import turtle

turtle.reset()

cnt = 0
x = -300
y = 300

while (cnt <= 5):
    turtle.penup()
    turtle.goto(x, y-(cnt*100))
    turtle.pendown()
    turtle.forward(500)
    cnt += 1

cnt = 0
turtle.right(90)

while (cnt <= 5):
    turtle.penup()
    turtle.goto(x+(cnt*100), y)
    turtle.pendown()
    turtle.forward(500)
    cnt += 1



turtle.exitonclick()
