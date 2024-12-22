import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
# height = 400 coordinates are from -200 to 200. Same goes for width.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "black"]
all_turtles = []
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!🎉🤩")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!🎉🤩")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
