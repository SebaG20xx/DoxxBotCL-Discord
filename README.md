# DoxxBotCL-Discord
Bot simple que hace una consulta al sitio "Nombrerutyfirma.com" y "Volanteomaleta.com"


¿Qué funciona?
- Consultas mediante rut
- Consultas mediante nombre

¿Cómo usarlo?
- Insertar tu token de bot de discord en la línea 130


Comandos:
- ;doxxrut <"rut"> (Hace la consulta mediante RUT)
- ;doxxname <Nombre_Separado_Por_Guiones_Bajos> (Hace la consulta mediante Nombre)
- ;doxxpatente <"patente"> (Consulta mediante patente gracias a volanteomaleta.com)


**Descargo de responsabilidad: "nombrerutyfirma.com" y "volanteomaleta.com"**

Quiero dejar constancia de que no tengo ninguna afiliación ni relación con los creadores de los sitios "nombrerutyfirma.com" y "volanteomaleta.com". Mi único propósito en relación con estos sitios ha sido realizar un proceso de "scraping" con el objetivo de obtener datos específicos. Sin embargo, desconozco por completo la identidad de los creadores, sus intenciones y el contenido completo de dichos sitios.

Por lo tanto, quiero aclarar que no tengo ninguna influencia ni control sobre los sitios "nombrerutyfirma.com" y "volanteomaleta.com", más allá de la acción de "scraping" realizada. Cualquier asunto, inquietud o consulta relacionada con los sitios en cuestión debe dirigirse directamente a los creadores y administradores de los mismos. No asumo ninguna responsabilidad por el contenido, la precisión de los datos ni las acciones llevadas a cabo en "nombrerutyfirma.com" y "volanteomaleta.com".



Requerimientos: 
- Python 3.9 o superior
- Discord.py (Integración de discord)
- CloudScraper (Request HTTP para el sitio + bypass Cloudflare)
- bs4 (Scraper HTML)
- rut-chile (Le da el formato correcto al rut)
- request
