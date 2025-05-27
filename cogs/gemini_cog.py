import os
from discord.ext import commands
from utils import getResponse

class GeminiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gemini")
    async def gemini(self, ctx, *args):
        if not args:
            await ctx.send("Por favor, ingresa un prompt para Gemini. Porejemplo: `$gemini ¿Qué es la programación?`")
            return
            
        user_prompt = " ".join(args)

        async with ctx.typing():
            response = getResponse(user_prompt)

        if len(response) > 2000:
            partes = [response[i:i+2000] for i in range(0, len(response),2000)]
            for parte in partes:
                await ctx.send(parte)
        else:
            await ctx.send(response)    

async def setup(bot):
    await bot.add_cog(GeminiCog(bot))