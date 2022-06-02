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
    historialname = open('historialname.txt', 'a')
    namehistorial = name + ", Solicitado por: " + str(ctx.message.author)  + ", " + "Id Discord: " + str(ctx.message.author.id)  + '\n'
    historialname.write(namehistorial)
    response = requests.get(URL, params={'term': name}).text
    soup = BeautifulSoup(response, 'html.parser')
    banned = False
    out = soup.find_all('td')
    botprotection = (soup.find_all('h2'))
    if botprotection != []:
        banned = True
    if out == [] and banned == False:
        await ctx.send("No hay resultados disponibles")
    elif banned == True:
        await ctx.send("El bot ha sido baneado :(")
    else:
        address = out[3].text + " " + out[4].text
        rutdoxx = out[1].text
        namedoxx = out[0].text
        Doxxtotal = "Resultado para: " + name
        await ctx.send(Doxxtotal)
        Doxxtotal = namedoxx + " ," + rutdoxx + " ," + address
        await ctx.send(Doxxtotal)
        await ctx.send("Nota, este es solo el primer resultado de la búsqueda.")
@client.command(aliases=['doxxruts','test'])
async def doxxrut(ctx,arg):
    user = ctx.message.author
    rut = arg
    URL = "https://www.nombrerutyfirma.com/rut"
    historialrut = open('historialrut.txt', 'a')
    ruthistorial = rut + ", Solicitado por: " + str(ctx.message.author)  + ", " + "Id Discord: " + str(ctx.message.author.id)  + '\n'
    historialrut.write(ruthistorial)
    response = requests.get(URL, params={'term': format_rut_with_dots(rut)}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    botprotection = (soup.find_all('h2'))
    if botprotection != []:
        banned = True
    if out == [] and banned == False:
        await ctx.send("No hay resultados disponibles")
    elif banned == True:
        await ctx.send("El bot ha sido baneado :(")
    else:
        address = out[3].text + " " + out[4].text
        nombrerut = out[0].text
        Doxxtotalrut = "Resultados para: "  + rut
        await ctx.send(Doxxtotalrut)
        Doxxtotalrut = nombrerut + ", " + rut + " ," + address
@client.command(aliases=['doxxpatentes'])
async def doxxpatente(ctx,arg):
    user = ctx.message.author
    patente = arg
    URL = 'https://www.volanteomaleta.com/pat'
    historialpatente = open('historialbusquedapatente.txt', 'a')
    patentehistorial = patente + ", Solicitado por: " + str(ctx.message.author) + ", " + "Id Discord: " +str(ctx.message.author.id) + '\n'
    historialpatente.write(patentehistorial)
    response = requests.get(URL, params={'term': patente}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    botprotection = (soup.find_all('h2'))
    if botprotection != []:
        banned = True
    if out == [] and banned == False:
        await ctx.send("No hay resultados disponibles")
    elif banned == True:
        await ctx.send("El bot ha sido baneado :(")
    else:
        marca = out[2].text + " "
        modelo = out[3].text + " Año: " + out[6].text + " "
        numeromotor = "Numero de motor: " + out[5].text + " "
        nombredueno = out[7].text + " "
        rutdueno = out[4].text
        doxxtotalpatente = "Resultados: " + marca + modelo + numeromotor + nombredueno + rutdueno
        await ctx.send(doxxtotalpatente)
client.run("Insert_Token_Here")
