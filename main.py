import disnake
import os
import logging
import aiosqlite

from disnake.ext import commands, tasks
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
    ping.start()

  
@bot.listen()
async def on_message(message):
    prefix = await bot.get_prefix(message)
    if bot.user in message.mentions and not message.reference:
        embed = disnake.Embed(
            description=f'Enter command `/help` or `{prefix}help`',
            color=disnake.Color.from_rgb(52,89,149)
        )
        await message.channel.send(embed=embed)
    await bot.process_commands(message)


  
@tasks.loop(minutes=25)
async def ping():
    channel = bot.get_channel(1270281823322247280)
    await channel.send('<@1342459857785061398>')
    
bot.run(os.getenv('TOKEN'))