import discord
from discord.ext import commands
import cloudscraper
from bs4 import BeautifulSoup
from rut_chile.rut_chile import format_rut_with_dots
import requests
import json
from PIL import Image
import tempfile
intents = discord.Intents.all()
scrap = cloudscraper.create_scraper()
client = commands.Bot(command_prefix = ';',intents=intents)
BASE_URL = "https://celuzador.online/celuzadorApi.php"

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
    response = scrap.get(URL, params={'term': name}).text
    soup = BeautifulSoup(response, 'html.parser')
    out = soup.find_all('td')

    if out == []:
        await ctx.send("No hay resultados disponibles")
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

@client.command()
async def phoneinfo(ctx, phone_number):
    headers = {
        'User-Agent': 'CeludeitorAPI-TuCulitoSacaLlamaAUFAUF'
    }
    response = requests.post(BASE_URL, data={"txttlf": phone_number}, headers=headers)
    data = response.json()

    if not data['error']:
        phone_info = json.loads(data['data'])
        if phone_info['fuente']:
            fuente_info = "\n".join([f"Nombre: {fuente['nombre']}" for fuente in phone_info['fuente']])
            await ctx.send(f"**Información de {phone_number}:**\n{fuente_info}")
        else:
            await ctx.send("Lo sentimos, no encontramos información sobre el teléfono en la fuente principal.")

        if phone_info['whatsapp']:
            tiene_whatsapp = 'Si tiene' if phone_info['whatsapp']['tiene_whatsapp'] else ' No tiene'
            await ctx.send(f"**WhatsApp:** {tiene_whatsapp}")

            if phone_info['whatsapp']['foto_perfil']:
                profile_pic_url = phone_info['whatsapp']['foto_perfil']
                image_response = requests.get(profile_pic_url, stream=True)
                image = Image.open(image_response.raw)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                    image.save(temp_file, format="JPEG")
                    await ctx.send(file=discord.File(temp_file.name))

                whatsapp_status = json.loads(phone_info['whatsapp']['estado'])
                await ctx.send(f"**Estado:** {whatsapp_status['status']}")
                await ctx.send(f"**Última Actualización:** {whatsapp_status['setAt']}")
        else:
            await ctx.send("**WhatsApp:** No tiene")

        await ctx.send(f"**_cva:** {phone_info['_cva']}")
    else:
        await ctx.send("El número indicado es inválido, intenta nuevamente.")

client.run("Insert_Token_Here")
