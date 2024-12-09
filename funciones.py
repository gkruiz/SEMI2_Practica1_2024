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
    print(df_long.head)

    df_long['fecha'] = pd.to_datetime(df_long['fecha'], format='%m/%d/%y' ,errors='coerce').fillna(
        pd.to_datetime(df_long['fecha'], format='%m/%d/%Y',errors='coerce')
    )

    #conversion de tipo fecha
    #df_long['fecha'] = pd.to_datetime(df_long['fecha'], format='%m/%d/%y' ,errors='coerce').fillna(
    #pd.to_datetime(df_long['fecha'], format='%m/%d/%Y',errors='coerce').fillna(
    #    pd.to_datetime(df_long['fecha'], format='%m-%d-%y',errors='coerce')
    #)
    
    #)

    
    print(df_long.head)


    return df_long

 


def global_calificacion(ruta_archivo):

    # Cargar los datos del archivo Excel
    df = pd.read_csv(ruta_archivo)

    # Seleccionar las columnas de interés
    columnas = ['Date_reported', 'Country', 'WHO_region', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
    df = df[columnas]

    # Convertir los tipos de datos
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    df['Country'] = df['Country'].astype(str)
    df['WHO_region'] = df['WHO_region'].astype(str)
    df['New_cases'] = pd.to_numeric(df['New_cases'], errors='coerce')
    df['Cumulative_cases'] = pd.to_numeric(df['Cumulative_cases'], errors='coerce')
    df['New_deaths'] = pd.to_numeric(df['New_deaths'], errors='coerce')
    df['Cumulative_deaths'] = pd.to_numeric(df['Cumulative_deaths'], errors='coerce')

    # Eliminar filas duplicadas basadas en las columnas especificadas
    df = df.drop_duplicates(subset=['Date_reported', 'Country', 'WHO_region'])

    return df




def paises(ruta_archivo):

    # Cargar los datos del archivo CSV
    df = pd.read_csv(ruta_archivo)

    df = df.apply(lambda x: x.astype(str).str.lower())

    df = df[['Country']] 
 
    # Eliminar filas duplicadas basadas en la columna "Country"
    df = df.drop_duplicates(subset='Country')


    return df
     




# Ejemplo de uso
#ruta_archivo = "mis_datos.xlsx"  # Reemplaza con la ruta de tu archivo
#datos_limpios = global_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")

#catalogo = paises("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/global_calificacion.csv")


#prueba = local_calificacion("/home/kruiz/SEMI2/SEMI2_Practica1_2024/Archivos/municipio.csv")

#print(datos_limpios.head())
#print(catalogo)

#print(prueba)