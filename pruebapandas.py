import numpy as np
import pandas as pd

# Leer un archivo CSV
#df = pd.read_csv("poblacion.csv")
datos = {"Nombre": ["Ana", "Juan", "Pedro"], "Edad": [25, 30, 35]}
df = pd.DataFrame(datos)       # Primeras 5 filas
print(df)
# Agregar una nueva columna
df["Salario"] = [3000, 4000, 5000]
print(df)
# Modificar valores
df["Edad"] = df["Edad"] + 1
print(df)

# Eliminar una columna
df = df.drop(0, axis=0)
print(df)
            