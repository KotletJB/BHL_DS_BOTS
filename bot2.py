#!/usr/bin/env python3

import discord
import asyncio
from discord.ext import commands
import subprocess


#creating insatns of bot
bot_command = commands.Bot(command_prefix='! ')

#geting token from file
with open('../token_BHL_DS.txt') as f:
    token = f.read().strip()


#bot commands
@bot_command.command(name='helpme') # help command
async def help(ctx):
    response = 'lore ipsum dole'

    await ctx.channel.send(response)



@bot_command.command(name='move')
async def get_members(ctx):
    x = bot_command.users
    print(x)

bot_command.run(token)


    

