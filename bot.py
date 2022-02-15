import os
from re import match

import discord

from dotenv import load_dotenv
import random
from rpg import RpgCommands

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
        match message.content.split()[0]:
            case 'b!roll':
                command = message.content.split()[1]
                if '+' in command:
                    dice, bonus = command.split('+')
                    roll = random.randint(1, int(dice))
                    result = f"Seu resultado foi {str(roll)} + {bonus} = {str(roll + int(bonus))}!"
                else:
                    roll = random.randint(1, int(command))
                    result = f"Seu resultado foi {str(roll)} + 0 = {str(roll)}!"
                print(result)
                await message.channel.send(result)

            case 'b!canta':
                await message.channel.send(f"Vai toma no cu")
            case 'b!rpg':
                category = message.content.split()[1]
                match category:
                    case 'party':
                        print(f'hello world!')
                    case 'character':
                        result = RpgCommands.character(message.content.split()[2:], message.author.name)
                        await message.channel.send(result + " from player " + message.author.mention)


client.run(TOKEN)
