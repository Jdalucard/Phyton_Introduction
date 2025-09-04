class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Tweet!"

    def speaking(self, beats):
        print(beats.speak())


animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")

bird = Bird()
dog = Dog()
bird.speaking(dog)
