#data type
#string
print(len("Hello"))

#subscripting
#to print out H
print("Hello"[0])
#to print out o
print("Hello"[4])
#to print out o
print("Hello"[-1])
print("123"+"456")
#integer
print(123 +456)
#large integer
print(123_456_789)
#float = decimal
print(123.45)
#boolean
print(True)
print(False)

#TypeError
#len(12345)
#print(len(12345))
len("12345")
print(len("12345"))
type("hello")
print(type(12345))

#print out all 4 data types
print(type("Hello"))
print(type(12345))
print(type(123.45))
print(type(True))

#type conversion
print(int("123") + int("456"))

user_name = input("Enter your name ")
name_length = len(user_name)
print("Number of letters in your name: " + str(name_length))

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# order = PEMDAS
print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3)

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))
print(round(bmi, 3))

score = 0
score = score + 1
print(score)
score += 1
print(score)
score *= 2
print(score)

#f-string
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, "
      f"your height is {height}."
      f" You are winning is {is_winning}")



