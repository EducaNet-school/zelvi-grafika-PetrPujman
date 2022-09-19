import turtle
from turtle import *

turtle.speed(10)

penup()
goto(x=-420, y=400)

pendown()

left(270)
delka = 750
souradnicex = -420
souradnicey = 400

for i in range(13):
    for i in range(4):
        forward(delka)
        left(90)
    delka -= 60
    penup()
    souradnicex += 30
    souradnicey -= 30
    goto(x=souradnicex, y=souradnicey)
    pendown()

done()