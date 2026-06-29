import random
azar = ["piedra", "papel", "tijera"]
juego = ["1","2"]
x = 0
y= 0
user= input("Bienvenido! Cual es tu nombre? ").title()
print("Hola,",user,"!")
while True:
    choice= input("Escoge entre piedra, papel o tijera: ").strip().lower()
    if choice in azar:
        print("Escogiste:",choice)
    else:
        print("ERROR:",choice, "no está en la lista")
        continue
    computer= random.choice(azar)
    print("Computadora escogió:",computer)
    if choice == computer:
        print("Empate")
    elif choice== "papel" and computer == "piedra":
        print("Ganaste")
        x += 1
    elif choice == "piedra" and computer == "tijera":
        print("Ganaste")
        x += 1
    elif choice == "tijera" and computer == "papel":
        print("Ganaste")
        x += 1
    else:
        print("Computadora Gana!")
        y += 1
    print("Puntaje", user,":",x,"Computadora:", y) 
    while True:
        ronda= input("Quieres jugar otra vez? Si o No? ").strip().lower()
        if ronda == "no":
            print("Gracias por jugar", user,"!")
            exit()
        elif ronda == "si":
            break
        else:
            print("Escoge entre 'si o 'no'")
  