import discord
from discord.ext import commands
import os
import requests
import cv2
import numpy as np

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
  if ctx.author == client.user:
    return
  if ctx.author.bot:
    return
    
  attachment = ctx.attachments[0]
  response = requests.get(attachment.url)

  file = open("rankpic.png", "wb")
  file.write(response.content)
  file.close()
  
  image = cv2.imread("rankpic.png")
  hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

  yellow_lo=np.array([252, 157, 3])
  yellow_hi=np.array([219, 252, 3])
  mask=cv2.inRange(hsv,yellow_lo,yellow_hi)

  image[mask>0]=(0,0,0)

  cv2.imwrite("rankpic-1.png",image)
  await ctx.channel.send(file=discord.File('rankpic-1.png'))

  img = cv2.imread('rankpic-1.png')
  img[img != 0] = 255 # change everything to white where pixel is not black
  cv2.imwrite('rankpic-edited.png', img)

  ranktext = pytesseract.image_to_string(Image.open('rankpic-edited.png'),config='--psm 11')
  print(ranktext)
  await ctx.channel.send("edited pic")
  await ctx.channel.send(file=discord.File('rankpic-edited.png'))
    
    
    
    
    
    #if ranktext.count("Titan") > 0:
     #   await ctx.channel.send("titan rank")
  #elif ranktext.count("Angelus") > 0:
   #     await ctx.channel.send("angelus rank")
  



client.run(token)
