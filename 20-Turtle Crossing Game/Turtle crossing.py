from turtle import Screen
import time
from car import CarManager
from Turtle_player import Player
from Turtle_crossing_scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

edi=Player()

car_manager=CarManager()

scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(edi.move_forward,"space")


game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(edi)<20:
            scoreboard.game_over()
            game_is_on=False

    if edi.ycor()>270:
        scoreboard.write_score()
        edi.replay()
        car_manager.car_speed+=5

screen.exitonclick()
