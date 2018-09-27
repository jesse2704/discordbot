import discord
from discord.ext import commands
"""Author Luuk de Haas and Jesse Akoma"""
"""Bot name Kelly""""
TOKEN = 'NDkxNTA0NTg4NzQ3NDQwMTI4.DoI1RA.pzurKfgfNlcX94pbspDyzkl2lOU'

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say ("Pong")

@bot.command()
async def hello():
    """Says world"""
    await bot.say("Hello there, how can I help you?")

@bot.command()
async def music(ctx):
    await bot.say("https://www.youtube.com/watch?v=qU5FWU0SH0o  also https://www.youtube.com/watch?v=Rw-hw7rVOrA")

@bot.command()
async def website(ctx):
    await bot.say("This is the Portfolio of Luuk de Haas https://81307.ict-lab.nl/Portfolio")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="Luuk de Haas")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Portfolio", value="https://81307.ict-lab.nl/Portfolio")
    
    await ctx.send(embed=embed)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)
    


bot.run(TOKEN)
