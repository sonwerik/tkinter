from tkinter import *

root = Tk()

root.title("Inicio Ahorcado")
root.configure(width=500, height=400)

def empezar_juego():
    root.destroy()

    ahorcado = Tk()
    ahorcado.title("Juego del Ahorcado")
    ahorcado.geometry("500x400")

    ahorcado.mainloop()


Label(root, text='Made by Hass & Èrik').place(x=190, y=100)

Button(text="¡Empezar Juego!", command=empezar_juego).place(x=200, y=200)


root.mainloop()
