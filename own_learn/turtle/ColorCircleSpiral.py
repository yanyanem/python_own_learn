#ColorCircleSpiral.py

import turtle

t = turtle.Pen()
turtle.bgcolor("black")

colors=["red","yellow","blue","green"]
t.pencolor("red")
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)

