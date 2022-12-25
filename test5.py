from turtle import *

b = 500
turtle = Turtle()

speed(200)
color('white')
bgcolor('black')
while b > 470:
    left(b/5)
    forward(100)
    b = b - 1

turtle.screen.mainloop()