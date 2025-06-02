import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

initial_extensions = [
    'cogs.basic_cog',
    'cogs.fun_cog',
    'cogs.gemini_cog',
    'cogs.moderator_cog',
    'cogs.welcome_cog'
]

@bot.event
async def on_ready() -> None:
    print(f"Bot logueado como: {bot.user}")

    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Cog {extension} cargado correctamente")
        except Exception as e:
            print(f"Error al cargar el cog {extension}: {e}")



bot.run(BOT_TOKEN)