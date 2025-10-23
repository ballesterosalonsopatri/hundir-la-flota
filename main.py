

from utils import crear_tablero
from utils import mostrar_tablero
from utils import colocar_barcos
from utils import disparar
from utils import turno_jugador
from utils import turno_rival
from utils import asignar_turno_inicial

def juego():
    print("=== ¡Bienvenido a Batalla Naval! ===")

    # Crear tableros
    tablero_jugador = crear_tablero()
    tablero_rival = crear_tablero()

    # Colocar barcos aleatoriamente
    barcos_jugador = colocar_barcos(tablero_jugador)
    barcos_rival = colocar_barcos(tablero_rival)
    tiros_rival = set()

    # Asignar turno inicial
    turno = asignar_turno_inicial()

    # Bucle principal
    while True:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)
        print("\nTablero del rival:")
        mostrar_tablero(tablero_rival)

        if turno == "jugador":
            turno_jugador(tablero_rival, barcos_rival)
            if len(barcos_rival) == 0:
                print("\n ¡Has ganado! Todos los barcos del rival hundidos.")
                break
            turno = "rival"
        else:
            turno_rival(tablero_jugador, barcos_jugador, tiros_rival)
            if len(barcos_jugador) == 0:
                print("\n ¡El rival ha ganado! Todos tus barcos hundidos.")
                break
            turno = "jugador"


if __name__ == "__main__":
    juego()

