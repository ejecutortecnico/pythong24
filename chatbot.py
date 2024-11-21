import csv

respuestas = {}
def cargarRespuestas():
    with open("datos.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            respuestas[fila["preguntas"]]=fila["respuestas"]

def entrenar():
    with open("datos.csv", "a", newline="") as archivo:
            escritor = csv.writer(archivo)
            pregunta=input("ingresa la pregunta: ")
            respuesta= input("ingresa la respuesta: ")
            escritor.writerow([pregunta, respuesta])

def responder(pregunta):
    if pregunta in respuestas:
        #pregunta = pregunta.lower()
        respuesta = respuestas[pregunta]
    else:
        respuesta = "lo siento no puedo ayudarte"
    return respuesta

print("hola soy un chatbot, ecribe salir para terminar")
cargarRespuestas()
while True:
    pregunta=input("en que puedo ayudarte: ")
    if pregunta == "salir":
        print("hasta luego")
        break
    if pregunta == "entrenar":
        entrenar()
        cargarRespuestas()
    else:
        respuesta = responder(pregunta)
        print(respuesta)