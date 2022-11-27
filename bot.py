import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!help'):
        await message.channel.send('no')
    if '4chan' in message.content:
        await message.channel.send(file=discord.File('images/pepebased.png'))
    if 'gaslighting' in message.content: 
        await message.channel.send('Gaslighting??? whats that?? what are you talking about? stop making up words.')




client.run(os.getenv('TOKEN'))
