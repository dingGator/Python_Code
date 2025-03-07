import calculator_art

print(calculator_art.logo)
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def function_calc(input1, operation1, input2):
    answer = operations[operation1](input1, input2)
    return answer

continue_calc = "y"
input_num1 = float(input("What's the first number?: "))

while continue_calc == "y":

    print("+ \n -\n *\n /\n")
    operation_type = input("Pick an operation: ")
    input_num2 = float(input("What's the next number?: "))

#Program works out the result based on the chosen
# mathematical operator.

    output_answer = function_calc(input1=input_num1,
                                  operation1=operation_type,
                                  input2=input_num2)
    print(f"{input_num1} "
          f"{operation_type} "
          f"{input_num2} = "
          f"{output_answer} ")
#Program asks if the user wants to continue working
# with the previous result.
    continue_calc  = input(f"Type 'y' to continue calculating with "
                           f"{output_answer}, "
                           f"or type 'n' to start new calculation "
                           f"or type 'q' to quit: ").lower()
#If yes, program loops to use the previous result
# as the first number and then repeats the calculation process.
    if continue_calc == "y":
        input_num1 = output_answer
    elif continue_calc == "n":
        input_num1 = float(input("What's the first number?: "))
        continue_calc = "y"
    elif continue_calc == "q":
        print("Thank you for using the calculator. Goodbye!")
        break

#
