# import colorgram

# rgb_colors = []

# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 6)

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r,g,b)
#   rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
  tim.dot(20, "black")
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()