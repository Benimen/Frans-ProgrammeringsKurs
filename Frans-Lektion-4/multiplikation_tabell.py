number = int(input("Multiply: "))
up_to = int(input("up to: "))

def multiplication_table(number, up_to):
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

multiplication_table(number, up_to)

