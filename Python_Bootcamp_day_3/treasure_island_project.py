from random import choice

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn_choice = input('You\'re at a crossroad, where do you want to go? '
                    'Type "left" or "right".\n').lower()


if turn_choice == "left":

    swim_choice = input('You\'ve come to a lake. '
                        'There is an island in the middle of the lake. '
                        'Type "wait" to wait for a boat. '
                        'Type "swim" to swim across.\n').lower()

    if swim_choice == "wait":

        door_choice = input('You arrive at the island unharmed. '
                            'There is house with 3 doors. '
                            'One red, one yellow and one blue. '
                            'Which colour do you choose?\n').lower()

        if  door_choice == "yellow":
            print("You Win!")
        elif door_choice == "red":
            print("You are burned by fire.  Game Over.")
        elif door_choice == "blue":
            print("You are eaten by beasts.  Game Over.")
        else:
            print("Not a door choice.  Game Over.")
    else: #Swim choice or anything else
        print("You were attacked by a trout.  Game Over.")
else:  #Right choice or anything else
    print("You fall into a hole. Game Over.")