from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("brown")

for j in range(5):
    t.left(72)
    for a in range(15):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()


screen = Screen()

screen.exitonclick()
