import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()




class DB:


    global hostG 
    global userG
    global passwordG 
    global databaseG 


    hostG = os.getenv('HOST')
    userG = os.getenv('USERG')
    passwordG = os.getenv('PASSWORD')
    databaseG = os.getenv('DATABASE')


 
    global mydb
    global mycursor
    # Datos de conexión (reemplaza con tus credenciales)
    mydb = mysql.connector.connect(
    host=hostG,
    user=userG,
    password=passwordG,
    database=databaseG
    )

    mycursor = mydb.cursor()





    def query (query,parametros):



    # Crear un cursor
        
        # Consulta con parámetros
        #sql = "SELECT * FROM tu_tabla WHERE departamento = %s"
        #val = ["DepartamentoA","",""]

        # Ejecutar la consulta
        mycursor.execute(query, parametros)

        # Obtener los resultados
        myresult = mycursor.fetchall()

        #mydb.commit()
        # Cerrar la conexión
        #mydb.close()

        return myresult
    


    def fin():

        mydb.commit()
        # Cerrar la conexión
        mydb.close()


    def printP():
        print (hostG)
        print (userG)
        print (passwordG)
        print (databaseG)

        mydb = mysql.connector.connect(
        host=hostG,
        user=userG,
        password=passwordG,
        database=databaseG
        )

        mycursor = mydb.cursor()