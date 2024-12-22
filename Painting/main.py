# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('spot painitng.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
hkb = turtle_module.Turtle()
hkb.speed("fastest")
hkb.penup()  # if u want to see path comment this line
hkb.hideturtle()
color_list = [(202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203),
              (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60),
              (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168),
              (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163),
              (49, 57, 66), (41, 75, 78)]

hkb.setheading(225)
hkb.forward(300)
hkb.setheading(0)
no_of_dots = 100

for dot_counts in range(1, no_of_dots + 1):
    hkb.dot(20, random.choice(color_list))
    hkb.forward(50)
    if dot_counts % 10 == 0:
        hkb.setheading(90)
        hkb.forward(50)
        hkb.setheading(180)
        hkb.forward(500)
        hkb.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
