
def multiplication_table():
    number = input("Value to multiply?: ")
    up_to = input("What max value?: ")
    
    
    if number.isdigit() and up_to.isdigit():
     
        return int(number), int(up_to)
    
    else: return None, None



number, up_to = multiplication_table()

if number is not None and up_to is not None:
    if int(number) <= int(up_to):
        for i in range(1, int(up_to / number) + 1):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Base value needs to be bigger than max value")
else:
    print("Multiplication table creation failed due to invalid input.")
