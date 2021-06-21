# Condicionales
import os
os.system('cls' if os.name == 'nt' else 'clear') # Limpiar pantalla

print('############## EJEMPLO 1 ##############')

color = 'rojo'
# color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("El color seleccionado es rojo")
else:
    print("El color NO es rojo")

# Operadores de comparación
"""
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos

and Y
or O
! negación
not NO

"""

print('\n############## EJEMPLO 2 ##############')

# year = int(input("¿En que año estamos?: "))
year = 2021

if year < 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior al 2021")

# Ejemplo 3

print('\n############## EJEMPLO 3 ##############')

nombre = "Ruben Castillo"
ciudad = "Chihuahua"
continente = "Europeo"
edad = 25
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!")

    if continente != "Americano":
        print("El usuario NO es Americano")
    else:
        print(f"Es Americano y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")


# Ejemplo 4

print('\n############## EJEMPLO 4 ##############')

# dia = int(input("Elige un día: "))
dia = 1

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado")
elif dia == 7:
    print("Es Domingo")
else:
    print("Numero de dia incorrecto")

# Ejemplo 5

print('\n############## EJEMPLO 5 ##############')

edad_minima = 18
edad_maxima = 65
# edad_oficial = int(input("¿Cual es tu edad?: "))
edad_oficial = 19

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar!")
else:
    print("No está en edad de trabajar")


# Ejemplo 6

print('\n############## EJEMPLO 6 ##############')

pais = "México"

if not (pais == "México" or pais == "España" or pais == "Colombia"):   
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} es un país de habla hispana")