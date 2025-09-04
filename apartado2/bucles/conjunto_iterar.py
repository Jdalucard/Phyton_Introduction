# CREATED LIST
dict = {"name": "lucas", "age": 30, "city": "dalton"}
letters = "hi jose"

for key, value in dict.items():
    print(f"{key} : {value}")
    if key == "age":
        dict[key] = value + 1
        print(f"{key} : {dict[key]}")

fruits = ["apple", "banana", "cherry", "tomato", "avocado"]

for fruit in fruits:
    if fruit == "banana":
        continue
    if fruit == "cherry":
        break
    print(f"this fruit is {fruit}")
# tour  chain text

for letter in letters:
    print(f"this letter is {letter}")

# for one line

number_Duplicate = [1, 2, 3, 4, 5]
print([X * 2 for X in number_Duplicate])


#
