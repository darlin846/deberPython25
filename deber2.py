import random

def generar_problema():
    # Seleccionar dos números aleatorios entre 1 y 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    operacion = random.choice(['+', '-', '*', '/'])
    
    if operacion == '+':
        respuestacorrecto = num1 + num2
        problema = f"{num1} + {num2}"
    elif operacion == '-':
        respuestacorrecto = num1 - num2
        problema = f"{num1} - {num2}"
    elif operacion == '*':
        respuestacorrecto = num1 * num2
        problema = f"{num1} * {num2}"
    elif operacion == '/':
        
        while num2 == 0 or num1 % num2 != 0:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        respuestacorrecto = num1 // num2
        problema = f"{num1} / {num2}"
    
    return problema, respuestacorrecto

def juegomatematico():
    problema, resultadocorrecto = generar_problema()
    intentos = 3
    
    print("¡Bienvenido al juego matemático!")
    print(f"Resuelve el siguiente problema: {problema}")
    
    while intentos > 0:
        intento = int(input("Tu respuesta: "))
        intentos -= 1
        
        if intento == resultadocorrecto:
            print("¡Correcto! Has resuelto el problema.")
            break
        else:
            if intentos > 0:
                print(f"Incorrecto. Te quedan {intentos} intentos.")
            else:
                print(f"Lo siento, has perdido. La respuesta correcta era {resultadocorrecto}.")

juegomatematico()