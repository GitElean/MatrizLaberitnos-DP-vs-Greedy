def RecorridoLaberintoPD(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal):
    n = len(laberinto)
    m = len(laberinto[0])

    DP = [[float('inf')] * m for _ in range(n)]
    DP[filaInicial][columnaInicial] = 0

    for i in range(n):
        for j in range(m):
            if laberinto[i][j] == 'pared':
                DP[i][j] = float('inf')
            else:
                if i > 0:
                    DP[i][j] = min(DP[i][j], DP[i-1][j] + 1)
                if j > 0:
                    DP[i][j] = min(DP[i][j], DP[i][j-1] + 1)

    if DP[filaFinal][columnaFinal] == float('inf'):
        return []  # No hay camino desde la posición inicial a la posición final

    camino = []
    i = filaFinal
    j = columnaFinal

    while i != filaInicial or j != columnaInicial:
        camino.append((i, j))
        if i > 0 and DP[i-1][j] < DP[i][j]:
            i -= 1
        else:
            j -= 1

    camino.append((filaInicial, columnaInicial))
    camino.reverse()

    return camino

