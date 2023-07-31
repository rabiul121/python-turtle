from turtle import Turtle, Screen, colormode

t = Turtle()
t.shape("turtle")
t.color("coral")
t.speed("fastest")
colormode(255)


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(90)


def turn_right():
    t.right(90)


s = Screen()
s.listen()

s.onkey(key="Right", fun=move_forward)
s.onkey(key="Left", fun=move_backward)
s.onkey(key="Up", fun=turn_left)
s.onkey(key="Down", fun=turn_right)

s.exitonclick()
