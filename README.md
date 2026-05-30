# GuardiánClima ITBA ("Clima2")

Aplicación de consola en Python que permite consultar el clima de cualquier ciudad,
guardar un historial global de consultas en un archivo csv, ver estadísticas de uso y recibir un consejo
de vestimenta generado por Inteligencia Artificial (de Google Gemini).

Proyecto del **Trayecto de Tecnología – ITBA**, Grupo 33.

Conformado por:
- Francisco Pedemonte 
- Juan Ignacio Bariffi Perez Chada 
- Juan Mateo Beltran Flores
- Jeronimo Sanguinetti

---

## Requisitos

- **Python 3.x**
- Librerias de Python:
  - `requests` (utilizada para peticiones HTTP a la API del clima)
  - `google-generativeai` (Libreria de Google para el consejo de vestimenta)
  - `pandas` (lectura, escritura y analisis de datos con los archivos CSV)

---

## Instalación de Librerías

Desde una terminal, instalá las librerías necesarias:

```
pip install requests google-generativeai pandas
```

> En caso de que no te funcion, puede ser que tengas que usar `pip3` en lugar de `pip`.

---

## Configuración y Obtención de Claves API

1. **OpenWeatherMap** — para averiguar el clima.
   Registrate en https://openweathermap.org/ y copiá tu clave desde la sección *API keys* (o crear una nueva en caso de necesitarlo).
2. **Google Gemini** — para el consejo de vestimenta.
   Generá una clave desde **Google AI Studio** (https://aistudio.google.com/) con tu cuenta de Google.

Las claves se ingresan y posteriormente se leen desde el archivo **`api.py`**, que tiene el siguiente formato:

```
OWM_API_KEY = "TU_CLAVE_DE_OPENWEATHERMAP"
GEMINI_API_KEY = "TU_CLAVE_DE_GEMINI"
```

---

## Cómo ejecutar la aplicación

1. Abrí una terminal y ubicate **dentro de la carpeta del proyecto** (donde está el archivo `main.py`):

   ```
   cd Challenge_Tecnologia
   ```

2. Ejecutá el programa:

   ```
   python main.py
   ```

   (o `python3 main.py` en caso de que no te funciones)

---

## Flujo de la aplicación

### Menú de Acceso (antes de iniciar sesión)

1. **Iniciar sesión** — se pide usuario y contraseña y los compara con los datos que hayan en `usuarios.csv`
   (respetando mayúsculas, minúsculas y caracteres especiales).
2. **Registrar un usuario** — pide un usuario nuevo y una contraseña que debe cumplir
   las reglas de seguridad: coincidir al repetirla, tener al menos **7 caracteres**, al menos **una mayúscula**, al menos **una minúscula** y al menos **un carácter especial**. (Reglas vistas en el bloque 4.4 sobre ciberseguridad)
   Si no cumple con alguna de las reglas, se indican las reglas incumplidas y se sugiere una contraseña más segura.
   ***PD:*** Guardar las contraseñas en un archivo `.csv` es mala practica ya que es inseguro, pero nos sirve para simular el sistema de logueo.
3. **Salir** — cierra el programa.

Una vez ingresados los datos correctos, se accede al Menú Principal.

### Menú Principal

1. **Consultar clima** — pide una ciudad, muestra sus datos (temperatura, humedad, presión, viento y descripción) y los guarda en `historial_global.csv`.
2. **Ver historial del clima** — pide una ciudad y muestra las consultas registradas para esa ciudad.
3. **Estadísticas globales y exportar** — permite por un lado:
   - ver la ciudad más consultada, el total de consultas y la temperatura promedio (de todas las consultas);
   - exportar el historial completo a un archivo CSV (el cual el usuarop puede elegir el nombre).
4. **Consejo IA (cómo vestirte)** — Acá el usuario puede elegir o una consulta del historial, hacer una nueva consulta o analizar la última consulta. Con esos datos se le pide a Gemini un consejo de vestimenta breve a través de un prompt prediseñado que admite variables..
*Hecho con datos del modulo de Prompt Engineering **(Bloque 2.7)***.
5. **Acerca de** — muestra información de la aplicación y del equipo.
6. **Cerrar sesión** — vuelve al Menú de Acceso.

---

## Archivos que genera la aplicación

- **`usuarios.csv`** — usuarios registrados
 *Estructura:* (`Usuario, Contraseña`).
- **`historial_global.csv`** — historial de consultas de clima
 *Estructura:* (`Usuario, Ciudad, Fecha, Temperatura, Descripcion, Humedad, Viento`).

Ambos se crean automáticamente la primera vez que se necesitan.
