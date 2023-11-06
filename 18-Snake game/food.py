from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("green")
        self.speed(10)
        self.locate()

    def locate(self):
        random_x=random.randint(-270,270)
        random_y=random.randint(-270,270)
        self.goto(random_x,random_y)