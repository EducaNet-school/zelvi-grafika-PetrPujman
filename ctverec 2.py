import turtle
from turtle import *


def ctverec(A):

  for i in range(4):
    forward(A)
    left(90)

delka = int(input("delka strany"))

ctverec(delka)

done()