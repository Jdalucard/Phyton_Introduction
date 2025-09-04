# lambda FUNCTION anonymous
# benefits: conciseness, readability, and ease of use return automatic

multiply = lambda x, y: x * y
print(multiply(5, 3))

# filter
number = []
specials = []
for num in range(1, 5000):
    if num == 2 or num == 4 or num == 6:
        specials.append(f"{num} this is special number")
    number.append(num)

even_numbers = list(filter(lambda x: x % 2 == 0, number))
print(even_numbers[:30])
print(specials)
