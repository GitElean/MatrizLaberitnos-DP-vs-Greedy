from mLDP import RecorridoLaberintoPD
from mLGreedy import RecorridoLaberintoGreedy

laberinto = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', 'X', 'X', ' ', 'X'],
    [' ', ' ', ' ', ' ', ' '],
    ['X', 'X', 'X', ' ', ' '],
    [' ', ' ', ' ', ' ', 'F']
]

filaInicial = 0
columnaInicial = 0
filaFinal = 4
columnaFinal = 4


caminoPD = RecorridoLaberintoPD(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal)

if caminoPD:
    print("Camino encontrado:")
    for fila, columna in camino:
        print(f"({fila}, {columna})")
else:
    print("No hay camino desde la posición inicial a la posición final.")


caminoGreedy = RecorridoLaberintoGreedy(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal)

if camino:
    print("Camino encontrado:")
    for fila, columna in camino:
        print(f"({fila}, {columna})")
else:
    print("No hay camino desde la posición inicial a la posición final.")    
