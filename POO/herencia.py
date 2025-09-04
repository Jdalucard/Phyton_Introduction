# Herencia
# pass no hace nada pero permite que la clase hija herede los atributos y métodos de la clase padre


class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age


# simple Inherent
class Student(Person):
    def __init__(self, name, lastname, age, student_id, subject):
        super().__init__(name, lastname, age)
        self.student_id = student_id
        self.subject = subject


studentOne = Student("John", "Doe", 20, "S123", "Mathematics")

print(studentOne.name)  # John


# multiple Inheritance
class GraduateStudent(Student):
    def __init__(self, name, lastname, age, student_id, subject, thesis_title):
        super().__init__(name, lastname, age, student_id, subject)
        self.thesis_title = thesis_title

    def defend_thesis(self):
        print(f"{self.name} is defending their thesis titled '{self.thesis_title}'.")


gradStudent = GraduateStudent(
    "Alice", "Smith", 25, "G456", "Physics", "Quantum Mechanics"
)

print(gradStudent.name)  # Alice


# Multilevel Inheritance


class TeachingAssistant(GraduateStudent):
    def __init__(
        self, name, lastname, age, student_id, subject, thesis_title, assistant_id
    ):
        super().__init__(name, lastname, age, student_id, subject, thesis_title)
        self.assistant_id = assistant_id


ta = TeachingAssistant(
    "Bob", "Johnson", 28, "T789", "Chemistry", "Organic Chemistry", "TA001"
)


print(ta.defend_thesis())


# Hierarchical Inheritance
class UnderGraduateStudent(Student):
    def __init__(self, name, lastname, age, student_id, subject, year):
        super().__init__(name, lastname, age, student_id, subject)
        self.year = year


ugStudent = UnderGraduateStudent("Charlie", "Brown", 19, "U123", "Biology", 2)

print(ugStudent.name)  # Charlie
