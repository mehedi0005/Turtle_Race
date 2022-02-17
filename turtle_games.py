#This is Turtle Race Game.
#By - team_error

from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)
for step in range(11):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

red_turtle = Turtle()
red_turtle.color('red')
red_turtle.shape('turtle')
red_turtle.penup()
red_turtle.goto(-160, 100)
red_turtle.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

coc = Turtle()
coc.color('green')
coc.shape('turtle')
coc.penup()
coc.goto(-160,40)
coc.pendown()

sob = Turtle()
sob.color('black')
sob.shape('turtle')
sob.penup()
sob.goto(-160,10)
sob.pendown()


for turn in range(40):
    red_turtle.forward(randint(1,10))
    bob.forward(randint(1,11))
    coc.forward(randint(1, 11))
    sob.forward(randint(1, 11))

exitonclick()
