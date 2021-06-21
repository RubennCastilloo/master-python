
import getpass
import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nVamos a registrarte en el sistema")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Cual es tu email?")
        password = getpass.getpass("Define una contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\n{registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\nIdentificate en el sistema")
        
        try:
            email = input("Introduce tu email: ")
            password = getpass.getpass("Introduce una contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("Login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        -Crear nota (c)
        -Mostrar tus notas (m)
        -Eliminar nota (e)
        -Salir (s)
        """)
        
        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion.lower() == 'c':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == "m":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == 'e':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == 's':
            print(f"Hasta pronto {usuario[1]}")
            exit()
        else:
            print("Seleccionaste una opción incorrecta")
            self.proximasAcciones(usuario)