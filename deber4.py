def mostrar_habi(habitacionActual):
    print(f"Estás en {habitacionActual}.")
    print("Puedes ir hacia:", ", ".join(laberinto[habitacionActual].keys()))

def mover_habi(habitacionActual, direccion):
    if direccion in laberinto[habitacionActual]:
        return laberinto[habitacionActual][direccion]
    else:
        print("No puedes ir en esa dirección.")
        return habitacionActual

laberinto = {
    'Entrada': {'norte': 'Pasillo Norte', 'sur': 'Pasillo Sur'},
    'Pasillo Norte': {'sur': 'Entrada', 'norte': 'Sala de Trofeos', 'este': 'Biblioteca'},
    'Pasillo Sur': {'norte': 'Entrada', 'sur': 'Cocina', 'oeste': 'Jardín'},
    'Sala de Trofeos': {'sur': 'Pasillo Norte', 'este': 'Habitación Secreta'},
    'Biblioteca': {'oeste': 'Pasillo Norte', 'norte': 'Estudio', 'este': 'Sala de Música'},
    'Cocina': {'norte': 'Pasillo Sur', 'este': 'Comedor'},
    'Jardín': {'este': 'Pasillo Sur'},
    'Habitación Secreta': {'oeste': 'Sala de Trofeos'},
    'Estudio': {'sur': 'Biblioteca', 'oeste': 'Laboratorio'},
    'Sala de Música': {'oeste': 'Biblioteca', 'sur': 'Sala de Pintura'},
    'Comedor': {'oeste': 'Cocina'},
    'Laboratorio': {'este': 'Estudio'},
    'Sala de Pintura': {'norte': 'Sala de Música'}
}

def laberinto():
    habitacionAc = 'Entrada'

    while True:
        mostrar_habi(habitacionAc)
        direccion = input("¿dónde quieres ir? ").lower()

        if direccion == 'salir':
            print("¡Gracias por jugar!")
            break

        habitacionAc = mover_habi (habitacionAc, direccion)
        
        laberinto()