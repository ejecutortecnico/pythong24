respuestas = {
    "hola":"hola como estas",
    "ayuda en programacion":"para ayuda en programaion acuda a w3school",
    "direccion de talento tech":"crr 29 no 50-55"
}

def responder(pregunta):
    if pregunta in respuestas:
        #pregunta = pregunta.lower()
        respuesta = respuestas[pregunta]
    else:
        respuesta = "lo siento no puedo ayudarte"
    return respuesta

print("hola soy un chatbot, ecribe salir para terminar")

while True:
    pregunta=input("en que puedo ayudarte: ")
    if pregunta == "salir":
        print("hasta luego")
        break
    respuesta = responder(pregunta)
    print(respuesta)