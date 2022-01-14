from ast import arg
import discord
from discord.ext import commands
import mysql.connector

db = mysql.connector.connect(
    host="INSERTE HOST AQUÍ",
    user="INSERTE USER AQUÍ",
    password="INSERTE CONTRASEÑA AQUI",
    database="INSERTE EL NOMBRE DE LA DB AQUÍ"
)
mycursor = db.cursor()
client = commands.Bot(command_prefix = ';')
@client.event
async def on_ready():
    print('Bot is ready')
@client.command(aliases=['doxxrut','test'])
async def doxxrut(ctx,arg):
    rut = arg
    rut = "'" + rut + "'"
    await ctx.send("Doxxeo en progreso >:)")
    #búsqueda mediante mysql
    sqlrut = "SELECT * FROM [inserte bd aqui] WHERE [inserte tabla aqui] LIKE " + rut 
    mycursor.execute(sqlrut)
    myresult = mycursor.fetchall()
    #envío del mensaje con los datos (si los obtuvo)
    for x in myresult:
        await ctx.send(x)
async def doxxname(ctx,arg):
    name = arg.replace("_","+")
    nameforreplacebeta = name.replace("+", " ")
    nameforreplacealpha = nameforreplacebeta.upper()
    url= 'INSERTE ENTRYPOINT AQUÍ' + name
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
            salida = "Su doxxeo es: " + output
    await ctx.send(salida)
client.run('INSERTE TOKEN AQUÍ')
