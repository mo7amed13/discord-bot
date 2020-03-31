import discord
import random
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')
"""""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('yaatik asba ya boty!')
@client.event
async def on_member_join(member):
    await member.send('marhba bik si zabour')
@client.event
async def on_member_remove(member):
    await member.channel.send('b akal mnayek')
"""

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency *1000)}ms')
@client.command()
async def flip(ctx):
    responses = ['Heads', 'Tails']
    await ctx.send(f'{random.choice(responses)}')


client.run('Njk0NTM1ODM0NDg5MDYxNDU4.XoNhhQ.8Q8pPRGD-FDURsfb-wSD_3fgK34')



