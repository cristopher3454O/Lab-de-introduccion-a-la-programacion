# Sistema de Inventario y POS: Cristopher

## Descripción del Proyecto

Este sistema de Punto de Venta (POS) y control de inventario fue
desarrollado por Cristopher Alexander Breceda Lerma. Está diseñado para
operar en un entorno de red local, utilizando un dispositivo móvil (como
un Samsung A26) como escáner inalámbrico y una laptop (Linux Mint) como
servidor y panel de gestión en tiempo real.

## Características Principales

-   **Identidad Propia:** Software personalizado para la gestión
    administrativa de productos.
-   **Escaneo Remoto:** Integración de la cámara del celular para leer
    códigos de barras comerciales (EAN-13, Code 128) y códigos QR
    mediante la librería html5-qrcode.
-   **Sincronización en Tiempo Real:** Interfaz de laptop que se
    actualiza automáticamente cada segundo para mostrar el carrito y
    detectar nuevos escaneos.
-   **Registro de Mercancía Dinámico:** Si se detecta un código no
    registrado, el sistema despliega un modal en la laptop para capturar
    Nombre, SKU, Precio y Stock inicial.
-   **Base de Datos:** Almacenamiento local mediante SQLite3 para
    garantizar la persistencia de la información.

## Tecnologías Utilizadas

-   **Backend:** Python 3 con el framework Flask.
-   **Base de Datos:** SQLite3 (archivo .sqlite).
-   **Frontend:** HTML5, CSS3 (Flexbox) y JavaScript (Fetch API).
-   **Hardware/Seguridad:** Implementación de protocolo HTTPS local con
    certificados ad-hoc para habilitar el uso de hardware de cámara en
    navegadores móviles.

## Estructura de Archivos

-   `app.py`: Servidor central y manejo de rutas API.
-   `inventario_db.sqlite`: Archivo de base de datos con la tabla de
    productos.
-   `templates/admin.html`: Panel de administración y visualización del
    carrito.
-   `templates/scanner.html`: Interfaz optimizada para el dispositivo
    móvil.

## Configuración de Seguridad y Red

-   **Firewall:** Se requiere habilitar el puerto 5000 (ej.
    `sudo ufw allow 5000/tcp`).
-   **Permisos de Cámara:** En Chrome Android, se debe configurar la
    bandera "Insecure origins treated as secure" apuntando a la IP de la
    laptop para permitir que la API de la cámara funcione sin un
    certificado SSL firmado por una autoridad externa.

## Resumen Técnico

El sistema Cristopher optimiza la entrada de datos al eliminar la
necesidad de un escáner físico USB. Se ajustó la configuración del
escaneo (FPS y QRBox rectangular) para maximizar la tasa de éxito en la
lectura de empaques comerciales, logrando una herramienta eficiente para
la recepción de mercancía y ventas rápidas.

------------------------------------------------------------------------

**Desarrollador:** Cristopher Alexander Breceda Lerma\
**Institución:** Ingeniería de Software - UAZ
