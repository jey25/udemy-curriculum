from modulefinder import IMPORT_NAME
from turtle import Screen, Turtle
import turtle

t = Turtle()

t.shape("turtle")
t.color("red")

for _ in range(4):
  t.forward(100)
  t.right(90) 


import heroes


screen = Screen()
screen.exitonclick()