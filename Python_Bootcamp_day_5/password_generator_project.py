import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_l_choice = 0
random_n_choice = 0
random_s_choice = 0 #8


letter_save = ""
letter_count = 0

for letter in range(0,nr_letters):
    random_l_choice = random.randint(0, 51)
#    print(letters[random_l_choice])
    letter_count += 1
    letter_save += str(letters[random_l_choice])
print(f"letter_count {letter_count}")
print(f"letter_save {letter_save}")

symbol_count = 0
symbol_save = ""
for symbol in range(0,nr_symbols):
    random_s_choice = random.randint(0, 8)
#    print(symbols[random_s_choice])
    symbol_count += 1
    symbol_save += str(symbols[random_s_choice])
print(f"symbol_count {symbol_count}")
print(f"symbol_save {symbol_save}")

number_count = 0
number_save = ""
for number in range(0,nr_numbers):
    random_n_choice = random.randint(0, 9)
#    print(numbers[random_n_choice])
    number_count += 1
    number_save += str(numbers[random_n_choice])
print(f"number_count {number_count}")
print(f"number_save {number_save}")


print(letter_save + number_save + symbol_save)
save_pass = letter_save + number_save + symbol_save
print("save pass: " + save_pass)

pass_list = list(save_pass)
print(f"original:  {pass_list}" )


random.shuffle(pass_list)
print("shuffle:  ", pass_list)

password = ''.join(pass_list)
print(f"Your password is:  {password}")


