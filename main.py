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
  ranktext = pytesseract.image_to_string(Image.open("rankpic.png"),config='--psm 11')
  print(ranktext)
  if ranktext.count("Titan") > 1:
        await ctx.channel.send("titan rank")
  elif ranktext.count("Angelus") > 1:
        await ctx.channel.send("angelus rank")
  elif ranktext.count("Ofanim") > 1:
        await ctx.channel.send("ofanim rank")
  elif ranktext.count("Cherubim") > 1:
        await ctx.channel.send("cherubim rank")
  elif ranktext.count("Seraphim") > 1:
        await ctx.channel.send("seraphim rank")
  elif ranktext.count("Archangel") > 1:
        await ctx.channel.send("archangel rank")
  elif ranktext.count("Almighty") > 1:
        await ctx.channel.send("almighty rank")
  print(ranktext)



client.run(token)
