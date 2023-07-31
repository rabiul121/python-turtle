import math
from turtle import Turtle, Screen, colormode

t = Turtle()
s = Screen()
t.shape("turtle")
t.speed("fastest")
colormode(255)

s.setup(900, 600)
t.forward(200)
t.left(90)
t.forward(200)
t.left(135)
t.forward(math.sqrt(200 ** 2 + 200 ** 2))

s.exitonclick()
