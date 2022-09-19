import turtle
from turtle import *


def ctverec(A):

  for i in range(4):
    forward(A)
    left(90)

delka = int(input("delka strany"))

ctverec(delka)
penup()
goto(x=200, y=0)
pendown()
ctverec(delka)


done()