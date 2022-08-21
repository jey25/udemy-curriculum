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

for _ in range(3):
  t.forward(100)
  t.rt(360/3)

t.color("blue")

for _ in range(4):
  t.forward(100)
  t.rt(360/4)

t.color("purple")

for _ in range(5):
  t.forward(100)
  t.rt(360/5)

t.color("black")

for _ in range(6):
  t.forward(100)
  t.rt(360/6)

t.color("gray")

for _ in range(7):
  t.forward(100)
  t.rt(360/7)




screen = Screen()
screen.exitonclick()