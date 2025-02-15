import random
#import turtle as t
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
#
color_list =[(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]
#

tim.speed(0)
tim.penup()
tim.hideturtle()

start_x = -200
start_y = -200
tim.setpos(start_x,start_y)


def create_painting(list_color, rows, cols, dot_size, spacing):
#
    for row in range(rows):
        for col in range(cols):
            tim.dot(dot_size,random.choice(list_color))
            tim.forward(spacing)
        tim.setpos(start_x, tim.ycor() + spacing)





create_painting(list_color = color_list, rows= 10,
                cols=10, dot_size = 20, spacing = 50)


screen = turtle_module.Screen()
screen.exitonclick()

