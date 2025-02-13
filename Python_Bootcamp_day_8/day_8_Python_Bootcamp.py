def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")
    print("Bye")

greet()

print("**************")

# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Kim", "Florida")
greet_with("Nowhere", "Jack Bauer")

greet_with(name = "Kim", location = "Florida")

greet_with(location = "Florida", name = "Kim")


print("*******************")