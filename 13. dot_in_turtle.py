import random
from turtle import Turtle, Screen, colormode

t = Turtle()
t.shape("turtle")
t.speed("fastest")
colormode(255)
t.hideturtle()



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_dot(num, size):
    for dot in range(num):
        t.dot(size, random_color())
        t.goto(random.randint(-300, 300), random.randint(-300, 300))


draw_dot(100, 20)

s = Screen()
s.exitonclick()
