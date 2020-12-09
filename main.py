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

  yellow_lo=np.array([23,41,133])
  yellow_hi=np.array([40,150,255])
  mask=cv2.inRange(hsv,yellow_lo,yellow_hi)

  image[mask>0]=(0,0,0)

  cv2.imwrite("rankpic-1.png",image)
  await ctx.channel.send(file=discord.File('rankpic-1.png'))

  img = Image.open("rankpic-1.png") # get image
  pixels = img.load() # create the pixel map

  for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
      if pixels[i,j] != (0,0,0): # if not black:
        pixels[i,j] = (255, 255, 255) # change to white

  img.save("rankpic-edited.png")

  ranktext = pytesseract.image_to_string(Image.open('rankpic-edited.png'),config='--psm 11')
  print(ranktext)
  await ctx.channel.send("edited pic")
  await ctx.channel.send(file=discord.File('rankpic-edited.png'))
    
    
    
    
    
    #if ranktext.count("Titan") > 0:
     #   await ctx.channel.send("titan rank")
  #elif ranktext.count("Angelus") > 0:
   #     await ctx.channel.send("angelus rank")
  



client.run(token)
