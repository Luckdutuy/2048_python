#Importamos nuestro programa de funciones donde tenemos toda la logica que vamos a usar
import funciones
  
# Llamamos a las funciones de usuario e iniciar_juego para comenzar
usuario = funciones.ingreso_usuario()
print("El usuario: ",usuario, "se registro correctamente")
matriz = funciones.iniciar_juego()
funciones.imprimir_matriz(matriz)
#Se lee el archivo de puntajes y se guarda en un diccionario
#el mejor puntaje de cada usuario para luego mostrarlo en pantalla
diccionario={}
try:
        archivo_tablero = open("Puntajes.txt","rt")
        for linea in archivo_tablero:
            linea = linea.rstrip("\n")
            player,score= linea.split(',')
            nuevo_score=int(score)
            if player not in diccionario:
                diccionario[player] = nuevo_score
            elif player in diccionario and nuevo_score > diccionario[player]:
                diccionario[player] = nuevo_score
except FileNotFoundError as mensajes:
        print("No se encuentran las puntuaciones")
except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
finally:
        try:
            archivo_tablero.close()
        except NameError:
            pass


while True: 

    #Le pedimos al usuario que ingrese el comando que desea
    comando = input("Presiona el comando: ")
    
    # Mover hacia arriba
    if comando.lower() == 'w':

        # LLamamos a la funcion arriba para desplazarnos hacia arriba
        matriz, matriz_distinta = funciones.arriba(matriz)

        # Llamamos a la funcion estado e imprimimos el resultado
        estado_juego = funciones.estado(matriz)
        print(estado_juego)

        # Si el juego todavia continua, llamamos a la funcion para agregar 2 o 4
        if estado_juego == '*EL JUEGO NO HA TERMINADO*':
             if matriz_distinta == True:   
                funciones.agregar2(matriz)
                #Volvemos a chequear el estado del juego y si perdimos con ese movimiento termina ahi
                estado_juego = funciones.estado(matriz)
                if estado_juego== 'PERDISTE':
                    funciones.imprimir_matriz(matriz)
                    print("Perdiste")
                    break
        
        else:
            funciones.imprimir_matriz(matriz)
            break
    # Mover hacia abajo
    elif comando.lower() == 's':
        matriz, matriz_distinta = funciones.abajo(matriz)
        estado_juego = funciones.estado(matriz)
        print(estado_juego)
        if estado_juego == '*EL JUEGO NO HA TERMINADO*':
            if matriz_distinta == True:
                funciones.agregar2(matriz)
                estado_juego = funciones.estado(matriz)
                if estado_juego== 'PERDISTE':
                    funciones.imprimir_matriz(matriz)
                    print("Perdiste")
                    break
        else:
            funciones.imprimir_matriz(matriz)
            break
    
    # Mover hacia la izquierda
    elif comando.lower() ==  'a':
        matriz, matriz_distinta = funciones.izquierda(matriz)
        estado_juego = funciones.estado(matriz)
        print(estado_juego)
        if estado_juego == '*EL JUEGO NO HA TERMINADO*':
            if matriz_distinta == True:        
                funciones.agregar2(matriz)
                estado_juego = funciones.estado(matriz)
                if estado_juego== 'PERDISTE':
                    funciones.imprimir_matriz(matriz)
                    print("Perdiste")
                    break
        else:
            funciones.imprimir_matriz(matriz)
            break

    # Mover hacia la derecha
    elif comando.lower() == 'd':
        matriz, matriz_distinta = funciones.derecha(matriz)
        estado_juego = funciones.estado(matriz)
        print(estado_juego)
        if estado_juego == '*EL JUEGO NO HA TERMINADO*':
             if matriz_distinta == True:
                funciones.agregar2(matriz)
                estado_juego = funciones.estado(matriz)
                if estado_juego== 'PERDISTE':
                    funciones.imprimir_matriz(matriz)
                    print("Perdiste")
                    break
        else:
            funciones.imprimir_matriz(matriz)
            break
                
    #Comando Para Salir de la partida
    elif comando.lower() =='q':
        salir=1
        #Iteracion que permite reiniciar la partida y no salir del programa
        while salir==1:
            print("'R': Para reiniciar la partida")
            print("'S': Para salir del juego y guardar puntaje")
            print("'P': Para ver las puntuaciones")
            respuesta=input("Presione un comando:")
            
            #Comando para reiniciar partida
            if respuesta.lower() == 'r':
                salir=0
                matriz = funciones.iniciar_juego()
            
            #Comando para salir del juego difinitivamente
            elif respuesta.lower() =="s":
                salir=0
            
            #Comando para ver los mejores puntajes de cada jugador
            elif(respuesta.lower() == 'p'):
                vacio= len(diccionario.keys())
                if vacio ==0:
                    print("No hay puntajes guardados")
                else:
                    print("Las mejores puntuaciones de los jugadores son:")
                    for player in diccionario:
                        print(f"{player} : {diccionario[player]}")
                
            else: 
                print("ERROR, se presiono un comando no valido")
        if respuesta =="s" or respuesta == "S" :
            break
        
    else:
        print("ERROR, se presiono un comando no valido")

    # Mostramos la matriz despues de cada movimiento
    funciones.imprimir_matriz(matriz)
    
# Llamamos a la funcion score para que calcule el puntaje de la partida    
puntaje= funciones.score(matriz) 
#Se crea un archivo donde se guarda el nombre del jugador y su puntaje maximo
#Si ya esta creado se suma al final el nuevo nombre del jugador y su puntaje
try:
    arch= open ("Puntajes.txt","at")
    arch.write(usuario + "," + str(puntaje) + '\n')
except OSError as Mensaje:
    print("No se puede grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass