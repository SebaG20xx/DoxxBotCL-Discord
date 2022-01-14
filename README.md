# DoxxBotCL-Discord
Bot simple que hace una consulta a una bd de mysql con datos, en este caso aplicadas a una base de datos con nombres,ruts,sexo y dirección de parte del Servel.

¿Qué funciona?
- Consultas mediante rut (Requiere acceso a una db)
- Consultas mediante nombre (Requiere entrypoint)

Tareas pendientes:
- [ ] Agregar mensaje en el caso de que la busqueda por rut sea vacía
- [ ] Mejorar la forma de entrega de datos
- [ ] Cambiar la librería discord.py (está un poco obsoleta)

Comandos:
- ;doxxrut (Hace la consulta mediante RUT)
- ;doxxname (Hace la consulta mediante Nombre)

Requerimientos: 
- Discord.py 
- mysql-connector-python (Consulta mediante mysql)
- beautifulsoup4 (Website Scraping)
- requests (Descargar sitio)
Encuentra todo esto en el archivo requirements.txt para ser instalado
