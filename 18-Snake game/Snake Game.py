from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
game_is_on=True

new_snake=Snake()
food = Food()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(new_snake.up, "Up")
my_screen.onkey(new_snake.down, "Down")
my_screen.onkey(new_snake.left, "Left")
my_screen.onkey(new_snake.right, "Right")

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    new_snake.move()
  
    if new_snake.head.distance(food)<15:
        food.locate()
        scoreboard.write_score()
        new_snake.grow()

    if (new_snake.head.xcor()>280) or (new_snake.head.xcor()<-280) or (new_snake.head.ycor()>280) or (new_snake.head.ycor()<-280):
        game_is_on=False
        scoreboard.game_over()

    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
        


my_screen.exitonclick()