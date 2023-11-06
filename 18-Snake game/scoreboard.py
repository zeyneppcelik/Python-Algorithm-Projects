from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}" ,move=False ,align='center',font=('Arial', 20, 'normal'))

    def write_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER" ,move=False ,align='center',font=('Arial', 28, 'normal'))