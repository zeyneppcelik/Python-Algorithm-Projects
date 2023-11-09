from turtle import Turtle

STARTING_POS=(0,-270)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move_forward(self):
        self.forward(10)

    def replay(self):
        self.goto(STARTING_POS)