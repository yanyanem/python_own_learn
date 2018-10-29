#ColorSquareSpiral.py

import turtle

turtle.bgcolor("black")

t = turtle.Pen()
colors=["red","yellow","blue","green"]
t.pencolor("red")
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)

