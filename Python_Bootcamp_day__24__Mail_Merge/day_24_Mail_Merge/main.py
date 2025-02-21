# TODO: Create a letter using starting_letter.txt
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




# TODO: Create a letter using starting_letter.txt

name_list_m =[]
def create_a_letter():
    contents = start_letter()
    load_names()
    replace_name(contents)


def start_letter():
    with open("./Input/Letters/starting_letter.txt") as letter_file:
        contents = letter_file.read()
        return contents


# for each name in invited_names.txt
def load_names():
    #name_list = []
    with open("./Input/Names/invited_names.txt") as name_file:
        name_list = name_file.readlines()
    for name in name_list:
        name_m = name.strip("\n")
        name_list_m.append(name_m)


# Replace the [name] placeholder with the actual name.
def replace_name(contents):
    for name_n in name_list_m:
        named_letter = contents.replace("[name]", name_n)
        letter_in_folder(named_letter, name_n)

# Save the letters in the folder "ReadyToSend".
def letter_in_folder(named_letter, name_n):
     with open(f"./Output/ReadyToSend/letter_for_{name_n}.txt", mode="w") as letter_for_Aang:
         letter_for_Aang.write(named_letter)


create_a_letter()
