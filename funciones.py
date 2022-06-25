# Funciones utilizadas en el programa 2048

# Importamos el modulo random para utilizar funciones de numeros al azar
import random

#creamos las clases para los errores
class ErrorVacio(Exception):
    pass
class ErrorNum(Exception):
    pass
class ErrorEspecial(Exception):
    pass

def ingreso_usuario():
    '''Función para validar el usuario'''
    while True:
        try:
            usuario = input("Ingrese su tag de jugador:")
            if len(usuario)==0:
                raise ErrorVacio              
            elif usuario.isdigit()==True:
                raise ErrorNum
            elif usuario.isalnum()==False:
                raise ErrorEspecial
            else:
                break
        except ErrorVacio:
            print("Se debe ingresar un tag")
        except ErrorNum:
            print("Se debe ingresar un tag valido, no puede ser solo numeros")
        except ErrorEspecial:
            print("Se debe ingresar un tag valido, no puede contener caracteres especiales")
    return usuario

def iniciar_juego():
    '''Función para inicializar el juego'''

    # Creamos una matriz vacia de 4x4
    matriz =[]
    for f in range(4):
        matriz.append([0] * 4)

    print("Los comandos son los siguientes : ")
    print("'W' : Para moverse hacia arriba")
    print("'S' : Para moverse hacia abajo")
    print("'A' : Para moverse hacia la izquierda")
    print("'D' : Para moverse hacia la derecha")
    print("'Q' : Para terminar partida y acceder al Menu")

    # Llamamos a la función para agregar un 2 o un 4 en la matriz despues de cada movimiento
    agregar2(matriz)
    return matriz



def separacionRenglon(cantCols, tamCol, tamPrimCol):
    """agrega formato de tabla a la matriz"""
    if tamPrimCol != 0:
        print("-","-"*tamPrimCol,"-",sep="",end="")
        print(("-"*tamCol)*(cantCols-1))
    else:
        print("-",("-"*tamCol)*cantCols,sep="")



def imprimir_matriz(matriz):
    """imprime la matriz en la pantalla"""
    filas= len(matriz)
    col=len(matriz[0])
    separacionRenglon(col+1, 10, 3)
    for f in range(filas):
        print("|",sep="",end="")
        for c in range(col):
            print(f"{matriz[f][c]}".center(10),end="|")
        print()
        separacionRenglon(col+1, 10, 3)


def agregar2(matriz):
    '''Añade un 2 o 4 en la matriz en cualquier parte de manera al azar'''

    fila = random.randint(0, 3)
    columna = random.randint(0, 3)

    # Busca una celda vacia
    while matriz[fila][columna] != 0:
        fila = random.randint(0, 3)
        columna = random.randint(0, 3)

    # Rellena esa celda vacia con un 2 o 4
    num_nuevo=[2,2,2,2,4]
    matriz[fila][columna] = random.choice(num_nuevo)

def estado(matriz):
    '''Informa el estado de la partida'''

    # Busca el 2048 para informar que se gano el juego
    
    for f in range(4):
        for c in range(4):
            if(matriz[f][c]== 2048):
                return 'GANASTE'

    # Si tenemos por lo menos 1 celda vacia, el juego sigue
    for f in range(4):
        for c in range(4):
            if matriz[f][c]== 0:
                return '*EL JUEGO NO HA TERMINADO*'

    # Si con algun movimiento se puede generar alguna celda vacia el juego tampoco termina
    for f in range(3):
        for c in range(3):
            if(matriz[f][c]== matriz[f + 1][c] or matriz[f][c]== matriz[f][c + 1]):
                return '*EL JUEGO NO HA TERMINADO*'

    for c in range(3):
        if(matriz[3][c]== matriz[3][c + 1]):
            return '*EL JUEGO NO HA TERMINADO*'

    for f in range(3):
        if(matriz[f][3]== matriz[f + 1][3]):
            return '*EL JUEGO NO HA TERMINADO*'

    # Si no se cumplen ninguna de las anteriores condiciones es porque se perdio la partida
    return 'PERDISTE'

def comprimir_matriz(matriz):
    '''Comprime la matriz después de cada paso, antes y despues de combinar las celdas'''

    # cambio para registrar cambios
    cambio_matriz = False

    # Creamos una matriz vacia y la rellenamos
    matriz_aux = [[0 for f in range(4)] for c in range(4)]
    # Vamos a mover las filas de cada celda a su limite
    for f in range(4):
        pos = 0
        for c in range(4):
            if(matriz[f][c] != 0):                
            #si la celda no esta vacia moveremos el numero anterior a esa fila 
                matriz_aux[f][pos] = matriz[f][c]               
                if pos != c:
                    cambio_matriz = True
                pos += 1
                
    return matriz_aux, cambio_matriz

def union(matriz):
    '''Fusiona las celdas en la matriz despues de la compresion'''
    multi = 2
    igual_matriz = False    
    for f in range(4):
        for c in range(3):
            # Revisamos que las celdas no esten vacias, y la actual y siguiente no tengan el mismo valor
            if matriz[f][c] == matriz[f][c + 1] and matriz[f][c] != 0:
                # Duplicamos el valor de la celda actual y la siguiente la dejamos vacia
                matriz[f][c] = matriz[f][c] * multi
                matriz[f][c + 1] = 0
                #Con el igual_matriz marcamos que la nueva matriz es diferente
                igual_matriz = True
    return matriz, igual_matriz

def invertir_matriz(matriz):
    '''Invertimos la matriz'''
    matriz_aux =[[0 for f in range(4)] for c in range(4)]
    for f in range(4):
        for c in range(4):
            matriz_aux[f][c] = matriz[f][3 - c]
    return matriz_aux

def transponer_matriz(matriz):
    '''Intercambiamos filas y columnas'''
    matriz_aux = [[0 for f in range(4)] for c in range(4)]
    for f in range(4):
        for c in range(4):
            matriz_aux[f][c]=matriz[c][f]
    return matriz_aux

def score (matriz):
    '''Función recursiva que suma todos los elementos de una matriz'''
    if len(matriz)==0:
        return 0
    elif type(matriz[0]) is list:
        return score(matriz[0]) + score(matriz[1:])
    else:
        return matriz[0] + score(matriz[1:]) 
    
def izquierda(matriz):
    '''Si nos movemos se actualiza la matriz hacia la izquierda'''

    # Primero comprimimos
    nueva_matriz, igual_matriz1 = comprimir_matriz(matriz)
    # Despues fucionamos las celdas
    nueva_matriz, igual_matriz2 = union(nueva_matriz)
    # Volvemos a comprimir despues de la union.
    nueva_matriz, igual_matriz3 = comprimir_matriz(nueva_matriz)    
    igual_matriz = igual_matriz1 or igual_matriz2
    # Retornamos la nueva matriz y el igual_matriz que indica si la matriz es igual o diferente
    return nueva_matriz,igual_matriz

def derecha(matriz):
    '''Si nos movemos se actualiza la matriz hacia la derecha'''

    # Para movernos a la derecha solo tenemos que invertir la matriz
    nueva_matriz = invertir_matriz(matriz)
    # Y despues nos movemos hacia la izquierda
    nueva_matriz, igual_matriz = izquierda(nueva_matriz)
    # Volvemos a invertir la matriz
    nueva_matriz = invertir_matriz(nueva_matriz)
    return nueva_matriz, igual_matriz

def arriba(matriz):
    '''Si nos movemos se actualiza la matriz hacia arriba'''
    
    # Para movernos hacia arriba vamos a transponer la matriz
    nueva_matriz = transponer_matriz(matriz)
    # Luego nos movemos hacia la izquierda
    nueva_matriz, igual_matriz = izquierda(nueva_matriz)
    # Volvemos a transponer la matriz
    nueva_matriz = transponer_matriz(nueva_matriz)
    return nueva_matriz, igual_matriz

def abajo(matriz):
    '''Si nos movemos se actualiza la matriz hacia abajo'''

    # Para movernos hacia abajo vamos a transponer la matriz
    nueva_matriz = transponer_matriz(matriz)
    # Luego nos movemos hacia la derecha
    nueva_matriz, igual_matriz = derecha(nueva_matriz)
    # Volvemos a transponer la matriz
    nueva_matriz = transponer_matriz(nueva_matriz)
    return nueva_matriz, igual_matriz



