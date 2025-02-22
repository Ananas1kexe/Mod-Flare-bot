import disnake
import aiosqlite
import logging

from disnake.ext import commands


class settings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        
    @commands.slash_command()
    async def set_prefix(self, inter: disnake.AppCommandInter, prefix: str):
        
        async with aiosqlite.connect('main.db') as db:
            await db.execute('REPLACE INTO prefixes (server_id, prefix) VALUES (?, ?)', (inter.guild.id, prefix,))
            await db.commit()
        
        embed = disnake.Embed(
            title='Setting saved',
            description=f'Command prefix set to `{prefix}`',
            color=disnake.Color.from_rgb(52,89,149)
        )
        
        
        await inter.response.send_message(embed=embed)    
        
    @commands.slash_command()
    async def set_report_channel(self, inter: disnake.AppCommandInter, channel: disnake.TextChannel):
        
        async with aiosqlite.connect('main.db') as db:
            await db.execute('REPLACE INTO report_channel (server_id, report_channel) VALUES (?, ?)', (inter.guild.id, channel.id,))
            await db.commit()
        
        embed = disnake.Embed(
            title='Setting saved',
            description=f'Report channel set to {channel.mention} (#{channel.name})',
            color=disnake.Color.from_rgb(52,89,149)
        )
        
        await inter.response.send_message(embed=embed) 
        
        channel_report = self.bot.get_channel(channel.id)
        
        
        embed = disnake.Embed(
            title='Setting saved',
            description=f'This channel was set up for reporting',
            color=disnake.Color.from_rgb(52,89,149)
        )
        await channel_report.send(embed=embed) 

def setup(bot: commands.Bot):
    bot.add_cog(settings(bot))
