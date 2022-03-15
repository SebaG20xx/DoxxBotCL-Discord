import discord
from discord.ext import commands
import requests
from time import sleep
from bs4 import BeautifulSoup
client = commands.Bot(command_prefix = ';')
@client.event
async def on_ready():
    print('Bot is ready')
@client.command(aliases=['doxxnombre','testnombre'])
async def doxxname(ctx,arg):
    user = ctx.message.author
    name = arg.replace("_"," ")
    URL = "https://www.nombrerutyfirma.com/buscar"
    inputfile = open('Historialname.txt', 'w')
    inputfile.write(name)
    print("procesando nombre:", name)
    response = requests.get(URL, params={'term': name}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    address = out[3].text + " " + out[4].text
    rutdoxx = out[1].text
    Doxxtotal = "Resultados: " + name + ", " + rutdoxx + ", " + address
    await ctx.send(Doxxtotal)
client.run("INSERTE TOKEN AQUÍ")
