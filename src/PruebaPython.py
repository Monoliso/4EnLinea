print("Bienvenido al juego '4 En Línea' por Luca Seri para la materia 'Adaptaciones del Ambiente de Trabajo':")

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

################################################# Imput

secuencia_texto = input("Introduzca una secuencia de juego: ")
secuencia = []
for items in secuencia_texto.split(','):
    secuencia.append(int(items))

################################################# Contenido Tablero

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
    return tablero[nro_fila - 1] #[6 - nro_fila] para conseguir de forma invertida

def ContenidoTodasLasFilas(tablero):
    return tablero

################################################# Formación Tablero

def Contorno(tablero):
    for fila in range(6):
        print("| ", end='')
        for columna in range (7):
            print(tablero[fila][columna], end='') # En estas 3 líneas se puede ver que imprimir una variable *Y* caracteres 
            if(columna != 6):                     # en un mismo print genera entre ellos un espacio automáticamente, es por ello
                print("  ", end='')               # que agrego ese cuestionable 'if'. Logra, al menos, su cometido.
        print(" |")
    print("+---------------------+")
    return tablero

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

################################################# Comprobación de Calidad

def ComprobacionSecuencia(secuencia):

    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

################################################# Output

def DibujarTablero(tablero):
    i = 1
    Contorno(ReemplazoPorEspacio(tablero))
    print ("Contenido de la columna {}:\n".format(i), ContenidoColumna(i, tablero)) #Acá hay más ejemplos del caso de las líneas 53-55.
    for x in range(7):
        print ("Columna numero {}:".format(x + 1))
        aux = ContenidoTodasLasColumnas(tablero)
        print (aux[x])
    
    # for x in ContenidoTodasLasColumnas(tablero): #Posibles versión
    #     i = i + 1
    #     print ("Columna numero {}:".format(i))  
    #     print (x)
    
    print ("Contenido de la fila {}:\n".format(i), ContenidoFila(i, tablero))
    for x in range(6):
        print ("Fila numero {}:".format(x + 1))
        aux = ContenidoTodasLasFilas(tablero)
        print (aux[x])
    
    # for x in ContenidoTodasLasFilas(tablero): #Posible versión
    #     i = i + 1
    #     print ("Fila numero {}:".format(i))
    #     print (x)

if ComprobacionSecuencia(secuencia):
    DibujarTablero( 
        CompletarTableroEnOrden(
            secuencia, TableroVacio()
        )
    )
else:
    print("Las columnas deberian ir de 1 a 7")