import discord
from discord.ext import commands
import cloudscraper
from bs4 import BeautifulSoup
from rut_chile.rut_chile import format_rut_with_dots
import requests
intents = discord.Intents.all()
scrap = cloudscraper.create_scraper()
client = commands.Bot(command_prefix = ';',intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases=['doxxnombre','testnombre'])
async def doxxname(ctx,*, name):
    user = ctx.message.author
    URL = "https://www.nombrerutyfirma.com/buscar"
    historialname = open('historialname.txt', 'a')
    namehistorial = name + ", Solicitado por: " + str(ctx.message.author)  + ", " + "Id Discord: " + str(ctx.message.author.id)  + '\n'
    historialname.write(namehistorial)
    response = scrap.get(URL, params={'term': name}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    if out == []:
        await ctx.send("No hay resultados disponibles")
    else:
            total_personas = len(out) // 5
            await ctx.send(f"Total de personas encontradas: {total_personas}")

            for i in range(0, len(out), 5):
                nombre = out[i].text
                rut = out[i+1].text
                direccion = out[i+3].text + " " + out[i+4].text
                resultado = f"{nombre}, {rut}, {direccion}"
                await ctx.send(resultado)


@client.command(aliases=['doxxruts','test'])
async def doxxrut(ctx,arg):
    user = ctx.message.author
    rut = arg
    URL = "https://www.nombrerutyfirma.com/rut"
    historialrut = open('historialrut.txt', 'a')
    ruthistorial = rut + ", Solicitado por: " + str(ctx.message.author)  + ", " + "Id Discord: " + str(ctx.message.author.id)  + '\n'
    historialrut.write(ruthistorial)
    response = scrap.get(URL, params={'term': str(format_rut_with_dots(rut))}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    if out == []:
        await ctx.send("No hay resultados disponibles")
    else:
        address = out[3].text + " " + out[4].text
        nombrerut = out[0].text
        await ctx.send("Resultados para: "  + rut)
        Doxxtotalrut = nombrerut + ", " + rut + " ," + address
        await ctx.send(Doxxtotalrut)

@client.command(aliases=['doxxpatentes'])
async def doxxpatente(ctx,arg):
    user = ctx.message.author
    patente = arg
    URL = 'https://www.volanteomaleta.com/pat'
    historialpatente = open('historialbusquedapatente.txt', 'a')
    patentehistorial = patente + ", Solicitado por: " + str(ctx.message.author) + ", " + "Id Discord: " +str(ctx.message.author.id) + '\n'
    historialpatente.write(patentehistorial)
    response = scrap.get(URL, params={'term': patente}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')
    botprotection = (soup.find_all('h2'))
    banned = botprotection != []
    if out == [] and not banned:
        await ctx.send("No hay resultados disponibles")
    elif banned:
        await ctx.send("El bot ha sido baneado :(")
    else:
        marca = out[2].text + " "
        modelo = out[3].text + " Año: " + out[6].text + " "
        numeromotor = "Numero de motor: " + out[5].text + " "
        nombredueno = out[7].text + " "
        rutdueno = out[4].text
        doxxtotalpatente = "Resultados: " + marca + modelo + numeromotor + nombredueno + rutdueno
        await ctx.send(doxxtotalpatente)

client.run("Inserte_Token")
