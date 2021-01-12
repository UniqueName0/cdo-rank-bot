import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
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

  file = open("rankpic-2.png", "wb")
  file.write(response.content)
  file.close()

  img1 = cv2.imread('rankpic-2.png')
  img1[img1 == 0] = 255 
  cv2.imwrite('rankpic-edited.png', img1)
  
  image = cv2.imread("rankpic-2.png")
  hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

  yellow_lo=np.array([23,120,120])
  yellow_hi=np.array([27,255,255])
  mask=cv2.inRange(hsv,yellow_lo,yellow_hi)

  image[mask>0]=(0,0,0)

  cv2.imwrite("rankpic-1.png",image)

  img = cv2.imread('rankpic-1.png')
  img[img != 0] = 255 
  cv2.imwrite('rankpic-edited.png', img)

  ranktext = pytesseract.image_to_string(Image.open('rankpic-edited.png'),config='--psm 11')
 
  if get(ctx.guild.roles, name="Master") == None:
    await ctx.guild.create_role(name="Master")
  master = discord.utils.get(ctx.guild.roles, name="Master")
    
    
    
    
    
    
  server = ctx.guild
  user = ctx.author
  ch = ctx.channel
    
  await Addrole("Master")
  await Addrole("GrandMaster")
  await Addrole("Hero")
  await Addrole("SuperHero")
  await Addrole("Persona")
  await Addrole("DemiGod")
  await Addrole("Titan")
  await Addrole("Angelus")
  await Addrole("Ofanim")
  await Addrole("Cherobim")
  await Addrole("Seraphim")
  await Addrole("ArchAngel")
  await Addrole("Almighty")
    
    
    
    
    
    
    
    
    
    
async def Addrole(role):
  if get(server.roles, name=role) == None:
    await server.create_role(name=role)
  role0 = discord.utils.get(server.roles, name=role)
  if ranktext.count(role) > 0:
    if master in user.roles:
      await user.remove_roles(master)
    if grandmaster in user.roles:
      await user.remove_roles(grandmaster)
    if hero in user.roles:
      await user.remove_roles(hero)
    if superhero in user.roles:
      await user.remove_roles(superhero)
    if persona in user.roles:
      await user.remove_roles(persona)
    if demigod in user.roles:
      await user.remove_roles(demigod)
    if titan in user.roles:
      await user.remove_roles(titan)
    if angelus in user.roles:
      await user.remove_roles(angelus)
    if ofanim in user.roles:
      await user.remove_roles(ofanim)
    if cherubim in user.roles:
      await user.remove_roles(cherubim)
    if seraphim in user.roles:
      await user.remove_roles(seraphim)
    if archangel in user.roles:
      await user.remove_roles(archangel)
    if almighty in user.roles:
      await user.remove_roles(almighty)
    await user.add_roles(role0)
    mention = user.mention
    await ch.send(f"{mention} now has the {role} role")
    
 
    
    
    


client.run(token)
