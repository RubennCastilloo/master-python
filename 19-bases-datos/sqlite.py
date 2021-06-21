# Importar modulo
import sqlite3

# Conexión
conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos("
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255), 
    descripcion TEXT, 
    precio INT(255)
");
""")

# Guardar cambios
conexion.commit()

# Insertar datos
# cursor.execute("INSERT INTO productos VALUES( null, 'Segundo Producto', 'Descripcion de mi producto', '550' )")
# conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen pc", 700),
    ("iPhone", "Buen teléfono", 600),
    ("MacBook Pro", "Funcionando correctamente", 1200),
    ("iPad Pro", "Buena tableta", 700)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 600")

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 650")
productos = cursor.fetchall()

for producto in productos:
    print("ID:", producto[0])
    print("Titulo:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print("Primer producto:", producto)


# Cerrar la conexión
conexion.close()