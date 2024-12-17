
create database PRACTICA1;

use PRACTICA1;




#INICIA CREACION DE TABLAS

CREATE TABLE fecha (
	id_fecha INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	fecha DATE NOT NULL
);

CREATE TABLE global (
	#Date_reported varchar(50) NOT NULL,
    id_fecha INT NOT NULL, #LLAVE FORANEA
    WHO_region varchar (10) NOT NULL,
    New_cases INT NOT NULL,
    Cumulative_cases INT NOT NULL,
    New_deaths INT NOT NULL,
    Cumulative_deaths INT NOT NULL ,
	FOREIGN KEY (id_fecha) REFERENCES fecha(id_fecha)
);
 

CREATE TABLE local(
	id_fecha INT NOT NULL,
	departamento varchar (100) NOT NULL,
	municipio varchar (100) NOT NULL , 
	poblacion INT NOT NULL,
	#fecha DATE NOT NULL,
	valor INT NOT NULL ,
    FOREIGN KEY (id_fecha) REFERENCES fecha(id_fecha)
);



#PROCEDURE PARA GUARDAR LA INFO DE NUEVO PAIS 

DROP PROCEDURE new_fecha;

CALL new_fecha('20240102')

select * from fecha

DELIMITER &&  
CREATE PROCEDURE new_fecha (IN fechap DATE)
		BEGIN
		DECLARE rs INT;
		
		SELECT count(id_fecha) INTO rs FROM fecha WHERE fecha = fechap;
        
        #Si no existe la fecha la inserta y crea
        IF rs = 0 THEN
			INSERT INTO fecha(fecha)VALUES(fechap);
		END IF;
END &&  
DELIMITER ;   





#PROCEDURE PARA GUARDAR INFO GLOBAL DATA 

DROP PROCEDURE new_global;

DELIMITER &&  
CREATE PROCEDURE new_global (
	IN Date_reported DATE ,
    #IN Country VARCHAR(100) ,
	#IN id_pais INT,
    IN WHO_region VARCHAR(10) ,
    IN New_cases INT ,
    IN Cumulative_cases INT ,
    IN New_deaths INT ,
    IN Cumulative_deaths INT 
)
       BEGIN
	   DECLARE id_fechaG INT;
       
		SELECT id_fecha INTO id_fechaG FROM fecha WHERE fecha = Date_reported;
       
		INSERT INTO global VALUES(
         	id_fechaG ,
			WHO_region ,
			New_cases ,
			Cumulative_cases ,
			New_deaths ,
			Cumulative_deaths 
		);
         
END &&  
DELIMITER ;   



Drop procedure new_local;

DELIMITER &&  
CREATE PROCEDURE new_local (
	IN fechaG DATE,
	IN departamento varchar (100),
	IN municipio varchar (100), 
	IN poblacion INT,
	IN valor INT
)
       BEGIN
       DECLARE id_fechaG INT;
       
		SELECT id_fecha INTO id_fechaG FROM fecha WHERE fecha = fechaG;
       
		INSERT INTO local VALUES(
			id_fechaG ,
			departamento ,
			municipio , 
			poblacion ,
			valor
		);
END &&  
DELIMITER ;   



 CREATE VIEW get_valores AS
		select 
		t0.fecha,
		t1.WHO_region ,
		t1.New_cases , 
		t1.Cumulative_cases , 
		t1.New_deaths , 
		t1.Cumulative_deaths , 
		CASE
			WHEN t2.departamento  is null THEN ''
			ELSE t2.departamento 
		END AS departamento ,
		#t2.departamento , 
		CASE
			WHEN t2.municipio  is null THEN ''
			ELSE t2.municipio 
		END AS municipio ,
		#t2.municipio , 
		CASE
			WHEN t2.poblacion  is null THEN 0
			ELSE t2.poblacion 
		END AS poblacion ,
		#t2.poblacion , 
		CASE
			WHEN t2.valor  is null THEN 0
			ELSE t2.valor 
		END AS valor  
		#t2.valor 
		from fecha t0
		left join global t1 on t0.id_fecha = t1.id_fecha
		left join local t2 on t1.id_fecha = t2.id_fecha ;



#INICIAN SELECTS

select count(*) from global;
select count(*) from local ;
select count(*) from fecha;
 


#QUERYS DE ELIMINACION Y BORRAR
 
truncate table fecha;
truncate table global; 
truncate table local;


DROP TABLE fecha;
DROP TABLE global;
DROP TABLE local;

----------------







