import copy
import pandas as pd



def local_calificacion(ruta_archivo):

    # Cargar los datos del archivo Excel
    df = pd.read_csv(ruta_archivo)

    df = df.drop(columns=['codigo_departamento'], axis=1)
    df = df.drop(columns=['codigo_municipio'], axis=1)
 
    df_long = pd.melt(df, 
                 id_vars=['departamento', 'municipio', 'poblacion'], 
                 var_name='fecha', 
                 value_name='valor'
                )
    #print(df_long.head)

    df_long['fecha'] = pd.to_datetime(df_long['fecha'], format='%m/%d/%y' ,errors='coerce').fillna(
        pd.to_datetime(df_long['fecha'], format='%m/%d/%Y',errors='coerce')
    )

    #conversion de tipo fecha
    #df_long['fecha'] = pd.to_datetime(df_long['fecha'], format='%m/%d/%y' ,errors='coerce').fillna(
    #pd.to_datetime(df_long['fecha'], format='%m/%d/%Y',errors='coerce').fillna(
    #    pd.to_datetime(df_long['fecha'], format='%m-%d-%y',errors='coerce')
    #)
    
    #)

    df_long = df_long.drop_duplicates(subset=['departamento', 'municipio', 'poblacion','fecha','valor'])

    fecha_inicio = '2020-01-01'
    fecha_fin = '2020-12-31'
    rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin)
    df_filtrado = df_long[df_long['fecha'].isin(rango_fechas)]

    df_sin_ceros = df_filtrado[(df_filtrado['valor'] != 0)]

    print(df_sin_ceros.head)
    print(len(df_sin_ceros))


    return df_sin_ceros




 


def global_calificacion(ruta_archivo):

    # Cargar los datos del archivo Excel
    df = pd.read_csv(ruta_archivo)

    # Seleccionar las columnas de interés
    columnas = ['Date_reported', 'Country', 'WHO_region', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
    df = df[columnas]

    filtro = df['Country'] == "Guatemala"
    df = df[filtro]

    # Convertir los tipos de datos
    #df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    #df['Date_reported'] = df['Date_reported'].astype(str)
    df['Date_reported'] = pd.to_datetime(df['Date_reported'], format='%m/%d/%y' ,errors='coerce').fillna(
        pd.to_datetime(df['Date_reported'], format='%m/%d/%Y',errors='coerce')
    )

    df['Country'] = df['Country'].astype(str)
    df['WHO_region'] = df['WHO_region'].astype(str)

    var0 = (df['New_cases'].astype(str)).str.replace('/', '')
    df['New_cases'] = pd.to_numeric(var0, errors='coerce')

    var1 = (df['Cumulative_cases'].astype(str)).str.replace('/', '')
    df['Cumulative_cases'] = pd.to_numeric(var1, errors='coerce')

    var2 = (df['New_deaths'].astype(str)).str.replace('/', '')
    df['New_deaths'] = pd.to_numeric(var2, errors='coerce')

    var3 = (df['Cumulative_deaths'].astype(str)).str.replace('/', '')
    df['Cumulative_deaths'] = pd.to_numeric(var3, errors='coerce')

    # Eliminar filas duplicadas basadas en las columnas especificadas
    df = df.drop_duplicates(subset=['Date_reported', 'Country', 'WHO_region'])

    fecha_inicio = '2020-01-01'
    fecha_fin = '2020-12-31'
    rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin)
    df_filtrado = df[df['Date_reported'].isin(rango_fechas)]

    df_sin_ceros = df_filtrado[(df_filtrado['Cumulative_cases'] != 0) ]

    print(df_sin_ceros.head)#1414

    return df_sin_ceros




def fechas1(df1 ,df2):

    # Cargar los datos del archivo CSV
    #df = pd.read_csv(ruta_archivo)
    #df = df.apply(lambda x: x.astype(str).str.lower())


    #GLOBAL ES EL PRIMERO
    df = df1
    df = df[['Date_reported']] 
    df = df.rename(columns={'Date_reported': 'fecha'})

    #print("FECHAS GLOBAL ")
    #print(df)

    print("GLOBAL ESTRUCTURA")
    print(df.size)
    print(df.iloc[0])




    #LOCAL ES EL SEGUNDO
    dfx = df2
    dfx = dfx[['fecha']] 

    #print("FECHAS LOCAL ")
    #print(dfx)

    print("LOCAL ESTRUCTURA")
    print(dfx.size)
    print(dfx.iloc[0])


    globalT=copy.deepcopy(df)
    localT=copy.deepcopy(dfx)

    dff = pd.concat([globalT, localT], ignore_index=True)

    print("final ESTRUCTURA")
    print(dff.size)
    print(dff.iloc[0])


    fecha_inicio = '2020-01-01'
    fecha_fin = '2020-12-31'
    rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin)
    df_filtrado = dff[dff['fecha'].isin(rango_fechas)]

    # Eliminar filas duplicadas basadas en la columna "Country"
    df_filtrado = df_filtrado.drop_duplicates(subset='fecha')

    print(df_filtrado)
    #print(df)
    #print(dfx)
    #print(dff)



    return df_filtrado
     





def unionDF():

    print("HACE LA UNION")

# Ejemplo de uso
#ruta_archivo = "mis_datos.xlsx"  # Reemplaza con la ruta de tu archivo
#datos_limpios = global_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")

#catalogo = paises("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")


#prueba = local_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/municipio.csv")

#print(datos_limpios.head())
#print(catalogo)

#print(prueba)