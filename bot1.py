#!/usr/bin/env python3

import discord
import asyncio
from discord.ext import commands

#creating insatns of bot
bot = discord.Client()

#geting token from file
with open('../token_BHL_DS.txt') as f:
    token = f.read().strip()


#bot behavior
@bot.event #respodnig on specif messeges
async def on_message(message):
    print(message.content)

    with open('responde_massage.csv') as f:
        x = f.readlines()
        key_words = {}
        for element in x:
            key, value = element.strip().split(',')
            key_words[key] = value

    if message.content in key_words:
        await message.channel.send(key_words[message.content])


@bot.event #Welcome new users
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Witaj na kanale BHL{member.name}!'
    )






bot.run(token)
