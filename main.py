import discord
from discord.ext import commands
import os
import requests

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

token = os.getenv('token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        
client = MyClient()
        
@client.event
async def on_message(ctx):
  attachment = ctx.attachments[0]
  response = requests.get(attachment.url)

  file = open("rankpic.png", "wb")
  file.write(response.content)
  file.close()
  ranktext = pytesseract.image_to_string(Image.open("rankpic.png"),config='--psm 4')
  print(ranktext)
  if ranktext.count("Master") > 1:
        await ctx.channel.send("master rank")
  elif ranktext.count("Grandmaster") > 1:
        await ctx.channel.send("Grandmaster rank")
  elif ranktext.count("Hero") > 1:
        await ctx.channel.send("Hero rank")
  elif ranktext.count("Superhero") > 1:
        await ctx.channel.send("Superhero rank")
  elif ranktext.count("Persona") > 1:
        await ctx.channel.send("Persona rank")
  elif ranktext.count("Demigod") > 1:
        await ctx.channel.send("Demigod rank")
  await ctx.channel.send(ranktext)



client.run(token)
