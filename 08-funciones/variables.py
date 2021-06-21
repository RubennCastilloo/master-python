""" 
 Las variables locales solo están disponibles dentro de la función y se declaran
 dentro de la misma.

 Las variables globales se declaran fuera de la función y están disponibles dentro
 y fuera de las funciones
"""

# Variable global

frase = "Hola mundo variable global"

print(frase)

def holaMundo():
    frase = "Hola mundo variable local"

    return frase

print(holaMundo())