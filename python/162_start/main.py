import colorsys
from modulefinder import IMPORT_NAME
from turtle import Screen, Turtle
import turtle
import random

t = Turtle()

t.shape("turtle")
t.color("red")

# for _ in range(4):
#   t.forward(100)
  # t.right(90) 

# for _ in range(15):
#   t.forward(5)
#   t.up()
#   t.forward(5) 
#   t.down()

colors = ["red", "blue", "gray", "black", "purple"]

# def draw_shape(num_sides):
#   angle = 360 / num_sides

#   for _ in range(num_sides):
#     t.forward(100)
#     t.rt(angle)

# for shape_side in range(3, 11):
#   t.color(random.choice(colors))
#   draw_shape(shape_side)

directions  = [0, 90, 180, 270]
t.pensize(15)
t.speed(50)

for _ in range(200):
  t.color(random.choice(colors))
  t.forward(50)
  t.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()