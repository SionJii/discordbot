import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')

TOKEN = 'ODY0MDYyMDczNDMxMjYxMjA1.YOv-gw.0dh7XcieJvTS6uVwFZooYGIyVjU'


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('>help'))
    print(bot.user.name)
    print('Link Start!')
    print('------')


@bot.command()
async def load(ctx, extention):
    bot.load_extension(f'cogs.{extention}')
    await ctx.send(f'loaded {extention}')


@bot.command()
async def unload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')
    await ctx.send(f'unloaded {extention}')


@bot.command()
async def reload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')
    bot.load_extension(f'cogs.{extention}')
    await ctx.send(f'reloaded {extention}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)