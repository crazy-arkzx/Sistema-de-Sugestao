import discord
from discord.ext import commands

TOKEN = "TOKEN"
CANAL = 12345678910

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.channel.id == CANAL and not message.author.bot:
        await message.add_reaction("✅")
        await message.add_reaction("❌")

    await bot.process_commands(message)

bot.run(TOKEN)