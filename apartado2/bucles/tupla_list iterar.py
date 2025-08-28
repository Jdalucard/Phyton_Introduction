# for
animals = ["dog", "cat", "rabbit"]
number = [1, 2, 3, 4, 5]

for animal in animals:
    print(f"this variable is {animal}")

dictionary = {"name": "lucas", "age": 30, "city": "dalton"}

for key, value in dictionary.items():
    print(f"{key} : {value}")
    if key == "age":
        dictionary[key] = value + 1
        print(f"{key} : {dictionary[key]}")

for num in number:
    result = num * 2
    print(f"this result is {result}")

for i in range(len(animals)):
    print(f"this index is {i} and the animal is {animals[i]}")

for animal, num in zip(animals, number):
    print(f"this animal is {animal} and the number is {num}")

for index, animal in enumerate(animals):
    print(f"this index is {index} and the animal is {animal}")
