from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
def move_backward():
    #tim.setheading(180)
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()




screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
