

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


threshold = int(input("Give a value: "))


squared_numbers = list(map(lambda x: x ** 2, numbers))


filtered_numbers = list(filter(lambda x: x > threshold, squared_numbers))


print(f"Original List: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Numbers greater than given value: {filtered_numbers}")