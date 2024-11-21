import random

opciones = ["piedra","papel","tijera"]
opcion_usuario = input("ingese su opcion\n")

opcion = random.choice(opciones)
print(opcion)

if opcion_usuario == "tijera" and opcion=="papel":
    print("has ganado")
elif opcion_usuario == "papel" and opcion=="piedra":
    print("has ganado")
elif opcion_usuario == "piedra" and opcion=="tijera":
    print("has ganado")
else:
    print("has perdido")