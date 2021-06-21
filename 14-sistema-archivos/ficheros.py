from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir archivo
archivo.write("***** Soy un texto metido desde python *****\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    lista_frase = frase.split()
    # print(lista_frase)
    print("- " + frase.capitalize())

# Copiar archivos

# ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/copiado.txt"
# shutil.copyfile(ruta_original, ruta_nueva)


# Mover archivos

# ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto_NUEVO.txt"

# shutil.move(ruta_original, ruta_nueva)

# Eliminar 
import os
# os.remove(ruta_nueva)

# Comprobar si existe
import os.path

# print(os.path.abspath("./"))

ruta_comrpobar = os.path.abspath("./") + "/14-sistema-archivos/fichero_texto.txt"
print(ruta_comrpobar)
ruta_comrpobar = "./14-sistema-archivos/fichero_texto.txt"

if os.path.isfile(ruta_comrpobar):
    print("El archivo existe")
else:
    print("El archivo no existe")