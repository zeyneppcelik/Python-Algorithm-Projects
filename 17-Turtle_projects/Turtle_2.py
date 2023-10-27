from turtle import Turtle, Screen 
from random import choice

colors=["indigo","teal","yellow","chocolate","firebrick","turquoise","aquamarine","navy"]

directions=[0,90,180,270]

my_screen = Screen()
my_screen.setup(width=600,height=600)

edi = Turtle()
edi.shape("turtle")
edi.pensize(4)
edi.speed(5)

for i in range(100):
    edi.color(choice(colors))
    edi.forward(30)
    edi.right(choice(directions))

my_screen.exitonclick()