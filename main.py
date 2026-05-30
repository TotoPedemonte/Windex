#-------------------------------------------------------------------------------
# Librerías:
#-------------------------------------------------------------------------------

from auth import login, registro
from limpiar_consola import limpiar_consola
        
#-------------------------------------------------------------------------------
# Acceso:
#-------------------------------------------------------------------------------

def Acceso():
    print("Elige una opcion para comenzar:")
    print("1. Iniciar sesion")
    print("2. Registrar a un usuario")
    print("3. Salir")
    opcion = input("Elige una opcion para comenzar: ")
    limpiar_consola()
    if opcion == "1":
        print("Perfecto, primero necesitamos tus credenciales")
        if login():
            return
        else:
            limpiar_consola()
            Acceso()
    elif opcion == "2":
        print("Te vamos a pedir un par datos para registrarte")
        registro()
        return
    elif opcion == "3":
        exit()
    else:
        limpiar_consola()
        print("Elegiste una opcion que no es válida, por favor intenta de nuevo")
        print("------------------------------------------------------------------------------")
        Acceso()
        return
 
#-------------------------------------------------------------------------------
# App:
#-------------------------------------------------------------------------------

print("------------------------------------------------------------------------------")
print("Bienvenido a Clima2!")
print("------------------------------------------------------------------------------")

Acceso() # Inicializador de la aplicación