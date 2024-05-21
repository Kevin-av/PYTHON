import random

def game():
    numRandom = random.randint(1, 20)
    chance = 0

    print("¡Adivina el número y llévate un premio!")
    print("Los números serán entre 1 y 20")

    while True:
        try:
            select = int(input("Introduce el número: "))
            chance += 1

            if select < numRandom:
                print("Demasiado bajo, inténtalo de nuevo")
            elif select > numRandom:
                print("Demasiado alto, inténtalo de nuevo")
            else:
                print(f"¡Felicidades por ganar el juego en {chance} intentos!")
                break
        except ValueError:
            print("Por favor, introduce un número válido")

game()
