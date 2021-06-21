""" 
# FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"El número iterado es {numero}")

contador = 0
resultado = 0

for contador in range(0, 10):
    print(f"Voy por el {contador}")

    resultado += contador

print(f"El resultado es: {resultado}")

# Ejemplo con tablas de multiplicar

print('\n############## EJEMPLO ##############')

numero_usuario = int(input("¿De que número quiere la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break
    
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")