import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


"""Author Luuk de Haas and Jesse Akoma"""

TOKEN = 'NDkxNTA0NTg4NzQ3NDQwMTI4.DoI1RA.pzurKfgfNlcX94pbspDyzkl2lOU'

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('are you ready??')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')




@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say ("Pong")
print ("user has pinged.")



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
    
    #auteur
    embed.add_field(name="Author", value="Luuk de Haas")
    

    
    #portfolio
    embed.add_field(name="Portfolio", value="https://81307.ict-lab.nl/Portfolio")
    
    await ctx.send(embed=embed)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) #haald de aantal berichten om te verwijderen.
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
if counter < number:
    await bot.delete_message(x)
    counter += 1
    await asyncio.sleep(1.2) #secondes van de timer die het delete proces kan verwerken



bot.run(TOKEN)
