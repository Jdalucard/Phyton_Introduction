import csv
import os

# created two lists

name = ["John", "Jane", "Doe"]
lastname = ["Smith", "Doe", "Johnson"]


directory_current = os.path.dirname(os.path.abspath(__file__))
rute_file = os.path.join(directory_current, "wie.txt")

with open(rute_file, "w", encoding="utf-8") as file:
    file.write("Name,Lastname\n\n")
    for name, lastname in zip(name, lastname):
        file.write(f"{name},{lastname}\n")
