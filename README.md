
![imagen](hundir-la-flota-juego-de-mesa.jpg)

# 🛳️ Batalla Naval (Hundir la Flota)
## 🧠 Descripción

Batalla Naval es una versión en consola del clásico juego de estrategia.
El jugador y el ordenador colocan barcos en un tablero y se turnan para disparar, intentando hundir todos los barcos del oponente antes de que el otro lo haga.

## 📁 Estructura del proyecto
hundir-la-flota/
│
├── mainpruebas.py   # Archivo principal que ejecuta el juego
├── utils.py         # Funciones auxiliares (tableros, disparos, turnos, etc.)
└── README.md        # Documentación del proyecto

## ⚙️ Requisitos

Python 3.10 o superior

Librería NumPy

Instala las dependencias con:

pip install numpy

## ▶️ Cómo ejecutar el juego

Abre una terminal en la carpeta del proyecto.

Ejecuta el siguiente comando:

python mainpruebas.py


Comienza a jugar e intenta hundir la flota enemiga.

## 🎮 Cómo jugar

Se generan dos tableros de 10x10: uno para el jugador y otro para el rival.

Los barcos se colocan automáticamente y de forma aleatoria.

En tu turno, introduce las coordenadas del disparo (fila y columna del 0 al 9).

Si aciertas podrás disparar de nuevo.

Si fallas el turno pasa al rival.

El primero en hundir todos los barcos del oponente gana.

## 🔢 Símbolos del tablero
| Símbolo | Significado       |
| ------- | ----------------- |
| `O`     | Parte de un barco |
| `X`     | Barco tocado      |
| `A`     | Agua (fallo)      |
| ` `     | Casilla vacía     |

## 🧩 Funciones principales
| Función                            | Descripción                                 |
| ---------------------------------- | ------------------------------------------- |
| `crear_tablero()`                  | Crea un tablero vacío de 10x10              |
| `mostrar_tablero(tablero)`         | Muestra el tablero por consola              |
| `colocar_barcos(tablero)`          | Coloca barcos aleatoriamente sin solaparlos |
| `disparar(coord, tablero, barcos)` | Ejecuta un disparo y actualiza el tablero   |
| `turno_jugador()`                  | Gestiona el turno del jugador               |
| `turno_rival()`                    | Gestiona el turno del ordenador             |
| `asignar_turno_inicial()`          | Decide quién comienza la partida            |

## 💡 Posibles mejoras
- 🔒 Ocultar los barcos del rival al mostrar su tablero
- 🧠 Mejorar la inteligencia del rival
- 🕹️ Añadir colocación manual de barcos
- 🎨 Crear una interfaz gráfica con **tkinter** o **pygame**
- 💾 Guardar y cargar partidas


🎯 “Apunta, dispara... y hunde la flota enemiga antes de que te hundan a ti.”
Licencia **MIT**


