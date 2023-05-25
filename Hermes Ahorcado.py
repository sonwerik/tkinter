import random
from tkinter import *

root = Tk()

root.title("Inicio Ahorcado")
root.configure(width=500, height=400)


def empezar_juego():
    root.destroy()

    ahorcado = Tk()
    ahorcado.title("Juego del Ahorcado")
    ahorcado.geometry("500x400")

    lista_palabras = ["HERMES", "HESTIA"]

    palabra = random.choice(lista_palabras)

    raya = ["_"] * len(palabra)
    raya_texto = " ".join(raya)

    Label(ahorcado, text="Introduce una letra").place(x=20, y=50)

    letra = Entry(ahorcado)
    letra.place(x=20, y=70)

    Label(ahorcado, text=raya_texto, font=("Arial", 20)).place(x=250, y=320, anchor="center")

    def reemplazar_letra():
        nonlocal raya

        letra_ingresada = letra.get()
        if letra_ingresada in palabra:
            Label(ahorcado, text="Has acertado la letra '{}'!".format(letra))

        else:
            Label(ahorcado, text="Esa letra no está en la palabra. ¡Sigue intentándolo!")
    reemplazar_letra()

    def click():
        boton = Button(ahorcado, text="Enviar", command=reemplazar_letra)
        boton.place(x=145, y=65)

    click()

    ahorcado.mainloop()


Label(root, text="Made by Hass & Èrik").place(x=190, y=100)

Button(text="¡Empezar Juego!", command=empezar_juego).place(x=200, y=200)

root.mainloop()