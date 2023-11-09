from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.color("white")
        self.penup()
        self.goto(cordinate)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(x=self.xcor(),y=new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(x=self.xcor(),y=new_y)
