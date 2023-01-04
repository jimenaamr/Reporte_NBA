# EQUIPO MIAMI HEAT

En este repositorio encontramos los archivos necesarios para crear un pdf que ofrece una serie de datos acerca de este equipo de baloncesto. 


## Archivos Adjuntados

- Diversos archivos jpeg: Todos los archivos jpeg son imágenes que se han empleado para añadirlas al pdf.

- config.txt: Archivo que contiene la clave necesaria para trabajar con la API y obetener los datos.

- requirements.txt: En este archivo encontramos las librerías que se necesitan instalar para poder ejecutar los archivos.

- pdf_miami.py: Contiene una ETL en la que primero se extraen los datos del equipo Miami Heat de la API. A continuación se transforman los datos para obtener una serie de estadísticas de cada jugador y gráficas sobre los distintos datos del equipo. Finalmente se crea un pdf con toda está información y se muestra de la manera adecuada.

- reporte_nba.pdf: Pdf generado con el archivo anterior.


## Modo de Ejecución

1- Instalar el requirements.txt

2- Ejecutar el archivo pdf_miami.py para obtener el reporte del equipo en formato pdf.



# PRONÓSTICO NBA

Además, en este repopsitorio también encontramos una predicción acerca de los partidos de la NBA que se jugarán próximamente. Mediante técnicas de webscraping, analizamos las apuestas y realizamos un pronóstico de los próximos ganadores.

## Archivos Adjuntados

- pronostico_juegos.py: Contiene una ETL en la que primero se extraen los datos de las casas de apuestas para los partidos de la NBA en los próximos días, mediante técnicas de webscraping. A continuación se transforman los datos de manera que obtengamos una lista con las cuotas de las apuestas y otra con los equipos que juegan. Finalmente se trabaja con esos datos para hacer una predicción para cada uno de los partidos.


## Modo de Ejecución

1- Instalar el requirements.txt

2- Ejecutar el archivo pronostico_juegos.py para imprimir por pantalla el pronóstico.