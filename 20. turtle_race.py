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

turtles = []


def draw_turtle(num):
    y = -200
    for tur in range(num):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(random_color())
        new_turtle.speed("fastest")
        turtles.append(new_turtle)
        new_turtle.goto(-280, y)
        y += 30


print(turtles)
draw_turtle(15)



s.exitonclick()
