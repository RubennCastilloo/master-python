from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="=>Bienvenido a mi programa<=")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Fira Code", 30),
    justify=RIGHT
)
texto.pack(anchor=W)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Ruben", apellidos="Castillo", pais="Mexico"))
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=8,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=NW)

ventana.mainloop()