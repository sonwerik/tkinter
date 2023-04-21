import random

elementos = ['Piedra', 'Papel', 'Tiejras']

def juego():
    global elementos
    mano = input("Piedra, Papel, Tijeras! ")
    while True:
        maquina = random.choice(elementos)
        print(maquina)
        if mano == "Piedra" and maquina == "Piedra":
            print("Empate")
            break
        elif mano == "Piedra" and maquina == "Papel":
            print("Has perdido")
            break
        elif mano == "Piedra" and maquina == "Tijeras":
            print("¡Has ganado!")
            break
        elif mano == "Papel" and maquina == "Papel":
            print("Empate")
            break
        elif mano == "Papel" and maquina == "Piedra":
            print("¡Has ganado!")
            break
        elif mano == "Papel" and maquina == "Tijeras":
            print("Has perdido")
            break
        elif mano == "Tijeras" and maquina == "Tijeras":
            print("Empate")
            break
        elif mano == "Tijeras" and maquina == "Papel":
            print("¡Has ganado!")
            break
        elif mano == "Tijeras" and maquina == "Piedra":
            print("Has perdido")
            break
        else:
            print("Por favor, introduce un valor correcto. Elige entre Piedra, Papel o Tijeras.")
            break

juego()