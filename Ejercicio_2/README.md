# Laboratorio de Introducción a la Programación

## Ejercicio 2: Conversor de Número Decimal a Múltiples Bases

Este documento describe el desarrollo de un programa en Python que
permite convertir un número decimal a distintos sistemas numéricos
utilizando programación orientada a objetos.


## 1. Objetivo del Ejercicio

Desarrollar una clase en Python que permita convertir un número decimal
a:

-   Binario (Base 2)\
-   Octal (Base 8)\
-   Hexadecimal (Base 16)\
-   Booleano

Aplicando estructuras de control, operadores matemáticos y reutilización
de código mediante métodos.


## 2. Estructura General del Programa

El programa está compuesto por:

-   Una clase llamada `Ejercicio2`\
-   Un método constructor `__init__`\
-   Un método general de conversión `convertir(base)`\
-   Métodos específicos para cada base\
-   Entrada de datos por teclado\
-   Impresión de resultados en consola



## 3. Definición de la Clase

``` python
class Ejercicio2:
```

La clase permite organizar el código y encapsular tanto el dato como los
métodos de conversión.



## 4. Método Constructor

``` python
def __init__(self, numero):
    self.numero = int(numero)
```

### Función del constructor:

-   Recibe el número ingresado por el usuario.\
-   Lo convierte a tipo entero.\
-   Lo almacena en el atributo `self.numero`.

El uso de `self` indica que el valor pertenece a la instancia del
objeto.



## 5. Método General de Conversión

``` python
def convertir(self, base):
```

Este método realiza la conversión del número decimal a la base indicada.

### Funcionamiento del algoritmo:

1.  Se copia el valor original en una variable temporal `num`.\
2.  Si el número es 0, retorna "0".\
3.  Se define una tabla de símbolos:

``` python
digitos = "0123456789ABCDEF"
```

Esta cadena permite representar valores hasta base 16.

4.  Se ejecuta un ciclo `while`:

``` python
while num > 0:
```

Mientras `num` sea mayor que 0:

-   Se obtiene el residuo usando `%`.\
-   Se obtiene el símbolo correspondiente desde `digitos`.\
-   Se concatena al inicio del resultado.\
-   Se divide el número usando división entera `//`.

### Operadores utilizados:

-   `num % base` → Obtiene el residuo de la división.\
-   `num // base` → Realiza división entera (descarta decimales).

El proceso se repite hasta que el número se reduce a 0.


## 6. Métodos Específicos por Base

Cada sistema numérico tiene su propio método, pero todos reutilizan el
método general:

``` python
def binario(self):
    return self.convertir(2)

def octal(self):
    return self.convertir(8)

def hexadecimal(self):
    return self.convertir(16)
```

Esto evita duplicación de código y mejora la estructura del programa.



## 7. Conversión a Booleano

``` python
def boolean(self):
    return bool(self.numero)
```

En Python:

-   0 → False\
-   Cualquier otro número → True



## 8. Ejecución del Programa

``` python
dato = input("Ingresa un número decimal: ")
obj = Ejercicio2(dato)

print("Binario:", obj.binario())
print("Octal:", obj.octal())
print("Hexadecimal:", obj.hexadecimal())
print("Booleano:", obj.boolean())
```



## 9. Ejemplo de Ejecución

   ![Ubicación de la carpeta](<assets/ejemplo.png>)


## 10. Conclusión

En este ejercicio se aplicaron conceptos fundamentales de programación
orientada a objetos en Python.

Se implementó un algoritmo general basado en divisiones sucesivas y
obtención de residuos, permitiendo convertir un número decimal a
distintas bases sin repetir código.

El uso de un método reutilizable mejora la organización, claridad y
escalabilidad del programa.
