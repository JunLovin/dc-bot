import discord
from discord.ext import commands

class ModeratorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    async def kick(self, ctx, member: discord.Member, reasons):
        # TODO: Poner funcionalidad del comando kick
        pass


async def setup(bot):
    await bot.add_cog(ModeratorCog(bot))