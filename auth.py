# -------------------------------------------------------------------------------
# Librerías:
# -------------------------------------------------------------------------------

import pandas as pd
from menu_principal import menu_principal
from limpiar_consola import limpiar_consola

# -------------------------------------------------------------------------------
# Funciones:
# -------------------------------------------------------------------------------

def obtener_usuarios():
    try: # Intentamos abirir el archivo de usuarios
        archivo_pd = pd.read_csv("usuarios.csv", header=None)
        usuarios = []
        for index, row in archivo_pd.iterrows():
            if index == 0: # Ignoramos la primera fila que es la cabecera de la tabla
                continue
            usuarios.append([row[0], row[1]])
        return usuarios
    except FileNotFoundError: # Si da error (porque no existse) creamos uno nuevo
        print("No se encontró ningun archivo de usuarios, creando uno nuevo...") # Poco seguro!!! pero lo usamos para fines de prueba de la app
        pd.DataFrame({"Usuario": [], "Contraseña": []}).to_csv("usuarios.csv", index=False)
        return []
        
def login():
    usuario = input("Ingresa tu usuario o 'salir' para salir de la aplicación:")
    if usuario == "salir":
        return False
    password = input("Ingresa tu contraseña:")
    comprobar_logueo(usuario, password)
        
def comprobar_logueo(usuario, password):
    usuarios = obtener_usuarios()
    for iterar_usuario in usuarios:
        if iterar_usuario[0] == usuario and iterar_usuario[1] == password:
            limpiar_consola()
            menu_principal(usuario)
            return True
    limpiar_consola()
    print("------------------------------------------------------------------------------")
    print("Credenciales incorrectas! Asegurate de respetar las Mayusculas, Minúsculas y Caracteres Especiales")
    print("------------------------------------------------------------------------------")
    
    login()

def registro():
    nuevo_usuario = input("Ingresa tu usuario:")
    for iterar_usuario in obtener_usuarios():
        if iterar_usuario[0].lower() == nuevo_usuario.lower():
            print("El usuario ya existe, por favor intenta de nuevo")
            print("------------------------------------------------------------------------------")
            registro()
            return
    nueva_password = input("Ingresa tu contraseña:")
    repetir = input("Ingresa tu contraseña de nuevo:")
    limpiar_consola()
    print("------------------------------------------------------------------------------")
    comprobar_contraseña(nuevo_usuario, nueva_password, repetir)

def comprobar_contraseña(usuario, contraseña, repetir_contraseña):
    criterios = []
    contiene_caracter = False
    
    # Criterios de ciberseguridad, se pueden agregar más si se quiere
    if contraseña != repetir_contraseña:
        criterios.append("- Las contraseñas no coinciden")
    if len(contraseña) < 7:
        criterios.append("- Debe tener al menos 7 caracteres")
    if contraseña.islower():
        criterios.append("- Debe tener al menos 1 mayuscula")
    if contraseña.isupper():
        criterios.append("- Debe tener al menos 1 minúscula")
    for caracter in contraseña:
        if caracter in caracteres_especiales:
            contiene_caracter = True
            break
    if not contiene_caracter:
        criterios.append("- Debe tener al menos 1 caracter especial")

    if criterios == []:
        try:
            pd.DataFrame({"Usuario": [usuario], "Contraseña": [contraseña]}).to_csv("usuarios.csv", mode='a', header=False, index=False)
        except FileNotFoundError:
            print("No se encontró ningún archivo de usuarios, creando uno nuevo...")
            pd.DataFrame({"Usuario": [usuario], "Contraseña": [contraseña]}).to_csv("usuarios.csv", index=False)
            
        print("Usuario registrado correctamente")
        menu_principal(usuario)
    else:
        print("Error!")
        for item in criterios:
            print(item)
        print("Deberías usar una contraseña más segura. Por ejemplo: 'gato_Libro#007'")
        print("-------------------------------------------------------------")
        
        contraseña = input("Ingresa tu contraseña:")
        repetir_contraseña = input("Ingresa tu contraseña de nuevo:")
        comprobar_contraseña(usuario, contraseña, repetir_contraseña)  
       
# -------------------------------------------------------------------------------
# Variables:
# -------------------------------------------------------------------------------

caracteres_especiales = "!@#$%^&*()-_=+[]{};:,.<>?/|\\~`"