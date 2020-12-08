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
  ranktext = pytesseract.image_to_string(Image.open("rankpic.png"))
  print(ranktext)
  await ctx.channel.send(ranktext.count("Master", beg= 0, end=len(ranktext)))



client.run(token)
