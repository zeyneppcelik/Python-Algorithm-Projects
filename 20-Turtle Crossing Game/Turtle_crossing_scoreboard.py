from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=-248,y=270)
        self.level=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}" ,move=False ,align='center',font=('Courier', 15, 'normal'))

    def write_score(self):
        self.level+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER" ,move=False ,align='center',font=('Arial', 28, 'normal'))