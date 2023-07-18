import discord
from discord.ext import commands

import laftel


class animecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 애니(self, ctx, *, title):
        await ctx.send(findAnime(title))


def findAnime(title):
    return laftel.sync.searchAnime(title)[0].url


def setup(bot):
    bot.add_cog(animecog(bot))
