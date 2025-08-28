a = 5
b = 10
c = a + b
print(c)

# Con strings
texto = "Hola Mundo"
print("Hola" in texto)   # True
print("Python" in texto) # False

# Con listas
frutas = ["manzana", "banana", "cereza"]
print("banana" in frutas)  # True
print("uva" in frutas)     # False

# Con diccionarios (verifica claves)
persona = {"nombre": "Ana", "edad": 25}
print("nombre" in persona)  # True (clave)
print("Ana" in persona)     # False (valor)