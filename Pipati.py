#Juego de Piedra Papel o Tijera
#By Geovas or MartL7

import random
opciones = ["piedra", "papel", "tijera"]
NombresBot = ["Pepe", "Pepito", "Juanito", "El bicho", "Goku", "Messi", "SpiderMan"]
print("Bienvenido al juego de piedra papel o tijera")


Reinicio = True
while Reinicio:
    bot = random.choice(NombresBot)
    print("Hola, soy ", bot, "Jugaras contra mi, preparate")
    usuario = input("Elije piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)

    if usuario == computadora:
        print(bot, "Escogio", computadora, "Por lo tanto empataron")
    elif usuario == "piedra" and computadora == "tijera":
        print(bot, "Escogio", computadora, "Por lo tanto le ganaste")
    elif usuario == "papel" and computadora == "piedra":
        print(bot, "Escogio", computadora, "Por lo tanto le ganaste")
    elif usuario == "tijera" and computadora == "papel":
        print(bot, "Escogio", computadora, "Por lo tanto le ganaste")
    elif usuario == "piedra" and computadora == "papel":
        print(bot, "Escogio", computadora, "Por lo tanto perdiste")
    elif usuario == "papel" and computadora == "tijera":
        print(bot, "Escogio", computadora, "Por lo tanto perdiste")
    elif usuario == "tijera" and computadora == "piedra":
        print(bot, "Escogio", computadora, "Por lo tanto perdiste")
    else:
        print("Eso no es una opcion")

    OtraVez = input("¿Desea jugar de nuevo? (si/no) ").lower()
    if OtraVez != "si":
        print("Chao 😅")
        break;