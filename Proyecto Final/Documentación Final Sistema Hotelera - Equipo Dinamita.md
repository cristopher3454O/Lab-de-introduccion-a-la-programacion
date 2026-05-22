# **UNIVERSIDAD AUTÓNOMA DE ZACATECAS**

Unidad Académica de Ingeniería Eléctrica

**Programa Académico:** Ingeniería de Software **Asignatura: Introducción a la Programación Docente:** Ing. Santiago Esparza Guerrero (ChagoUaz)

**Integrantes del Equipo:** Dean Yeshua Guerrero Rivera, Cristopher Alexander Breceda Lerma, Renata Ramos Piña y Alfredo de Robles Noriega

**Líder del Proyecto:** Cristopher Alexander Breceda Lerma

**Fecha de entrega:** 19 de Mayo de 2026

# **TRABAJO FINAL: SISTEMA DE GESTIÓN HOTELERA**

2. **Descripción del Programa**

El programa es un sistema software que sirve para satisfacer las necesidades de reserva de habitaciones de un hotel, para llevar un control de los huéspedes y guardar los datos en tiempo real. Además de contar con un mini sistema de facturación. Creado casi 100% por humanos (apoyo mínimo en IA) y usando los siguientes lenguajes: HTML, CSS, algo de JavaScript, Python y SQLite

## **Requerimientos Funcionales**

Para que todo funcione como debe, creamos un sistema seguro donde el administrador entra con su propia cuenta. Una vez dentro, se encuentra con un panel muy visual que muestra cada habitación y permite filtrarlas rápidamente para ver cuáles están ocupadas o disponibles. Además, registrar una nueva reserva es súper fácil: solo se vinculan los datos del cliente y listo.

* Registrar huéspedes en el sistema.

  * Consultar la información de los huéspedes almacenados.

  * Actualizar datos de los huéspedes cuando sea necesario.

  * Eliminar registros de huéspedes.

  * Registrar habitaciones disponibles del hotel.

  * Mostrar el estado de las habitaciones (ocupada, disponible).

  * Permitir la reserva de habitaciones.

  * Guardar la información de las reservas en tiempo real.

  * Consultar reservas existentes.

  * Cancelar o modificar reservas.

  * Generar facturas básicas de hospedaje.

  * Calcular costos de hospedaje.

  * Almacenar la información en una base de datos SQLite.

  * Mostrar información organizada y fácil de usar para el usuario.

  * Mantener actualizados los datos del hotel en tiempo real.

## **Requerimientos No Funcionales**

Por detrás, usamos herramientas modernas y confiables. El motor de todo es Flask (de Python), mientras que la información se guarda de forma segura en una base de datos SQLite. Lo mejor es que la base de datos es "inteligente": incluimos disparadores que actualizan los

estados automáticamente, y organizamos el código en piezas llamadas Blueprints para que sea fácil de mantener a futuro.

* l sistema debe tener una interfaz sencilla, intuitiva y fácil de usar.

  * El sistema debe responder de manera rápida a las consultas y registros.

  * La información almacenada debe mantenerse segura y protegida.

  * El sistema debe garantizar la integridad de los datos guardados en SQLite.

3. # **Problema a Resolver**

En hoteles pequeños, es común que todavía se use papel o Excel para llevar las cuentas, lo que causa problemas como vender dos veces la misma habitación o no saber qué control llevar en habitación. Con nuestro sistema, el flujo de trabajo es claro: el administrador ingresa los datos del huésped y el cuarto (entradas), el sistema valida todo y actualiza el inventario (proceso), y finalmente entrega un panel interactivo con todo al día (salidas).

4. # **Herramientas Utilizadas**

Lenguajes de programación: Python 3 y Flask como los pilares principales. HTML, CSS, JavaScript, DB Browser.

Entorno de Desarrollo: Visual Studio CODE Herramientas de apoyo: Flask, IA (Gemini)

5. # **Programa (Código Fuente)**

A continuación se adjunta el código fuente completo correspondiente a cada cosa:

[**Login.py**](http://login.py/)**:** from flask import request

**Panel Principal:** import sqlite3

conexion.row\_factory \= sqlite3.Row cursor \= conexion.cursor()  
*\# TOOODAS LAS HABITACIONESS*

cursor.execute(

"SELECT \* FROM habitaciones"

)

habitaciones \= cursor.fetchall()

*\# HABITACIONES ACTUALMENTE DISPONIBLES*

cursor.execute("""

SELECT \* FROM habitaciones WHERE estatus \= 'Disponible' """)  
disponibles \= cursor.fetchall()

*\# OCUPADAS*

cursor.execute("""

SELECT \* FROM habitaciones WHERE estatus \= 'Ocupada' """)  
ocupadas \= cursor.fetchall()

*\# LIMPIEZA*

cursor.execute("""

SELECT \* FROM habitaciones WHERE estatus \= 'Limpieza' """)  
limpieza \= cursor.fetchall()

[**App.py**](http://app.py/)**:**

*import sqlite3 import os*

*from flask import Flask, render\_template, request, redirect, flash, url\_for from routes.panel\_central import panel\_principal*

*from routes.checkin\_modulo import checkin\_bp from routes.directorio\_modulo import directorio\_bp from routes.checkout\_modulo import checkout\_bp*

*base\_dir \= os.path.abspath(os.path.dirname(* *file* *)) db\_path \= os.path.join(base\_dir, 'hotel.db')*

*app \= Flask(*  *name*  *)*

*app.secret\_key \= 'mi\_llave\_secreta\_para\_el\_hotel'*

*app.register\_blueprint(checkin\_bp) app.register\_blueprint(directorio\_bp) app.register\_blueprint(checkout\_bp)*

*USUARIOCORRECTO \= "admin" CONTRASENA\_CORRECTA \= "admin2026"*

*@app.route('/') def index():*

*return render\_template('index.html')*

*@app.route('/login', methods=\['POST'\]) def login():*

*usuario \= request.form.get("username") password \= request.form.get("password")*

*if usuario \== USUARIOCORRECTO and password \== CONTRASENA\_CORRECTA: return redirect("/panel")*

*else:*

*flash('Usuario o contraseña incorrectos. Intenta de nuevo.', 'error') return redirect('/')*

*@app.route('/panel')*

*def render\_panel\_principal():*

*conn \= sqlite3.connect(db\_path) conn.row\_factory \= sqlite3.Row cursor \= conn.cursor()*

*cursor.execute("SELECT id, tipo, estatus FROM habitaciones") lista\_habitaciones \= cursor.fetchall()*

*print(f"DEBUG: Encontré {len(lista\_habitaciones)} habitaciones")*

*conn.close()*

*return panel\_principal(datos\_habitaciones=lista\_habitaciones)*

*if*   *name*  *\== '*  *main*  *':*

*app.run(debug=True)*

*Asimismo, se detalla la estructura lógica del esquema DDL ejecutado en el motor relacional SQLite para el soporte de datos corporativos: CREATE TABLE IF NOT EXISTS habitaciones (*

*id INTEGER PRIMARY KEY, tipo TEXT NOT NULL,*

*estatus TEXT NOT NULL CHECK(estatus IN ('Disponible', 'Ocupada', 'Limpieza')), precio\_noche REAL NOT NULL*

*);*

*CREATE TABLE IF NOT EXISTS reservaciones ( id\_reserva INTEGER PRIMARY KEY AUTOINCREMENT,*

*nombre TEXT NOT NULL, apellido\_p TEXT NOT NULL, apellido\_m TEXT NOT NULL, telefono TEXT,*

*id\_habitacion INTEGER NOT NULL, fecha\_entrada TEXT NOT NULL, fecha\_salida TEXT NOT NULL, total\_pagar REAL,*

*pagada INTEGER DEFAULT 0 CHECK(pagada IN (0, 1)),*

*FOREIGN KEY(id\_habitacion) REFERENCES habitaciones(id) ON DELETE RESTRICT*

*);*

*CREATE TRIGGER IF NOT EXISTS actualizar\_estatus\_habitacion AFTER INSERT ON reservaciones*

*BEGIN*

*UPDATE habitaciones SET estatus \= 'Ocupada'*

*WHERE id \= NEW.id\_habitacion; END;*

Asimismo, se detalla la estructura lógica del esquema DDL ejecutado en el motor relacional SQLite para el soporte de datos corporativos:

CREATE TABLE IF NOT EXISTS habitaciones (

	id INTEGER PRIMARY KEY,

	tipo TEXT NOT NULL,

	estatus TEXT NOT NULL CHECK(estatus IN ('Disponible', 'Ocupada', 'Limpieza')),

	precio\_noche REAL NOT NULL

);

CREATE TABLE IF NOT EXISTS reservaciones (

	id\_reserva INTEGER PRIMARY KEY AUTOINCREMENT,

	nombre TEXT NOT NULL,

	apellido\_p TEXT NOT NULL,

	apellido\_m TEXT NOT NULL,

	telefono TEXT,

	id\_habitacion INTEGER NOT NULL,

	fecha\_entrada TEXT NOT NULL,

	fecha\_salida TEXT NOT NULL,

	total\_pagar REAL,

	pagada INTEGER DEFAULT 0 CHECK(pagada IN (0, 1)),

	FOREIGN KEY(id\_habitacion) REFERENCES habitaciones(id) ON DELETE RESTRICT

);

CREATE TRIGGER IF NOT EXISTS actualizar\_estatus\_habitacion AFTER INSERT ON reservaciones

BEGIN

	UPDATE habitaciones

	SET estatus \= 'Ocupada'

	WHERE id \= NEW.id\_habitacion; END;

Asimismo, se detalla la estructura lógica del esquema DDL ejecutado en el motor relacional SQLite para el soporte de datos corporativos:

CREATE TABLE IF NOT EXISTS habitaciones (

  id INTEGER PRIMARY KEY,

  tipo TEXT NOT NULL,

  estatus TEXT NOT NULL CHECK(estatus IN ('Disponible', 'Ocupada', 'Limpieza')),

  precio\_noche REAL NOT NULL

);

CREATE TABLE IF NOT EXISTS reservaciones (

  id\_reserva INTEGER PRIMARY KEY AUTOINCREMENT,

  nombre TEXT NOT NULL,

  apellido\_p TEXT NOT NULL,

  apellido\_m TEXT NOT NULL,

  telefono TEXT,

  id\_habitacion INTEGER NOT NULL,

  fecha\_entrada TEXT NOT NULL,

  fecha\_salida TEXT NOT NULL,

  total\_pagar REAL,

  pagada INTEGER DEFAULT 0 CHECK(pagada IN (0, 1)),

  FOREIGN KEY(id\_habitacion) REFERENCES habitaciones(id) ON DELETE RESTRICT

);

CREATE TRIGGER IF NOT EXISTS actualizar\_estatus\_habitacion AFTER INSERT ON reservaciones

BEGIN

  UPDATE habitaciones

  SET estatus \= 'Ocupada'

 WHERE id \= NEW.id\_habitacion; END;

**Prompt utilizado:** Corrige el siguiente codigo de una manera limpia y señala los errores para poder elegir

6. # **Pruebas del Sistema**

Se definieron y ejecutaron casos de prueba controlados para validar la resiliencia y el comportamiento dinámico de la solución ante diferentes entradas de datos:

| Caso | Entrada Utilizada | Resultado Esperado | Resultado Obtenido |
| :---- | :---- | :---- | :---- |
| **01\. Control de Acceso Erróneo** | Usuario: admin Password: incorrecto | Rechazo del inicio de sesión, redirección a la raíz y despliegue del mensaje flash de error. | **Validado Correctamente** |
| **02\. Autenticación Exitosa** | Usuario: admin Password: admin2026 | Aceptación de credenciales y redirección transparente hacia la vista "/panel". | **Validado Correctamente** |
| **03\. Renderizado de Habitaciones** | Petición HTTP GET a la ruta "/panel" | Consulta completa a la tabla 'habitaciones' y transmisión de la estructura al renderizador HTML. | **Validado Correctamente** |
| **04\. Automatización de Estatus** | Inserción manual de reserva en habitación ID 104 | Activación del Trigger en SQLite, modificando de forma automática el estatus de la habitación a 'Ocupada'. | **Validado Correctamente** |

7. # **Evidencia Visual (Pantallas)**

Inicio de sesión:

Panel principal:

Check in:

Directorio:

Checkout y facturación:

Vista cuando está ocupada una habitación:

8. # **Conclusiones**

Hacer este proyecto fue una experiencia increíble para poner en práctica lo que aprendimos en clase. Nos dimos cuenta de que programar una web con bases de datos requiere mucho orden y una lógica clara para que el usuario no tenga problemas. Uno de los mejores momentos fue cuando decidimos simplificar el modelo de datos uniendo la información del huésped directamente con su reserva; eso nos ahorró muchas complicaciones innecesarias. Al final, este trabajo nos deja claro cómo la tecnología puede transformar un negocio tradicional en algo moderno y eficiente. Fue una ventaja tener un compañero que supiera sobre HTML y CSS porque al hacer la interfaz fue más realista y humano, no dependimos de la IA para hacer la interfaz , lo cual le da más el toca humanizado. En general nos ayudó también a tomar experiencia para el futuro crear nuestros propios programas.

**Mensaje Final estilo Chago UAZ:** “Entenderás, explicarás y codificarás el código sin depender directamente de una inteligencia artificial.” “Registrarás a todos los huéspedes sin depender del papel.”