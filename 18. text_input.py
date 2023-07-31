import random
import math
from turtle import Turtle, Screen, colormode

t = Turtle()
s = Screen()
t.shape("turtle")
t.speed("fastest")
colormode(255)

s.setup(900, 600)
name = s.textinput("What's your name?", "My name is: ")
print(name)



s.exitonclick()
