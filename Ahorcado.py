import random

lista_palabras = ["MUERTE", "ASESINATO", "HOMICIDIO", "MASACRE", "CRIMEN", "EXTERMINACION"]
palabra = random.choice(lista_palabras)
letras_falladas = set


def palabra_a_resolver():
    print("La palabra tiene", len(palabra), "letras")
    raya = ("_ " * len(palabra))
    print(raya)
palabra_a_resolver()


def preguntar_letra():
    while True:
        letra = input("\nIntroduce una letra: ")
        letra_upper = letra.upper()
        letra = letra_upper

        if letra in palabra:
            print("Muy bien, has acertado la letra!!")
            palabra_a_resolver()
        else:
            print("Esa letra no esta en la palabra. ¡Sigue intentandolo!")
preguntar_letra()

def remplazar_letra():
    global raya

