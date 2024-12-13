# Proyecto de Gestión de Archivos ZIP para Genexus

Este proyecto proporciona un conjunto de scripts en Python para manejar la extracción de archivos ZIP y la instalación de Genexus. El script permite al usuario seleccionar archivos y carpetas, desbloquear archivos y ejecutar un instalador.

## Archivos del Proyecto

- **main.py**: El archivo principal que gestiona la extracción de archivos ZIP y la ejecución del instalador.
- **run_genexus.bat**: Un archivo por lotes que se ejecuta para iniciar la instalación de Genexus.
- **SyncBuild.py**: Un módulo que contiene funciones para procesar y manejar archivos ZIP.

## Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

1. **Python**: Necesitas tener Python 3.x instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

   Para verificar si Python está instalado, puedes ejecutar este comando en la terminal asegurate de tener la variable de ambiente:

   python --version

2. **Pip**: Pip es el gestor de paquetes de Python. Por lo general, se incluye con la instalación de Python. Puedes verificar su instalación con:

   pip --version

3. **Bibliotecas necesarias**: Este proyecto utiliza la biblioteca `tqdm` para mostrar el progreso de la extracción. Instala la biblioteca ejecutando:

   pip install tqdm

4. **Streams.exe**: Necesitarás la herramienta `streams.exe` para desbloquear archivos. Asegúrate de que esté disponible en `C:\Tools\streams.exe`. Puedes descargarla desde [Sysinternals](https://docs.microsoft.com/en-us/sysinternals/downloads/streams).

## Estructura del Proyecto

Asegúrate de que tu proyecto tenga la siguiente estructura de archivos:

## Uso

1. **Ejecuta el script**: Abre tu terminal o línea de comandos y navega hasta el directorio donde está ubicado `main.py`. Luego ejecuta el siguiente comando:

   python main.py

2. **Selecciona la carpeta de extracción**: El script te pedirá que selecciones la carpeta donde deseas extraer los archivos. Puedes elegir una de las carpetas listadas o ingresar una ruta manualmente.

3. **Selecciona el archivo a extraer**: El script buscará archivos que coincidan con el criterio que ingresaste. Selecciona el número correspondiente al archivo que deseas extraer.

4. **Ejecución del instalador**: Una vez extraído, el script creará un archivo por lotes (`run_genexus.bat`) en la carpeta de extracción y lo ejecutará con privilegios de administrador para instalar Genexus.

## Notas Adicionales

- **Errores**: El script maneja varios tipos de errores, incluyendo problemas de permisos y archivos no encontrados. Asegúrate de revisar los mensajes de error en caso de que algo no funcione como se espera.
- **Privilegios de Administrador**: La ejecución del instalador requiere privilegios de administrador. Asegúrate de que tu cuenta de usuario tenga los permisos necesarios.
