import random
from turtle import Turtle



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SMALLER_INCREMENT = 2


class CarManager(Turtle):
    def  __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        if random.randint(1,6) ==1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len= 2, stretch_wid= 1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self,current_level):
        if current_level == 1:
            self.car_speed += MOVE_INCREMENT
        else:
            self.car_speed += SMALLER_INCREMENT


    def set_speed(self, speed):
        self.car_speed = speed

