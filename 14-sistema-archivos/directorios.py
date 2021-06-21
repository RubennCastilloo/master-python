import os
import shutil

# Crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("El directorio ya existe")

# Copiar  una carpeta

# ruta_original = "./mi_carpeta"
# ruta_nueva = "./mi_carpeta_copiada"
# shutil.copytree(ruta_original, ruta_nueva)

# Eliminar

# os.rmdir("./mi_carpeta")

print("Contenido de mi carpeta: ")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for fichero in contenido:
    print(f"Fichero: ", fichero)