# EstadisticasYCovid19

Se dispone de un archivo de valores separados por comas que contiene información sobre los casos de COVID19 registrados en el país
(https://datos.gob.ar/dataset/salud-covid-19-casos-registrados-republica-argentina/archivo/salud_fd657d02-a33a-498b-a91b-2ef1a68b8d16).

Dado que el archivo es muy extenso como para abrirlo y analizarlo en Excel, se prefirió realizar un programa en Python que pueda responder con complejidad O(n), y 
evitando recorrer el archivo más de una vez, las siguientes estadísticas de interés:

1. Cantidad de casos por provincia, separados por género
2. Cantidad de casos por rango etario (0 a 20, 20 a 40, 40 a 60, 60 o más)
3. Promedio de edad de los infectados por provincia
4. Provincias ordenadas por cantidad de casos, con los casos

Toda esta información deberá presentarse en forma de tablas, en dos archivos diferentes.

1. Archivo con campos de longitud fija
2. Archivo con campos de longitud variable

- - - -
- Se ejecuta el archivo "LectorDeArchivo.py"

- El programa funciona descargando el archivo csv y "colocandolo" en la funcion "recorrer_archivo" de la misma clase, no hace un analisis desde el link que
se menciona anteriormente.

- "campos_fijos.v1" y "campos_variables.v1" son ejemplos de lo que se espera de la salida, los obtuve ejecutando el archivo "LectorDeArchivo.py", así como
también, los valores obtenidos son antiguos (noviembre del 2020) por si desea compararlos con valores actuales.

