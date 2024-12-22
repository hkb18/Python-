# from turtle import Turtle, Screen
#
# hkb = Turtle()
# print(hkb)
# hkb.shape("turtle")
# hkb.color("cyan")
# hkb.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
