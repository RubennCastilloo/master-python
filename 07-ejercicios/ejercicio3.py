"""
Ejercicio 3. Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo)
de los primeros 60 numeros naturales. Resolverlo con for y con while
"""

# WHILE

contador = 0

while contador <= 60:

    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")

    contador += 1

# FOR

for numero in range(61):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")