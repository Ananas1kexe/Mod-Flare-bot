import disnake
import aiosqlite
import logging

from disnake.ext import commands


class slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    async def ping(self, inter: disnake.AppCommandInter):
        await inter.response.send_message('pong')
    
def setup(bot: commands.Bot):
    bot.add_cog(slash_commands(bot))
