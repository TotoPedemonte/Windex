#-------------------------------------------------------------------------------
# Librerías:
#-------------------------------------------------------------------------------
import pandas as pd

from asistente import obtener_consejo_ia_gemini
from estadisticas import mostrar_estadisticas, exportar_historial_completo
from api import OWM_API_KEY, GEMINI_API_KEY
from clima import obtener_clima, mostrar_historial
from acerca_de import mostrar_info

#-------------------------------------------------------------------------------
# Funciones:    
#-------------------------------------------------------------------------------

def limpiar_consola(): # Función que limpia la consola, buscada de google para lograr mayor prolijidad (no es nesesaria)
    print("\033[2J")
    print("\033[1;1H")

def seleccionar_historial():
    print("¿Qué consulta deseas seleccionar del historial?")
    print("------------------------------------------------------------------------------")
    try:
        archivo_pd = pd.read_csv("historial_global.csv")
    except(FileNotFoundError,pd.errors.EmptyDataError):
        return "No hay historial y/o Archivo de clima, primero debes realizar una consulta!"
    if archivo_pd.empty:
        return "No hay historial y/o Archivo de clima, primero debes realizar una consulta!"
    df = pd.DataFrame(archivo_pd)
    for index, row in df.iterrows():
        print(f"{index + 1}. Usuario: {row['Usuario']}, Ciudad: {row['Ciudad']}, Fecha: {row['Fecha']}, Temperatura: {row['Temperatura']}°C, Humedad: {row['Humedad']}%, Viento: {row['Viento']} m/s")
    print("------------------------------------------------------------------------------")
    
    try:
        opcion = int(input("Elige una consulta: "))
        if opcion < 1 or opcion > archivo_pd.shape[0]:
            return "Elegiste un valor que no era válido!"
        limpiar_consola()
        opcion = opcion - 1
        return obtener_consejo_ia_gemini(GEMINI_API_KEY, df.iloc[opcion]['Ciudad'], df.iloc[opcion]['Temperatura'], df.iloc[opcion]['Descripcion'], df.iloc[opcion]['Humedad'], df.iloc[opcion]['Viento'])
    except ValueError:
        return "Elegiste un valor que no era válido!"

def nueva_consulta(usuario):
    print("Realizar una nueva consulta")
    print("¿Sobre qué ciudad quieres consultar?")
    ciudad = input("Ciudad: ")
    limpiar_consola()
    resultado_clima = obtener_clima(usuario, ciudad, OWM_API_KEY)
    if not resultado_clima:
        return ""
    return obtener_consejo_ia_gemini(GEMINI_API_KEY, resultado_clima[0], resultado_clima[1], resultado_clima[2], resultado_clima[3], resultado_clima[4])

def analizar_ultima_consulta():
    print("Analizar la ultima consulta")
    print("------------------------------------------------------------------------------")
    try:
        archivo_pd = pd.read_csv("historial_global.csv")
    except(FileNotFoundError,pd.errors.EmptyDataError):
        return "No hay historial y/o Archivo de clima, primero debes realizar una consulta!"
    if archivo_pd.empty:
        return "No hay historial y/o Archivo de clima, primero debes realizar una consulta!"
    df = pd.DataFrame(archivo_pd)
    df = df.sort_values(by=['Fecha'], ascending=False)
    primera_fila = df.iloc[0]
    limpiar_consola()
    return obtener_consejo_ia_gemini(GEMINI_API_KEY, primera_fila['Ciudad'], primera_fila['Temperatura'], primera_fila['Descripcion'], primera_fila['Humedad'], primera_fila['Viento'])
 
#-------------------------------------------------------------------------------
# Menu Principal:    
#-------------------------------------------------------------------------------

def menu_principal(usuario):
    print("------------------------------------------------------------------------------")
    print("Bienvenido", usuario ,"al Menú Principal!")
    print("¿Qué deseas hacer?")
    print("1. Consultar clima")
    print("2. Ver historial del clima")
    print("3. Ver estadísticas globales y exportar historial completo")
    print("4. Consultar con la IA cómo vestirte")
    print("5. Acerca de")
    print("6. Cerrar Sesión")
    opcion = input("Elige una opción: ")
    limpiar_consola()
    if opcion == "1":
        print("Vamos a consultar el clima!")
        print("¿Sobre qué ciudad quieres consultar?")
        ciudad = input("Ciudad: ")
        limpiar_consola()
        obtener_clima(usuario, ciudad, OWM_API_KEY)
    elif opcion == "2":
        print("Vamos a ver el historial del clima")
        print("Sobre qué ciudad quieres consultar?")
        ciudad = input("Ciudad: ")
        limpiar_consola()
        mostrar_historial(ciudad, usuario)
    elif opcion == "3":
        print("¿Qué deseas hacer?")
        print("1. Mostrar estadísticas")
        print("2. Exportar historial completo")
        opcion = input("Elige una opción: ")
        limpiar_consola()

        if opcion == "1":
            mostrar_estadisticas()
        elif opcion == "2":
            exportar_historial_completo()
        else:
            print("Elegiste una opción que no es válida.")
    elif opcion == "4":  
        print("¿De donde quieres consultar el clima?")
        print("1. Seleccionar una consulta del Historial")
        print("2. Realizar una nueva consulta")
        print("3. Analizar la ultima consulta")
        opcion = input("Elige una opción: ")
        limpiar_consola()
        if opcion == "1":
            resultado = seleccionar_historial()
        elif opcion == "2":
            resultado = nueva_consulta(usuario)
        elif opcion == "3":
            resultado = analizar_ultima_consulta()
        print(resultado)
    elif opcion == "5":
        mostrar_info()
    elif opcion == "6":
        print("------------------------------------------------------------------------------")
        print("Sesión Cerrada")
        
        from main import Acceso # No importamos la funcion arriba ya que sino entra en un bucle y da error!
        Acceso()
        return
    else:
        print("Elegiste una opción que no es válida.")
    print("------------------------------------------------------------------------------")
    input("\nPulsa enter para volver al menu")
    limpiar_consola()
    menu_principal(usuario)