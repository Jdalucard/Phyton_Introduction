import pandas as pd
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, "datos.csv")

file = pd.read_csv(ruta_archivo, encoding="utf-8", names=["name", "age", "city"])
print(file)

# slicing
chain = "2455415151515"

# Muestra la columna "name"
# Slicing de columnas con loc (de "name" hasta "age")
print(file.loc[:, "name":"age"])


order = file.sort_values(by=["age", "name"], ascending=False)
df_concant = pd.concat([file, order], axis=0)
total_file_and_columns = df_concant.shape[0]
df_info = df_concant.describe()

print(order)
print(df_concant)
print(chain[1:5])
print(df_info)
print(total_file_and_columns)
