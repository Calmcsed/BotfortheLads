import discord
from discord.ext import commands
from dotenv import load_dotenv
from functionsOfBot import *
import os
import time
import logging

starttime = time.time()
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "b&" in message.content.lower():
        await message.channel.send("Lock it. Lock it now. This is the friendlist message I will send while I look for ways to get you banned from GitHub for gross social misconduct.")

    if isProfane(message, str(message.channel.id)):
           await message.add_reaction(r'\:bonkstick:807123014360760380')

    if appreciation(message):
        await message.channel.send("Thank you! <3")

    if sad(message):
        await message.channel.send("):")

    #IT IS EXTRREMELY IMPORTANT TO ADD THIS LINE
    #THIS LINE ALLOWS EVENT COMMANDS TO BE RUN
    await bot.process_commands(message)

@bot.command(
    #Adding a help thing to this
    help = "A basic ping command to see if this works. Use !ping to run this command",
    brief = "A basic ping command to see if this works. Use !ping to run this command"    
)
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command(
    help = "Current options available are: grape, pineapple, apple, banana. Results may not come out as expected (screw you discord formatting) Use !fruit [fruit]"
    ,brief = "A command that prints out an ASCII representation of a fruit."
)
async def fruit(ctx,args):
    await ctx.channel.send(fruitReturn(args.lower()))

@bot.command(
    help = "A command to check the uptime of the bot.",
    brief = "Uptime status command"
)
async def uptime(ctx):
    await ctx.channel.send(getUptime((time.time() - starttime)))

@bot.command(
    help = "Sends a gif of an enchanted stick, or a superbonk",
    brief = "Use this against your horny friends for massive damage"
)
async def superbonk(ctx):
    await ctx.channel.send("https://files.calced.net/DebugStick.gif")

@bot.command(
    help = "Sends a gif of a banana",
    brief = "KRIS GET THE BANANA"
)
async def banana(ctx):
    await ctx.channel.send("https://files.calced.net/365.gif")

@bot.command(
    help = "Converts the at.tumblr.com link to a regular permalink"
)
async def c(ctx, args):
    await ctx.channel.send(betterLink(args.lower()))

@bot.command(
    help = "Send a gif of our beloved popped sickle"
)
async def boy(ctx):
    await ctx.channel.send("https://files.calced.net/poppedsickle.gif")

@bot.command(
    help = "Send a picture of a beanis"
)
async def beanis(ctx):
    await ctx.channel.send("https://files.calced.net/beanis.png")

@bot.command(
    help = "Send a picture of a ralsei splat"
)
async def ralsei(ctx):
    await ctx.channel.send("https://files.calced.net/ralsei.png")

@bot.command(
    help = "Send a picture of a AOUUGHHHUHG I HATE HIM"
)
async def morgott(ctx):
    await ctx.channel.send("https://files.calced.net/morgott.png")

bot.run(os.getenv('DISCORD_TOKEN'), log_handler=handler)
