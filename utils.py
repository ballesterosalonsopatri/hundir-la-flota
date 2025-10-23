# ==========================
# 🔹FUNCIONES
# ==========================

"""Importar numpy para realizar el juego de hundir la flota y random para funciones con valores
aleatorios"""
import numpy as np
import random

# ===============================
# 🔹 CREAR Y MOSTRAR TABLEROS
# ===============================

def crear_tablero():
    """Con esta función he creado el tablero utilizando numpy de dos dimensiones."""
    tablero = np.full((10,10), " ")
    return(tablero)


def mostrar_tablero(tablero):
    """Muestra el tablero completo (sin ocultar barcos)."""
    print("   " + " ".join(str(i) for i in range(10)))
    for i in range(10):
        fila = [tablero[i, j] for j in range(10)]
        print(f"{i:2} " + " ".join(fila))
    print()


# ==================================
# 🔹 COLOCAR BARCOS ALEATORIAMENTE
# ==================================

def colocar_barcos(tablero):
    """
    Coloca barcos de forma aleatoria en el tablero sin solaparse.
    Barcos: 1x4, 2x3, 2x2, 1x1 (total 6 barcos)
    """
    tamaños_barcos = [4, 3, 3, 2, 2, 2]
    barcos = []

    for tamaño in tamaños_barcos:
        colocado = False
        while not colocado:
            orientacion = random.choice(["H", "V"])
            if orientacion == "H":
                x = random.randint(0, 9)
                y = random.randint(0, 10 - tamaño)
                posiciones = [(x, y + i) for i in range(tamaño)]
            else:
                x = random.randint(0, 10 - tamaño)
                y = random.randint(0, 9)
                posiciones = [(x + i, y) for i in range(tamaño)]

            # Comprobamos que no haya solapamiento
            if all(tablero[pos] == " " for pos in posiciones):
                for pos in posiciones:
                    tablero[pos] = "O"
                barcos.append(posiciones)
                colocado = True

    return barcos

# ===================================
# 🔹 DISPARAR Y ACTUALIZAR TABLEROS
# ===================================

def disparar(coord, tablero, barcos):
    """Ejecuta un disparo y devuelve True (tocado), False (agua), None (repetido)."""
    x, y = coord

    if tablero[x, y] == "O":
        tablero[x, y] = "X"
        print("¡Tocado!")
        for barco in barcos:
            if (x, y) in barco:
                barco.remove((x, y))
                if len(barco) == 0:
                    barcos.remove(barco)
                    print("¡Barco hundido!")
                break
        return True

    elif tablero[x, y] in ("X", "A"):
        print("Ya disparaste aquí.")
        return None

    else:
        tablero[x, y] = "A"
        print("Agua.")
        return False


# ===============================
# 🔹 TURNOS
# ===============================

def turno_jugador(tablero_rival, barcos_rival):
    """Turno del jugador: sigue disparando mientras acierte."""
    print("\n=== Tu turno ===")
    continuar = True
    while continuar and len(barcos_rival) > 0:
        mostrar_tablero(tablero_rival)
        try:
            x = int(input("Fila (0-9): "))
            y = int(input("Columna (0-9): "))
            if 0 <= x <= 9 and 0 <= y <= 9:
                resultado = disparar((x, y), tablero_rival, barcos_rival)
                if resultado is False:
                    continuar = False  # Agua → cambia de turno
                elif resultado is None:
                    print("Intenta otra coordenada.")
            else:
                print("Introduce números válidos entre 0 y 9.")
        except ValueError:
            print("Introduce números válidos.")


def turno_rival(tablero_jugador, barcos_jugador, tiros_previos):
    """Turno del rival: dispara al azar mientras acierte."""
    print("\n=== Turno del rival ===")
    continuar = True
    while continuar and len(barcos_jugador) > 0:
        x, y = random.randint(0, 9), random.randint(0, 9)
        if (x, y) not in tiros_previos:
            print(f"El rival dispara a ({x},{y})")
            resultado = disparar((x, y), tablero_jugador, barcos_jugador)
            tiros_previos.add((x, y))
            if resultado is False:
                continuar = False


# ===============================
# 🔹 ASIGNAR TURNO INICIAL
# ===============================

def asignar_turno_inicial():
    """Devuelve 'jugador' o 'rival' de forma aleatoria e imprime mensaje."""
    turno = random.choice(["jugador", "rival"])
    if turno == "jugador":
        print("\n Le toca el turno al jugador.")
    else:
        print("\n Le toca el turno al rival.")
    return turno