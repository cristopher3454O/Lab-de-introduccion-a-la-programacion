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



5. # **Pruebas del Sistema**

Se definieron y ejecutaron casos de prueba controlados para validar la resiliencia y el comportamiento dinámico de la solución ante diferentes entradas de datos:

| Caso | Entrada Utilizada | Resultado Esperado | Resultado Obtenido |
| :---- | :---- | :---- | :---- |
| **01\. Control de Acceso Erróneo** | Usuario: admin Password: incorrecto | Rechazo del inicio de sesión, redirección a la raíz y despliegue del mensaje flash de error. | **Validado Correctamente** |
| **02\. Autenticación Exitosa** | Usuario: admin Password: admin2026 | Aceptación de credenciales y redirección transparente hacia la vista "/panel". | **Validado Correctamente** |
| **03\. Renderizado de Habitaciones** | Petición HTTP GET a la ruta "/panel" | Consulta completa a la tabla 'habitaciones' y transmisión de la estructura al renderizador HTML. | **Validado Correctamente** |
| **04\. Automatización de Estatus** | Inserción manual de reserva en habitación ID 104 | Activación del Trigger en SQLite, modificando de forma automática el estatus de la habitación a 'Ocupada'. | **Validado Correctamente** |




6. # **Conclusiones**

Hacer este proyecto fue una experiencia increíble para poner en práctica lo que aprendimos en clase. Nos dimos cuenta de que programar una web con bases de datos requiere mucho orden y una lógica clara para que el usuario no tenga problemas. Uno de los mejores momentos fue cuando decidimos simplificar el modelo de datos uniendo la información del huésped directamente con su reserva; eso nos ahorró muchas complicaciones innecesarias. Al final, este trabajo nos deja claro cómo la tecnología puede transformar un negocio tradicional en algo moderno y eficiente. Fue una ventaja tener un compañero que supiera sobre HTML y CSS porque al hacer la interfaz fue más realista y humano, no dependimos de la IA para hacer la interfaz , lo cual le da más el toca humanizado. En general nos ayudó también a tomar experiencia para el futuro crear nuestros propios programas.

**Mensaje Final estilo Chago UAZ:** “Entenderás, explicarás y codificarás el código sin depender directamente de una inteligencia artificial.” “Registrarás a todos los huéspedes sin depender del papel.”
