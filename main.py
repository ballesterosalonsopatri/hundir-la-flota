from funciones import tablero
from funciones import colocar_barco
from funciones import validar_posicion_aleatoria
from funciones import disparar
from funciones import borrar_barco



tablero_barcos_jugador = tablero()
tablero_disparos_jugador = tablero()
tablero_rival = tablero()
tablero_disparos_rival = tablero()


barco_jugador = [[(0,0), (0,1), (0,2)], [(7, 4), (6, 4)]]
for barco in barco_jugador:
    print(barco)
    for posicion in barco:
        print(posicion)
        tablero_barcos_jugador [posicion] = "O"

print(tablero_barcos_jugador)




while(len(barco_jugador) > 0):
    coord = input("Introduce coord separados por un espacio")
    coord = coord.split()
    x = int(coord[0])
    y = int((coord[1]))

    disparar(tablero_barcos_jugador,x,y)
    borrar_barco(barco_jugador, x, y)

print("El huego ha finalizado")


