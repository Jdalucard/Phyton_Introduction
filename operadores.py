# operadores.py
# Operadores de Pertenencia y Concatenación en Python

def main():
    print("=" * 50)
    print("OPERATORS DE PERTINENCY (in, not in)")
    print("=" * 50)
    
    # Operador in con strings
    texto = "Hola Mundo"
    print(f"\n📌 'in' con strings:")
    print(f"¿'Hola' está en '{texto}'? -> {'Hola' in texto}")
    print(f"¿'Python' está en '{texto}'? -> {'Python' in texto}")
    
    # Operador in con listas
    frutas = ["manzana", "banana", "cereza"]
    print(f"\n📌 'in' con listas:")
    print(f"¿'banana' está en {frutas}? -> {'banana' in frutas}")
    print(f"¿'uva' está en {frutas}? -> {'uva' in frutas}")
    
    # Operador in con diccionarios (verifica claves)
    persona = {"nombre": "Ana", "edad": 25}
    print(f"\n📌 'in' con diccionarios (verifica claves):")
    print(f"¿'nombre' está en {list(persona.keys())}? -> {'nombre' in persona}")
    print(f"¿'Ana' está en las claves? -> {'Ana' in persona}")
    
    # Operador not in
    print(f"\n📌 'not in' (no está contenido):")
    numeros = [1, 2, 3, 4, 5]
    print(f"¿6 NO está en {numeros}? -> {6 not in numeros}")
    print(f"¿3 NO está en {numeros}? -> {3 not in numeros}")
    
    print("\n" + "=" * 50)
    print("OPERADORES DE CONCATENACIÓN (+)")
    print("=" * 50)
    
    # Concatenación de strings
    nombre = "Juan"
    apellido = "Pérez"
    nombre_completo = nombre + " " + apellido
    print(f"\n📌 Concatenación de strings:")
    print(f"'{nombre}' + ' ' + '{apellido}' = '{nombre_completo}'")
    
    # Concatenación de listas
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista_completa = lista1 + lista2
    print(f"\n📌 Concatenación de listas:")
    print(f"{lista1} + {lista2} = {lista_completa}")
    
    # Concatenación de tuplas
    tupla1 = (1, 2)
    tupla2 = (3, 4)
    tupla_completa = tupla1 + tupla2
    print(f"\n📌 Concatenación de tuplas:")
    print(f"{tupla1} + {tupla2} = {tupla_completa}")
    
    print("\n" + "=" * 50)
    print("ERRORES COMUNES Y SOLUCIONES")
    print("=" * 50)
    
    # Error común: concatenar diferentes tipos
    texto = "Edad: "
    numero = 25
    print(f"\n❌ Error al concatenar str + int:")
    print(f"texto = '{texto}', numero = {numero}")
    print("print(texto + numero) -> TypeError")
    
    # Solución: convertir el tipo primero
    print(f"\n✅ Solución - convertir a str:")
    print(f"texto + str(numero) = '{texto + str(numero)}'")
    
    # Diccionarios no se pueden concatenar con +
    dict1 = {"a": 1}
    dict2 = {"b": 2}
    print(f"\n❌ Diccionarios no permiten concatenación con +:")
    print(f"dict1 = {dict1}, dict2 = {dict2}")
    print("dict1 + dict2 -> TypeError")
    
    # Solución para diccionarios (Python 3.9+)
    print(f"\n✅ Solución para diccionarios (| operator):")
    dict_completo = dict1 | dict2
    print(f"dict1 | dict2 = {dict_completo}")
    
    print("\n" + "=" * 50)
    print("EJEMPLOS PRÁCTICOS COMBINADOS")
    print("=" * 50)
    
    # Ejemplo práctico 1: Verificar y luego concatenar
    frutas = ["manzana", "banana"]
    print(f"\n📌 Ejemplo 1 - Agregar elemento si no existe:")
    print(f"frutas inicial: {frutas}")
    
    if "uva" not in frutas:
        frutas += ["uva"]  # Equivalente a: frutas = frutas + ["uva"]
        print(f"Después de agregar 'uva': {frutas}")
    
    # Ejemplo práctico 2: Concatenación condicional
    nombre = "Ana"
    print(f"\n📌 Ejemplo 2 - Saludo condicional:")
    saludo = "Hola " + nombre if nombre else "Hola anónimo"
    print(f"nombre = '{nombre}' -> saludo = '{saludo}'")
    
    # Ejemplo con string vacío
    nombre_vacio = ""
    saludo_vacio = "Hola " + nombre_vacio if nombre_vacio else "Hola anónimo"
    print(f"nombre = '{nombre_vacio}' -> saludo = '{saludo_vacio}'")

if __name__ == "__main__":
    main()