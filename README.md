## Practica 1 - Seminario de Sistemas 2
<br>
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png" width="300px" align="center">
<br>
<br>

### Introduccion 

La siguiente practica tuvo la finalidad de poner a prueba los conocimientos adquiridos para el manejo de informacion haciendo uso de diferentes fuentes , en este caso usamos excel para la carga de la informacion ademas de usar el lenguaje de programacion
python para el analisis de los datos ,asi mismo usamos las librerias como panda para el manejo de los datos ya cargados ,asi tambien para la depuracion y limpieza de los mismo , posterior a su analisis y limpieza se procedio a 
cargar estos a una base de datos mysql esta levantada en una instacia de docker


### Diagrama ER

<img src="https://github.com/gkruiz/SEMI2_Practica1_2024/blob/master/IMAGENES/diagrama.png?raw=true" width="800px">

Para el desarrollo de esta practica , se hizo uso el siguiente diagrama que cuenta con 3 entidades ,Pais ,General , Local ,en las cuales se guardara la informacion depurada por las libreria panda y demas funciones asociadas,
para el caso de el dataset LOCAL se excluyeron las columnas CODIGO-DEPARTAMENTO ,CODIGO-MUNICIPIO , para el dataset GLOBAL se quitaron las columnas COUNTRY-CODE 


### Descripcion de Limpieza de datos

para iniciar el proceso de limpieza de informacion ,se procedio primero a realizar la carga de los respectivos exceles el de LOCAL se realizo la carga desde la pc , y la carga del archivo GLOBAL se realizo la carga desde un
archivo en la nube

#### Paso 1

se procedio a realizar la carga del archivo para el caso del LOCAL,se quito la columna CODIGO-DEPARTAMENTO ,CODIGO-MUNICIPIO ,luego de eso se procedio a convertir las columnas en filas para el caso de las fechas
para poder ser analizadas posterior a eso se procedio a estandarizar la columna de fecha a un unico formato para poder realizar correctamente la union entre los dos dataframes, tambien todos los elementos que no tuvieran como
ano el 2020 fueron excluidos para usos practicos del analisis

#### Paso 2

se procedio a realizar la carga del archivo para el caso de GLOBAL, se quito la columna COUNTRY-CODE ,luego de eso se procedio a realizar un filtraje por pais y dejar solo los elementos de GUATEMALA , 
posterior a eso , se dio formato a las columnas y se estandarizo tambien el campo de fecha para poder realizar la union entre los dos dataframes ,posterior a eso , se realizo un filtraje donde solo hubieran elementos 
que estuvieran durante al ano 2020 y los demas elementos fueron excluidos 

#### Paso 3

se procedio a realizar la union de los 2 dataframes y asi hacer converger la informacion en un unico dataset

#### Paso 4

se procedio a distribuir la informacion en las tablas correspondientes asi mismo se uso el commit y rollback para el manejo de transacciones y evitar tener informacion erronea en la base de datos













