import discord
from discord.ext import commands
import requests
from time import sleep
from bs4 import BeautifulSoup
from rut_chile.rut_chile import format_rut_with_dots
client = commands.Bot(command_prefix = ';')
@client.event
async def on_ready():
    print('Bot is ready')
@client.command(aliases=['doxxnombre','testnombre'])
async def doxxname(ctx,arg):
    user = ctx.message.author
    name = arg.replace("_"," ")
    URL = "https://www.nombrerutyfirma.com/buscar"
    historialname = open('historialname.txt', 'w')
    namehistorial = name + "/n"
    historialname.write(namehistorial)
    print("procesando nombre:", name)
    response = requests.get(URL, params={'term': name}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    address = out[3].text + " " + out[4].text
    rutdoxx = out[1].text
    print("RUT encontrado:", out[1].text)
    print("dirección:", address)
    Doxxtotal = "Resultados" + name + " ," + rutdoxx + " ," + address
    await ctx.send(Doxxtotal)
@client.command(aliases=['doxxruts','test'])
async def doxxrut(ctx,arg):
    user = ctx.message.author
    rut = arg
    URL = "https://www.nombrerutyfirma.com/rut"
    historialrut = open('historialrut.txt', 'w')
    ruthistorial = rut + "/n"
    historialrut.write(ruthistorial)
    response = requests.get(URL, params={'term': format_rut_with_dots(rut)}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    address = out[3].text + " " + out[4].text
    nombrerut = out[0].text
    Doxxtotalrut = "Resultados: " + nombrerut + " ," + rut + " ," + address
    await ctx.send(Doxxtotalrut)
client.run("INSERT_TOKEN_HERE")