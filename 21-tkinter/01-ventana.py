# Tkinter es un módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Master en Python con Ruben Castillo"
        self.icon = "./imagenes/icon.ico"
        self.icon_alt = "./21-tkinter/imagenes/icon.ico"
        self.size = "770x470"
        self.resiable = False

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        ventana.resizable(0, 0)

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)
        # img = Image("photo", file="./imagenes/icon.ico")
        # ventana.iconphoto(True, img)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
         # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
programa.addTexto("Hola soy un texto")
programa.mostrar()