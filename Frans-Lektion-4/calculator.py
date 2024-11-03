def add(x, y): 
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y):

    return x * y

def divide(x, y): 
    if y == 0:
        return "Error: Division with 0 is not allowed"
    return x / y

OPERATOR = {"+": add, "-": subtract, "*": multiply, "/": divide}

def user_input():
    try:
        First_number = int(input("Basenumber: "))
        operation = input("give me a operation[ +, -, *, /]: ")
        second_number = int(input("Number after operator: "))

    except ValueError:
        print("ERROR: Give a valid number.")
        return


    if operation in OPERATOR:
        result = OPERATOR[operation](First_number, second_number)
        print("Result:", result)

    else:
        print("ERROR, Give a valid operator.")
        return

user_input()