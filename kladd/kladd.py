#words = ["God father", "Lotr", "Interstellar"]
#result = ", ".join(words)
#print(result)

#str = "hello world"
#print(str.capitalize())
#print(str.title())

#str = " Hello world "
#print(str)
#print(str.strip())
#print(str.rstrip())
#print(str.lstrip())

#skapar lista från en string
#str = "orange,banana,kiwi"
#fruits = str.split(",")
#print(fruits)


#words = "I like banana"
#print(words.replace("banana", "kiwi"))


#words = "Hello world"
#print(words.find("world"))


#name = "beni"
#age = 29
#print(f"My name is {name} and I am {age}")

#empty_list = []
#my_list = ["kiwi", 42, True, 6.9]
#print(empty_list, my_list[2])

#kolla vad som är längst bak i listan
#print(my_list[-1])

#my_list = ["kiwi", 33, True, 3.6]
#my_list[1] = "banan"
#print(my_list)

#numbers = [1,2,3,4,5]
#numbers[1:4] = [20,30,40]
#print(numbers)

#numbers = [1,2,3,4,5]
#numbers.append(6)
#print(numbers)

#numbers = [1,2,3,4,5]
#numbers.insert(2, "blabla")
#print(numbers)


#fruits = ["kiwi", "banana", "melon", "raspberry"]
#fruits.remove("banana")
#print(fruits)

#deleted = fruits.pop(2)
#print(f"We removed {deleted} in our list: {fruits}")

#fruits.pop()
#print(fruits)

#del fruits
#print(fruits)

#fruits.clear()
#print(fruits)


#fruits = ["kiwi", "raspberry", "melon", "cherry", "pear"]
#print(fruits[1:4])
#print(fruits[:3])
#print(fruits[2:])
#print(fruits[::2])
#print(fruits[::-1])


#fruits = ["kiwi", "raspberry", "melon", "cherry", "pear"]
#numbers = [1,3,2,6,4,5]
#print(fruits.count("kiwi"))
#fruits.sort()
#print(fruits)
#numbers.sort()
#print(numbers)


#fruits = ["kiwi", "raspberry", "melon", "cherry", "pear"]
#print(len(fruits))

#numbers = [1,3,2,6,4,5]
#print(sum(numbers))

## Dictionaries ##

#empty_dict = {}

#person = {"name": "ben", "age": 29, "city": "stockholm"}
#print(person.get("name"))

#person["age"] = 25
#print(person)

#person["proffession"] = "pentester"

#print (person)

#person = {"name": "ben", "age": 29, "city": "stockholm"}

#age = person.pop("age")
#print(age)
#print(person)

#del person["name"]
#print(person)

#person["proffession"] = "pentester"
#print(person)

#tar bort senaste tillagda
#key, value = person.popitem()

#print(key, value)
#print(person)

#person = {"name": "ben", "age": 29, "city": "stockholm"}

#person.clear()
#print(person)

#keys = person.keys()
#print(keys)

#values = person.values()
#print(values)

#tuples = person.items()
#print(tuples)

## Tuples ##

#empty_tuple = ()

#small_tuple = (5,)

#fruits = ("kiwi", "raspberry", "cherry")

#blir till en tuple automatiskt
#fruits = "kiwi", "raspberry", "cherry"
#print(fruits)
#print(type(fruits))

#fruits = ("kiwi", "raspberry", "cherry", "banana", "melon", "apple")
#print(fruits[0])
#print(fruits[::-1])

#print(fruits[1:4])

#fruits = ("kiwi", "raspberry", "cherry", "banana", "melon", "apple")
#fruits_list = list(fruits)
#fruits_list[3] = "orange"
#fruits = tuple(fruits_list)
#print(fruits)

#fruits = ("kiwi", "raspberry", "cherry", "banana", "apple")
#fruit1, fruit2, fruit3 = fruits
#print(fruit1)
#print(fruit2)
#print(fruit3)

#fruits = ("kiwi", "raspberry", "cherry", "banana", "melon", "apple")
#fruit1, fruit2, *rest = fruits
#print(fruit1)
#print(fruit2)
#print(rest)

#numbers = fruits.count("melon")
#print(numbers)

#index = fruits.index("cherry")
#print(index)

## Sets ##

#empty_set = set()
#fruits = {"cherry", "raspberry", "kiwi", "apple", "apple",}
#print(fruits)
#print(fruits[2]) #kommer inte fungera

#fruits.add("grape")
#print(fruits)

#fruits.update(["orange", "mango"])
#fruits.remove("apple")
#print(fruits)

#fruits.discard("cherry")
#print(fruits)

#element = fruits.pop()
#print(element)
#print(fruits)

#fruits.clear()
#print(fruits)

set1 = {1,2,3}
set2 = {3,4,5}

#union_set = set1 | set2
#union_set = set1.union(set2)

#print(union_set)

#intersection_set = set1 - set2
#print(intersection_set)

#symmetric = set1 ^ set2
#print(symmetric)

frozen_fruit = frozenset(["apple", "orange", "grape"])
print(frozen_fruit)

frozen_fruit.add("banana")