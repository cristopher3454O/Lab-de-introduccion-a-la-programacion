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

    def Clasificacion_numeros(self):
          opcion=0
          while True:
               num=int(input("Ingresa el numero que quieres clasificar, solo numeros enteros "))
               if (num<0):
                    print("Tu numero es negativo")
               elif (num==0):
                    print("Tu numero es Cero")
               elif (num>0):
                    if (num%2==0):
                         print("Tu numero es positivo y es par ")
                    else:
                         print("Tu numero es positvo y es impar ")
          
               opcion=int(input("1.Salir a menún principal "
               "2. Continuar "))
               if (opcion==1):
                    return False


    def Menu(self):
         while True:
            print("MENU DE OPCIONES ")
            print("1.Clasificar número (positivo/negativo/cero +par/inpar)")
            print("2.Categoria de edad y permiso (reglas de negocio)")
            print("3.Calcular tarifa final (descuentos multiples)")
            print("4.Cerrar sesión (volver login )")
            print("5.Salir")
            opcion=int(input("Selecciona una opción: "))

            match opcion:
              case 1:
                   obj.Clasificacion_numeros()
              case 2:
                   obj.Reglas_negocio()
              case 3:
                   obj.Calcular_Tarifa()
              case 4:
                   print("Cerrando sesion")  
                   return True                
              case 5:
                   print("Cerrando programa ")
                   return False
              case _:
                   print("Opcion no valida")
            
while True:
    usuario=str(input("Ingresa tu Usuario: "))
    obj=Login(usuario, "")

    resultadoUsuario=obj.Usuario(usuario)
    if (resultadoUsuario == True):
        contraseña=str(input("Ingrese la contraseña: "))
        if obj.Contraseña(contraseña)==True:
                regresar=obj.Menu()
                if regresar==True:
                     continue
                elif regresar==False:
                     break
