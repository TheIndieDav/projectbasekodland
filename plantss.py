import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, riega a mis amigos, soy {bot.user}!')

@bot.command()
async def plant(ctx, times: int, content='Cuando plantamos árboles, plantamos las semillas de la paz y de la esperanza'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run("eso tilin")