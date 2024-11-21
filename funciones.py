def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()  # Imprime "¡Hola, mundo!"

def saludar(nombre, apellido):
    persona = {"nombre":nombre, "apellido":apellido}
    print(persona)

while True:
    nombre = input("ingrese el nombre\n")
    if nombre == "salir":
        break
    apellido = input("ingrese el apellido\n")
    # Llamar a la función con un argumento
    saludar(nombre, apellido)  # Imprime "¡Hola, Ana!"

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Imprime 8

suma = lambda x, y: x + y

resultado = suma(4, 7)
print(resultado)  # Imprime 11