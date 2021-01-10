import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready.")

# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server :-)')
#
# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left our server :-(')
#

#bot latency
@client.command()
async def ping(ctx):
    await ctx.send(f'PONG! My latency: {round(client.latency * 1000)}ms')

#response to client's question
@client.command(aliases=['8ball', 'eightball', '8BALL'])
async def _8ball(ctx, *, question):
    responses = ['NO!', 'YES!', 'IT IS CERTAIN!', 'ASK AGAIN LATER!', 'CANNOT PREDICT NOW!', 'MY SOURCES SAY NO!']
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}!')

#deletes messages
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

#kick/ban
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#unban
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run("Nzk3Nzk5MDUyOTEyODg1NzYw.X_ruRA.1tq39NM09BG3KOiPJarb5YsdtDQ")
