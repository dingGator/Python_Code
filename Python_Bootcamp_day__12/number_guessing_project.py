from random import randint
from number_guessing_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    user_level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    #print(user_level)

    if user_level == "easy":
        turns  = EASY_LEVEL_TURNS

    elif user_level == "hard":
        turns = HARD_LEVEL_TURNS
    return turns

def check_answer(user_guess, answer, turns):
    if user_guess != answer:
        turns -= 1
        if user_guess > answer:
            print("Too high.")
        else:
            print("Too low.")
    else:
        print(f"You got it! The answer was {answer}")

    return turns



def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()

    user_guess = 0

    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns= check_answer(user_guess,answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != answer:
            print("Guess again.")


game()
