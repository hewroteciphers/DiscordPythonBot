#!/usr/bin/python3
# client.py
#
# see https://realpython.com/how-to-make-a-discord-bot-python/
#
# prerequisites:
#   pip3 install discord python-dotenv
#
import os
import discord
from dotenv import load_dotenv

# get token ids from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# create the bot
client = discord.Client()

@ client.event
async def on_ready():
    #print(f'{client.user} has connected to Discord!')
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    #for guild in client.guilds:
    #    if guild.name == GUILD:
    #        break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
