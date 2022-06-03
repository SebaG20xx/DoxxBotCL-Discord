# DoxxBotCL-Discord
# NOTA, EL SITIO AGREGÓ CAPTCHA POR CLOUDFLARE, ESTOY TRABAJANDO EN UNA SOLUCIÓN
Bot simple que hace una consulta al sitio "Nombrerutyfirma.com" y "Volanteomaleta.com"

¿Qué funciona?
- Consultas mediante rut
- Consultas mediante nombre

¿Cómo usarlo?
- Insertar tu token de bot de discord en la línea 73

Tareas pendientes: ~~Todo listo!~~
- [x] Agregar mensaje en el caso de que la busqueda por rut y nombre no obtenga resultados
- [x] Agregar mensaje en el caso de que la protección CloudFlare impida la consulta
- [ ] Agregar bypass al captcha cloudflare

Comandos:
- ;doxxrut <"rut"> (Hace la consulta mediante RUT)
- ;doxxname <Nombre_Separado_Por_Guiones_Bajos> (Hace la consulta mediante Nombre)
- ;doxxpatente <"patente"> (Consulta mediante patente gracias a volanteomaleta.com)

Requerimientos: 
- Python 3.9 o superior  
- Discord.py (Integración de discord)
- requests (Request HTTP para el sitio)
- bs4 (Scraper HTML)
- rut-chile (Le da el formato correcto al rut)
