
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print(fruits)

print("--------------")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score = sum(student_scores)
print(total_score)

sum_score = 0
for score in student_scores:
    sum_score += score
print(sum_score)

print(max(student_scores))


print("--------------")
score = 0
score_index = 0
max_score = 0

for score in student_scores:
        if max_score <= score:
#            print(score_save)
            max_score = score
print(f"highest score:  {max_score}")

print("--------------")

for number   in range(1,11):
    print(number)

for number in range(1,10,3):
    print(number)


print("-----for range loop----------")
number_total = 0
for number in range(1,101):
    number_total += number
#    print(f"print: {number_total}")

print(f"total: {number_total}")



print("Fizzbuzz game ----------")
for number in range (1,101):

    if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


