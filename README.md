# DoxxBotCL-Discord
Bot simple que hace una consulta al sitio "Nombrerutyfirma.com"

¿Qué funciona?
- Consultas mediante rut
- Consultas mediante nombre

Tareas pendientes:
- [ ] Agregar mensaje en el caso de que la busqueda por rut y nombre no obtenga resultados

Comandos:
- ;doxxrut <"rut"> (Hace la consulta mediante RUT)
- ;doxxname <Nombre_Separado_Por_Guiones_Bajos> (Hace la consulta mediante Nombre)

Requerimientos: 
- Discord.py (Integración de discord)
- requests (Request HTTP para el sitio)
- bs4 (Scraper HTML)
- rut-chile (Le da el formato correcto al rut)
