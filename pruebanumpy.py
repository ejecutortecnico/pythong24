import numpy as np
# Array unidimensional
# lista1 = [1, 2, 3]
# print(lista1)
# arr_1d = np.array(lista1)
# print(arr_1d)
# lista2 = [[1, 2, 3], [4, 5, 6]]
# print(lista2)
# # Array bidimensional
# arr_2d = np.array(lista2)
# print(arr_2d)
lista1=[1, 2, 3,5,6,7,8,9]
lista2=[4, 5, 6,8,9,5,6,5]
resultado=[]
for i in range(len(lista1)):
    resultado.append(lista1[i]+lista2[i])
print(resultado)
arr1 = np.array(lista1)
arr2 = np.array(lista2)

# Suma de arrays
resultado = np.add(arr1, arr2)
print(resultado)
media = np.mean(arr2)
mediana = np.median(arr2)
ds = np.std(arr2)
print(media)
print(mediana)
print(ds)