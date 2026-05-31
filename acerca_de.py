def mostrar_info():
    print("\nAcerca de Windex")
    print("------------------------------------------------------------------------------")
    print("""
    Windex es una aplicación desarrollada en Python (3.14.5) como parte del Proyecto Integrador Básico de Tecnologías.

    Desarrollado por (Grupo 33):
    - Juan Ignacio Bariffi Perez Chada (69056)
    - Juan Mateo Beltran Flores (68928)
    - Francisco Pedemonte (69099)
    - Jerónimo Sanguinetti (68880)
    
    Acceso:
    - Permite registrar a nuevos usuarios y nos ocupamos de validar las contraseñas para asegurarnos de que sean seguras.
    - También se puede iniciar sesión y luego verificamos las credenciales con las que se encuentran almacenadas en el archivo usuarios.csv.
    - Opcion para cerrar la aplicación.

    Menú Principal:
    1. Consultar el clima actual de cualquier ciudad del mundo usando la API de OWM (OpenWeatherMap). Los datos obtenidos se muestran en pantalla y se almacenan en un archivo (historial_global.csv).
    2. Consultar el historial de búsquedas por ciudad, segun el usuario logueado..
    3. Generar estadísticas globales basadas en el historial de todos los usuarios: ciudad más consultada, cantidad total de búsquedas, y temperatura promedio de todas las busquedas.
    4. Obtener un consejo personalizado de vestimenta mediante la API de Google Gemini, utilizando los datos climáticos que el usuario desee (Ultima consulta, Elegir del historial, Hacer una nueva consulta).
    5. Ver la descripción del proyecto.
    6. Cerrar sesión y volver al menú de acceso.

    Almacenamiento de Datos:
    - `usuarios.csv`: Almacena usuarios y contraseñas. (Muy inseguro)
    - `historial_global.csv`: Almacena las búsquedas con usuario, ciudad, clima, humedad, viento y fecha/hora.

    Herramientas Utilizadas:
    - Lenguaje: Python 3.14.5
    - Librerías: `requests`, `pandas`, `google-generativeai`, `datetime`, `json`
    - APIs: OpenWeatherMap y Google Gemini
    - Formato de almacenamiento: archivos `.csv`""")