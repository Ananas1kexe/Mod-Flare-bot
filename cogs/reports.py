import disnake
import aiosqlite
import logging

from disnake.ext import commands


class reports(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name='report', description='Send a report')
    async def report(self, inter: disnake.AppCommandInter, report):
        async with aiosqlite.connect('main.db') as db:
            cursor = await db.execute('SELECT server_id, report_channel FROM report_channel WHERE server_id = ?', (inter.guild.id,)) 
            row = await cursor.fetchone()
            
            if row is None:
                embed = disnake.Embed(
                    title='Error occurred',
                    description='Channel not installed'
                )
                await inter.response.send_message(embed=embed, ephemeral=True)
                return

            channel_id = row[1]
            channel = self.bot.get_channel(channel_id)
            
            embed = disnake.Embed(
                title='New report',
                description=f'{report}'
            )
            await channel.send(embed=embed)
def setup(bot: commands.Bot):
    bot.add_cog(reports(bot))
