from turtle import Turtle, Screen
import random

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")

t1.color("red")
t2.color("blue")
t3.color("black")
t4.color("green")

t1.speed("fastest")
t2.speed("fastest")
t3.speed("fastest")
t4.speed("fastest")

angles = [0, 90, 180, 270, 360]

for a in range(400):
    t1.forward(10)
    t1.right(random.choice(angles))
    t2.forward(10)
    t2.right(random.choice(angles))
    t3.forward(10)
    t3.right(random.choice(angles))
    t4.forward(10)
    t4.right(random.choice(angles))

s = Screen()
s.exitonclick()
