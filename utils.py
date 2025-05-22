from google import genai
import os
from dotenv import load_dotenv

# . Cargar las variables de entorno desde el archivo .env
load_dotenv()

# . Guardo la API key de Gemini
geminiKey = os.getenv('GEMINI_TOKEN')
#. Creo un objeto cliente de genai y le paso la API key
client = genai.Client(api_key=f'{geminiKey}')

# - Función que devuelve la respuesta de Gemini y acepta un prompt como parámetro
def getResponse(prompt: str) -> str:
    try: 
        response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = prompt + "Dilo en máximo 2000 carácteres"
    )
    except Exception as e:
        return "Error: " + str(e)
    return response.text