# Laboratorio de Introducción a la Programación

## Ejercicio 1: Creación del Entorno Virtual y Configuración

Este documento detalla el proceso para configurar un entorno de desarrollo profesional utilizando Python, Visual Studio Code y entornos virtuales.

---

### 1. Instalación del Entorno de Desarrollo (IDE)
Antes de comenzar, es necesario contar con un editor de código. En este curso utilizaremos **Visual Studio Code**.

* **Descarga:** Puedes obtenerlo en [code.visualstudio.com](https://code.visualstudio.com/).
* **Instalación:** El proceso toma aproximadamente 10 minutos. Al iniciar, acepta todos los permisos y recomendaciones en la ventana de bienvenida para asegurar un funcionamiento óptimo.

### 2. Organización de Archivos
La organización es clave en la programación. Crearemos una estructura de carpetas local que luego se sincronizará con GitHub.

* Crea una carpeta llamada `Lab_de_introduccion_a_la_programacion` en tu directorio de **Documentos**.
   ![Ubicación de la carpeta](<assets/Carpeta en documentos.png>)

### 3. Apertura del Proyecto en VS Code
Para comenzar a trabajar en la carpeta creada:
1. Ve a la barra superior y selecciona **File**.
   ![Menú File](assets/file.png)
2. Haz clic en **Open Folder**.
   ![Open Folder](<assets/open folder.png>)
3. Selecciona la carpeta de la materia y presiona **Enter** para abrirla.
   ![Carpeta abierta](<assets/Carpeta en documentos.png>)

---

### 4. Creación y Activación del Entorno Virtual (Venv)
El entorno virtual permite instalar librerías (como NumPy) sin afectar a otros proyectos del sistema.

1. Abre la terminal integrada: Ve a **View** > **Terminal**.
   ![Menú View](assets/view.png) ![Opción Terminal](assets/terminal.png)
2. Verás la consola en la parte inferior.
   ![Terminal abierta](<assets/terminal 2.png>)
3. **Creación:** Ejecuta el siguiente comando para crear el entorno (llamado `venv` por convención):

    ```
   python3 -m venv venv
    
    ```
   ![Creación de venv](<assets/comando1.png>)
   *Se creará una subcarpeta llamada `venv` en tu proyecto.* ![Carpeta venv](<assets/carpeta venv.png>)

4. **Activación:** Para empezar a usarlo, ejecútalo con:
   ```
   source venv/bin/activate
   ```
   ![Comando de activación](<assets/activacion entorno virtua.png>)
   *Sabrás que está activo porque aparecerá `(venv)` al inicio de tu línea de comandos.* ![Indicador venv](<assets/activacion correcta.png>)

---

### 5. Desarrollo del Primer Programa
Crearemos nuestro primer script de Python para probar la instalación.

1. Haz clic en el icono de **New File** y nombra el archivo como `ejercicio1.py`.
   ![Crear archivo](<assets/archivo nuevo.png>) ![Nombre del archivo](assets/ejercicio1py.png)
2. **Instalación de Librerías:** En la terminal activa, instala la librería **NumPy** para manejo de arrays:
   ```
   pip install numpy 
   ```
   ![Instalación de numpy](<assets/instalacion libreria numpy.png>)

3. **Código de Prueba:** Copia y pega el siguiente código dentro de `ejercicio1.py`:

    ```python
    import numpy as np

    # Creamos un array sencillo 
    numeros = np.array([1, 2, 3, 4])

    # Imprimimos el resultado
    print(numeros)

---

### 6. Conclusión y Resumen de Aprendizaje

En esta primera práctica logramos establecer un flujo de trabajo profesional que garantiza que nuestro código sea organizado, reproducible y fácil de compartir. 

#### **¿Por qué hicimos todo esto?**
1. **VS Code:** Nos da las herramientas necesarias para escribir código de forma eficiente.
2. **Entornos Virtuales (venv):** Evitan conflictos entre diferentes proyectos. Si mañana necesitamos una versión distinta de una librería, no romperemos lo que hicimos hoy.
3. **NumPy:** Es la base para el manejo de datos en Python, permitiéndonos usar **arrays** que son mucho más potentes que las listas normales.

#### **Tabla rápida de comandos utilizados:**

| Acción | Comando en Terminal |
| :--- | :--- |
| **Crear entorno** | `python3 -m venv venv` |
| **Activar entorno** | `source venv/bin/activate` |
| **Instalar librerías** | `pip install numpy` |
| **Ejecutar programa** | `python ejercicio1.py` |

> **Nota final:** Recuerda siempre verificar que el prefijo `(venv)` aparezca en tu terminal antes de empezar a programar o instalar nuevas librerías.