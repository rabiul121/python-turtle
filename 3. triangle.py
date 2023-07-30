from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("blue")

for j in range(3):
    t.forward(100)
    t.right(120)

# for j in range(3):
#     t.backward(100)
#     t.right(120)


screen = Screen()

screen.exitonclick()
