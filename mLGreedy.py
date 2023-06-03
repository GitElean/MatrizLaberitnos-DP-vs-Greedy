def RecorridoLaberintoGreedy(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal):
    camino = []
    i = filaInicial
    j = columnaInicial
    
    while i != filaFinal or j != columnaFinal:
        camino.append((i, j))
        if i < filaFinal and laberinto[i+1][j] != 'X':
            i += 1
        elif j < columnaFinal and laberinto[i][j+1] != 'X':
            j += 1
        elif i > filaFinal and laberinto[i-1][j] != 'X':
            i -= 1
        elif j > columnaFinal and laberinto[i][j-1] != 'X':
            j -= 1
        else:
            return []  # No hay camino válido
    
    camino.append((filaFinal, columnaFinal))
    
    return camino

