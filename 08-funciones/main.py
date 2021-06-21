"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden utilizarse
invocando a la función tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

def holaMundo(nombre):
    nombre = nombre
    print(f"Hola {nombre}")

holaMundo("Ruben")
holaMundo("Alexandra")

print("##### EJEMPLO 2 #####")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))

nombre = "Ruben Castillo"
edad = 18

mostrarTuNombre(nombre, edad)

print("##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero * contador

        print(f"{numero} x {contador} = {operacion}")

    print("\n")

# numero = int(input("Introduce un numero para obtener su tabla de mutliplicar: "))
numero = 2

tabla(numero)

# Ejemplo 3.1

for numero_tabla in range(1, 11):
    tabla(numero_tabla)


print("##### EJEMPLO 4 #####")

# Parametros opcionales

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Ruben Castillo", "0938080")

# Ejemplo 5: return o devolver datos

print("##### EJEMPLO 5 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Ruben"))

# Ejemplo 6

print("##### EJEMPLO 6 #####")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Mutiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(5, 5, True))

# Ejemplo 7

print("##### EJEMPLO 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"

    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"

    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)

    return texto

print(devuelveTodo("Ruben", "Castillo Gonzalez"))

# Ejemplo 8 Funciones Lambda

print("\n##### EJEMPLO 8 #####")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034))
