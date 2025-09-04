"""
Ask the age of the classmates who came to class today and order the data from least to greatest.

b The oldest is the teacher and the youngest is the assistant."""

alumni = []

try:
    n = int(input("How many classmates came today? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if n <= 0:
    print("No classmates came today.")
    exit()

for i in range(n):
    name = input(f"Enter the name of classmate {i+1}: ")
    age = int(input(f"Enter the age of {name}: "))
    dictionary = {"name": name, "age": age}
    alumni.append(dictionary)

ordered_alumni = sorted(alumni, key=lambda x: x["age"])

younger = ordered_alumni[0]
older = ordered_alumni[-1]

print(
    f"The youngest is the assistant, {younger['name']}, who is {younger['age']} years old."
)
print(f"The oldest is the teacher, {older['name']}, who is {older['age']} years old.")


# primo
