from tkinter import *

root = Tk()

root.title("Boton Erik")
root.configure(width=300, height=200)

Label(root,text='Este boton no hace nada...').place(x=80, y=75)

Button(text="Boton").place(x=125, y=50)

root.mainloop()