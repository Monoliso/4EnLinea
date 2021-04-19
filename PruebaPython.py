print("Hello World")

print("Vamos a ver qué tal andamos con esto, Shall we?")

print("Introduzca una secuencia de juego")

secuencia = [1, 2, 3, 1]

def TableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

#def ReiniciarTablero(tablero):
#    tablero = TableroVacio()
#    return

def SoltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return
    print("La columna", columna, "ya está llena")
    return tablero

def CompletarTableroEnOrden(secuencia, tablero):
    ficha = 0
    for i in range (1, len(secuencia), +1): #(i = 1, len(secuencia) => i, i++)
        if(i % 2 == 0):
            ficha = 2
        else:
            ficha = 1
        SoltarFichaEnColumna(ficha, secuencia[i], tablero)
    return tablero

def DibujarTablero(tablero):
    print(tablero)

DibujarTablero( 
    CompletarTableroEnOrden(
        secuencia, TableroVacio()
    )
)