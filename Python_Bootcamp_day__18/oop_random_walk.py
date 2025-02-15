import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()

t.colormode(255)
colors = ["CornflowerBlue", "rosybrown", "gold", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colors = (r,g,b)
    return random_colors



#
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for _  in range(200):
#    tim.color((random.choice(colors)))
#
    tim.color(random_color())
    tim.forward(30)
    tim.setheading((random.choice(directions)))


screen = Screen()
screen.exitonclick()


