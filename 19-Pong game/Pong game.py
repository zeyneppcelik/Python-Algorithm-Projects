from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from pong_scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

r_scoreboard=Scoreboard(200)
l_scoreboard=Scoreboard(-200)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce("w")

    if (ball.xcor()>330 and ball.distance(r_paddle)<50) or (ball.xcor()<-330 and ball.distance(l_paddle)<50) :
        ball.bounce("p")
    elif ball.xcor()>390 :
        ball.replay()
        l_scoreboard.write_score()
    elif ball.xcor()<-390:
        ball.replay()
        r_scoreboard.write_score()
   

screen.exitonclick()
