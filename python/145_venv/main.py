# from tkinter import Variable
# import module

# print(module.variable)

# from turtle import Screen, Turtle
# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)

