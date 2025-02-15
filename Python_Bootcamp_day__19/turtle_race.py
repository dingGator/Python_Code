import turtle
import random


is_race_on =False
screen = turtle.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                 prompt= "Which turtle will win the race? Enter a color:  ")
name1_list = ["winston", "andrew", "britney", "rick", "kim", "deanne"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = {}

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])

    all_turtles[name1_list[turtle_index]] = new_turtle
    #all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for name, turtle_obj in all_turtles.items():
        turtle_obj.clear()
        turtle_obj.write(name,
                         align="right",font=("Arial", 12, "normal"))
        if turtle_obj.xcor() > 230:
            is_race_on = False
            winning_color = turtle_obj.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {name} turtle is the winner!")
            else:
                print(f"You've lost! The {name} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle_obj.forward(rand_distance)




screen.exitonclick()

