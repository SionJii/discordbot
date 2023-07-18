import discord
from discord.ext import commands
import os
from discord import Permissions

client = commands.Bot(command_prefix='!')

TOKEN = 'ODY0MDYyMDczNDMxMjYxMjA1.YOv-gw.0dh7XcieJvTS6uVwFZooYGIyVjU'


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('히히 못해 ^^'))
    print(client.user.name)
    print('Link Start!')
    print('------')


@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f'loaded {extention}')


@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f'unloaded {extention}')


@client.command()
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f'reloaded {extention}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)