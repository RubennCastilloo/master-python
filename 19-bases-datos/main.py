import mysql.connector

# Conexión a la base de datos

database = mysql.connector.connect(
    host="127.0.0.1",
    port="8888",
    user="root",
    passwd="root",
    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', # Para conectar a la base de datos en MacOS o Linux
    database="master_python"
)

# ¿Como saber si la conexión es correcta?
# print(database)

cursor = database.cursor(buffered=True) # Parametro para que no falle el código al hacer varias consultas a la BD

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# cursor.execute("SHOW DATABASES")

# for bd in cursor:
#     print(bd)

# Crear tablas
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vehiculos (
id int(10) AUTO_INCREMENT NOT NULL,
marca varchar(40) NOT NULL,
modelo varchar(40) NOT NULL,
precio float(10,2) NOT NULL,
CONSTRAINT pk_vehiculo PRIMARY KEY(id) 
)
""")

# cursor.execute("SHOW TABLES")

# for table in cursor:
#     print(table)

# cursor.execute("INSERT INTO vehiculos VALUES(NULL, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Chevrolet', 'Corsa', 2000),
    ('Mercedes', 'Clase C', 35000),
]

# Insertar varios datos
# cursor.executemany("INSERT INTO vehiculos VALUES (NULL, %s, %s, %s)", coches)
database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result = cursor.fetchall()

print("----- Todos mis coches -----")
for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()

print(coche)

# Borrar registros

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "borrados!!")

# Actualizar registros

cursor.execute("UPDATE vehiculos SET modelo = 'León' WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "actualizados!!")