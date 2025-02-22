import disnake
import aiosqlite
import logging

from disnake.ext import commands


class event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
def setup(bot: commands.Bot):
    bot.add_cog(event(bot))
