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
#intento de búsqueda en la db con el nombre, no lo sé implementar aún
"""
@client.command()
async def doxxname(ctx,arg):
   name = arg
    name = "'" + name + "'"
    sqlname = "SELECT * FROM chilenos_db WHERE nombre LIKE " + name
    mycursor.execute(sqlname)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(x)
"""
client.run('INSERTE TOKEN AQUÍ')
