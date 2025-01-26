from random import random

import black_jack_art
import random

print(black_jack_art.logo)


def deal_card():
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards_list)
    return random_card


def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    # print(f"hint_sum {hint_sum}")
    sum_cards = sum(cards_list)
    return sum_cards


def compare(computer_score, user_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        print("Computer win! Black Jack")

    elif user_score == 0:
        print("You Win! Black Jack")

    elif user_score > 21:
        print("You are over. You lose")


    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while is_game_over == False:


        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score, user_score))


play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while (play_again == "y"):
    print("\n" * 20)
    print(black_jack_art.logo)
    play_game()
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
