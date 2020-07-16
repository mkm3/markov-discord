import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        await message.channel.send('Hello!')


client.run(os.environ['DISCORD_TOKEN'])
