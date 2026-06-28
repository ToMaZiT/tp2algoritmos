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
    global victorias_bj

    limpiar_pantalla()

    indice = pedirNombre()
    if indice == -1:
        input("\nPresione Enter para volver al menú principal")
        return
    nombre = nombres_jugadores[indice]

    jugar_otra = True

    while jugar_otra:

        # -- MAZO --
        palos  = ["♠", "♥", "♦", "♣"]
        valores = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

        mazo = [None] * 52
        i = 0
        p = 0
        while p < 4:
            v = 0
            while v < 13:
                mazo[i] = valores[v] + palos[p]
                i += 1
                v += 1
            p += 1

        random.shuffle(mazo)
        carta_actual = 0  # índice de la próxima carta a repartir

        # -- MANO JUGADOR Y BANCA --
        mano_jugador = [None] * 52
        mano_banca   = [None] * 52
        cant_jugador = 0
        cant_banca   = 0

        # repartir 2 cartas a cada uno
        mano_jugador[0] = mazo[carta_actual]; carta_actual += 1
        mano_banca[0]   = mazo[carta_actual]; carta_actual += 1
        mano_jugador[1] = mazo[carta_actual]; carta_actual += 1
        mano_banca[1]   = mazo[carta_actual]; carta_actual += 1
        cant_jugador = 2
        cant_banca   = 2

        limpiar_pantalla()

        # -- FUNCIÓN INTERNA: calcular puntaje --
        def calcularPuntaje(mano, cantidad):
            total = 0
            ases  = 0
            i = 0
            while i < cantidad:
                carta = mano[i][:-1]  # saca el palo (último caracter)
                if carta in ["J", "Q", "K"]:
                    total += 10
                elif carta == "A":
                    total += 11
                    ases  += 1
                else:
                    total += int(carta)
                i += 1
            while total > 21 and ases > 0:
                total -= 10
                ases  -= 1
            return total

        # -- FUNCIÓN INTERNA: mostrar mano --
        def mostrarMano(mano, cantidad, propietario):
            print(f"  {propietario}: ", end="")
            i = 0
            while i < cantidad:
                print(mano[i], end=" ")
                i += 1
            print(f"  → {calcularPuntaje(mano, cantidad)} puntos")

        # -- TURNO DEL JUGADOR --
        jugador_perdio = False
        jugador_planto = False

        while not jugador_planto and not jugador_perdio:
            limpiar_pantalla()
            print("=" * 45)
            mostrarMano(mano_banca,   cant_banca,   "Banca  ")
            mostrarMano(mano_jugador, cant_jugador, nombre)
            print("=" * 45)

            puntaje_jugador = calcularPuntaje(mano_jugador, cant_jugador)

            if puntaje_jugador == 21:
                print("¡Tenés 21! Turno de la banca.")
                jugador_planto = True
            elif puntaje_jugador > 21:
                print(f"¡Te pasaste de 21! Perdiste.")
                jugador_perdio = True
            else:
                accion = input("¿Querés PEDIR carta o PLANTARTE?: ").upper()
                while accion != "PEDIR" and accion != "PLANTARTE":
                    accion = input("Opción inválida. Escribí PEDIR o PLANTARTE: ").upper()

                if accion == "PEDIR":
                    mano_jugador[cant_jugador] = mazo[carta_actual]
                    carta_actual  += 1
                    cant_jugador  += 1
                else:
                    jugador_planto = True

        # -- TURNO DE LA BANCA --
        if not jugador_perdio:
            while calcularPuntaje(mano_banca, cant_banca) < 17:
                mano_banca[cant_banca] = mazo[carta_actual]
                carta_actual += 1
                cant_banca   += 1

            limpiar_pantalla()
            puntaje_jugador = calcularPuntaje(mano_jugador, cant_jugador)
            puntaje_banca   = calcularPuntaje(mano_banca,   cant_banca)

            print("=" * 45)
            print("RESULTADO FINAL")
            print("=" * 45)
            mostrarMano(mano_banca,   cant_banca,   "Banca  ")
            mostrarMano(mano_jugador, cant_jugador, nombre)
            print("=" * 45)

            if puntaje_banca > 21:
                print(f"¡La banca se pasó! Ganaste, {nombre}!")
                victorias_bj[indice] += 1
            elif puntaje_jugador > puntaje_banca:
                print(f"¡Ganaste, {nombre}!")
                victorias_bj[indice] += 1
            elif puntaje_jugador < puntaje_banca:
                print(f"Ganó la banca. ¡Suerte la próxima, {nombre}!")
            else:
                print("¡Empate!")

        otra = input("\n¿Querés jugar otra partida? (SI/NO): ").upper()
        while otra != "SI" and otra != "NO":
            otra = input("Opción inválida. Escribí SI o NO: ").upper()
        jugar_otra = otra == "SI"

    input("\nPresione Enter para volver al menú principal")
"""
nombre, opcion_pi: string
creditos, apuesta_cant, dado1, dado2, suma: int
es_par: boolean
"""
def parImpar():
    global aciertos_dados_arr, creditos_arr

    limpiar_pantalla()

    indice = pedirNombre()
    if indice == -1:
        input("\nPresione Enter para volver al menú principal")
        return
    nombre = nombres_jugadores[indice]

    if creditos_arr[indice] <= 0:
        print(f"Lo sentimos {nombre}, no tenés créditos para jugar.")
        input("\nPresione Enter para volver al menú principal")
        return

    print(f"Bienvenido {nombre}! Tienes {creditos_arr[indice]} créditos.")

    # pedir apuesta
    apuesta_cant = input(f"¿Cuántos créditos deseas apostar? (Máximo {creditos_arr[indice]}): ")
    while not apuesta_cant.isdigit():
        apuesta_cant = input("Entrada inválida, ingrese un número: ")
    apuesta_cant = int(apuesta_cant)

    while apuesta_cant <= 0 or apuesta_cant > creditos_arr[indice]:
        apuesta_cant = input(f"Monto inválido. Ingresa entre 1 y {creditos_arr[indice]}: ")
        while not apuesta_cant.isdigit():
            apuesta_cant = input("Entrada inválida, ingrese un número: ")
        apuesta_cant = int(apuesta_cant)

    # pedir par o impar ANTES de tirar los dados
    opcion_pi = input("¿Apuestas a PAR o IMPAR?: ").upper()
    while opcion_pi != "PAR" and opcion_pi != "IMPAR":
        opcion_pi = input("Opción inválida. Escribe PAR o IMPAR: ").upper()

    # tirar dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2

    print(f"\nLos dados cayeron: {dado1} y {dado2}")
    print(f"La suma es: {suma}")

    # resultado
    if (suma % 2 == 0 and opcion_pi == "PAR") or (suma % 2 != 0 and opcion_pi == "IMPAR"):
        creditos_arr[indice] += apuesta_cant
        aciertos_dados_arr[indice] += 1
        print(f"¡GANASTE! Ahora tienes {creditos_arr[indice]} créditos.")
    else:
        creditos_arr[indice] -= apuesta_cant
        print(f"PERDISTE. Te quedan {creditos_arr[indice]} créditos.")
        if creditos_arr[indice] <= 0:
            print(f"Te quedaste sin créditos. Ya no podrás jugar a Par o Impar.")

    input("\nPresione Enter para volver al menú principal...")


#no utiliza variables locales, accede a las variables globales para lectura
def reporte():
    global nombres_jugadores, rachas_mm, jugadas_secreto_arr
    global victorias_secreto_arr, derrotas_secreto_arr
    global victorias_bj, creditos_arr, aciertos_dados_arr
    global cantidad_jugadores

    opc_reporte = ""
    while opc_reporte != "E":
        limpiar_pantalla()
        print("=" * 45)
        print("           REPORTE DEL SISTEMA")
        print("=" * 45)
        print("A- Jugadores ordenados por victorias")
        print("B- Juegos jugados por un jugador")
        print("C- Jugadores de Par/Impar por crédito")
        print("D- Racha de un jugador en Menor/Mayor")
        print("E- Volver al menú principal")
        print("=" * 45)

        opc_reporte = input("Ingrese su opción: ").upper()
        while opc_reporte != "A" and opc_reporte != "B" and opc_reporte != "C" and opc_reporte != "D" and opc_reporte != "E":
            opc_reporte = input("Opción inválida, reintente: ").upper()

        if opc_reporte == "A":
            limpiar_pantalla()
            print("=" * 45)
            print("  JUGADORES ORDENADOS POR VICTORIAS")
            print("=" * 45)

            if cantidad_jugadores == 0:
                print("No hay jugadores registrados.")
            else:
                # arrays temporales para ordenar
                nombres_ord   = [None] * cantidad_jugadores
                victorias_ord = [0]    * cantidad_jugadores

                i = 0
                while i < cantidad_jugadores:
                    nombres_ord[i]   = nombres_jugadores[i]
                    victorias_ord[i] = victorias_secreto_arr[i] + victorias_bj[i] + aciertos_dados_arr[i]
                    i += 1

                # burbuja mayor a menor
                i = 0
                while i < cantidad_jugadores - 1:
                    j = 0
                    while j < cantidad_jugadores - i - 1:
                        if victorias_ord[j] < victorias_ord[j + 1]:
                            # swap victorias
                            aux               = victorias_ord[j]
                            victorias_ord[j]  = victorias_ord[j + 1]
                            victorias_ord[j + 1] = aux
                            # swap nombres
                            aux             = nombres_ord[j]
                            nombres_ord[j]  = nombres_ord[j + 1]
                            nombres_ord[j + 1] = aux
                        j += 1
                    i += 1

                i = 0
                while i < cantidad_jugadores:
                    print(f"  {i + 1}. {nombres_ord[i]} → {victorias_ord[i]} victorias")
                    i += 1

            input("\nPresione Enter para continuar...")

        elif opc_reporte == "B":
            limpiar_pantalla()
            print("=" * 45)
            print("      JUEGOS JUGADOS POR JUGADOR")
            print("=" * 45)

            nombre_buscar = input("Ingrese el nombre del jugador: ")
            while nombre_buscar == "":
                nombre_buscar = input("El nombre no puede estar vacío: ")

            indice = buscarJugador(nombre_buscar)

            if indice == -1:
                print(f"No se encontró el jugador '{nombre_buscar}'.")
            else:
                print(f"\n  Jugador: {nombres_jugadores[indice]}")
                print("-" * 45)

                if rachas_mm[indice] > 0:
                    print(f"  Menor/Mayor     → Racha máxima: {rachas_mm[indice]}")

                if jugadas_secreto_arr[indice] > 0:
                    print(f"  Número Secreto  → Victorias: {victorias_secreto_arr[indice]} / Jugadas: {jugadas_secreto_arr[indice]}")

                if victorias_bj[indice] > 0:
                    print(f"  Blackjack       → Victorias: {victorias_bj[indice]}")

                if creditos_arr[indice] != 1000 or aciertos_dados_arr[indice] > 0:
                    print(f"  Par o Impar     → Créditos: {creditos_arr[indice]} | Aciertos: {aciertos_dados_arr[indice]}")

                if rachas_mm[indice] == 0 and jugadas_secreto_arr[indice] == 0 and victorias_bj[indice] == 0 and aciertos_dados_arr[indice] == 0 and creditos_arr[indice] == 1000:
                    print("  Este jugador aún no ha jugado ningún juego.")

            input("\nPresione Enter para continuar...")

        elif opc_reporte == "C":
            limpiar_pantalla()
            print("=" * 45)
            print("   JUGADORES PAR/IMPAR POR CRÉDITO")
            print("=" * 45)

            if cantidad_jugadores == 0:
                print("No hay jugadores registrados.")
            else:
                # arrays temporales para ordenar
                nombres_ord  = [None] * cantidad_jugadores
                creditos_ord = [0]    * cantidad_jugadores

                i = 0
                while i < cantidad_jugadores:
                    nombres_ord[i]  = nombres_jugadores[i]
                    creditos_ord[i] = creditos_arr[i]
                    i += 1

                # burbuja menor a mayor
                i = 0
                while i < cantidad_jugadores - 1:
                    j = 0
                    while j < cantidad_jugadores - i - 1:
                        if creditos_ord[j] > creditos_ord[j + 1]:
                            # swap creditos
                            aux              = creditos_ord[j]
                            creditos_ord[j]  = creditos_ord[j + 1]
                            creditos_ord[j + 1] = aux
                            # swap nombres
                            aux            = nombres_ord[j]
                            nombres_ord[j] = nombres_ord[j + 1]
                            nombres_ord[j + 1] = aux
                        j += 1
                    i += 1

                i = 0
                while i < cantidad_jugadores:
                    print(f"  {i + 1}. {nombres_ord[i]} → ${creditos_ord[i]} créditos")
                    i += 1

            input("\nPresione Enter para continuar...")

        elif opc_reporte == "D":
            limpiar_pantalla()
            print("=" * 45)
            print("      RACHA EN MENOR/MAYOR")
            print("=" * 45)

            nombre_buscar = input("Ingrese el nombre del jugador: ")
            while nombre_buscar == "":
                nombre_buscar = input("El nombre no puede estar vacío: ")

            indice = buscarJugador(nombre_buscar)

            if indice == -1:
                print(f"No se encontró el jugador '{nombre_buscar}'.")
            else:
                print(f"\n  {nombres_jugadores[indice]} → Racha máxima: {rachas_mm[indice]}")

            input("\nPresione Enter para continuar...")









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
    print("test. no subir al cvg")

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

