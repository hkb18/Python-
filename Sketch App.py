from turtle import Turtle, Screen

hkb = Turtle()
hkb.shape("classic")


def forward():
    hkb.forward(10)


def backward():
    hkb.backward(10)


def left():
    new_heading = hkb.heading() + 10
    hkb.setheading(new_heading)


def right():
    new_heading = hkb.heading() - 10
    hkb.setheading(new_heading)


def clear():
    hkb.clear()
    hkb.penup()
    hkb.home()
    hkb.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
