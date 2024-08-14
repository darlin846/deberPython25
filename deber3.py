import random

def seleccionar_pa():

    palabras = {
        'python': 'Lenguaje de programación',
        'variable': 'Elemento que guarda un valor',
        'funcion': 'Bloque de código que realiza una tarea',
        'algoritmo': 'resolver un problema',
        'bucle': 'Estructura que repite código'
    }
    
    
    palabra_secreta, pista = random.choice(list(palabras.items()))
    
    return palabra_secreta, pista

def mostrar_palabra(palabra_secreta, letras_adivinadas):
    
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada

def ahorcado():
    palabra_se, pista = seleccionar_pa()
    letras_adivinadas = []
    intentos_restantes = 6  # Número de intentos permitidos

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"Pista: {pista}")
    print(f"La primera letra de la palabra secreta es: {palabra_se[0]}")
    letras_adivinadas.append(palabra_se[0])

    while intentos_restantes > 0:
        
        palabra_mostrada = mostrar_palabra(palabra_se, letras_adivinadas)
        print(f"Palabra: {palabra_mostrada}")
        print(f"Intentos restantes: {intentos_restantes}")

        
        letra = input("Adivina una letra: ").lower()

        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        
        letras_adivinadas.append(letra)

        
        if letra in palabra_se:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            intentos_restantes -= 1

        
        if "_" not in mostrar_palabra(palabra_se, letras_adivinadas):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_se}")
            break

    if intentos_restantes == 0:
        print(f"Has perdido. La palabra secreta era: {palabra_se}")

ahorcado()