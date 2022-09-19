import turtle
from turtle import *


def polygon(A,B,C):

  for i in range(B):
    forward(A)
    left(C)

strany = int(input("kolik stran?"))
delka = int(input("delka strany?"))
stupne = 360/strany

polygon(delka, strany, stupne)
done()