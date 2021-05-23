print("Bienvenido al juego '4 En Línea' por Luca Seri para la materia 'Adaptaciones del Ambiente de Trabajo':")

#print("Introduzca una secuencia de juego")
#Para en el futuro agregar algo como un Scanf.

secuencia = [1, 2, 3, 1, 4, 7, 1, 1, 1]

def TableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

# (Intento de hacer recursivo)
#
# def ContenidoColumna2(columna, tablero):
#     L = len(tablero)
#     if(tablero == []):
#         return []
#     return [tablero[L - 1][columna - 1]] + ContenidoColumna2[columna, tablero.pop()]

############################################## Contenido Tablero

def ContenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna

def ContenidoTodasLasColumnas(tablero):
    columnas = []
    for columna in range(7):
        columnas.append(ContenidoColumna(columna + 1, tablero))
    return columnas

def ContenidoFila(nro_fila, tablero):
    return tablero[6 - nro_fila]

def ContenidoTodasLasFilas(tablero):
    return tablero

############################################## Formación Tablero

def ReemplazoPorEspacio(tablero):
    for fila in range(6):
        for columna in range (7):
            if(tablero[fila][columna] == 0):
                tablero[fila][columna] = " "
    return tablero

def SoltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return tablero
    print("La columna", columna, "ya está llena")
    return tablero

def CompletarTableroEnOrden(secuencia, tablero):
    ficha = 0
    for indice, columna in enumerate(secuencia):
        ficha = 1 + (indice % 2)
        SoltarFichaEnColumna (ficha, columna, tablero)
    return tablero

############################################## Comprobación de Calidad

def ComprobacionSecuencia(secuencia):

    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

############################################# Output

def DibujarTablero(tablero):
    #ReemplazoPorEspacio(tablero)
    for x in tablero:
        print(x)
    print (ContenidoColumna(1, tablero))
    # print (ContenidoColumna2(1, tablero))
    i = 0
    for x in ContenidoTodasLasColumnas(tablero):
        i = i + 1
        print ("Columna número", i)
        print (x)
    print (ContenidoFila(1, tablero))
    print (ContenidoTodasLasFilas(tablero))

if ComprobacionSecuencia(secuencia):
    DibujarTablero( 
        CompletarTableroEnOrden(
            secuencia, TableroVacio()
        )
    )
else:
    print("Las columnas deberian ir de 1 a 7")