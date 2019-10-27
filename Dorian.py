# Work with Python 3.6
import discord
import asyncio

TOKEN = 'NjM2NDAyNjc0MzAwMDkyNDU2.XbUMXA.MwV_ogaCEyoWxiMKZeDYXnKSnpM'
TOPIC = ['love', 'math', 'deep learning','sex']
RESPONSE = ['Uh, you have a crush on me?', 'Algebra or analysis, choose your side', 'learn deep','www.pornhub.com']
UPDATE = 'Version 0.0.2 Simple implementation of chat '
HELP_MSG = 'Add prefix !Dorian to talk to Dorian! -chat -hug -update'

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def one_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Yo {member.name}, you here to chat? '
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!Dorian':
        await message.channel.send('Whats up')

    if message.content == '!Dorian help':
        await message.channel.send(HELP_MSG)

    if message.content == '!Dorian hug':
        await message.channel.send("Mua! My sweetie~ ")

    if message.content == '!Dorian update':
        await message.channel.send(UPDATE)


@client.event
async def on_message(message):
    if message.content.startswith('!Dorian chat'):
        channel = message.channel
        await channel.send(f'{message.author.name}, what do you want to know?')

        def check(m):
            return m.content in TOPIC and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(RESPONSE[1].format(msg))


client.run(TOKEN)