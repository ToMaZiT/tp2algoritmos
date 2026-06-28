"""
Integrantes del grupo:
    - Tomás Flores
    - Narella Rochetti
    - Luka Cracco
    - Lautaro Simi

Declaración de variables globales y sus tipos:
    racha_maxima_global, jugadas_secreto, victorias_secreto, derrotas_secreto, aciertos_dados: int
    nombre_ganador_menor_mayor: string
    
"""


import os
import random

# REGISTRO DE JUGADORES ──────────────────────────────
MAX_JUGADORES = 10

nombres_jugadores        = [None] * MAX_JUGADORES

# Menor/Mayor
rachas_mm                = [0] * MAX_JUGADORES

# Número Secreto
jugadas_secreto_arr      = [0] * MAX_JUGADORES
victorias_secreto_arr    = [0] * MAX_JUGADORES
derrotas_secreto_arr     = [0] * MAX_JUGADORES

# Blackjack
victorias_bj             = [0] * MAX_JUGADORES

# Par o Impar
creditos_arr             = [0] * MAX_JUGADORES
aciertos_dados_arr       = [0] * MAX_JUGADORES

cantidad_jugadores       = 0
# ──────────────────────────────────────────────────────

# devuelve el índice del jugador si existe, -1 si no existe
def buscarJugador(nombre):
    i = 0
    indice = -1
    while i < cantidad_jugadores and indice == -1:
        if nombres_jugadores[i].upper() == nombre.upper():
            indice = i
        i += 1
    return indice


# registra un jugador nuevo. Devuelve su índice, o -1 si no hay cupo
def registrarJugador(nombre):
    global cantidad_jugadores
    indice = -1
    if cantidad_jugadores < MAX_JUGADORES:
        nombres_jugadores[cantidad_jugadores] = nombre
        creditos_arr[cantidad_jugadores]      = 1000
        indice                                = cantidad_jugadores
        cantidad_jugadores                   += 1
    return indice

# nombre: string
def pedirNombre():
    global cantidad_jugadores
    nombre = input("Por favor, ingrese su nombre antes de jugar: ")
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Reintenta: ")

    indice = buscarJugador(nombre)

    if indice != -1:
        print(f"Bienvenido de vuelta, {nombre}!")
    elif cantidad_jugadores < MAX_JUGADORES:
        indice = registrarJugador(nombre)
        print(f"Nuevo jugador registrado: {nombre}")
    else:
        print("No hay cupos disponibles para nuevos jugadores.")
        indice = -1

    return indice
    

# sin variables locales
def limpiar_pantalla():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpiar_pantalla()



# ADVERTENCIA
print("#########################################")
print("#  ADVERTENCIA: PROHIBIDO MENORES DE 18 #")
print("#    EL JUEGO ES PERJUDICIAL PARA LA    #")
print("#                 SALUD                 #")
print("#########################################")
#el integrante que hizo este cartel se gastó 30 lucas ayer en cajitas del counter

input("\nPresione Enter para continuar...")

limpiar_pantalla()










# FUNCIONES QUE CONTIENEN LOS JUEGOS
# (CADA JUEGO INCLUYE AL PRINCIPIO LA FUNCIÓN "limpiarpantalla()" PARA LIMPIAR LA TERMINAL)

"""
nombre, respuesta: string
sigue_jugando: boolean
primerNumero, proximoNumero, racha: int
"""
def menorMayor():
    global rachas_mm
    limpiar_pantalla()

    indice = pedirNombre()
    if indice == -1:
        input("\nPresione Enter para volver al menú principal")
        return
    nombre = nombres_jugadores[indice]

    sigue_jugando = True
    primerNumero = random.randint(1, 1000)
    racha = 0

    while sigue_jugando:
        print(f"El número aleatorio es: {primerNumero}")
        proximoNumero = random.randint(1, 1000)

        respuesta = input('¿El número es mayor o menor?: ').upper()
        match respuesta:
            case "MAYOR":
                if proximoNumero > primerNumero:
                    limpiar_pantalla()
                    print("¡CORRECTO! El número es mayor")
                    racha += 1
                    primerNumero = proximoNumero
                else:
                    print(f"Incorrecto, el número era {proximoNumero}.")
                    sigue_jugando = False
            case "MENOR":
                if proximoNumero < primerNumero:
                    limpiar_pantalla()
                    print("¡CORRECTO! El número es menor")
                    racha += 1
                    primerNumero = proximoNumero
                else:
                    print(f"Incorrecto, el número era {proximoNumero}.")
                    sigue_jugando = False
            case _:
                print("Opción inválida. Escriba MAYOR o MENOR.")

    print("-" * 45)
    print(f"JUEGO TERMINADO, {nombre}.")
    print(f"Tu racha de aciertos fue de: {racha}")
    
    
    if racha > rachas_mm[indice]:
        rachas_mm[indice] = racha
        
    input("\nPresione Enter para volver al menú principal")

"""
nombre: string
objetivo, intentos, apuesta: int
gano: boolean
"""
def numeroSecreto():
    global jugadas_secreto_arr, victorias_secreto_arr, derrotas_secreto_arr

    limpiar_pantalla()

    indice = pedirNombre()
    if indice == -1:
        input("\nPresione Enter para volver al menú principal")
        return
    nombre = nombres_jugadores[indice]

    objetivo = random.randint(1, 100)
    intentos = 6
    acerto = False

    jugadas_secreto_arr[indice] += 1

    while intentos > 0:

        print(f"Te quedan {intentos} intentos.")
        apuesta = input("Ingresa un número del 1 al 100: ")
        while not apuesta.isdigit():
            apuesta = input("Entrada inválida, ingrese un número: ")
        apuesta = int(apuesta)

        if apuesta == objetivo:
            limpiar_pantalla()
            intentos_usados = 6 - intentos + 1
            print(f"¡CORRECTO! Lo adivinaste en {intentos_usados} intentos.")
            victorias_secreto_arr[indice] += 1
            acerto = True
            intentos = 0
        elif apuesta > objetivo:
            intentos -= 1
            limpiar_pantalla()
            print("Fallaste, el número ingresado es MAYOR al objetivo.")
        elif apuesta < objetivo:
            intentos -= 1
            limpiar_pantalla()
            print("Fallaste, el número ingresado es MENOR al objetivo.")

    if not acerto:
        derrotas_secreto_arr[indice] += 1
        print(f"Sin intentos restantes. El número era {objetivo}.")

    print("JUEGO TERMINADO,", nombre + ".")
    input("\nPresione Enter para volver al menú principal")
#no utiliza variables locales
def blackjack():
    limpiar_pantalla()
    print("\n          JUEGO EN CONSTRUCCIÓN. VOLVER LUEGO.")
    input("\nPresione Enter para volver al menú principal")

"""
nombre, opcion_pi: string
creditos, apuesta_cant, dado1, dado2, suma: int
es_par: boolean
"""
def parImpar():
    global aciertos_dados
    global creditos

    limpiar_pantalla()
    nombre = pedirNombre()

    
    print(f"Bienvenido {nombre}! Tienes {creditos} créditos.")
    
    # pedir cantidad
    apuesta_cant = int(input(f"¿Cuántos créditos deseas apostar? (Máximo {creditos}): "))
    while apuesta_cant <= 0 or apuesta_cant > creditos:
        apuesta_cant = int(input(f"Monto inválido. Ingresa entre 1 y {creditos}: "))
    
    # pedir par o impar
    opcion_pi = input("¿Apuestas a PAR o IMPAR?: ").upper()
    while opcion_pi != "PAR" and opcion_pi != "IMPAR":
        opcion_pi = input("Opción inválida. Escribe PAR o IMPAR: ").upper()
    
    # ludopatía
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    
    print(f"\nLos dados cayeron: {dado1} y {dado2}")
    print(f"La suma es: {suma}")
    
    # 4. resultado
    if (suma % 2 == 0 and opcion_pi == "PAR") or (suma % 2 != 0 and opcion_pi == "IMPAR"):
        creditos += apuesta_cant
        aciertos_dados += 1
        print(f"¡GANASTE! Ahora tienes {creditos} créditos.") 
    else:
        creditos -= apuesta_cant
        print(f"PERDISTE. Te quedan {creditos} créditos.") 
        
    input("\nPresione Enter para volver al menú principal...") #


#no utiliza variables locales, accede a las variables globales para lectura
def reporte():
    limpiar_pantalla()
    print("█▀▀ █▀ ▀█▀ ▄▀█ █▀▄ █ █▀ ▀█▀ █ █▀▀ ▄▀█ █▀   █▀▄ █▀▀ █░░   █▀ █ █▀ ▀█▀ █▀▀ █▀▄▀█ ▄▀█")
    print("██▄ ▄█ ░█░ █▀█ █▄▀ █ ▄█ ░█░ █ █▄▄ █▀█ ▄█   █▄▀ ██▄ █▄▄   ▄█ █ ▄█ ░█░ ██▄ █░▀░█ █▀█")

    # menorMayor()
    print(f"\n\nMejor racha registrada: {racha_maxima_global}")
    print(f"Lograda por el jugador: {nombre_ganador_menor_mayor}")

    # numeroSecreto()
    print("\n--- JUEGO: NÚMERO SECRETO ---")
    print(f"Partidas totales: {jugadas_secreto}")
    print(f"Victorias: {victorias_secreto} | Derrotas: {derrotas_secreto}")

    # parImpar()
    print("\n--- JUEGO: PAR O IMPAR ---")
    print(f"Cantidad total de aciertos: {aciertos_dados}")

    # --------
    print("\n" + "="*45)
    input("Presione Enter para volver al menú principal...")












# FUNCIÓN DEL MENU --
#no utiliza variables locales
def MENU():
    limpiar_pantalla()
    print("\n" + "="*78)

    print("\n" + "  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$             /$$$$$$ ")
    print(" /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$ /$$__  $$           /$$__  $$")
    print("| $$  \__/| $$  \ $$| $$  \__/  | $$  | $$$$| $$| $$  \ $$          |__/  \ $$")
    print("| $$      | $$$$$$$$|  $$$$$$   | $$  | $$ $$ $$| $$  | $$            /$$$$$$/")
    print("| $$      | $$__  $$ \____  $$  | $$  | $$  $$$$| $$  | $$           /$$____/ ")
    print("| $$    $$| $$  | $$ /$$  \ $$  | $$  | $$\  $$$| $$  | $$          | $$      ")
    print("|  $$$$$$/| $$  | $$|  $$$$$$/ /$$$$$$| $$ \  $$|  $$$$$$/       /$$| $$$$$$$$")
    print(" \______/ |__/  |__/ \______/ |______/|__/  \__/ \______/       |__/|________/")

    print("\n\n" + "="*78)
    print("\n" + "A-                         Juego del menor-mayor")
    print("B-                      Adivinar el número secreto")
    print("C-                               Blackjack")
    print("D-                              Par o impar")
    print("\nE-                                Reporte")
    print("S-                          Salir del programa")
    print("\n" + "="*78)


# LÓGICA DEL MENÚ --


# opc: string
opc = ""
while opc != "S":
    MENU()
    opc = input("Ingrese su opción: ").upper()

    match opc:
        case "A":
            menorMayor()
        case "B":
            numeroSecreto()
        case "C":
            blackjack()
        case "D":
            parImpar()
        case "E":
            reporte()
        case "S":
            print("Saliendo del sistema...")
        case _:
            print("Opción inválida, reintente.")

limpiar_pantalla()

