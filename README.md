# DoxxBotCL-Discord
Bot simple que hace una consulta al sitio "Nombrerutyfirma.com" y "Volanteomaleta.com", junto con poder idenfiticar el número de teléfono y su foto de whatsapp gracias a
["Celuzador"](https://github.com/Theblood/Celuzador) por [Theblood](https://github.com/Theblood)


¿Qué funciona?
- Consultas mediante rut
- Consultas mediante nombre
- Consultas mediante número de teléfono

¿Cómo usarlo?
- Insertar tu token de bot de discord en la línea 130


Comandos:
- ;doxxrut <"rut"> (Hace la consulta mediante RUT)
- ;doxxname <Nombre_Separado_Por_Guiones_Bajos> (Hace la consulta mediante Nombre)
- ;doxxpatente <"patente"> (Consulta mediante patente gracias a volanteomaleta.com)
- ;phoneinfo <"numero"> (Consulta su informacion y whatsapp gracias a "Celuzador")


**Descargo de responsabilidad: "nombrerutyfirma.com" y "volanteomaleta.com"**

Quiero dejar constancia de que no tengo ninguna afiliación ni relación con los creadores de los sitios "nombrerutyfirma.com" y "volanteomaleta.com". Mi único propósito en relación con estos sitios ha sido realizar un proceso de "scraping" con el objetivo de obtener datos específicos. Sin embargo, desconozco por completo la identidad de los creadores, sus intenciones y el contenido completo de dichos sitios.

Por lo tanto, quiero aclarar que no tengo ninguna influencia ni control sobre los sitios "nombrerutyfirma.com" y "volanteomaleta.com", más allá de la acción de "scraping" realizada. Cualquier asunto, inquietud o consulta relacionada con los sitios en cuestión debe dirigirse directamente a los creadores y administradores de los mismos. No asumo ninguna responsabilidad por el contenido, la precisión de los datos ni las acciones llevadas a cabo en "nombrerutyfirma.com" y "volanteomaleta.com".

**Descargo de responsabilidad: "Celuzador"**
Quiero dejar en claro que el proyecto "Celuzador" no es de mi autoría en ningún sentido. Este proyecto ha sido creado y desarrollado exclusivamente por @Theblood, y puede encontrarse en su repositorio de GitHub. Cualquier procedimiento o acción relacionada con la manipulación de datos vinculados a "Celuzador" debe ser gestionada directamente con @Theblood a través de su perfil en GitHub. Quiero enfatizar que no poseo control alguno ni asumo ninguna responsabilidad con respecto al proyecto ni a la manera en que se tratan los datos relacionados. En consecuencia, se recomienda encarecidamente dirigir cualquier consulta sobre el uso y tratamiento de datos de "Celuzador" directamente a @Theblood para obtener información precisa y exhaustiva.


Requerimientos: 
- Python 3.9 o superior
- Discord.py (Integración de discord)
- CloudScraper (Request HTTP para el sitio + bypass Cloudflare)
- bs4 (Scraper HTML)
- rut-chile (Le da el formato correcto al rut)
- request
- pillow
