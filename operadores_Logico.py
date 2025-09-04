# Operator logic en Python
x = True
y = False

print(f"x and y: {x and y}")  # False
print(f"x or y: {x or y}")  # True
print(f"not x: {not x}")  # False
print(f"not y: {not y}")  # True


a = 5
b = 10
c = 15

print(f"\n{a} < {b} and {b} < {c}: {a < b and b < c}")  # True
print(f"{a} > {b} or {b} < {c}: {a > b or b < c}")  # True
print(f"not ({a} < {b}): {not (a < b)}")  # False

# Table de true complete
print("\nTabla de true AND:")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")

print("\nTabla de true OR:")
print(f"True or True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"False or False: {False or False}")

d = 5
g = 10

print(f"d < g: {d < g}")

# Uso del operator not con comparative
print(f"not ({d} < {g}): {not (d < g)}")
