class Ejercicios:
    def __init__(self, opcion):
        self.opcion = int(opcion)

    def Ejercicio1(self):
        while True:
            texto = str(input("Dame la palabra a repetir 10 veces: "))
            for i in range(10): 
                print(texto)
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False


    def Ejercicio2(self):
        while True:
            años = int(input("¿Cuántos años tienes ?: "))
            print("Años cumplidos ")
            for i in range(1, años + 1):
                if i < años:
                    print("Años:", i, end=", ")
                else:
                    print(f"Años {i}")
            print()
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False


    def Ejercicio3(self):
        while True:
            inicio=int(input("Numero a terminar : "))
            for i in range(inicio+1):
                if i%2!=0:
                    if i+2<=inicio:
                        print(i, end=", ")
                    else:
                        print(i)
            print()
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio4(self):
        while True:
            inicio=int(input("Dame el numero a iniciar: "))
            while inicio>=0:
                print(inicio, end=", ")
                inicio=inicio-1
                if inicio==0:
                    print("0")
                    break
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio5(self):
        while True:
            cantidad_invertir=float(input("Dame la cantidad a invertir : "))
            interes_anual=float(input("Interes Anual: "))
            interes_anual=interes_anual*0.01
            años=int(input("Años de la inversión: "))

            Capital_total=cantidad_invertir*(1+interes_anual)**años
            ganacia=Capital_total-cantidad_invertir

            capital_aux = cantidad_invertir
            for i in range(años):
                ganacia_este_año = capital_aux * interes_anual
                capital_aux = capital_aux + ganacia_este_año
                print(f"Ganancias el {i+1} año: {ganacia_este_año:.2f}")

            print(f"Tu capital es: {cantidad_invertir} con un interes anual de {interes_anual} por {años} años tu ganacia neta es {ganacia:.2f}")
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio6(Self):
        while True:
            num=int(input("Altura de la piramide: "))
            for i in range(num):
                print("*" * (i + 1))
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio7(self):
        while True:
            dat=int(input("Elige la tabla que quieres ver 1-10: "))
            print(f"Tabla del {dat}")
            for i in range(10):
                i=i+1
                mult=i*dat
                print(f"{dat} x {i}")
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio8(self):
        while True:
            num=int(input("Dame un numero: "))
            for i in range(1, num+1):
                for j in range(2*i-1,0,-2):
                    print(j, end=", ")
                print()
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False
            
    def Ejercicio9(self):
        while True:
            contraseña=str(input("Dame la contraseña a crear: "))
            contraseñaNew=str(input("Ingresa tu contraseña creada: "))
            while contraseñaNew!=contraseña:
                    contraseñaNew=str(input("CONTRASEÑA INCORRECTA INTENTA DE NUEVO: "))
            print("CONTRASEÑA CORRECTA")
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio10(self):
        while True:
            print("Es primo o no es primo? ")
            num=int(input("Ingresa un número entero: "))
            if num%2!=0:
                print(f"Tu numero es primo {num}")
            else:
                print(f"Tu numero no es primo {num}")
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

    def Ejercicio11(self):
        while True:
            palabra=str(input("Introduce una palabra: "))
            for i in range(len(palabra) - 1, -1, -1):
                print(palabra[i], end=", ")
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False

        
    def Ejercicio12(self):
        while True:
            palabra=str(input("Dame una palabra: "))
            letra=str(input("Dame la letra a contar: "))
            contador=palabra.count(letra)
            print(f"La letra {letra} aparece {contador} veces en la frase :) ")
            opc=int(input("1.REINICIAR 2.SALIR MENÚ: "))
            if opc==2:
                return False
            
    def Ejercicio13(self):
        dat=str(input())
        while dat!="salir":
            dat=str(input())

        print("SALISTE")


while True:
    print("""
    --- MENÚ DE EJERCICIOS ---
    1. Repetir palabra (10x)
    2. Contador de edad
    3. Impares hasta n
    4. Cuenta regresiva
    5. Cálculo de inversión anual
    6. Triángulo de asteriscos (*)
    7. Tablas de multiplicar (1-10)
    8. Triángulo de números impares
    9. Validación de contraseña
    10. Verificador de números primos
    11. Palabra a la inversa
    12. Contador de letras en frase
    13. Eco (Escribir "salir" para terminar)
    """)

    
    opcion = int(input("Elige una opción: ")) 
    

        
    obj = Ejercicios(opcion)

    def Menu():
        match obj.opcion:
            case 1:
                obj.Ejercicio1()
            case 2:
                obj.Ejercicio2()
            case 3:
                obj.Ejercicio3()
            case 4:
                obj.Ejercicio4()
            case 5:
                obj.Ejercicio5()
            case 6:
                obj.Ejercicio6()
            case 7:
                obj.Ejercicio7()
            case 8:
                obj.Ejercicio8()
            case 9:
                obj.Ejercicio9()
            case 10:
                obj.Ejercicio10()
            case 11:
                obj.Ejercicio11()
            case 12:
                obj.Ejercicio12()
            case 13:
                obj.Ejercicio13()
            case _:
                print("Error")

    Menu()