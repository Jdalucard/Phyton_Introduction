""" INT """
x = 10
y = -5
z = 0
print(type(x)) 

""" FLOAT """
x = 3.14
y = -0.5
z = 2.0
print(type(x)) 

x = 3 + 4j
y = complex(2, -3)  # 2 - 3j
print(x.real)  # 3.0
print(x.imag)  # 4.0

name = "Juan"
message = 'Hola WORD'
multiplex = """Este es un
text de multiplex
Lines"""
print(type(name))  # <class 'str'>


fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed  = [1, "hello", 3.14, True]
print(type(fruits))  # <class 'list'>


unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
empty = set()  # ¡No usar {} para conjunto vacío!
print(type(unique_numbers))  # <class 'set'>

todos_los_tipos = [
    10,                   # int
    3.14,                 # float
    2 + 3j,               # complex
    "Hola Python",        # str
    True,                 # bool
    [1, 2, 3],            # list
    (4, 5, 6),            # tuple
    range(3),             # range
    {7, 8, 9},            # set
    frozenset([10, 11]),  # frozenset
    {"clave": "valor"},   # dict
    b"bytes",             # bytes
    bytearray(b"array"),  # bytearray
    None                  # NoneType
]

# Verificar tipos
for element in todos_los_tipos:
    print(f"{element} -> {type(element).__name__}")