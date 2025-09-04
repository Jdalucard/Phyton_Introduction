class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Person details: {self.name}, {self.age}")


class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree

    def degree_Info(self):
        print(f"Student degree is:  {self.degree}")


p = Person("Alice", 30)
p.info()
s = Student("Bob", 20, "A")
s.degree_Info()
