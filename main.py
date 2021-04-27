
spammerid = []
spammerspams = []
import os
import random
from keep_alive import keep_alive
import discord
import http
import time
from time import sleep
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from asyncio import sleep
class MyClient(discord.Client):
    async def on_ready(self):
        global spammerid, spammerspams
        await client.change_presence(activity=discord.Game(name="Minecraft and Muppets"))
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format
        (self.user))
        print(self.user.id)
        print(self.user.avatar_url)
        from time import sleep
       
        
    async def on_message(self, message):
      
      print('message')
      if message.author.bot or message.channel.id == 809382402610036767:
        return
      with open('spammerid.txt', 'r') as f:
        spammerid = list(f.read().split(', '))
      with open('spammerspams.txt', 'r') as f:
        spammerspams = list(f.read().split(', '))
      
      print(spammerid)
      print(spammerspams)
      print(spammerspams.index('1'))
      try:
        
        spammerspams[spammerid.index(str(message.author.id))] = str(int(spammerspams[spammerid.index(str(message.author.id))]) + 1)
      except:
        spammerid.append(str(message.author.id))
        spammerspams.append('1')
      for spam in range(len(spammerid)):
        print('spam check')
        try:
          if int(spammerspams[spam]) >= 7:
            print('omg')
            for member in client.guilds[0].members:
              print(member)
              print(client.guilds[0])
              if int(spammerid[spam]) == member.id:
                print('ergtsrfddghnfgf')

                await member.add_roles(client.guilds[0].get_role(834841196979028088))
        except:
          print('error')
      
      with open('spammerid.txt', 'w') as f:
        f.write(str(spammerid).replace('[', '').replace(']', '').replace("'", ''))
      with open('spammerspams.txt', 'w') as f:
        f.write(str(spammerspams).replace('[', '').replace(']', '').replace("'", ''))

if os.fork():
          
          print('ree')
          from time import sleep
          
          while True:
            with open('spammerid.txt', 'w') as f:
              f.write('1')
            with open('spammerspams.txt', 'w') as f:
              f.write('1')
            
            sleep(10)
            print('reset')
            
else:
          print('forked')
          spammerid = []
          spammerspams = []

    

intents = intents = discord.Intents().all()
keep_alive()
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
