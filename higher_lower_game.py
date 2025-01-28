import random

import higher_lower_art
import higher_lower_data


# 50 entries in game_data

#print(len(game_data.data))
follower_count_a =0
follower_count_b =0

score = 0
game_on = True
def data_info(letter, data_in):
    random_num = random.randint(0, len(data_in)-1)
    #print(random_num)
    info_data = data_in[random_num]
    name = info_data['name']
    description = info_data['description']
    country = info_data['country']
    if letter == 'a':
        follower_count_a = info_data['follower_count']
        print(f"Compare A:  {name},"
              f" a {description},"
              f" from {country}")
        return name,description, country, follower_count_a
    elif letter == 'b':
        follower_count_b = info_data['follower_count']
        print(f"Against B:  {name},"
              f" a {description},"
              f" from {country}")
        return name, description, country, follower_count_b


def play_game(data):
    print(higher_lower_art.logo)
    name_a, description_a, country_a, follower_count_a= data_info(letter = 'a',data_in= data)
    game_on = True
    score = 0
    while game_on:

        print(higher_lower_art.vs)
        name_b, description_b, country_b, follower_count_b = data_info(letter= 'b', data_in= data)

        if follower_count_a > follower_count_b:
            won_answer = 'a'
        else:
            won_answer = 'b'

        user_input = input("Who has more followers? Type 'A' or 'B'  ").lower()
        if user_input == won_answer:
            print(higher_lower_art.logo)
            score += 1
            print(f"You're right! Current score:{score}")
        # b entry becomes a entry
            name_a = name_b
            description_a = description_b
            country_a = country_b
            follower_count_a = follower_count_b
            print(f"Compare A:  {name_a},"
                f" a {description_a},"
                f" from {country_a}")
            game_on = True
        else:
            print(f"Sorry, That's wrong.  Final score: {score}")
            game_on = False

play_game(higher_lower_data.data)

