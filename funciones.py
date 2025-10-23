import numpy as np

def tablero():
    tablero = np.full((10,10), " ")
    return(tablero)

#Para poner los barcos en los tableros 
def colocar_barco(tablero, lista):
    for barco in lista:
        #Para acceder al barco
        print(barco)
        for posicion in barco:
            #Para que me saque cada posicon de los barcos
            print(posicion)
            #Reemplazar los " " por "\
            tablero[posicion] = "O"
    return tablero

#Barcos aleaotrios
def validar_posicion_aleatoria(tablero, inicio_fila, inicio_columna, eslora, direccion):
    #Verifica si un barco cabe y no se superpone en las coordenadas generadas.
    tamaño = tablero.shape[0]
    coordenadas = []
    for i in range(eslora):
        # 1. Calcular la coordenada de la parte del barco
        if direccion == 'H':  # Horizontal
            fila, columna = inicio_fila, inicio_columna + i
        else:  # Vertical
            fila, columna = inicio_fila + i, inicio_columna
        # 2. Comprobar límites
        if not (0 <= fila < tamaño and 0 <= columna < tamaño):
            return False, []
        # 3. Comprobar superposición
        if tablero[fila, columna] != "_":
            return False, [] # La casilla no está vacía
        coordenadas.append((fila, columna))
    return coordenadas

def disparar(tablero, fila, columna):
    print("EL TANdsfs",tablero[0,0])
    print("FILA", fila, "col",columna)
    if tablero[fila] [columna] == "O":
        tablero[fila] [columna] = "X"
        print(tablero)
        print("Tocado")
    elif tablero[fila] [columna] == " ":
        tablero[fila] [columna] = "A"
        print(tablero)
        print("Agua")
    elif tablero[fila] [columna] == "A":
        return disparar(tablero, fila, columna)
    else:
        print("Esa poscion no existe")
    print(tablero)

def borrar_barco(barcos,x, y):
    for barco in barcos:
        if len(barco) >1 :
            for pos in barco:
                if pos[0]== x and pos[1]==y:
                    barco.remove(pos)
                    print("Quedan los barcos",barcos)
        elif len(barco) == 1:
            barcos.remove(barco)
