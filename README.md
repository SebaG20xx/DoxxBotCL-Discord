# DoxxBotCL-Discord
# NOTA, EL SITIO AGREGÓ CAPTCHA POR CLOUDFLARE, ESTOY TRABAJANDO EN UNA SOLUCIÓN
Bot simple que hace una consulta al sitio "Nombrerutyfirma.com" y "Volanteomaleta.com"

¿Qué funciona?
- Consultas mediante rut
- Consultas mediante nombre

¿Cómo usarlo?
- Insertar tu token de bot de discord en la línea 85

~~Tareas pendientes:~~ Todo listo!
- [x] Agregar mensaje en el caso de que la busqueda por rut y nombre no obtenga resultados
- [x] Agregar mensaje en el caso de que la protección CloudFlare impida la consulta
- [x] Agregar bypass al captcha cloudflare

Comandos:
- ;doxxrut <"rut"> (Hace la consulta mediante RUT)
- ;doxxname <Nombre_Separado_Por_Guiones_Bajos> (Hace la consulta mediante Nombre)
- ;doxxpatente <"patente"> (Consulta mediante patente gracias a volanteomaleta.com)

Requerimientos: 
- Python 3.9 
- Discord.py (Integración de discord)
- CloudScrap (Request HTTP para el sitio + bypass Cloudflare)
- bs4 (Scraper HTML)
- rut-chile (Le da el formato correcto al rut)
