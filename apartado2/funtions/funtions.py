# search
number = [100, 500, 10000, 1000000, 85]

max = max(number)

print("the largest number is: ", max)

minor = min(number)
print("the smallest number is: ", minor)

# round
rounded = round(5.6789, 2)
print("the rounded number is: ", rounded)


# bool
print(bool(1))  # True
print(bool(0))  # False
print(bool("text"))  # True (string not empty)
print(bool(""))  # False (string empty)
print(bool([]))  # False (list empty)
print(bool([1, 2]))  # True (list with elements)

# all
print(all([True, True, True]))  # True (all are true)
print(all([True, False, True]))  # False (there is a False)
print(all([]))  # True (empty list = no false)

# Con numbers
print(all([1, 2, 3]))  # True (all != 0)
print(all([0, 1, 2]))  # False (there is a 0)

# sum
print(sum([1, 2, 3]))  # 6
print(sum([1, 2, 3], 10))  # 16 (start = 10)

# Con strings
print(all(["a", "b", "c"]))  # True (all not empty)
print(all(["a", "", "c"]))  # False (there is an empty string → False)
