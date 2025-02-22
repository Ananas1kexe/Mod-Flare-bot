import disnake
import os
import logging
import aiosqlite

from disnake.ext import commands
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('bot.log', encoding='utf-8'), logging.StreamHandler()])

async def get_prefix(bot, message):
    if message.guild:
        async with bot.db.execute('SELECT prefix FROM prefixes WHERE server_id = ?', (message.guild.id,)) as cursor:
            row = await cursor.fetchone()
        return row[0] if row else '!'
    else:
        return '!'

intents = disnake.Intents.all()
intents.messages = True

bot = commands.AutoShardedBot(command_prefix=get_prefix, intents=intents, help_command=None)


bot.load_extensions('cogs')

@bot.event
async def on_ready():
    bot.db = await aiosqlite.connect('main.db')
    await bot.db.execute('''
        CREATE TABLE IF NOT EXISTS prefixes (
            server_id INTEGER PRIMARY KEY AUTOINCREMENT,
            prefix TEXT
        )
    ''')
    await bot.db.commit()
bot.run(os.getenv('TOKEN'))