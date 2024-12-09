import datetime
import bd as base
import funciones as fun



global global_datos
global catalogo
global local_datos


rutaG = "/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv"
rutaL = "/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/municipio.csv"


def menu():


    global_datos= list()
    catalogo=list()
    local_datos=list()

    var= "/8"

    var=var.replace("/", "")
    print(var)

    while True:
        print("--------------------------------------------------------------")
        print("---------------------SEMINARIO DE SISTEMAS 2------------------")
        print("---------------------KEVIN RUIZ 9----------------------------")
        print("--------------------------------------------------------------")
        print("Seleccione una opcion *")
        print("1) REVISION Y UNION EXCELES")
        print("2) CARGA MASIVA BLOQUES")
        print("3) Salir X")

        valor = input() 



        if valor == '1' :
            

            global_datos = fun.global_calificacion(rutaG)
            catalogo = fun.paises(rutaG)

            local_datos = fun.local_calificacion(rutaL)

        elif valor == '2' :




            #CARGA CATALOGO PAISES            
            print("CARGA PARTE 1")
            i=0
            conexion = base.DB
            conexion.start()
 
            while catalogo.size>i :

                sql = "CALL new_pais( %s )"
                val = [catalogo.iloc[i]['Country']]
                #base.query(sql,val)

                conexion.query(sql,val)

                i=i+1

            conexion.save()
            conexion.fin()



            

            #SELECCIONA EL PAIS GUATEMALA PARA ENLAZAR NUEVA INFO
            sqlT = "SELECT id_pais FROM pais WHERE nombre = 'guatemala';"
            conexion = base.DB
            conexion.start()
            result = conexion.query(sqlT,[])
            conexion.save()
            conexion.fin()
            id_gt = result[0][0]
            print(id_gt)




            #INICIA CARGA DE LOCAL Y ESPACIADO 
            print("CARGA PARTE 2")
            valorx = input() 

            i=0
            conexion2 = base.DB
            conexion2.start()
            #while local_datos.size>i :
            while 50300>i :
                sql = "CALL new_local (%s,%s,%s,%s,%s,%s);"
                ts=local_datos.iloc[i]

                fecha_solo_fecha = ts["fecha"].date()
                fecha_str = fecha_solo_fecha.strftime('%Y-%m-%d')

                lista = [
                        int(id_gt) , 
                        ts["departamento"] ,
                        ts["municipio"] ,
                        int(ts["poblacion"]) ,
                        fecha_str ,
                        int(ts["valor"])
                    ]
 
                print(lista)

                result = conexion2.query(sql,lista)

                if i%50000 == 0 :
                    print("50k registros guardados ,presione para continuar")
                    conexion2.save()
                    valorx = input() 
                    
                i=i+1

            conexion2.fin()
            





            #INICIA CARGA DE GLOBAL ESPACIADO TAMBIEN 
            print("CARGA PARTE 3")
            valorx = input() 

            i=0
            conexion2 = base.DB
            conexion2.start()
            #while global_datos.size>i :
            while 50300>i :
                sql = "CALL new_global (%s,%s,%s,%s,%s,%s,%s)";
                ts=global_datos.iloc[i]
                #SI DA ERROR AQUI SE PUEDE VER
                #print(ts)


                lista = [
                        ts["Date_reported"] , 
                        ts["Country"] , 
                        ts["WHO_region"] ,
                        int(ts["New_cases"]) ,
                        int(ts["Cumulative_cases"]) ,
                        int(ts["New_deaths"]),
                        int(ts["Cumulative_deaths"])
                    ]
 
                print(lista)

                result = conexion2.query(sql,lista)

                if i%50000 == 0 :
                    print("50k registros guardados ,presione para continuar")
                    conexion2.save()
                    valorx = input() 
                    

                i=i+1

            conexion2.fin()

             

        elif valor == '3' :

            exit()



menu()

 
# Ejemplo de uso
#ruta_archivo = "mis_datos.xlsx"  # Reemplaza con la ruta de tu archivo
#datos_limpios = global_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")

#catalogo = paises("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")


#prueba = local_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/municipio.csv")

#print(datos_limpios.head())
#print(catalogo)

#print(prueba)