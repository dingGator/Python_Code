from turtle import Screen
from pong_game__paddle import Paddle
from pong_game__ball import Ball
from pong_game__scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  #** turn the animation off **

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball= Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")


game_is_on = True



while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() #** show the paddle in its new position
    ball.move()

    #ball hit top or bottom edge
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or\
        ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    #detect miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



    #ball.pendown()
    #




screen.exitonclick()

