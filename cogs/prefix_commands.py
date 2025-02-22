import disnake
import aiosqlite
import logging

from disnake.ext import commands


class prefix_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')        

def setup(bot: commands.Bot):
    bot.add_cog(prefix_commands(bot))
