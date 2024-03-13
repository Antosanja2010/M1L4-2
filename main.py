import discord
from bot_logic import gen_pass
from igra import flip_coin



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client (intents=intents)
@client.event
async def on_ready():
    your_channel = client.guilds[0].text_channels[0]
    await your_channel.send (f'Привет!  Вы вошли в систему как...: {client.user} доступные команды,пароль-выдает вам случайных пароль от 13 символов,игра-кидает орел и решку.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('пароль'):
        await message.channel.send(gen_pass(13))
    

    if message.content.startswith('игра'):
        await message.channel.send(flip_coin())


    
    




client.run('')
