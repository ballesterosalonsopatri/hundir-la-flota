
![imagen](hundir-la-flota-juego-de-mesa.jpg)

# 🚢 Batalla Naval en Python

Pequeño proyecto en **Python** que recrea el clásico juego de **Batalla Naval**.
El jugador dispara a coordenadas intentando hundir todos los barcos enemigos.

---

## ⚙️ Funcionalidades

* Genera un **tablero 10x10** con NumPy
* Permite **colocar barcos manualmente**
* Función de **disparo** (tocado, agua, repetido)
* Elimina partes de barcos hundidos
* Finaliza cuando no quedan barcos

---

## 🧠 Estructura principal

* `tablero()` → crea el tablero
* `colocar_barco()` → coloca los barcos
* `disparar()` → realiza disparos
* `borrar_barco()` → actualiza la lista de barcos
* `validar_posicion_aleatoria()` → (en progreso) para colocar barcos automáticamente

---

## 🚀 Cómo ejecutar

```bash
pip install numpy
python batalla_naval.py
```

---

## 🧩 Próximos pasos

* Añadir IA o modo 2 jugadores
* Mejorar interfaz y validaciones

---
**
Licencia **MIT**


