from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("blue")


def draw(num):
    for a in range(num):
        t.left(360 / num)
        for b in range(15):
            t.forward(5)
            t.penup()
            t.forward(5)
            t.pendown()


# draw(5)

def main(num_of_shape):
    for j in range(3, num_of_shape + 1):
        draw(j)


main(6)

screen = Screen()

screen.exitonclick()
