"""
 LISTAS (arrays)
 Son colecciones o conjuntos de datos/valores, bajo un único nombre.
 Para acceder a esos valores podemos usar un índice numérico.
"""

pelicula = "Batman"
# print(pelicula)

# Definir una lista
peliculas = [pelicula, "Spiderman", "El señor de los anillos"]
cantantes = list(('2pack', 'Drake', 'Jennifer Lopez', 'Megan Nicole'))
years = list(range(2020, 2050))
variada = ["Ruben", 30, 30.4, True, "Texto"]

# print(peliculas)
# print(cantantes)
# print(years)
# print(variada)

# Indices
peliculas[0] = "El Hobbit"

print(peliculas[1])
print(peliculas[-2])
print(cantantes[3:4])
print(peliculas[0:])

# Añadir elementos a una lista
cantantes.append("Dua Lipa")
cantantes.append("Bruno Mars")
print(cantantes)

# Recorrer lista
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n********** LISTADO PELICULAS **********")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")
"""
print("\n********** LISTADO DE CONTACTOS **********")

contactos = [
    [
        'Ruben',
        'rcastillo@raivtech.com'
    ],
    [
        'Luis',
        'luis@raivtech.com'
    ],
    [
        'Alexandra',
        'alexandra@raivtech.com'
    ]
]

print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: ", elemento)
        else:
            print("Email: ", elemento)
    print("\n")