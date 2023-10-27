from turtle import Turtle, Screen 
from random import choice


def spirograph(size, rad, color):
    for i in range(int(360/size)):
        edi.color(color)
        edi.circle(rad)
        current_heading=edi.heading()
        edi.setheading(current_heading+size)

my_screen = Screen()
my_screen.bgcolor("green")

edi =Turtle()
edi.pensize(3)
edi.speed(10)

spirograph(20, 100, "white")
spirograph(5, 30, "yellow")

my_screen.exitonclick()