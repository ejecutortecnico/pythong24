print("seleccione una opcion")
print("1 para sumar")
print("2 para restar")
print("3 para multiplicar")
print("4 para Dividir")
operacion = int(input())
if operacion == 1:
    numero1 = input("ingrese el numero 1")
    numero2 = input("ingrese el numero 2")
    resultado = float(numero1) + float(numero2)
    print(f"el resultado de la suma es: {resultado}")
elif operacion == 2:
    numero1 = input("ingrese el numero 1")
    numero2 = input("ingrese el numero 2")
    resultado = float(numero1) - float(numero2)
    print(f"el resultado de la resta es: {resultado}")
elif operacion == 3:
    numero1 = input("ingrese el numero 1")
    numero2 = input("ingrese el numero 2")
    resultado = float(numero1) * float(numero2)
    print(f"el resultado de la multiplicacion es: {resultado}")
elif operacion == 4:
    numero1 = input("ingrese el numero 1")
    numero2 = input("ingrese el numero 2")
    resultado = float(numero1) / float(numero2)
    print(f"el resultado de la division es: {resultado}")