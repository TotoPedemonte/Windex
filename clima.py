#-------------------------------------------------------------------------------
# Librerías:
#-------------------------------------------------------------------------------

import requests
import json
from datetime import datetime
import pandas as pd
from limpiar_consola import limpiar_consola

#-------------------------------------------------------------------------------
# Funciones:
#-------------------------------------------------------------------------------

def guardar_clima(usuario, ciudad, temperatura, humedad, viento, descripcion):
    try:
        pd.read_csv("historial_global.csv", header=None)
        formato = pd.DataFrame({"Usuario": [usuario], "Ciudad": [ciudad], "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "Temperatura": [temperatura], "Descripcion": [descripcion], "Humedad": [humedad], "Viento": [viento]})
        formato.to_csv("historial_global.csv", mode='a', header=False, index=False)
    except FileNotFoundError:
        formato = pd.DataFrame({"Usuario": [], "Ciudad": [], "Fecha": [], "Temperatura": [], "Descripcion": [], "Humedad": [], "Viento": []})
        formato.to_csv("historial_global.csv", index=False)
        formato = pd.DataFrame({"Usuario": [usuario], "Ciudad": [ciudad], "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "Temperatura": [temperatura], "Descripcion": [descripcion], "Humedad": [humedad], "Viento": [viento]})
        formato.to_csv("historial_global.csv", mode='a', header=False, index=False)
        return
    
def mostrar_historial(ciudad):
    hay_historial = False
    print("------------------------------------------------------------------------------")
    print("Historial del clima para", ciudad)
    print("------------------------------------------------------------------------------")
    archivo_pd = pd.read_csv("historial_global.csv")
    if archivo_pd.empty:
        return "No hay historial y/o Archivo de clima, primero debes realizar una consulta!"
    for index, row in archivo_pd.iterrows():
        if index == 0: # Ignoramos la primera fila que es la cabecera de la tabla
            continue
        if row['Ciudad'] == ciudad:
            print(f"- Usuario: {row['Usuario']}, Fecha: {row['Fecha']}, Temperatura: {row['Temperatura']}°C, Humedad: {row['Humedad']}%, Viento: {row['Viento']} m/s")
            hay_historial = True
    if not hay_historial:
        print("No hay historial de clima para", ciudad)

def obtener_clima(usuario, ciudad, api_key):
    datos_clima_recibidos = obtener_clima_ciudad_owm(ciudad, api_key)
    if datos_clima_recibidos:
        try:
            temperatura = datos_clima_recibidos['main']['temp']
            descripcion = datos_clima_recibidos['weather'][0]['description']
            humedad = datos_clima_recibidos['main']['humidity']
            presion = datos_clima_recibidos['main']['pressure']
            viento = datos_clima_recibidos['wind']['speed']
            city = datos_clima_recibidos['name']
            print("------------------------------------------------------------------------------")
            print(f"Mostrando el clima para {city}:")
            print("------------------------------------------------------------------------------")
            print(f"- Temperatura: {temperatura}°C")
            print(f"- Humedad: {humedad}%")
            print(f"- Presión: {presion}hPa")
            print(f"- Velocidad del Viento: {viento}m/s")
            print(f"- Descripción del clima: {descripcion.capitalize()}")
            guardar_clima(usuario, ciudad, temperatura, humedad, viento, descripcion)
            return [city, temperatura, descripcion, humedad, viento] # Devolvemos el clima en formato lista en caso de que queramos descomponerlo y mandarlo a otra funcion
        except KeyError:
            print("Error: Formato inesperado en datos.")
            return
    else:
        print("Error: No se pudo obtener datos de OpenWeatherMap.")
        return

def obtener_clima_ciudad_owm(ciudad, api_key):
    # Función que obtiene el clima de una ciudad a partir de la API de OpenWeatherMap (Sacado del pdf de ChallengeTecnologia)
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        'q': ciudad,
        'appid': api_key,
        'units': 'metric',
        'lang': 'es'
    }
    print(f"\nConsultando el clima (OpenWeatherMap) para: {ciudad}...")
    try:
        respuesta = requests.get(base_url, params=parametros, timeout=10)
        respuesta.raise_for_status()
        datos_clima = respuesta.json()
        return datos_clima
    except requests.exceptions.HTTPError as errh:
        if respuesta.status_code == 401:
            print(f"Error de autenticación OWM: API Key inválida.")
        elif respuesta.status_code == 404:
            print(f"Error OWM: Ciudad '{ciudad}' no encontrada.")
        else:
            print(f"Error HTTP OWM: {errh}")
            return None
    except requests.exceptions.RequestException as err:
        print(f"Error de conexión/petición OWM: {err}")
        return None
    except json.JSONDecodeError:
        print("Error OWM: La respuesta de la API no es JSON válido.")
        return None