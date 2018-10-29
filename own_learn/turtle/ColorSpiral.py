#ColorSpiral.py

import turtle

turtle.bgcolor("black")

t = turtle.Pen()

sides=6

colors=["red","yellow","blue","green","orange","purple"]

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)




