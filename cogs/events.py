import disnake
import aiosqlite
import logging
import asyncio
import time

from colorama import init, Fore
from disnake.ext import commands

init()
class event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'Bot has started as {self.bot.user}✅')
        logging.info(f'Servering in {len(self.bot.guilds)}')
        logging.info(f'Bot started and all sytem {Fore.GREEN}OK{Fore.RESET}')
        statuse = [
            disnake.Game('Official bot Mod-Flare'),
            disnake.Activity(type=disnake.ActivityType.watching, name='https://mod-flare.vercel.app', url='https://mod-flare.vercel.app'),
            disnake.Activity(type=disnake.ActivityType.watching, name='https://pine-x.vercel.app', url='https://pine-x.vercel.app'),
        ]
    
        
        while True:
            for status in statuse:
                await self.bot.change_presence(activity=status)
                await asyncio.sleep(60)
    
    
def setup(bot: commands.Bot):
    bot.add_cog(event(bot))
