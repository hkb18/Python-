import turtle
from turtle import Turtle, Screen
import random

hkb_the_turtle = Turtle()
hkb_the_turtle.shape("turtle")
hkb_the_turtle.color("cyan")

turtle.colormode(255)


def random_color():
    """Randomly generates different colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    """To make turtle walk randomly"""
    hkb_the_turtle.speed("fastest")
    directions = [0, 90, 180, 270, 360]
    hkb_the_turtle.pensize(16)
    for _ in range(150):
        hkb_the_turtle.color(random_color())
        hkb_the_turtle.forward(30)
        hkb_the_turtle.setheading(random.choice(directions))


# random_walk()


def dashed_line():
    """To print a dashed line using turtle"""
    for _ in range(15):
        hkb_the_turtle.forward(10)
        hkb_the_turtle.penup()
        hkb_the_turtle.forward(10)
        hkb_the_turtle.pendown()


# dashed_line()


def shape(no_of_sides):
    """To print different shapes using turtle"""
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        hkb_the_turtle.forward(100)
        hkb_the_turtle.right(angle)


for shape_size in range(3, 11):
    hkb_the_turtle.color(random_color())
    # shape(shape_size)


def spirograph(size_of_gap):
    hkb_the_turtle.shape("classic")
    hkb_the_turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        hkb_the_turtle.color(random_color())
        hkb_the_turtle.circle(100)
        hkb_the_turtle.setheading(hkb_the_turtle.heading() + size_of_gap)


spirograph(6)

screen = Screen()
screen.exitonclick()
