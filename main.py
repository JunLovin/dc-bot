# Importo discord
import discord
# Importo commands de discord
from discord.ext import commands
# Importo os junto con dotenv para poder usar las variables de entorno
import os
from dotenv import load_dotenv
# Importo genai
from google import genai
# Importo mi función getResponse para separar el código
from utils import getResponse

# . Cargo las variables de entorno
load_dotenv()

# . Creo un objeto intents y le digo que quiero usar todos los intents
intents = discord.Intents.all()
# . Le digo que quiero usar el intent de message content
intents.message_content = True

# . Creo un objeto bot y le digo que el prefijo es $ y que quiero usar los intents
bot = commands.Bot(command_prefix='$', intents=intents)

# - Creo un comando que se ejecuta cuando se escribe $gemini
@bot.command(name="gemini")
async def gemini(ctx, *args):
    response = getResponse(args[0])
    await ctx.send(response)

# - Creo un evento que se ejecuta cuando el bot esta listo
@bot.event
async def on_ready():
    print(f"Bot logueado como: {bot.user}")

# . Ejecuto el bot con el token
bot.run(os.getenv('BOT_TOKEN'))