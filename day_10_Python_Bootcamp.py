
print("************Functions with outputs****")
f_name = ""
l_name = ""
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"in {formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"


format_name(f_name= "kiM", l_name= "jfoiH")
formated_str = format_name(f_name= "kiM", l_name= "jfoiH")
print("out " + formated_str)
print(format_name(f_name= "kiM", l_name= "jfoiH"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

print(f"\n  ********* Multiple Return Values************")

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f" Result: {formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
print(format_name(input("What is your first name?"), input ("What is your last name?")))

print(f"\n****************** Docstrings *********\n")
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
print(formatted_name)

print(f"\n ********** calculator**************\n")

def add(n1, n2):
    return n1 + n2

def multiply(n1,n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def function_calc(input1, operation1, input2, ):
    answer = 0

    if operation1 == "+":
        answer = operations["+"](n1=input1, n2=input2)
    elif operation1 == "-":
        answer = operations["-"](n1=input1, n2=input2)
    elif operation1 == "*":
        answer = operations["*"](n1=input1, n2=input2)
    elif operation1 == "/":
        answer = operations["/"](n1=input1, n2=input2)

    return answer


output_calc=function_calc(input1=25,operation1="*", input2= 6)
print(f"output of function_calc:  {output_calc}")

calc_dictionary  = {}

calc_dictionary["+"] = add
calc_dictionary["-"] = subtract
calc_dictionary["*"] = multiply
calc_dictionary["/"] = divide


print(f"calc_dictionary + = {calc_dictionary["+"](n1=4,n2=8)}")
print(f"calc_dictionary * = {calc_dictionary["*"](n1=4, n2=8)}")

