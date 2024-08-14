import random

def juego_adivinanzas():
    numero_secreto = random.randint(1, 100)
    adivinado = False

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")

    while not adivinado:
        intento = int(input("Adivina el número: "))

        if intento == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número!")
            adivinado = True
        else:
            distancia = abs(numero_secreto - intento)
            if distancia <= 5:
                print("Muy cerca")
            elif distancia <= 15:
                print("Cerca")
            else:
                print("Muy lejos")

juego_adivinanzas()