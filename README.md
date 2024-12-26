## Proyecto 1 - Seminario de Sistemas 2
<br>
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png" width="300px" align="center">
<br>
<br>

### Introduccion 

El siguiente proyecto tuvo como finalidad el poner en practica los conocimientos en analisis de datos haciendo uso de Python con las librerias panda o Mathiplot y consumiendo datos desde la base de datos , se analizo la informacion y se llegaron a ciertas conclusiones las cuales se describiran mejor en el reporte ipynb


### Diagrama ER

<img src="https://github.com/gkruiz/SEMI2_Practica1_2024/blob/proyecto_1/IMAGENES/nuevo_diagrama.png?raw=true" width="800px">

Para el desarrollo de esta practica , se hizo uso el siguiente diagrama que cuenta con 3 entidades ,Fecha ,General , Local ,en las cuales se guardara la informacion depurada por las libreria panda y demas funciones asociadas,
para el caso de el dataset LOCAL se excluyeron las columnas CODIGO-DEPARTAMENTO ,CODIGO-MUNICIPIO , para el dataset GLOBAL se quitaron las columnas COUNTRY-CODE 


### Descripcion Modificaciones Diagrama

se hicieron modificaciones al diagrama ER pues estaba malo en algunos aspectos ,pues la union tenia que ser con el campo fecha y no con el campo pais , se tomo como catalogo principal la columna fecha , a la cual se le podia asociar tanto un grupo de registros que pertenecieran a diferentes departamentos y municipios como tambien que le pudiera pertenecer a unicamente un dia en especifico que tuviera el total del dia , con esto se evita la redundacia de los datos en este caso fechas y se tiene un pivote principal que seria la tabla fecha 

#### Observaciones 

para este analisis se observo que los datos obtenidos GLOBAL ,lo datos cuadran y son secuenciales , con respecto a nuevos casos y sumatoria de casos , tambien nuevas muertes y sumatoria de muertes , caso contrario para los datos DEPARTAMENTOS , para este caso , pueden o no haber registros asociados por dia ,por lo que hay faltantes

#### Analisis  
para este caso ,se evitaron los datos vacios que no aportaran al analisis si era necesario ,tambien se eliminaron todos los valores repetidos y asi mismo se valido que los datos coincidieran con la fecha que le correspondia ,luego de eso se procedio a realizar conteo de datos para verificar que si se hubieran obtenido todos los datos de manera correcta.

se hizo uso de pandas para el analis de los datos tambien de la herramienta de Mathiplot para graficar los datos en el archivo ipynb ,todo en el lenguaje python.

Se aplicaron calculos estadisticos como cuartiles, desviacion estandar , maximos ,minimos , conteo de datos y otros para tener mas informacion sobre la data 

### Estadisticas Monovariable Ejemplos

#### Imagen de estadistica nuevas muertes con Cuartiles

<img src="https://github.com/gkruiz/SEMI2_Practica1_2024/blob/proyecto_1/IMAGENES/MONOVARIABLE/nmc.png?raw=true" width="500px">


#### Imagen de estadistica pais con Cuartiles

<img src="https://github.com/gkruiz/SEMI2_Practica1_2024/blob/proyecto_1/IMAGENES/MONOVARIABLE/pc.png?raw=true" width="500px">


#### Imagen de estadistica acumulado muertes con Cuartiles

<img src="https://github.com/gkruiz/SEMI2_Practica1_2024/blob/proyecto_1/IMAGENES/MONOVARIABLE/amc.png?raw=true" width="500px">










