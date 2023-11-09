from turtle import Turtle
import random

colors=["blue","red","violet","purple","indigo","crimson","maroon","navy","gold","sienna"]

class CarManager():
    def __init__(self):
        self.cars=[]
        self.car_speed=5

    def create_car(self):
        change=random.randint(1,6)
        if change==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            y_cor=random.randint(-240,240)
            new_car.goto(x=-310,y=y_cor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)