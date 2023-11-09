from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.r_score=0
        self.l_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Player1: {self.l_score}                 Player2: {self.r_score}" ,move=False ,align='center',font=('Arial', 20, 'normal'))

    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()

    def game_over(self,winner):
        self.color("red")
        self.goto(0,0)
        self.write(f"{winner} win!" ,move=False ,align='center',font=('Arial', 28, 'normal'))