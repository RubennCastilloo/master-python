""""
    Diccionario: Un tipo de dato que almacena un conjunto de datos
    en formato Clave > valor.
    Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Ruben",
    "apellidos": "Castillo",
    "web": "raivtech.com"
}

print(persona["nombre"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Ruben',
        'email': 'rcastillo@raivtech.com'
    },
    {
        'nombre': 'Alexandra',
        'email': 'areyes@raivtech.com'
    },
    {
        'nombre': 'Nayelli',
        'email': 'nreyes@raivtech.com'
    }
]

contactos[0]['nombre'] = "Rubencito"
print(contactos[0]['nombre'])
print(contactos)

print("\n Listado de contactos: ")
print("----------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("----------------------")