import colorsys
from modulefinder import IMPORT_NAME
from turtle import Screen, Turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# for _ in range(4):
#   t.forward(100)
  # t.right(90) 

# for _ in range(15):
#   t.forward(5)
#   t.up()
#   t.forward(5) 
#   t.down()

# colors = ["red", "blue", "gray", "black", "purple"]

# def draw_shape(num_sides):
#   angle = 360 / num_sides

#   for _ in range(num_sides):
#     t.forward(100)
#     t.rt(angle)

# for shape_side in range(3, 11):
#   t.color(random.choice(colors))
#   draw_shape(shape_side)

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_color = (r, g, b)
  return random_color

directions  = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(50)

for _ in range(200):
  tim.color(random_color())
  tim.forward(50)
  tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()