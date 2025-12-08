#Primero debemos importar el modulo 'random'
import random
#Creamos una lista de opciones 
azar = ["piedra", "papel", "tijera"]
#Damos la bienvenida al usuario
user= input("Bienvenido! Cual es tu nombre? ")
print("Hola,",user,"!")
#Empezamos un loop con el contenido y reglas de juego
while True:
    choice= input("Escoge entre piedra, papel o tijera: ").strip().lower()
    if choice in azar:
        print("Escogiste:",choice)
#Establecer que hacer si la opción no está en la lista
    else:
        print("ERROR: Elección no está en la lista")
        continue
#Utilizando el modulo random creamos una elección al azar
    computer= random.choice(azar)
    print("Computadora escogió:",computer)
#Establecemos las reglas
    if choice == computer:
        print("Empate")
    elif choice== "papel" and computer == "piedra":
        print("Ganaste")
    elif choice == "piedra" and computer == "tijera":
        print("Ganaste")
    elif choice == "tijera" and computer == "papel":
        print("Ganaste")
    else:
        print("Computadora Gana!")
    break