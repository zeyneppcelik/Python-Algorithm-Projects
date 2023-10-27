import turtle
from random import choice
#################
#import colorgram

##selecting colors from an image by using colorgram module##
#colors=colorgram.extract('image.jpg',20)

#rgb_colors=[]
#for i in colors:
#    r=i.rgb.r
#    g=i.rgb.g
#    b=i.rgb.b
#    rgb_colors.append((r,g,b))

#rgb_colors.pop(0)
#rgb_colors.pop(0)
#rgb_colors.pop(0)
#################

turtle.colormode(255)

def draw_row():
    for i in range(10):
        edi.dot(25,choice(rgb_color_list))
        edi.forward(60)

rgb_color_list=[(229, 249, 73), (229, 237, 253), (67, 252, 194), (17, 184, 82), (19, 15, 96), (218, 153, 94), (74, 37, 23), (94, 1, 56), (59, 4, 180), (247, 102, 203), (28, 245, 41), (248, 21, 135), (168, 3, 123), (6, 99, 40), (100, 179, 5), (50, 15, 253), (106, 172, 243)]

my_screen=turtle.Screen()
my_screen.setup(width=600, height=600)

edi=turtle.Turtle()
edi.speed(10)
edi.penup()
edi.hideturtle()
edi.setpos(x=-275,y=-275)
for i in range(10):
    draw_row()
    edi.left(90)
    edi.forward(60)
    edi.left(90)
    edi.forward(600)
    edi.right(180)


my_screen.exitonclick()