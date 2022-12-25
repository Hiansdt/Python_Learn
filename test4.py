from turtle import *
import random

speed(200)
color('cyan')
bgcolor('black')
b = 200
c = 200
d = 200
e = 200
f = 200
g = 200
h = 200
i = 200
j = 200

turtle = Turtle()
screen = Screen()

colormode(255)
rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
goto(0, 0)

while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

penup()
goto(0, 0)
left(60)
rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while c > 0:
    left(c)
    forward(c * 3)
    c = c - 1

penup()
goto(0, 0)
left(60)
rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while d > 0:
    left(d)
    forward(d * 3)
    d = d - 1

penup()
goto(0, 0)
left(60)
rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while e > 0:
    left(e)
    forward(e * 3)
    e = e - 1
    
penup()
goto(0, 0)
left(60)

rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while f > 0:
    left(f)
    forward(f * 3)
    f = f - 1
    
penup()
goto(0, 0)
left(60)

rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while g > 0:
    left(g)
    forward(g * 3)
    g = g - 1
    
penup()
goto(0, 0)
left(60)

rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while h > 0:
    left(h)
    forward(h * 3)
    h = h - 1
    
penup()
goto(0, 0)
left(60)

rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while i > 0:
    left(i)
    forward(i * 3)
    i = i - 1

penup()
goto(0, 0)
left(60)

rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

while j > 0:
    left(j)
    forward(j * 3)
    j = j - 1

penup()
goto(0, 0)
left(60)

rdred = random.randrange(0, 20)
rdbg = random.randrange(70, 255)
color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
pendown()

turtle.screen.mainloop()