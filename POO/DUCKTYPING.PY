# 1. ENLACE ESTÁTICO
def saludo():
    return "Hola! (enlace estático)"


print(saludo())  # El intérprete ya sabe exactamente qué función llamar


# 2. ENLACE DINÁMICO (POLIMORFISMO)
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# El método speak depende del OBJETO en tiempo de ejecución
animals = [Animal(), Dog(), Cat()]

for a in animals:
    print(f"{a.__class__.__name__}: {a.speak()}")


# 3. ENLACE DINÁMICO CON LIBRERÍAS (importación en runtime)
import importlib

# Cargo dinámicamente el módulo 'math'
math_module = importlib.import_module("math")

print("Raíz cuadrada de 16:", math_module.sqrt(16))
