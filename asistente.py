# -------------------------------------------------------------------------------
# Librerías:
# -------------------------------------------------------------------------------

import google.generativeai as genai # Instalar con 'pip install google-generativeai' o 'pip3 install google-generativeai'

# -------------------------------------------------------------------------------
# Funciones:
# -------------------------------------------------------------------------------

def obtener_consejo_ia_gemini(api_key_gemini, ciudad, temperatura, condicion,humedad, viento):
    # Codigo tomado del pdf de ChallengeTecnologia y modificado acorde a nuestra app
    try:
        genai.configure(api_key=api_key_gemini)
        model = genai.GenerativeModel('gemini-3.5-flash') # Este modelo era el más rapido y estable durante las pruebas
        prompt_diseñado_por_equipo = (
            # Promt realizado por el equipo basandonos en el modulo de Prompt Engineering
            f"""Eres un asistente que da consejos de vestimenta según el clima.

            Contexto: el usuario está en {ciudad} y quiere saber cómo vestirse hoy.

            Datos del clima:
            Temperatura: {temperatura} °C
            Condición: {condicion}
            Humedad: {humedad}%
            Viento: {viento} m/s

            Instrucciones:
            Da un consejo de vestimenta práctico y concreto basado en esos datos.
            Responde en español, en un máximo de 2 frases.
            No repitas los datos del clima ni des explicaciones largas.
            No uses introducciones del tipo "Claro" o "Aquí tienes".
            No incluyas corchetes ni puntos suspensivos.

            Ejemplo de formato esperado:
            [Lleva un abrigo abrigado y bufanda; hace frío y hay viento. Sumá una campera impermeable por si llueve.]

            Consejo:"""
        )
        print("\nGenerando consejo de vestimenta con IA...")
        # Generar contenido
        response = model.generate_content(prompt_diseñado_por_equipo)
        # Asegurarse de que hay texto en la respuesta
        if response.text:
            return response.text
        else:
            # A veces la API puede no devolver texto si hay problemas con el prompt o filtros de seguridad
            # Investigar response.prompt_feedback si hay problemas
            print("La IA no pudo generar un consejo. Razón (si está disponible):",response.prompt_feedback)
            return "No se pudo generar un consejo en este momento."
    except Exception as e:
        print(f"Error al contactar la API de Gemini o procesar la respuesta: {e}")
        return "Error al generar el consejo de IA."