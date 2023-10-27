from turtle import Turtle, Screen
from random import choice

def draw_shapes(sides):
    angle=360/sides
    for j in range(0,sides):
        edi.fd(100)
        edi.right(angle)

colors=["indigo","teal","yellow","chocolate","firebrick","turquoise","aquamarine","navy"]

edi = Turtle()
edi.shape("turtle")
edi.pensize(5)

my_screen = Screen()
my_screen.bgcolor("green")
my_screen.setup(width=500, height=500)

edi.penup()
edi.setx(-50)
edi.sety(150)
edi.pendown()

for i in range(3,11):
    edi.color(choice(colors))
    draw_shapes(i)


my_screen.exitonclick()