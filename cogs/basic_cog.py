import discord
from discord.ext import commands
import datetime

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ayuda")
    async def ayuda(self, ctx):
        embed = discord.Embed(
            title="Comandos Básicos",
            description="Aquí podrás ver todos los comandos del bot.",
            color=0x09E5DE,
            url="https://github.com/JunLovin/dc-bot",
            timestamp=datetime.datetime.now()
        )
        embed.add_field(name="**1.** `$gemini <pregunta>`", value="Este comando le hará una pregunta a la IA Gemini.\n", inline=False)
        embed.add_field(name="**2.** `$ayuda`", value="Enviará un mensaje Embed con todos los comandos disponibles\n", inline=False)
        embed.add_field(name="**3.** `$creditos`", value="Dará la información del creador del bot", inline=False)
        embed.set_footer(text="Bot creado por JunLovin", icon_url="https://cdn.discordapp.com/avatars/446418348943867904/dc9015a8bb1b7e0e50545603b4e8c5f6.webp?size=512")
        await ctx.send(embed=embed)

    @commands.command(name="creditos")
    async def creditos(self, ctx):
        embed = discord.Embed(
            title="Créditos del Bot",
            description="Mostraré información del usuario más hermoso de Discord llamado <@446418348943867904>",
            color=0xDDE015
        )
        embed.add_field(name="Redes sociales", value="**GitHub:** https://github.com/JunLovin\n\n**LinkedIn:** https://www.linkedin.com/in/saidre20/\n\n**Twitter:** https://x.com/saidre20\n\n", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="Información", value="**Portfolio:** https://said-portfolio-three.vercel.app\n\n**Coverletter:** https://said-coverletter.vercel.app", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/446418348943867904/dc9015a8bb1b7e0e50545603b4e8c5f6.webp?size=512")
        embed.set_footer(text="Bot creador por JunLovin", icon_url="https://cdn.discordapp.com/avatars/446418348943867904/dc9015a8bb1b7e0e50545603b4e8c5f6.webp?size=512")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(BasicCog(bot))