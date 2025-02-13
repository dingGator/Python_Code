import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_on = True
game_list = ["rock", "paper", "scissors"]
while game_on:
    user_choice = int(input("What do you choose? \n"
      "Type 0 for Rock, 1 for Paper, 2 for Scissors.  "))
    if user_choice not in[0,1,2]:
        print(f"{user_choice} is not a valid choice.")
        game_on = False
        continue

    computer_index = random.randint(0,2)

    print(f"You chose: {game_list[user_choice]}")

    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)


    print(f"Computer chose:  {game_list[computer_index]}")

    if computer_index == 0:
        print(rock)
    elif computer_index == 1:
        print(paper)
    elif computer_index == 2:
        print(scissors)


    if user_choice == computer_index:
        print("It is a draw.")
    elif (user_choice == 0 and computer_index == 2) or \
         (user_choice == 2 and computer_index == 1) or \
         (user_choice == 1 and computer_index == 0):
        print("You win.")
    else:
        print("You lose.")

