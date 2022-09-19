import turtle
from turtle import *


def trojuhelnik(A):

  for i in range(3):
    forward(A)
    left(120)

delka = int(input("delka strany"))

for i in range(6):
    trojuhelnik(delka)
    left(60)

done()