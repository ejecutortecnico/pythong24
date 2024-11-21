# diccionario
alumno = {
    "nombre": "Juan",
    "edad": 20,
    "curso": "Matemáticas"
}
# Imprimir el diccionario
print(alumno)
print(alumno["nombre"])  # Imprime: valores
print(alumno["edad"])
print(alumno["curso"])
# Agregar elemento
alumno["nota"] = 8.5
print(alumno)
#eliminar un elemento
del alumno["curso"]
print(alumno)
# Solución
for clave, valor in alumno.items():
    print(clave, ":", valor)

# diccionario anidado
clase = {
    "alumno1": {"nombre": "Ana", "edad": 21, "nota": 9.0},
    "alumno2": {"nombre": "Carlos", "edad": 22, "nota": 7.5}
}

# Imprimir el diccionario completo
for clave, valor in clase.items():
    print(clave, ":", valor)

clase["alumno1"]["nota"] = 9.5
print(clase["alumno1"])
            