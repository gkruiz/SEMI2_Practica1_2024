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

    while True:
        print("Seleccione una opcion *")
        print("1) REVISION Y UNION EXCELES")
        print("2) CARGA MASIVA BLOQUES")
        

        valor = input() 



        if valor == '1' :
            

            global_datos = fun.global_calificacion(rutaG)
            catalogo = fun.paises(rutaG)

            local_datos = fun.local_calificacion(rutaL)

        elif valor == '2' :

            #CARGA CATALOGO PAISES
            '''
            i=0
            while catalogo.size>i :

                sql = "CALL new_pais( %s )"
                val = [catalogo.iloc[i]['Country']]
                base.query(sql,val)

                i=i+1
            '''

            #SELECCIONA EL PAIS GUATEMALA PARA ENLAZAR NUEVA INFO
            sqlT = "SELECT id_pais FROM pais WHERE nombre = 'guatemala';"
            result = base.query(sqlT,[])
            
            id_gt = result[0][0]
            print(id_gt)


            
            i=0
            while local_datos.size>i :
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
                base.query(sql,lista)

                #local_datos.size%10 == 0
                if i%50000 == 0 :
                    print("50k registros guardados ,presione para continuarl")
                    valorx = input() 

                i=i+1




            '''
            i=0
            while global_datos.size<i :
                sql = "CALL new_global (%s,%s,%s,%s,%s,%s,%s);"
                base.query(sql,global_datos[i])
            '''

        elif valor == '3' :

            base.printP()



menu()

 
# Ejemplo de uso
#ruta_archivo = "mis_datos.xlsx"  # Reemplaza con la ruta de tu archivo
#datos_limpios = global_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")

#catalogo = paises("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")


#prueba = local_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/municipio.csv")

#print(datos_limpios.head())
#print(catalogo)

#print(prueba)