import discord
from discord.ext import commands

import random


class commandcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)

    @commands.command()
    async def 마소님(self, ctx, *, question):
        responses = [
            '확실해.', '확실히 맞아.', '의심의 여지도 없어.', '그래. 확실해.', '믿어도 좋아.',
            '내가 보기엔, 맞아.', '그럴 가능성이 높아.', '전망이 밝아.', '그래.',
            '표지판이 "그래"를 가리키고 있어.', '대답이 흐릿한데, 다시 해봐.', '나중에 물어봐.',
            '지금 말하지 않는 것이 좋겠군.', '지금은 예언할 수 없어.', '생각해보고 다시 물어봐.', '그렇지 않을거야.',
            '내 대답은 "아니"야.', '내 정보원이 아니라는군.', '그럴 가능성이 낮아.', '매우 의심스러워.'
        ]
        await ctx.send(f'질문: {question}\n대답: {random.choice(responses)}')

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention}님을 서버에서 차단했어요')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention}님의 차단을 해제했어요')
                return


def setup(bot):
    bot.add_cog(commandcog(bot))
