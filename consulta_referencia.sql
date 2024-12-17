

use PRACTICA1;

select * from global;
select * from local order by id_fecha;
select * from fecha;


select * from local t0
left join global t1 on t0.id_fecha = t1.id_fecha 
where t0.valor >0
order by t1.id_fecha ;



#Consulta general 
select * from get_valores;

#CONTEOS 
 
#Cantidad de nuevas muertes
select count(*) as valor from get_valores
where New_deaths>0;
 
#Cantidad de muertes acumuladas 
select count(*) as valor from get_valores
where Cumulative_deaths>0;


#conteo de poblacion municipios
select count(*) as valor 
from (
select departamento , municipio ,poblacion  
from get_valores
where poblacion>0
group by departamento , municipio ,poblacion) t ;

df = df.rename(columns={0 :'fecha'})
df = df.rename(columns={1 :'region'})
df = df.rename(columns={2 :'nuevos_casos'})
df = df.rename(columns={3 :'acumulado_casos'})
df = df.rename(columns={4 :'nuevas_muertes'})
df = df.rename(columns={5 :'acumulado_muertes'})
df = df.rename(columns={6 :'departamento'})
df = df.rename(columns={7 :'municipio'})
df = df.rename(columns={8 :'poblacion'})
df = df.rename(columns={9 :'valor'})



#PROMEDIO 

#promedio de nuevas muertes
select avg(New_deaths) as valor from get_valores
#where New_deaths>0;
 
#promedio de muertes acumuladas 
select avg(Cumulative_deaths) as valor from get_valores
#where Cumulative_deaths>0;


#promedio de poblacion municipios
select avg(poblacion) as valor 
from (
select departamento , municipio ,poblacion  
from get_valores
where poblacion>0
group by departamento , municipio ,poblacion) t ;



#DESVIACION ESTANDAR 

#MINIMOS

#minimo de nuevas muertes
select min(New_deaths) as valor from get_valores
#where New_deaths>0;
 
#minimo de muertes acumuladas 
select min(Cumulative_deaths) as valor from get_valores
#where Cumulative_deaths>0;


#minimio de poblacion municipios
select min(poblacion) as valor 
from (
select departamento , municipio ,poblacion  
from get_valores	
where poblacion>0
group by departamento , municipio ,poblacion) t ;




#MAXIMOS

#minimo de nuevas muertes
select max(New_deaths) as valor from get_valores
#where New_deaths>0;
 
#minimo de muertes acumuladas 
select max(Cumulative_deaths) as valor from get_valores
#where Cumulative_deaths>0;


#minimio de poblacion municipios
select max(poblacion) as valor 
from (
select departamento , municipio ,poblacion  
from get_valores	
where poblacion>0
group by departamento , municipio ,poblacion) t ;



#CUARTILES



### HISTOGRAMA , DIAGRAMA DE CAJAS 

-------------------------------------------------

#Consulta general 
select * from get_valores;

#coutn departamentos
select count(*) as valor 
from (
select departamento  
from get_valores	
where poblacion>0
group by departamento  ) t ;



#count municipios
select count(*) as valor 
from (
select  municipio   
from get_valores	
where poblacion>0
group by  municipio ) t ;

































