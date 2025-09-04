import os

# Obtener la ruta del directorio actual del script
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, "text.txt")

try:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo en: {ruta_archivo}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
