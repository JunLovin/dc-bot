import discord
from discord.ext import commands

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        canal = member.guild.system_channel
        if canal is not None:
            await canal.send(f"¡Bienvenido {member.mention}!")
    
    @commands.command()
    async def greetings(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self.last_member is None or self.last_member.id != member.id:
            await ctx.send(f"oli {member.mention}")
        else:
            await ctx.send(f"oli {member.mention}... se siente familiar")
        self.last_member = member

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))