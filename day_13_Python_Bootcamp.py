import day_13_maths
import random

print("****** describe the problem*****\n")

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()

print("\n***** reproduce the bug*******\n")
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

print("\n***** play computer *****\n")
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")


print("\n******** fix the errors*****\n")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))


if age > 18:
    print(f"You can drive at age {age}.")

print("***** use print*******")

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

print("******* use a debugger******")


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = day_13_maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

