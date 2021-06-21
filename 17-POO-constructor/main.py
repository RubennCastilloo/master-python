from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Chevrolet", "Corsa", 150, 200, 4)
carro3 = Coche("Negro", "Porsche", "GT2RS", 380, 600, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado

carro3 = "Aleatorio"
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

# Visibilidad

print(carro.getPrivado())