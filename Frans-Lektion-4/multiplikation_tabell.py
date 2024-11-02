

def multiplication_table(number, up_to):
    """ Generate a multiplication table for a given number up to a specified range."""
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

multiplication_table(number = int(input("Multiply: ")), up_to = int(input("How many times to multiply: ")))