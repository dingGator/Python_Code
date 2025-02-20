from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height= 600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
     screen.update()
     time.sleep(.5)
     snake.move()

     #detect collision with food
     if snake.head.distance(food) < 15:
          #print("non,non,non")
          food.refresh()
          snake.extend()
          scoreboard.increase_score()


     #detect collision with wall
     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
          scoreboard.reset()
          snake.reset()

     #detect collision with tail
     # if head collides with any segment in the tail
     # trigger game over
     for segment in snake.segments:
          if segment == snake.head:
               pass

          elif snake.head.distance(segment) < 10:
               scoreboard.reset()
               snake.reset()




screen.exitonclick()
