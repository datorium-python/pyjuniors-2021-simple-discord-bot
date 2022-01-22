from discord import Client, TextChannel
from messages import *

client = Client()


@client.event
async def on_ready():

    channels = client.get_all_channels()
    for channel in channels:

        if isinstance(channel, TextChannel):
            await channel.send(f'Hi! {client.user} is online!')


    print(f'{client.user} has come online...')


@client.event
async def on_message(message):

    if message.content.startswith('!hello'):

        text = say_hello()
        await message.channel.send(text)

    if message.content.startswith('!calc'):

        text = calc(message.content)
        await message.channel.send(text)

    if message.content.startswith('!spam'):

        amount, text = spam(message.content)

        for _ in range(amount):
            await message.channel.send(text)


client.run('tavs token')