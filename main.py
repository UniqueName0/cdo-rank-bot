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
  img1[img1 == 0] = 255 # change everything to white where pixel is not black
  cv2.imwrite('rankpic-edited.png', img1)
  
  image = cv2.imread("rankpic-2.png")
  hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

  yellow_lo=np.array([23,120,120])
  yellow_hi=np.array([27,255,255])
  mask=cv2.inRange(hsv,yellow_lo,yellow_hi)

  image[mask>0]=(0,0,0)

  cv2.imwrite("rankpic-1.png",image)

  img = cv2.imread('rankpic-1.png')
  img[img != 0] = 255 # change everything to white where pixel is not black
  cv2.imwrite('rankpic-edited.png', img)

  ranktext = pytesseract.image_to_string(Image.open('rankpic-edited.png'),config='--psm 11')
   
  
  if get(ctx.guild.roles, name="Master") == None:
    await ctx.guild.create_role(name="Master")
  master = discord.utils.get(ctx.guild.roles, name="Master")
  if get(ctx.guild.roles, name="GrandMaster") == None:
    await ctx.guild.create_role(name="GrandMaster")
  grandmaster = discord.utils.get(ctx.guild.roles, name="GrandMaster")
  if get(ctx.guild.roles, name="Hero") == None:
    await ctx.guild.create_role(name="Hero")
  hero = discord.utils.get(ctx.guild.roles, name="Hero")
  if get(ctx.guild.roles, name="SuperHero") == None:
    await ctx.guild.create_role(name="SuperHero")
  superhero = discord.utils.get(ctx.guild.roles, name="SuperHero")
  if get(ctx.guild.roles, name="Persona") == None:
    await ctx.guild.create_role(name="Persona")
  persona = discord.utils.get(ctx.guild.roles, name="Persona")
  if get(ctx.guild.roles, name="DemiGod") == None:
    await ctx.guild.create_role(name="DemiGod")
  demigod = discord.utils.get(ctx.guild.roles, name="DemiGod")
  if get(ctx.guild.roles, name="Titan") == None:
    await ctx.guild.create_role(name="Titan")
  titan = discord.utils.get(ctx.guild.roles, name="Titan")
  if get(ctx.guild.roles, name="Angelus") == None:
    await ctx.guild.create_role(name="Angelus")
  angelus = discord.utils.get(ctx.guild.roles, name="Angelus")
  if get(ctx.guild.roles, name="Ofanim") == None:
    await ctx.guild.create_role(name="Ofanim")
  ofanim = discord.utils.get(ctx.guild.roles, name="Ofanim")
  if get(ctx.guild.roles, name="Cherubim") == None:
    await ctx.guild.create_role(name="Cherubim")
  cherubim = discord.utils.get(ctx.guild.roles, name="Cherobim")
  if get(ctx.guild.roles, name="Seraphim") == None:
    await ctx.guild.create_role(name="Seraphim")
  seraphim = discord.utils.get(ctx.guild.roles, name="Seraphim")
  if get(ctx.guild.roles, name="ArchAngel") == None:
    await ctx.guild.create_role(name="ArchAngel")
  archangel = discord.utils.get(ctx.guild.roles, name="ArchAngel")
  if get(ctx.guild.roles, name="Almighty") == None:
    await ctx.guild.create_role(name="Almighty")
  almighty = discord.utils.get(ctx.guild.roles, name="Almighty")
    
    
    
    
  if ranktext.count("Master") > 0:
    user = ctx.author
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
    await user.add_roles(master)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Master role")
    
    
  if ranktext.count("Grandmaster") > 0:
    user = ctx.author
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
    await user.add_roles(grandmaster)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the GrandMaster role")
    
    
  if ranktext.count("Hero") > 0:
    user = ctx.author
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
    await user.add_roles(hero)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Hero role")
    
    
  if ranktext.count("Superhero") > 0:
    user = ctx.author
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
    await user.add_roles(superhero)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the SuperHero role")
    
  
  if ranktext.count("Persona") > 0:
    user = ctx.author
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
    await user.add_roles(persona)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Persona role")
    
    
  if ranktext.count("DemiGod") > 0:
    user = ctx.author
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
    await user.add_roles(demigod)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the DemiGod role")
    
    
  if ranktext.count("Titan") > 0:
    user = ctx.author
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
    await user.add_roles(titan)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Titan role")
    
    
  if ranktext.count("Angelus") > 0:
    user = ctx.author
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
    await user.add_roles(angelus)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Angelus role")
    
    
  if ranktext.count("Ofanim") > 0:
    user = ctx.author
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
    await user.add_roles(ofanim)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Ofanim role")
    
    
  if ranktext.count("Cherubim") > 0:
    user = ctx.author
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
    await user.add_roles(cherubim)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Cherubim role")
    
    
  if ranktext.count("Seraphim") > 0:
    user = ctx.author
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
    await user.add_roles(seraphim)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Serphim role")
    
    
  if ranktext.count("Archangel") > 0:
    user = ctx.author
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
    await user.add_roles(archangel)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the ArchAngel role")
    
    
  if ranktext.count("Almighty") > 0:
    user = ctx.author
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
    await user.add_roles(almighty)
    mention = user.mention
    await ctx.channel.send(f"{mention} now has the Almighty role")
    
    
    


client.run(token)
