#Este es la representacion del juego Piedra, papel y tijera
#desarrollado en python y aplicando logica de programacion
import random 
#importamos la funcion *random* para que nos ayude a generar un numero random
#Ese numero se interpretara como lo opcion escogida por el ordenador

print("Bienvenido al juego piedra - papel - tijera")
nombre = input("Ingresa tu nombre porfavor: ")
opcion = int(input('''
                   
    Opciones a escoger
                    
    piedra = 1
    papel = 2
    tijera = 3 
    
    Elije el numero del comodin para la partida: '''))

computadora = random.randint(1,3)
print(computadora)

if computadora == 1:
    comodin = "piedra"
elif computadora == 2:
    comodin = "papel"
elif computadora == 3:
    comodin = "tijera"

if opcion == 1:
    usuario = "piedra"
elif opcion == 2:
    usuario = "papel"
elif opcion == 3:
    usuario = "tijera"

print(f"La computadora eligio {comodin}, mientras qué, {nombre} selecciono {usuario}")

if opcion == computadora:
    print("Esto es un empate")
elif (opcion == 1 and computadora == 3) or (opcion == 2 and computadora == 1) or (opcion == 3 and computadora == 2):
    print("Ganaste")
else:
    print(f"{nombre}, perdiste")