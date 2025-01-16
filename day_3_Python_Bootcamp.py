print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

if height == 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")


#odd or even number

user_num = int(input("Please give me a number: "))
num_modulo = user_num % 2

if num_modulo == 0:
    print("Your number is even")
else:
    print("Your number is odd.")

print("***************************\n")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 18:
        print("Please pay $7. ")
    else:
        print("Please pay $12. ")
else:
    print("Sorry you have to grow taller before you can ride.")

weight = 85
height = 1.85

bmi = weight / (height ** 2)


# Write your code below 👇
if bmi >= 18.5:

    if bmi < 25:  # weight between 18.5 and 25
        print("normal weight")
    elif bmi >= 25:
        print("overweight")
else:  # weight < 18.5
    print("underweight")
    print("*****************************\n")
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster")
        age = int(input("What is your age? "))
        if age <= 12:
            print("Please pay $5.")
        elif age <= 18:
            print("Please pay $7.")
        else:
            print("Please pay $12.")
    else:
        print("Sorry you have to grow taller before you can ride.")

print("***********************\n\n")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        print("free ticket")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


