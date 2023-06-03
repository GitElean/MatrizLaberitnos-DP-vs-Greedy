import numpy as np
import matplotlib.pyplot as plt
import time

from mLDP import RecorridoLaberintoPD
from mLGreedy import RecorridoLaberintoGreedy
from mazes import *


laberinto = laberinto30

for row in range(len(laberinto)):
    for col in range(len(laberinto[row])):
        if laberinto[row][col] == 'F':
            filaFinal = row
            columnaFinal = col
            break

filaInicial = 0
columnaInicial = 0

caminoPD = RecorridoLaberintoPD(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal)

if caminoPD:
    print("Camino encontrado:")
    for fila, columna in caminoPD:
        print(f"({fila}, {columna})")
else:
    print("No hay camino desde la posición inicial a la posición final.")


caminoGreedy = RecorridoLaberintoGreedy(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal)

if caminoGreedy:
    print("Camino encontrado:")
    for fila, columna in caminoGreedy:
        print(f"({fila}, {columna})")
else:
    print("No hay camino desde la posición inicial a la posición final.")    




def medir_tiempo(funcion, laberinto, fila_inicial, columna_inicial, fila_final, columna_final):
    inicio = time.perf_counter()
    funcion(laberinto, fila_inicial, columna_inicial, fila_final, columna_final)
    fin = time.perf_counter()
    tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos
    return tiempo_ejecucion

# Lista para almacenar los tamaños de entrada
sizes = [5, 8, 10, 20, 30]

# Lista para almacenar los tiempos de ejecución
tiempos_ejecucion = []

# Ejecutar el programa y medir los tiempos de ejecución para cada laberinto
for laberinto in [laberinto5, laberinto8, laberinto10, laberinto20, laberinto30]:
    tiempo = medir_tiempo(RecorridoLaberintoGreedy, laberinto, 0, 0, len(laberinto)-1, len(laberinto[0])-1)
    tiempos_ejecucion.append(tiempo)

coeficientes = np.polyfit(sizes, tiempos_ejecucion, 3)
polinomio = np.poly1d(coeficientes)

# Generar valores para el polinomio ajustado
tamanios_interp = np.linspace(min(sizes), max(sizes), 100)
tiempos_interp = polinomio(tamanios_interp)

ssr = np.sum((tiempos_ejecucion - polinomio(sizes)) ** 2)
sst = np.sum((tiempos_ejecucion - np.mean(tiempos_ejecucion)) ** 2)
r_squared = 1 - (ssr / sst)

# Graficar el diagrama de dispersión y el polinomio ajustado
plt.scatter(sizes, tiempos_ejecucion, label='Datos')
plt.plot(tamanios_interp, tiempos_interp, label='Regresión polinomial')
plt.xlabel('Tamaño de entrada')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Tiempos de ejecución y regresión polinomial')
plt.legend()

plt.text(0.5, 0.95, f'R² = {r_squared:.4f}', transform=plt.gca().transAxes, ha='center')
plt.show()