#Este es la representacion del juego Piedra, papel y tijera
#desarrollado en python y aplicando logica de programacion
import random 
#importamos la funcion *random* para que nos ayude a generar un numero random
#Ese numero se interpretara como lo opcion escogida por el ordenador

print("Bienvenido al juego piedra - papel - tijera")
nombre = input("Ingresa tu nombre porfavor: ")

opcion = -1 #valor inicial para entrar al ciclo

while opcion != 0: #Bucle infito hasta que la condicion sea falsa
    
    #menu de opciones para el usuario 
    opcion = int(input('''                    
        Opciones a escoger
                        
        piedra = 1
        papel = 2
        tijera = 3 
                       
        Salir = 0
        
        Elije una opcion, para la partida: '''))
    
    if opcion == 0: #condicional para terminar el bucle
        print(f"Gracias jugar, {nombre}")
        break #uso de sentencias

    computadora = random.randint(1,3) #generador de la jugada aleatoria

    #bloque para mejorar los mensajes por parte de la pc
    if computadora == 1:
        comodin = "piedra"
    elif computadora == 2:
        comodin = "papel"
    elif computadora == 3:
        comodin = "tijera"

    #bloque para mejorar los mensajes por parte del usuario
    if opcion == 1:
        usuario = "piedra"
    elif opcion == 2:
        usuario = "papel"
    elif opcion == 3:
        usuario = "tijera"
    else:
        print("Esa opcion, no está disponible por el momento. :( )")
        break

    #mensaje informando, lo sucedido en el juego
    print(f"La computadora eligio {comodin}, mientras qué, {nombre} selecciono {usuario}")

    #seccion logica del juego
    if opcion == computadora:
        print(f"Esto es un empate, ambos eligieron la misma figura {comodin}")
    elif (opcion == 1 and computadora == 3) or (opcion == 2 and computadora == 1) or (opcion == 3 and computadora == 2):
        print(f"Ganaste{nombre}")
    else:
        print(f"{nombre}, perdiste")