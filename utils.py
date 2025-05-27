from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

geminiKey = os.getenv('GEMINI_TOKEN')
#. Creo un cliente
client = genai.Client(api_key=f'{geminiKey}')

# - Función que devuelve la respuesta de Gemini y acepta un prompt como parámetro
def getResponse(prompt: str) -> str:
    try: 
        response = client.models.generate_content(
        model = "gemini-1.5-flash",
        contents = prompt + " Dilo en máximo 2000 caracteres"
    )
    except Exception as e:
        return "Error: " + str(e)
    return response.text