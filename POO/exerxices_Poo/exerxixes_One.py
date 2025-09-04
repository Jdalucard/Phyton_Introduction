data = input("Enter student details (name, age, grade): ")


class Student:  #
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"The student {self.name} is studying.")


parts = data.replace(",", " ").split()
if len(parts) == 3:
    studentOne = Student(parts[0], int(parts[1]), parts[2])
    studentOne.study()
    print(studentOne.name)
    print(studentOne.age)
    print(studentOne.grade)
else:
    print("❌ Please enter the data in the format: name, age, grade")

    studentOne = None
if studentOne:
    action = input("Enter action (study): ").capitalize()
    if action == "Study":
        studentOne.study()
    else:
        print("❌ Invalid action. Please enter 'study'.")
