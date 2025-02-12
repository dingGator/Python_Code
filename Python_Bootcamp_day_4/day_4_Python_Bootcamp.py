import random
import day_4_my_module

random_integer = random.randint(1,10)
print(random_integer)

print(day_4_my_module.my_favorite_number)

print("\n*****************\n")

random_number_0_to_1 = random.random()
print(f"random_number_0_to_1 = {random_number_0_to_1}")

random_number_0_to_10 = random.random() *10
print(f"random_number_0_to_10 = {random_number_0_to_10}")

random_float = random.uniform(1,10)
print(f"random_float = {random_float}")

print("\n******Game: heads or tails *******")
head_or_tail = random.randint(0,1)
print(head_or_tail)
if head_or_tail == 0:
    print("Heads")
else:
    print("Tails")

print("******************")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina","Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio","Louisiana", "Indiana",
                     "Mississippi", "Illinois","Alabama", "Maine", "Missouri", "Arkansas", "Michigan","Florida", "Texas", "Iowa",
                     "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[15])
print(states_of_america[-2])
print(len(states_of_america))
num_of_states = len(states_of_america)
index_of__last_state = len(states_of_america) -1
print("the index of the last state in the list\n states_of_america "
      "is:    len(states_of_america -1)")

print("\n******************\n")
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(f"{random.choice(friends)} will pay the bill today")

pay_bill_index = random.randint(0,4)
print(f"{friends[pay_bill_index]} will pay the bill today!.")





