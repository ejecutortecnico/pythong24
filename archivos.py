import csv

# Leer un CSV con encabezados
with open("datos.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)  # Imprime cada fila como un diccionario