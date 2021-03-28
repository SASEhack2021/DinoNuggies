

# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import quickstart

quickstart.main()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='remindme', help='Responds with a confirmation of a reminder')
@commands.has_role('Admin')
async def nine_nine(ctx):
    Reminder = ['for now',]
    
    

    response = Reminder
    await ctx.send(response)

bot.run(TOKEN)