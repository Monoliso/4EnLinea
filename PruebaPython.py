print("Hello World")

print("Vamos a ver qué tal andamos con esto, Shall we?")

#print("Introduzca una secuencia de juego")
#Para en el futuro agregar algo como un Scanf.

secuencia = [1, 2, 3, 1, 4, 7, 8]

def TableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def SoltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return tablero
    print("La columna", columna, "ya está llena")
    return tablero

def CompletarTableroEnOrden(secuencia, tablero): #Modificar en la próxima versión, es mucho mejor la del profesor, y más claro.
    ficha = 0
    for i in range (1, len(secuencia)+1, +1):
        if(i % 2 == 0):
            ficha = 2
        else:
            ficha = 1
        SoltarFichaEnColumna(ficha, secuencia[i-1], tablero)
    return tablero

def DibujarTablero(tablero):
    print(tablero)

def ComprobacionSecuencia(secuencia):

    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

if ComprobacionSecuencia(secuencia):
    DibujarTablero( 
        CompletarTableroEnOrden(
            secuencia, TableroVacio()
    )
)
else:
    print("Las columnas deberian ir de 1 a 7")