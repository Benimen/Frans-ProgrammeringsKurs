class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: Name: {self.name}, Age: {self.age}"


def get_user_input():
    while True:
        
        name = input("Give me a name: ")
        if name.isalpha():
            try:
                age = int(input("Give me a age: "))
                if age < 0:
                    print("Age must have a positive value, try again.")
                    continue

                person = Person(name, age)
                print(person)
            except ValueError:
                print("Give a valid age (integer not float)")
        else:
            print("error: Please use characters and not integers")
            continue

get_user_input()