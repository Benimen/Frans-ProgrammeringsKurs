

def calculate(*args, operation ="add"):
    if not args:
        return 0
    

    if not all(isinstance(arg, (int, float)) for arg in args):
        return "Error, must be number: "


    if operation == "add":
        return sum(args)
    

    elif operation == "subtract":
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    

    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    

    elif operation == "divide":
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error, can not divide with 0"
            result /= num
        return result
    

    else:
        return "Error, Invalid operation"
    
numbers_input = input("Enter numbers and separate with space: ")
operation_input = input("Enter operation (add, subtract, multiply, divide): ")


try:
    numbers = [float(num) for num in numbers_input.split()]
except ValueError:
    print("Error: Enter valid number.")
else:
    result = calculate(*numbers, operation=operation_input)
    print("Result:", result)