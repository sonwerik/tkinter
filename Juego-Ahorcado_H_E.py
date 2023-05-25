import random
import tkinter as tk
from tkinter import messagebox


def empezar_juego():
    root.destroy()

    top = tk.Tk()
    top.title("Juego del Ahorcado")
    top.geometry("1000x800")

    # Puntuación por letra
    puntuacion_letras = {
        "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4,
        "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "Ñ": 8, "O": 1,
        "P": 3, "Q": 5, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4,
        "X": 8, "Y": 4, "Z": 10
    }

    # Lista de palabras
    lista_palabras = ["ZAFIRO", "ESMERALDA", "AMATISTA", "AGUAMARINA", "LAPISLAZULI", "TURMALINA", "AGATA",
                      "NITROGENO", "MAGNESIO", "FOSFORO", "AZUFRE", "TITANIO", "MANGANESO", "ESTAÑO", "PRASEODIMIO",
                      "VICTIMOLOGÍA", "IMPUNIDAD", "SECUESTRO", "VICTIMIZACION", "HOMICIDIO", "IMPUTABILIDAD",
                      "CRIMINOLOGIA",
                      "INVESTIGACION", "SENTENCIA", "ELECTROENCEFALOGRAMA", "ONTOLOGIA", "EPISTEMOLOGIA", "METAFISICA",
                      "COSMOLOGIA", "FENOMENOLOGIA", "MATERIALISMO", "EXISTENCIALISMO"]

    # Lista de Fotos
    listaFotos = [
        'Images1/fto1.png',
        'Images1/fto2.png',
        'Images1/fto3.png',
        'Images1/fto4.png',
        'Images1/fto5.png',
        'Images1/fto6.png'
    ]

    # Variables globales
    palabra = ""
    raya = []
    letras_falladas = set()
    letras_adivinadas = set()
    puntuacion_acumulada = 0
    intentos = 0

    # Función de Mostrar imagen
    def mostrar_imagen():
        nonlocal intentos
        if intentos < len(listaFotos):
            image = tk.PhotoImage(file=listaFotos[intentos])
            label_imagen.config(image=image)
            label_imagen.image = image

    label_imagen = tk.Label(top)
    label_imagen.place(x=500, y=400, anchor="center")

    # Función de Mostrar raya
    def mostrar_raya():
        label_raya.config(text=" ".join(raya))

    label_raya = tk.Label(top, text="", font=("Arial", 24))
    label_raya.place(x=500, y=670, anchor="center")

    # Función de Importante para mostrar y remplazar letra
    def comprobar_letra():
        nonlocal intentos, puntuacion_acumulada

        letra = entry_letra.get().upper()
        entry_letra.delete(0, "end")

        if letra.isalpha() and len(letra) == 1 and letra not in letras_adivinadas and letra not in letras_falladas:
            if letra in palabra:
                letras_adivinadas.add(letra)
                puntuacion_acumulada += puntuacion_letras[letra]
                for i in range(len(palabra)):
                    if letra == palabra[i]:
                        raya[i] = letra
                mostrar_raya()
                label_puntuacion.config(
                    text="Puntuación acumulada: {}".format(puntuacion_acumulada))
                if "_" not in raya:
                    opcion_continuar = messagebox.askquestion(
                        "¡Felicidades!", "¡Has adivinado la palabra!\n¿Deseas continuar?")
                    if opcion_continuar == "yes":
                        iniciar_juego()
                    else:
                        top.destroy()
            else:
                letras_falladas.add(letra)
                intentos += 1
                mostrar_imagen()
                label_letras_falladas.config(
                    text="Letras falladas: {}".format(", ".join(letras_falladas)))
                if intentos >= len(listaFotos):
                    opcion_continuar = messagebox.askquestion(
                        "¡Has perdido!", "La palabra era: {}\n¿Quieres continuar?: ".format(palabra))
                    if opcion_continuar == "yes":
                        iniciar_juego()
                    else:
                        top.destroy()
        else:
            messagebox.showinfo(
                "Error", "Introduce una única letra válida y no repetida.")

    label_letras_falladas = tk.Label(
        top, text="Letras falladas:", font=("Arial", 15))
    label_letras_falladas.place(x=900, y=30, anchor="ne")

    label_puntuacion = tk.Label(top, text="Puntuación acumulada: {}".format(
        puntuacion_acumulada), font=("Arial", 15))
    label_puntuacion.place(x=500, y=780, anchor="center")

    label_letra = tk.Label(
        top, text="Introduce una letra: ", font=("Arial", 15))
    label_letra.grid(column=0, row=0)

    entry_letra = tk.Entry(top, width=10, font=("Arial", 14))
    entry_letra.grid(column=1, row=0)

    # Principal
    def iniciar_juego():
        nonlocal palabra, raya, letras_falladas, letras_adivinadas, puntuacion_acumulada, intentos

        palabra = random.choice(lista_palabras).upper()
        raya = ["_"] * len(palabra)
        letras_falladas = set()
        letras_adivinadas = set()
        puntuacion_acumulada = 0
        intentos = 0

        label_raya.config(text=" ".join(raya))
        label_letras_falladas.config(text="Letras falladas:")
        label_puntuacion.config(
            text="Puntuación acumulada: {}".format(puntuacion_acumulada))
        mostrar_imagen()
    iniciar_juego()

    # Botón para comprobar la letra ingresada
    button_comprobar = tk.Button(top, text="🔍", font=(
        "Arial", 14), command=comprobar_letra)
    button_comprobar.grid(column=2, row=0)

    # Comprobar con enter
    def comprobar_letra_con_enter():
        entry_letra.bind('<Return>', comprobar_letra_con_enter)

    top.mainloop()


root = tk.Tk()
root.geometry("500x400")
root.title("Inicio Ahorcado")

tk.Label(root, text="Made by Hass & Èrik").place(x=190, y=85)
tk.Label(root, text="¡Bienvenidos al Juego del Ahorcado!",
         font=("Arial", 20)).place(x=250, y=60, anchor="center")

tk.Button(root, text="¡Empezar Juego!",
          command=empezar_juego).place(x=190, y=250)

root.mainloop()
