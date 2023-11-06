from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in range(3):
            a=(-20)*i
            b=0
            self.add__segment((a,b))

    def add__segment(self, positions):
        new_segment = Turtle(shape="circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def grow(self):
        self.add__segment(self.segments[-1].position())        

    def move(self):
        s=len(self.segments)-1
        for segment_num in range(s,0,-1):
            new_x=self.segments[segment_num-1].xcor()
            new_y=self.segments[segment_num-1].ycor()
            self.segments[segment_num].goto(new_x,new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

