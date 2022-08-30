from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwords():
  tim.forward(10)




screen.listen()
screen.onkey(key="w", fun=move_forwords)
screen.exitonclick()