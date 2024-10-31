# for loop with if, elif and else

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:    # Checks if current value of x is dividable by 3 and 5, if True then print Fizz if True prints FizzBuzz
        print("FizzBuzz")
   
    elif x % 3 == 0:        # Checks if current value of x is dividable by 3 and prints Fizz if True
        print("Fizz")
   
    elif x % 5 == 0:        # Checks if current value of x is dividable by 5 and prints Buzz if True
        print("Buzz")
    
    else: print(x)          # If value of x is not dividable by 3 or 5 then print value of x





# while loop with if, elif and else

#counter = 100
#while counter > 0: 
#    if counter % 3 == 0 and counter % 5 == 0:
#        print("FizzBuzz")
#    elif counter % 3 == 0:
#        print("Fizz")
#    elif counter % 5 == 0:
#        print("Buzz")
#    else: print(counter)
#    counter = counter -1