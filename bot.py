import discord
import random
from discord.ext import commands

TOKEN = open("token.txt", "r").readline()
client = commands.Bot(command_prefix = '~')

client.remove_command('help')

@client.command()
async def wholesome(ctx):
    responses = open('./text files/quotes.txt').read().splitlines()
    random.seed(a = None)
    response = random.choice(responses)
    await ctx.send(response)

@client.command()
async def pickup(ctx):
    responses = open('./text files/pickuplines.txt').read().splitlines()
    random.seed(a = None)
    response = random.choice(responses)
    await ctx.send(response)

@client.command()
async def coco(ctx):
    response = "You are the most perfect human there is to exist in history!"
    await ctx.send(response)

@client.command()
async def hello(ctx):
    await ctx.send('Hello, I\'m the SimpBot :) Have a great day!')

@client.command()
async def meme(ctx):
    responses = open('./text files/memes.txt').read().splitlines()
    random.seed(a = None)
    response = './memes/'+random.choice(responses)
    await ctx.send(file = discord.File(response))

@client.command()
async def love(ctx):
    responses = open('./text files/love.txt').read().splitlines()
    random.seed(a = None)
    response = './love/'+random.choice(responses)
    await ctx.send(file = discord.File(response))

@client.command()
async def she(ctx):
    responses = open('./text files/twss.txt').read().splitlines()
    random.seed(a = None)
    response = './twss/'+random.choice(responses)
    await ctx.send(file = discord.File(response))

@client.command()
async def cheerup(ctx):
    responses = open('./text files/cheerup.txt').read().splitlines()
    random.seed(a = None)
    response = './cheerup/'+random.choice(responses)
    await ctx.send(file = discord.File(response))

@client.command()
async def homie(ctx):
    responses = open('./text files/homies.txt').read().splitlines()
    random.seed(a = None)
    response = './homies/'+random.choice(responses)
    await ctx.send(file = discord.File(response))

@client.command()
async def ily(ctx):
    responses = open('./text files/ily.txt').read().splitlines()
    random.seed(a = None)
    response = random.choice(responses)
    await ctx.send(response)

@client.command()
async def qt(ctx):
    await ctx.send(file = discord.File('./memes/meme (40).jpg'))

@client.command()
async def noU(ctx):
    await ctx.send(file = discord.File('./love/noU.jpg'))

@client.command()
async def bb(ctx):
    await ctx.send(file = discord.File('./cheerup/bb.jpg'))

@client.command()
async def ohh(ctx):
    await ctx.send(file = discord.File('./love/bestf.png'))

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'({error}), use ~help for usage')

@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name = 'Help : list of commands available')
    embed.add_field(name = '~info', value = 'Gives info about the SimpBot', inline = False)
    embed.add_field(name = '~all', value = 'List of all commands', inline = False)
    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def all(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red())
    embed.set_author(name = 'All commands of SimpBot')
    embed.add_field(name = '~wholesome', value = 'Responds with a wholesome quote', inline = False)
    embed.add_field(name = '~meme', value = 'Posts a random whomesome meme', inline = False)
    embed.add_field(name = '~qt', value = 'Responds with you\'re a cutie meme', inline = False)
    embed.add_field(name = '~ily', value = 'Responds with an ily message', inline = False)
    embed.add_field(name = '~coco', value = 'Easter Egg ;)', inline = False)
    embed.add_field(name = '~pickup', value = 'Responds with a cheesy pickup-line', inline = False)
    embed.add_field(name = '~hello', value = 'Responds with have a nice day', inline = False)
    embed.add_field(name = '~love', value = 'Responds with a love meme', inline = False)
    embed.add_field(name = '~cheerup', value = 'Responds with a cheerup meme', inline = False)
    embed.add_field(name = '~noU', value = 'Responds with a uno reverse card', inline = False)
    embed.add_field(name = '~homie', value = 'Responds with a homies meme', inline = False)
    embed.add_field(name = '~bb', value = 'For the office fans', inline = False)
    embed.add_field(name = '~ohh', value = 'Remember the yellow sunglasses guy?', inline = False)
    embed.add_field(name = '~she', value = 'THAT\'S WHAT SHE SAID!', inline = False)
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name = 'Information')
    embed.add_field(name = 'What is it?', value = 'SimpBot is a discord bot made using `python` for Simpin content ;)', inline = False)
    embed.add_field(name = 'Hosting', value = 'Hosted on Heroku, currently in development stage', inline = False)
    embed.add_field(name = 'Author', value = 'Made with *UwU* by `Sunil B`', inline = False)
    embed.add_field(name = 'Visit', value = 'https://github.com/SunilBoopalan/SimpBot', inline = False)
    await ctx.send(embed = embed)

client.run(TOKEN)
