import os
from dotenv import load_dotenv
from discord.ext import commands
import random
import requests

load_dotenv()

tenor_key = os.getenv('TENOR_KEY')

terms = [
    "reaccionar",
    "reacción graciosa",
    "sorprendido",
    "inesperado",
    "wtf",
    "llegar tarde gracioso",
    "caída graciosa",
    "torpe gracioso",
    "comedia reacción",
    "expresión facial graciosa",
    "unbelievable reaction",
    "epic reaction",
    "funny animated",
    "triste",
    "impactado",
    "amor"
]

def obtener_gif_random(termino: str):
        try:
            respuesta = requests.get(f'https://tenor.googleapis.com/v2/search?q={termino}&key={tenor_key}&client_key=test_app&limit=1', headers={
                'Content-Type': 'application/json'
            })
            data = respuesta.json()

            results = data.get('results', [])
            if results and len(results) > 0:
                return results[0]["media_formats"]["gif"]["url"]
            else:
                print("No se encontaron términos para " + termino)
                return None

        except Exception as e:
            print(f"Hubo un error: {e}")

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="random_gif")
    async def random_gif(self, ctx):
        random_term = random.choice(terms)
        gif_url = obtener_gif_random(random_term)
        await ctx.send(gif_url)


async def setup(bot):
    await bot.add_cog(FunCog(bot))