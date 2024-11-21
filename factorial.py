factorial = int(input("ingrese el valor del factorial a calcular"))
resultado = 1
lista = [9,8,7,5,6]
for i in range(factorial):
    resultado *= i
    print(lista[i])

print(resultado)