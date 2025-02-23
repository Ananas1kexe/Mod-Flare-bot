import disnake
import aiosqlite
import logging

from disnake.ext import commands


class reports(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name='report', description='Send a report')
    async def report(self, inter: disnake.AppCommandInter, report: str, img: disnake.Attachment = None, note: str = None,  user: disnake.Member = None, proof: str = None):
        async with aiosqlite.connect('main.db') as db:
            cursor = await db.execute('SELECT server_id, report_channel FROM report_channel WHERE server_id = ?', (inter.guild.id,)) 
            row = await cursor.fetchone()
            
            if user is None:
                user = 'Not specified'
            else:
                user = f"{user.mention} (@{user.name})"
                
            if note is None:
                note = 'Not specified'
            
            if proof is None:
                proof = 'Not specified'
                
            if img is None:
                return     
                     
            if row is None:
                embed = disnake.Embed(
                    title='Error occurred',
                    description='Channel not installed'
                )
                await inter.response.send_message(embed=embed, ephemeral=True)
                return

            channel_id = row[1]
            channel = self.bot.get_channel(channel_id)
            emogi = '<:yes_mf:1343244273939775551>'
            embed = disnake.Embed(
                title=f'Report sent successfully {emogi}',
                description=(
                    '**Brief information**\n'
                    f'Author: {inter.author.mention} (@{inter.author.name})'
                    f'Sent to: {user}\n'
                    f'Description: {report}\n'
                    f'Note: {note}\n'
                    f'Proof: {proof}\n'
                ),
                color=disnake.Color.from_rgb(52,149,89)
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
            
            embed = disnake.Embed(
                title='New report',
                description=('**Brief information**\n'
                    f'Author: {inter.author.mention} (@{inter.author.name})'
                    f'Sent to: {user}\n'
                    f'Description: {report}\n'
                    f'Note: {note}\n'
                    f'Proof: {proof}\n'
                    f'Image: {img.url}'
                )
            )
            await channel.send(embed=embed)
def setup(bot: commands.Bot):
    bot.add_cog(reports(bot))
