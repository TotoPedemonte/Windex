#-------------------------------------------------------------------------------
# Librerías:
#-------------------------------------------------------------------------------

import pandas as pd

#-------------------------------------------------------------------------------
# Funciones:
#-------------------------------------------------------------------------------

def mostrar_estadisticas():
    try:
        archivo_csv = pd.read_csv("historial_global.csv")
        print("------------------------------------------------------------------------------")
        print("Ciudad más consultada:")
        print("- Ciudad:", archivo_csv.sort_values(by=['Ciudad'], ascending=False).mode()["Ciudad"][0])
        print("------------------------------------------------------------------------------")
        print("Cantidad de consultas:")
        print("- Total:", archivo_csv.shape[0])
        print("------------------------------------------------------------------------------")
        print("Temperatura promedio de todas las consultas:")
        print("- Promedio:", str(archivo_csv['Temperatura'].mean().round(2)) + "°C")
    except FileNotFoundError:
        print("No se encontró ningún archivo de historial de clima")
        
def exportar_historial_completo():
    try:
        archivo_csv = pd.read_csv("historial_global.csv")
        nombre_archivo = str(input("Nombre del archivo de exportación (sin espacios ni puntos): "))
        nombre_archivo = nombre_archivo.replace(" ", "_").lower() + ".csv"
        archivo_csv.to_csv(nombre_archivo, index=False)
        print("Historial completo exportado a", nombre_archivo)
    except FileNotFoundError:
        print("No se encontró ningún archivo de historial de clima")