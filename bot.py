import requests
import mysql.connector
import discord
import os
from bs4 import BeautifulSoup
from ast import arg
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv('config.env')
env = 'config.env'
token = os.getenv("TOKEN")
pagina_entrypoint = os.getenv("WEB_ENTRYPOINT")
sqlhost,userdb,userpass,nombredb = os.getenv("SQLHOST"),os.getenv("SQLUSER"),os.getenv("SQLPASS"),os.getenv("SQLDBNAME")

#Recomiendo no tocar esta zona, salvo que sea para mejorar el código
def conectar_sql():
    db = mysql.connector.connect(
        host = sqlhost,
        user = userdb,
        password = userpass,
        database = nombredb
    )
    mycursor = db.cursor()

def botdc():
    client = commands.Bot(command_prefix = ';')
    @client.event
    async def on_ready():
        print('Bot operativo!')
    @client.command()
    async def doxxname(ctx,arg):
        user = ctx.message.author
        name = arg.replace("_","+")
        nameforreplacebeta = name.replace("+", " ")
        nameforreplacealpha = nameforreplacebeta.upper()
        print(nameforreplacealpha)
        url= pagina_entrypoint + name
        res= requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        output = ''
        blacklist = [
            '[document]',

        'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'style',
        ]
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
                salida = output.replace("RUT", "")
                salida1 = salida.replace("NOMBRE", "")
                salida2 = salida1.replace("GÉNERO", "")
                salida3 = salida2.replace("DIRECCIÓN", "")
                salida4 = salida3.replace("COMUNA", "")
                salida5 = salida4.replace("RESULTADOS PARA: ", "").split()
                salida6 = ' '.join(map(str, salida5))
                salida7 = "Su doxxeo es: (Formato: INPUT busqueda, Nombre, Rut, Nombre completo, dirección) " + salida6 + "."
        await ctx.send("Información enviada por DM!")
        await user.send(salida7)
    @client.command(aliases=['doxxruts','test'])
    async def doxxrut(ctx,arg):
        user = ctx.message.author
        rut = arg
        rut = "'" + rut + "'"
        await ctx.send("Doxxeo en progreso >:)")
        #búsqueda mediante mysql
        sqlrut = "SELECT * FROM chilenos WHERE rut LIKE " + rut 
        mycursor.execute(sqlrut)
        myresult = mycursor.fetchall()
        #envío del mensaje con los datos (si los obtuvo)
        await ctx.send("Información enviada por DM!")
        for x in myresult:
            await user.send(x)
    client.run(token)

if token != 'Inserte_Discord_Token_Aquí':
    if pagina_entrypoint != 'Inserte_Entrypoint_Aquí':
        if sqlhost != 'INSERTE_HOST_DB_AQUÍ' and userdb != 'Inserte_el_User_de_la_DB_Aquí' and userpass != 'Inserte_el_Pass_de_la_DB_Aquí' and nombredb != 'Inserte_el_nombre_de_la_DB_aquí':
            print("Datos cargados exitosamente!")
            print("NOTA: Esto no significa que no puedan haber problemas de conexión\nSolo se refiere a que los datos fueron rellenados")
            conectar_sql()
            botdc()
        else:
            print("Alguno de los datos pertenecientes a la DB no ha sido rellenado :'(")
            print("Saliendo...") 
    else:
        print("El entrypoint no ha sido rellenado! :'(")
        print("Saliendo...")     
else:
    print("El token no fue rellenado :'(")
    print("Saliendo...") 
