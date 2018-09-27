import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


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
print ("user has pinged.")

@bot.command(pass.pass_context=True)
async def info(ctx, user, discord.Member):
await bot.say("The users name is: {}".format(user.name))
await bot.say("The use ID is:".format(iser.id))
await bot.say("The users status is:".format(user.status))
await bot.say("The users highest rank is:".format(user.top_rule))
await bot.say("The user joined at:".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord_Member):
await bot.say(":boot: Bye Bye I hope you enjoyed your stay".format(user.name))
await bot.kick(user)

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
    
    #welke servers die zit
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    
    #portfolio
    embed.add_field(name="Portfolio", value="https://81307.ict-lab.nl/Portfolio")
    
    await ctx.send(embed=embed)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)
    


bot.run(TOKEN)
