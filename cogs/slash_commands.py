import disnake
import aiosqlite
import logging
from config import VERSION
from disnake.ext import commands
from disnake.utils import format_dt


class slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name='information', description="information")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def information(self, inter: disnake.AppCommandInter):
        prefix = await self.bot.get_prefix(inter)
        guild_count = len(self.bot.guilds)
        
        embed = disnake.Embed(
            title='Information',
            description=(
            '**Mod Flare**\n'
            f"Name: `{self.bot.user}`\n"
            f"Guilds: `{guild_count}`\n"
            "Create: `21.02.2025`\n"
            "Server support: https://discord.gg/KmskWpN5nb\n"
            'Website Mod Flare: https://mod-flare.vercel.app\n'
            'Website PINE X: https://mod-flare.vercel.app\n\n'
            
            '** Team and Other **\n'
            "Devloper: ** @ananas1k47 **\n"
            'Information: Mod Flare is the younger brother of the PINE X project\n'
            "Description: This bot was created to help protection and moderation on your server!!\n"
            f"For help, write the command: `/help` or `{prefix}help`"),
            color=disnake.Color.from_rgb(52,89,149)

        )
        embed.set_author(
            name='Mod Flare',
            url='https://mod-flare.vercel.app/',
            icon_url=self.bot.user.display_avatar.url)
        embed.set_footer(
            text='All rights reserved!',
            icon_url=inter.author.display_avatar
        )
        support_btn = disnake.ui.Button(label='Server support', url='https://discord.gg/KmskWpN5nb', style=disnake.ButtonStyle.link, emoji='🔍')
        website_mod_flare_btn = disnake.ui.Button(label='Website', url='https://mod-flare.vercel.app/', style=disnake.ButtonStyle.link, emoji='🌐')
        website_pine_x_btn = disnake.ui.Button(label='Website', url='https://pine-x.vercel.app/', style=disnake.ButtonStyle.link, emoji='🌐')

        action_row = disnake.ui.ActionRow(support_btn, website_mod_flare_btn, website_pine_x_btn)
        
        await inter.send(embed=embed,components=[action_row], ephemeral=True)
        
    @information.error
    async def info_error(self, inter: disnake.AppCommandInter, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = disnake.Embed(
                title='Anti-raid limit',
                description=
                f'\n{inter.author.mention}\n'
                '**Wait 5 sec**\n'
                f'>>> Please wait {error.retry_after:.2f} seconds before using this command again.',
                color=disnake.Color.from_rgb(52,89,149)
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
    #====================================================================================================================================================#
    
    
    @commands.slash_command(name='info-bot', description="Bot information")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info_bot(self, inter: disnake.AppCommandInter):
        prefix = await self.bot.get_prefix(inter)
        guild_count = len(self.bot.guilds)
        shard = self.bot.shard_count
        guild_ping = (
            round(self.bot.latency, 3)
            if self.bot.latency
            else 'N/D'
        )
        api_ping_start = disnake.utils.utcnow()
        await self.bot.http.request(disnake.http.Route('GET','/gateway'))
        api_ping = (disnake.utils.utcnow() - api_ping_start).total_seconds()
        api_ping = (round(api_ping, 4)
        if api_ping
        else 'N/D'
        )
    
            
        embed = disnake.Embed(
            title='Bot info',
            description=(
            '**Mod Flare**\n'
            f"Name: `{self.bot.user}`\n"
            f"Version: `{VERSION}`\n"
            f"Prefix: `{prefix}`\n"
            f"Guilds: `{guild_count}`\n"
            f'API Ping: `{api_ping}`\n'
            f'Guild ping: `{guild_ping}`\n\n'
            
            '**Information**\n'
            'Last updating: `22.02.2025`\n'
            'Next planned update: `27.02.2025`\n'
            'Update number: `#1`\n'
            f'All shards: `{shard}`\n\n'
            "Devloper: ** [@ananas1k47](https://pine-x.vercel.app/) **\n"
            'Information: Mod Flare is the younger brother of the PINE X project\n'
            f"For help, write the command: `/help` or `{prefix}help`"),
            color=disnake.Color.from_rgb(52,89,149)

        )
        embed.set_author(
            name='PINE X',
            url='https://pine-x.vercel.app/',
            icon_url=self.bot.user.display_avatar.url)
        embed.set_footer(
            text='All rights reserved',
            icon_url=inter.author.display_avatar
        )
        support_btn = disnake.ui.Button(label='Server support', url='https://discord.gg/KmskWpN5nb', style=disnake.ButtonStyle.link, emoji='🔍')
        website_mod_flare_btn = disnake.ui.Button(label='Website', url='https://mod-flare.vercel.app/', style=disnake.ButtonStyle.link, emoji='🌐')
        website_pine_x_btn = disnake.ui.Button(label='Website', url='https://pine-x.vercel.app/', style=disnake.ButtonStyle.link, emoji='🌐')
        
        action_row = disnake.ui.ActionRow(support_btn, website_mod_flare_btn, website_pine_x_btn)
        
        await inter.response.send_message(embed=embed, components=[action_row], ephemeral=True)
        
    @info_bot.error
    async def info_error(self, inter: disnake.AppCommandInter, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = disnake.Embed(
                title='Anti-raid limit',
                description=
                f'\n{inter.author.mention}\n'
                '**Wait 5 sec**\n'
                f'>>> Please wait {error.retry_after:.2f} seconds before using this command again.',
                color=disnake.Color.from_rgb(52,89,149)
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
    
    @commands.slash_command()
    async def ping(self, inter: disnake.AppCommandInter):
        await inter.response.send_message('pong')
    
    
    
    
    @commands.slash_command(name='serverinfo', description="Information about this server")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def server_info(self, inter: disnake.AppCommandInter):
        guild = inter.guild
        
        server_name = guild.name
        server_id = guild.id
        
        server_owner_name = guild.owner.name
        server_owner_mention = guild.owner.mention

        members_count = guild.member_count
        bots = len([member for member in guild.members if member.bot])
        human_count = members_count - bots
        server_icon = guild.icon.url if guild.icon else None 
        server_banner = guild.banner.url if guild.banner else None
        server_description = guild.description or 'Not found'
        created_at = format_dt(guild.created_at, style='F')
        
        text_channel = len([channel for channel in guild.text_channels if isinstance(channel, disnake.TextChannel)])
        voice_channel = len([channel for channel in guild.voice_channels if isinstance(channel, disnake.VoiceChannel)])
    
        boost_count = guild.premium_subscription_count
        boost_level = guild.premium_tier
        
        invites = await guild.invites()
        if invites:
            invite_link = invites[0].url 
        else:
            invite = await inter.channel.create_invite(max_age=0, max_uses=0)
            invite_link = invite.url   

        embed = disnake.Embed(
            title=f'Server information {server_name}',
            color=disnake.Color.from_rgb(52, 89, 149)
        )
        
        embed.set_thumbnail(url=server_icon)
        embed.set_image(url=server_banner)
        embed.add_field(name='**Description**', value=server_description, inline=False)
        embed.add_field(name='**Server name**', value=f'**>>> {server_name}**', inline=False)
        embed.add_field(name='**ID**', value=f'`{server_id}`', inline=False)
        embed.add_field(name='**Owner**', value=f'>>> {server_owner_mention} **(@{server_owner_name})**', inline=False)
        embed.add_field('**Created**', value=created_at, inline=False)
        embed.add_field(name='**Text channels**', value=f'`{text_channel}`', inline=True)
        embed.add_field(name='**Voice channels**', value=f'`{voice_channel}`', inline=True)
        embed.add_field(name='**ID**', value=f'`{server_id}`',inline=False)
        embed.add_field(name='**Members count**', value=f'`{members_count}`',inline=False)
        embed.add_field('**Bots**', value=f'`{bots}`',inline=True)
        embed.add_field(name='**Human count**', value=f'`{human_count}`', inline=True)
        embed.add_field(name='**Boosts**', value=f'`{boost_level}` (**Boost:** `{boost_count}`)', inline=False)

        await inter.response.send_message(invite_link, embed=embed, ephemeral=True)
    @server_info.error
    async def server_info_error(self, inter: disnake.AppCommandInter, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = disnake.Embed(
                title='Anti-raid limit',
                description=
                f'\n{inter.author.mention}\n'
                '**Wait 5 sec**\n'
                f'>>> Please wait {error.retry_after:.2f} seconds before using this command again.',
                color=disnake.Color.from_rgb(52,89,149)
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
    
def setup(bot: commands.Bot):
    bot.add_cog(slash_commands(bot))
