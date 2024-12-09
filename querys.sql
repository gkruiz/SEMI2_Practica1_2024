SELECT user, authentication_string, plugin, host FROM mysql.user;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'secure_pass_here';
FLUSH PRIVILEGES;



FLUSH PRIVILEGES;
CREATE USER kruiz@localhost IDENTIFIED BY 'secure_pass_here';
grant all privileges on *.* to kruiz@localhost with grant option;
FLUSH PRIVILEGES;

create database PRACTICA1;

use PRACTICA1;

DROP TABLE pais;
DROP TABLE global;
DROP TABLE local;



CREATE TABLE pais(
	id_pais INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nombre varchar (100) NOT NULL
);

CREATE TABLE global (
	Date_reported DATE NOT NULL,
    id_pais INT NOT NULL, #LLAVE FORANEA
    WHO_region varchar (10) NOT NULL,
    New_cases INT NOT NULL,
    Cumulative_cases INT NOT NULL,
    New_deaths INT NOT NULL,
    Cumulative_deaths INT NOT NULL ,
	FOREIGN KEY (id_pais) REFERENCES pais(id_pais)
);
 

CREATE TABLE local(
	id_pais INT NOT NULL,
	departamento varchar (100) NOT NULL,
	municipio varchar (100) NOT NULL , 
	poblacion INT NOT NULL,
	fecha DATE NOT NULL,
	valor INT NOT NULL ,
    FOREIGN KEY (id_pais) REFERENCES pais(id_pais)
);

CALL new_pais('aglg');

select * from pais

drop procedure new_pais;

DELIMITER &&  
CREATE PROCEDURE new_pais (IN paisp varchar(100))
       BEGIN
         INSERT INTO pais(nombre)VALUES(@pais);
END &&  
DELIMITER ;   


DELIMITER &&  
CREATE PROCEDURE new_global (
	IN Date_reported DATE ,
	IN id_pais INT,
    IN WHO_region varchar(10) ,
    IN New_cases INT ,
    IN Cumulative_cases INT ,
    IN New_deaths INT ,
    IN Cumulative_deaths INT 
)
       BEGIN
         INSERT INTO global VALUES(
         	Date_reported ,
			id_pais,
			WHO_region ,
			New_cases ,
			Cumulative_cases ,
			New_deaths ,
			Cumulative_deaths 
         );
END &&  
DELIMITER ;   


DELIMITER &&  
CREATE PROCEDURE new_local (
	IN id_pais INT,
	IN departamento varchar (100),
	IN municipio varchar (100), 
	IN poblacion INT,
	IN fecha DATE,
	IN valor INT
)
       BEGIN
         INSERT INTO local VALUES(
			id_pais ,
			departamento ,
			municipio , 
			poblacion ,
			fecha ,
			valor
         );
END &&  
DELIMITER ;   

 




