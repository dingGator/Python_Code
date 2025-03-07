import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #check if the player has reached the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up(scoreboard.level)
        scoreboard.increase_level()

screen.mainloop()
