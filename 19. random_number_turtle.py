import random
from turtle import Turtle, Screen, colormode

t = Turtle()
s = Screen()
t.shape("turtle")
t.speed("fastest")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


s.setup(600, 600)


def draw_turtle(num):
    for tur in range(num):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(random_color())
        new_turtle.speed("fastest")
        new_turtle.goto(random.randint(-280, 280), random.randint(-280, 280))


draw_turtle(100)

s.exitonclick()
