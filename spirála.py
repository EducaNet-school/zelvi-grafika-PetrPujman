import turtle
from turtle import *
turtle.speed(50)
penup()
goto(x=-420, y=400)

pendown()
left(270)
delka = 750

for i in range(27):
    forward(delka)
    left(90)
    delka -= 30

done()