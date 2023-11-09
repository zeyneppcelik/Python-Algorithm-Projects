from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.x_move=2
        self.y_move=2
        self.move_speed=0.01
    
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce(self, w_or_p):
        if w_or_p=="w":
            self.y_move*=-1
            self.move_speed*=0.1
        elif w_or_p=="p":
            self.x_move*=-1
            self.move_speed*=0.1

    def replay(self):
        self.home()
        self.x_move*=-1
        self.y_move*=-1
        self.move_speed=0.01