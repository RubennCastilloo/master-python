#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Proyecto Python y MySQL:
- Abrir asistente
- Login o Registro
- Si elegimos registro creará un usuario en la base de datos
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas o salir
"""

from usuarios import acciones

print(""" 
Acciones disponibles:
    - Registro (R)
    - Login (L)
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion.lower() == "r":
    hazEl.registro()

elif accion.lower() == "l":
    hazEl.login()
    

else:
    print("Seleccionaste una opción incorrecta")