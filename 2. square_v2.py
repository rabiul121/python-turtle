from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("blue")

for a in range(4):
    t.right(90)
    for j in range(15):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

screen = Screen()
screen.exitonclick()
