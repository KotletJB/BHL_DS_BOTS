#!/usr/bin/env python3

import discord
import asyncio

bot = discord.Client()
with open('../token_BHL_DS.txt') as f:
    token = f.read().strip()

@bot.event
async def on_message(message):
    print(message.content)

bot.run(token)