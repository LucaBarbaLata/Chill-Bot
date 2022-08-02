from ast import JoinedStr
from cgi import test
from logging import exception
from multiprocessing.connection import Client
from pyexpat.errors import messages
from tokenize import Token
from urllib import response
import discord
import random
import os
import time
import asyncio
from requests import get
from discord import Webhook, RequestsWebhookAdapter
import datetime
import time
from discord.ext import commands
import keep_alive
import json
from pytube import YouTube


client = discord.Client()
client = commands.Bot(command_prefix = '.')


global count
count = 1


TOKEN = os.environ['token']




@client.event
async def on_ready():
    print('I have logged in as {0.user} '.format(client))
    await client.change_presence(status=discord.Status.dnd, activity = discord.Game(name=f'.help for a list of commands! 🥳 🎉 Currently in {len(client.guilds)} servers! 🎉'))




  
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    with open("log.txt", "a") as f:
      f.write(time.ctime())
      f.write(f' {username}: {user_message} ({channel})\n')
    if message.author == client.user:
        return
    if message.channel.name == '🍓general':
        if user_message.lower() == 'hello':
            await message.reply(f'Hello {username}!')
            return
        elif user_message.lower() == '.profile':
          name = message.author
          await message.channel.send(name)
        elif user_message.lower() == '.owner':
          response = 'Luca-rickrolled-himself is my owner'
          await message.channel.send(response)
          return
        elif user_message.lower() == ".kpop":
          with open("k-pop.txt", "r") as f:
            v = f.readlines()
          song = random.choice(v)
          yt = YouTube(song)
          title = "Title: ",yt.title
          NV = "Number of views: ",yt.views
          LV = "Length of video: ",yt.length
          RV = "Rating of video: ",yt.rating
          await message.channel.send(title)
          await message.channel.send(NV)
          await message.channel.send(LV)
          await message.channel.send(RV)
          await message.channel.send(song)
          return
        elif user_message.lower() == 'bye':
            await message.reply(f'See you later {username}.')
            return 
        elif user_message.lower() == 'hi':
            response = f'Hello {username}.'
            await message.reply(response)
            return
        elif user_message.lower() == 'its my birthday':
            response = f'Happy Birthday {username}'
            await message.reply(response)
            return
        elif user_message.lower() == '.source':
            link = 'https://github.com/LucaBarbaLata/Chill-Bot'
            await message.channel.send(link)
        elif user_message.lower() == 'uwu':
            response = 'UwU'
            await message.channel.send(response)
            return
        elif user_message.lower() == ".fact":
          with open("facts.txt", "r") as f:
            v = f.readlines()
          await message.channel.send(random.choice(v))
          return
        elif user_message.lower() == '<@966018572352639007>':
            await message.channel.send('Hi')
        elif user_message.lower() == '.count':
            global count
            count +=1
            res = f"The current number is {count}. The next number is {count + 1}"
            await message.channel.send(res)
            with open("count.txt", "w") as f:
              f.write(str(count))
        elif user_message.lower() == 'ass':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="ass", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'sex':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="sex", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'fuck':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="fuck", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'gay':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="gay", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'nigga':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="nigga", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'dick':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="dick", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'bitch':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="bitch", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
        elif user_message.lower() == 'ass':
            await message.reply(f"Dont use that word! {username}")
            await message.delete()
            channel = client.get_channel(961644384481316875)
            embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#961633965394001953>", color=0xbd0000)
            embed.add_field(name="KeyWord:", value="ass", inline=True)
            embed.add_field(name="Author:", value=message.author.mention, inline=True)
            await channel.send(embed=embed)
            help = '<@&961642369592197140> <@&964548735260565535>'
            await channel.send(help)
    if message.channel.name == '🤖bot-commands':
        if user_message.lower() == '.random':
            response = f'This is your random number: {random.randrange(1000000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '.help':
            embed=discord.Embed(title="Help", description="This is a list of all availabe commands:", color=0x391fff)
            embed.add_field(name="1. .random", value="(Displays you a random number)", inline=False)
            embed.add_field(name="2. .help", value="(Displays you a list with all avaiable commands)", inline=False)
            embed.add_field(name="3. .webhook", value="(Send an webhook message)", inline=False)
            embed.add_field(name="4. .online/.idle/.dnd", value="(Set the status of the bot)", inline=False)
            embed.add_field(name="5. .ping", value="(Displays the delay of the bot)", inline=True)
            embed.add_field(name="6. .fact", value="(Displays a random fact)", inline=False)
            embed.add_field(name="7. .meme", value="(Displays you a random meme)", inline=False)
            embed.add_field(name="8. .count", value="(Count with other people)", inline=True)
            embed.add_field(name="9. .kpop", value="(Displays you a random k-pop song)", inline=False)
            embed.set_footer(text="Thats it, have fun!")
            await message.reply("Check DM's")
            await message.author.send(embed=embed)
            return
        elif user_message.lower() == '.ping':
            response = (f'**Pong** {round(client.latency * 1000)}ms')
            await message.reply(response)
            return
        elif user_message.lower() == '.':
            response = 'Thats my prefix!'
            await message.channel.send(response)
            return
        elif user_message.lower() == '..':
            response = 'What???'
            await message.channel.send(response)
            return
        elif user_message.lower() == '.webhook':
          response = 'Webhook Is Preparing!'
          await message.channel.send(response)
          time.sleep(2)
          response = 'Setup Is Starting'
          webhook = Webhook.from_url(os.environ['webhook'], adapter=RequestsWebhookAdapter())
          webhook.send("Hello World")
          return
        elif user_message.lower() == '.idle':
          await client.change_presence(status=discord.Status.idle, activity=discord.Game('morache.go.ro/wordpress'))
          await message.delete() 
          return
        elif user_message.lower() == '.online':
          await client.change_presence(status=discord.Status.online, activity=discord.Game('morache.go.ro/wordpress'))
          await message.delete() 
          return
        elif user_message.lower() == '.dnd':
          await client.change_presence(status=discord.Status.dnd, activity=discord.Game('morache.go.ro/wordpress'))
          await message.delete() 
          return
        elif user_message.lower() == '.owner':
          response = 'Luca-rickrolled-himself is my owner'
          await message.channel.send(response)
          return
        elif user_message.lower() == ".kpop":
          with open("k-pop.txt", "r") as f:
            v = f.readlines()
          song = random.choice(v)
          yt = YouTube(song)
          title = "Title: ",yt.title
          NV = "Number of views: ",yt.views
          LV = "Length of video: ",yt.length
          RV = "Rating of video: ",yt.rating
          await message.channel.send(title)
          await message.channel.send(NV)
          await message.channel.send(LV)
          await message.channel.send(RV)
          await message.channel.send(song)
          return
    if message.channel.name == '😂memes':
        if user_message.lower() == '.meme':
           content = get("https://meme-api.herokuapp.com/gimme").text
           data = json.loads(content,)
           meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
           await message.reply(embed=meme)
    if message.channel.name == 'test':
      if user_message.lower() == 'ass':
          await message.reply(f"Dont use that word! {username}")
          await message.delete()
          channel = client.get_channel(1002608638571061369)
          embed=discord.Embed(title="Bad Word Detected!", description="BadWord detected in <#1002608638571061369>", color=0xbd0000)
          embed.add_field(name="KeyWord:", value="ass", inline=True)
          embed.add_field(name="Author:", value=message.author.mention, inline=True)
          await channel.send(embed=embed)
          help = ' <@&964548735260565535>'
          await channel.send(help)
      elif user_message.lower() == ".kpop":
          with open("k-pop.txt", "r") as f:
            v = f.readlines()
          song = random.choice(v)
          yt = YouTube(song)
          title = "Title: ",yt.title
          NV = "Number of views: ",yt.views
          LV = "Length of video: ",yt.length
          RV = "Rating of video: ",yt.rating
          await message.channel.send(title)
          await message.channel.send(NV)
          await message.channel.send(LV)
          await message.channel.send(RV)
          await message.channel.send(song)
          return
keep_alive.keep_alive()
client.run(TOKEN)

