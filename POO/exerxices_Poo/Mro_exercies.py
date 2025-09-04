class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eating(self):
        print(f"{self.name} is eating.")


class Mammal(Animal):
    def __init__(
        self,
        name,
        age,
    ):
        super().__init__(name, age)

    def breast_feed(self):
        print(f"{self.name} is breastfeeding.")
        return self


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print(f"{self.name} is flying.")
        return self


class Bat(Mammal, Bird):
    def __init__(self, name, age):
        super().__init__(name, age)


bat1 = Bat("Batty", 3)

print(bat1.fly().breast_feed().eating())
print(Bat.__mro__)
