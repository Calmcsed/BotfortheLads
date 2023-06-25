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


handler = logging.FileHandler(filename=(os.getenv('DISCORD_DIR')+"discord.log"), encoding='utf-8', mode='a')
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
    help = "Converts the at.tumblr.com link to a regular permalink"
)
async def c(ctx, args):
    await ctx.channel.send(betterLink(args.lower()))

@bot.command(
    help = ("Invoke a hot key you have already created." + 
    "\n Command format is !hotkey [name of the hotkey or its alias]" + 
    "\n To add a new hotkey, do !addhotkey. To list your hotkeys, do !listhotkey. To delete a hotkey, do !delhotkey."),
    aliases = ["h"]
)
async def hotkey(ctx, *args):
    await ctx.channel.send(sendHotkey(ctx.author.id, args))

@bot.command(
    help = ("List all created hotkeys." + 
    "\n Command format is !listhotkey [-all (for all details), -name (for only the names)]. For example, listing all available hotkey is !listhotkey -all." + 
    "\n To add a new hotkey, do !addhotkey. To invoke a hotkey, do !hotkey. To delete a hotkey, do !delhotkey."),
    aliases = ['lhk']
)
async def listhotkey(ctx, *args):
    await ctx.channel.send(listHotkey(ctx.author.id, args))
    
@bot.command(
    help = ("Delete a hotkey." + 
    "\n Command format is !delhotkey [name of hotkey or its alias]" + 
    "\n To add a new hotkey, do !addhotkey. To list your hotkeys, do !listhotkey. To invoke a hotkey, do !hotkey."),
    aliases = ['dhk']
)
async def delhotkey(ctx, *args):
    await ctx.channel.send(delHotkey(ctx.author.id, args))

@bot.command(
    help = ("Create a new hotkey. If given an existing hotkey name, will edit the link." +
    "\n Command format is !addhotkey [name of hotkey] [link to send] [alias (optional)]" + 
    "\n!hotkey  To invoke a hotkey, do !hotkey. To list your hotkeys, do !listhotkey"),
    aliases = ['ahk']
)
async def addhotkey(ctx, *args):
    await ctx.channel.send(addHotkey(ctx.author.id, args))

bot.run(os.getenv('DISCORD_TOKEN'), log_handler=handler)
