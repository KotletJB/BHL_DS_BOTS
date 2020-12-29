#!/usr/bin/env python3

import discord
import asyncio

bot = discord.Client()
with open('../token_BHL_DS.txt') as f:
    token = f.read().strip()

@bot.event
async def on_message(message):
    print(message.content)

    with open('responde_massage.csv') as f:
        x = f.readlines()
        key_words = {}
        for element in x:
            key, value = element.strip().split(',')
            key_words[key] = value

    if message.content in key_words:
        await message.channel.send(key_words[massage.content])
        
bot.run(token)