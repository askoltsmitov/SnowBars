import discord
import os

bot = discord.Client()


@bot.event
async def on_message(message):
    if message.author.name == 'Vexera':
        await message.delete(delay=10)

    if message.content.startswith('-'):
        await message.delete(delay=3)


bot.run(os.getenv('TOKEN'))
