from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("blue")

for j in range(4):
    t.forward(100)
    t.right(90)

screen = Screen()
screen.exitonclick()
