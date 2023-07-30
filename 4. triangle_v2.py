from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("blue")

for a in range(3):
    t.left(120)
    for b in range(15):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()



screen = Screen()

screen.exitonclick()
