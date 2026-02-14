class Ejercicio2:

    # Constructor: guarda el número como entero
    def __init__(self, numero):
        self.numero = int(numero)

    # Método general para convertir a cualquier base
    def convertir(self, base):
        num = self.numero

        if num == 0:
            return "0"

        digitos = "0123456789ABCDEF"
        resultado = ""

        while num > 0:
            residuo = num % base          # Obtiene el residuo
            resultado = digitos[residuo] + resultado
            num = num // base             # División entera

        return resultado

    def binario(self):
        return self.convertir(2)

    def octal(self):
        return self.convertir(8)

    def hexadecimal(self):
        return self.convertir(16)

    # 0 es False, cualquier otro número es True
    def boolean(self):
        return bool(self.numero)


dato = input("Ingresa un número decimal: ")
obj = Ejercicio2(dato)

print("Binario:", obj.binario())
print("Octal:", obj.octal())
print("Hexadecimal:", obj.hexadecimal())
print("Booleano:", obj.boolean())



