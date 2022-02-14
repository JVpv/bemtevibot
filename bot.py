import os

import discord

from dotenv import load_dotenv
from messageResponse import MessageResponse

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():  # Simple hello world when it goes online.
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to discord!')


@client.event
async def on_message(message):
    if message.content.startswith('b!'):
        if message.content.startswith('b!roll'):
            result = MessageResponse.rollDice(message.content.split()[1])
            print(result)
            await message.channel.send(f"Seu resultado foi {str(result)}!")
        if message.content.startswith('b!canta'):
            await message.channel.send(f"Vai toma no cu")

client.run(TOKEN)
