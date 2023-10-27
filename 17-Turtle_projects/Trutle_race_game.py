from turtle import Turtle, Screen 
from random import choice
import random

turtle_colors=["red","orange","yellow","green","blue","purple"]

is_race_on=False

all_turtles=[]

def create_turtle(colors):
    a=0
    for color in colors:
        new_turtle =Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-170,y=-130+a)
        a+=50
        all_turtles.append(new_turtle)

my_screen = Screen()
my_screen.setup(width=400,height=400)

bet=my_screen.textinput("Bet","Who will win the race?")

create_turtle(turtle_colors)

if bet:
    is_race_on=True

while is_race_on:
    for _turtle in all_turtles:
        if _turtle.xcor()>180:
            is_race_on=False
            winner_color=_turtle.pencolor()
        else:
            dist= random.randint(0,10)
            _turtle.forward(dist)

if winner_color.lower()==bet.lower():
    print(f"You've won. The winner is {winner_color} turtle")
else:
    print(f"You've lost. The winner is {winner_color} turtle")
my_screen.exitonclick()