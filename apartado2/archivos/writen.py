import os

# Obtener la ruta del directorio actual del script
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, "text.txt")

# con esta linea remplazo el contenido del archivo "w"

""" with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Este es un nuevo contenido para el archivo.")
    archivo.close()
 """
# |  Append content to the file
with open(ruta_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("Este es un nuevo contenido para el archivo.")
    archivo.close()
