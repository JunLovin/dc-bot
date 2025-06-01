import discord
from discord.ext import commands

class ModeratorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    async def kick(self, ctx, member: discord.Member, *args: str):  
        if not member or not args:
            await ctx.send("Por favor, ingresa un usuario para expulsar y una razón válida.")
        try:
            reason = " ".join(args)
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} ha sido expulsado del servidor por: \"*{reason}*\"")
        except Exception as e:
            await ctx.send(f"Ocurrió un error: {e}")

    @commands.command(name="clean_chat")
    async def limpiar_chat(self, ctx):
        await ctx.channel.purge() # ? También se puede poner limite con `purge(limit=n)`


async def setup(bot):
    await bot.add_cog(ModeratorCog(bot))