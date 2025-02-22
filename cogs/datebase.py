import disnake
import aiosqlite
import logging

from disnake.ext import commands


class datebase(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        try:
            async with aiosqlite.connect('main.db') as db:
                await db.execute('''
                    CREATE TABLE IF NOT EXISTS prefixes (
                        server_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        prefix TEXT
                    )
                ''')
                await db.commit()
                
                await db.execute('''
                    CREATE TABLE IF NOT EXISTS report_channel (
                        server_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        report_channel INTEGER NOT NULL
                    )
                ''')
                await db.commit()
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            
def setup(bot: commands.Bot):
    bot.add_cog(datebase(bot))
