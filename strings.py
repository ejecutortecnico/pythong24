variable = "texto"
print(variable.upper())

texto = "OTRO TEXTO"
print(texto.lower())

print('   texto   '.strip())
if '   texto  '.strip() == "texto":
    print("son iguales")
else:
    print("son diferentes")

print('Hola, mundo'.replace('mundo', 'Python') )
print(type('jorge, carlos, pedro'))
print(type(type('jorge, carlos, pedro'.split(','))))
datos = 'jorge, carlos, pedro'
for dato in datos:
    print(dato)

