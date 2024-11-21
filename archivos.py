import csv

# Crear un archivo CSV y escribir en él
with open("datos.csv", "a", newline="") as archivo:
    escritor = csv.writer(archivo)
    pregunta=input("ingresa la pregunta")
    respuesta= input("ingresa la respuesta")
    escritor.writerow([pregunta, respuesta])  # Escribir encabezados      # Escribir datos