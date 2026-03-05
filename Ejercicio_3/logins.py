class Login:
    def __init__(self, usuario, contraseña):
        self.usuario= str(usuario)
        self.contraseña=str(contraseña)


    def Usuario(self,usuario):
            usuarioAdmin="Admin"
            while (usuario == "" or usuario != usuarioAdmin or usuario==" "):
                if (usuario == ""):
                    print("Usuario vacio")
                    usuario = str(input("Ingresa un Usuario valido: "))
                elif " "in usuario:
                     print("EL usario no puede tener espacios")
                     usuario = str(input("Ingresa un Usuario valido: "))
                else:
                    print("Usuario no encontrado intenta otra vez")
                    usuario = input("Usuario : ")
        
            print("Usuario encontrado")
            return True

    def Contraseña(self,contraseña):
        intentos=0
        contraseñaAdmin="Admin2026"
        while (contraseña!=contraseñaAdmin and intentos<3):
            largo = len(contraseña) >= 8
            tiene_numero = any(letra.isdigit() for letra in contraseña)
            tiene_letra = any(digito.isalpha() for digito in contraseña)
            if not tiene_numero:
                 print("Al menos un numero")
                 contraseña = str(input("Intenta una contraseña válida: "))
                 continue
            elif  not tiene_letra:
                 print("Al menos una letra")
                 contraseña = str(input("Intenta una contraseña válida: "))
                 continue
            elif not largo:
                 print("minimo 8 caracteres")
                 contraseña = str(input("Intenta una contraseña válida: "))
                 continue

            print(f"Contraseña incorrecta, vuelve a intentarlo intentos restantes {3-intentos}")
            contraseña=str(input("Contraseña: "))
            intentos=intentos+1

            
        if (contraseña==contraseñaAdmin):
                print("Bienvenido")
                return True
        else:
            print("Intentos acabados usuario bloqueado ")


 
 
