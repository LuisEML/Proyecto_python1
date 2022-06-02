import usuarios.usuario as modelo

class Acciones:
    def registro(self):
        print("Se procedera a realizar tu registro en el sistema..")
        
        nombre = input("Cual es tu nombre?:")
        apellidos = input("Cuales son tus apellidos?:")
        email = input("Introduce tu email?:")
        password = input("Introduce tu contraseña?:")
        
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")    
    
    
    def login(self):
        print("Indentificate en el sistema")
        try:
            email = input("Introduce tu email:")
            password = input("introduce tu contraseña:")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido  {login[1]}, te has registrado {login[5]} en el sistema")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("\n Login incorrecto intentalo mas tarde ")
    def proximasAcciones(self,usuario):
        print("""Acciones disponibles
              1-Crear nota (nota)
              2-Mostrar nota (mostrar)
              3-Eliminar nota (eliminar)
              4-Salir (salir)
              
            """)
        
        accion = input("Que quieres hacer?")
        if accion == "1":
            print("Vamos a crear una nota")
            self.proximasAcciones(usuario)
        elif accion == "2":
            print("Vamos a mostrar una nota")
            self.proximasAcciones(usuario)
        elif accion == "3":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "4":
            exit()
            
           