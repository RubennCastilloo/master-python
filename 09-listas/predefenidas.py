cantantes = ['Megan Nicole', 'Dua Lipa', 'Bebe Rexha']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Bruno Mars")
print(cantantes)
cantantes.insert(1,"David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("Bebe Rexha")
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("Bruno Mars" in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir un indice
print(cantantes)
print(cantantes.index("Megan Nicole"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)