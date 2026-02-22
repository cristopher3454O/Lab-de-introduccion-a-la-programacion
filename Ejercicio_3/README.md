# Sistema de Autenticación en Python ejercicio 3

## Descripción General

Este proyecto implementa un sistema básico de autenticación utilizando
Programación Orientada a Objetos en Python. El objetivo principal es
validar un usuario y una contraseña mediante estructuras de control,
validaciones lógicas y control de intentos.

El sistema está compuesto por una clase llamada `Login`, la cual
encapsula la lógica de autenticación y permite organizar el código de
forma estructurada y reutilizable.



## Estructura del Programa

El programa se divide en tres partes principales:

1.  Definición de la clase `Login`
2.  Métodos de validación de usuario y contraseña
3.  Instanciación de la clase y ejecución del flujo principal



## 1. Definición de la Clase

``` python
class Login:
    def __init__(self, usuario, contraseña):
        self.usuario = str(usuario)
        self.contraseña = str(contraseña)
```

### Constructor (`__init__`)

El método constructor se ejecuta automáticamente al crear un objeto de
la clase.

-   `self.usuario`: almacena el usuario recibido y lo convierte a tipo
    string.
-   `self.contraseña`: almacena la contraseña recibida y la convierte a
    tipo string.

El uso de `self` permite que los atributos pertenezcan a la instancia
del objeto.



## 2. Método de Validación de Usuario

``` python
def Usuario(self, usuario):
```

### Lógica Implementada

-   Se define un usuario administrador preestablecido:

``` python
usuarioAdmin = "Admin"
```

-   Se utiliza un ciclo `while` con condición:

``` python
while (usuario == "" or usuario != usuarioAdmin):
```

La condición utiliza el operador lógico `or`, lo que significa que el
ciclo continuará si:

-   El usuario está vacío.
-   El usuario es diferente al registrado.

### Validaciones Internas

Dentro del ciclo se utiliza una estructura condicional `if`:

-   Si el usuario está vacío:
    -   Se muestra el mensaje "Usuario vacío".
    -   Se solicita nuevamente el ingreso.
-   Si el usuario no coincide con el administrador:
    -   Se muestra el mensaje "Usuario no encontrado".
    -   Se solicita nuevamente el ingreso.

El ciclo termina únicamente cuando el usuario coincide con `"Admin"`.

Al finalizar correctamente:

``` python
print("Usuario encontrado")
return True
```

Se retorna `True`, lo cual permite continuar con la validación de la
contraseña.



## 3. Método de Validación de Contraseña

``` python
def Contraseña(self, contraseña):
```

### Variables Iniciales

``` python
intentos = 0
contraseñaAdmin = "Admin2026"
```

-   `intentos`: controla el número de intentos permitidos.
-   `contraseñaAdmin`: contraseña registrada en el sistema.

### Condición del Ciclo

``` python
while (contraseña != contraseñaAdmin and intentos < 3):
```

El ciclo se ejecuta mientras:

-   La contraseña no coincida.
-   Los intentos sean menores a 3.

### Validaciones de Seguridad

Antes de descontar intentos, se valida el formato:

``` python
largo = len(contraseña) >= 8
tiene_numero = any(letra.isdigit() for letra in contraseña)
tiene_letra = any(digito.isalpha() for digito in contraseña)
```

Se verifica que:

-   Tenga al menos 8 caracteres.
-   Contenga al menos un número.
-   Contenga al menos una letra.

Si no cumple estas condiciones:

``` python
if not (largo and tiene_numero and tiene_letra):
```

Se solicita nuevamente la contraseña sin descontar intentos.

Si cumple el formato pero no coincide con la registrada:

-   Se descuenta un intento.
-   Se informa cuántos intentos restan.

### Finalización

Si la contraseña coincide:

``` python
print("Bienvenido")
```

Si se agotan los intentos:

``` python
print("Intentos acabados")
```



## 4. Flujo Principal del Programa

``` python
usuario = str(input("Ingresa tu Usuario: "))
obj = Login(usuario, "")
```

Se solicita el usuario y se instancia la clase.

Posteriormente:

``` python
resultadoUsuario = obj.Usuario(usuario)
```

Si el método retorna `True`:

``` python
if (resultadoUsuario == True):
    contraseña = str(input("Ingrese la contraseña: "))
    obj.Contraseña(contraseña)
```

Solo en ese caso se procede a validar la contraseña.

Esto garantiza que la contraseña no sea solicitada hasta que el usuario
sea correcto.



## Conceptos Aplicados

-   Programación Orientada a Objetos
-   Uso de clases e instancias
-   Método constructor
-   Estructuras de control (`while`, `if`)
-   Operadores lógicos (`and`, `or`, `not`)
-   Validación de cadenas (`len`, `isdigit`, `isalpha`)
-   Control de intentos



## Conclusión

El programa implementa un sistema de autenticación estructurado y
organizado mediante el uso de clases. Se aplican validaciones tanto de
contenido como de coincidencia, además de un control de intentos que
limita accesos incorrectos.

El flujo lógico garantiza que primero se valide el usuario y
posteriormente la contraseña, manteniendo una secuencia ordenada y
controlada.
