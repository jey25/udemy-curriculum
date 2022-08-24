from modulefinder import IMPORT_NAME
from turtle import Screen, Turtle
import turtle

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


def draw_shape(num_sides):
  angle = 360 / num_sides

  for _ in range(num_sides):
    t.forward(100)
    t.rt(angle)

for shape_side in range(3, 11):
  draw_shape(shape_side)


screen = Screen()
screen.exitonclick()