class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: Name: {self.name}, Age: {self.age}"


while True:
    
    name = input("Give me a name: ")


    if not name.isalpha():
        print("error: Please use characters and not integers")
        continue


    age = input("Give me a age: ")
    if not age.isdigit():
        print("Age must have a positive value, try again.")
        continue


    age = int(age)


    person = Person(name, age)
    print(person)
    break