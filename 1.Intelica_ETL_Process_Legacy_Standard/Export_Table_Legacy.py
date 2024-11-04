import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# Configuración de la conexión a SQL Server
server = '10.0.4.100'  # Reemplaza con el nombre de tu servidor
database = 'ITLCMN'  # Reemplaza con el nombre de tu base de datos
username = 'SoporteITX'  # Reemplaza con tu usuario
password = 'kSN^3xrW7Mw0'  # Reemplaza con tu contraseña
table_name = 'BTRLRO_MC_CCA'  # Reemplaza con el nombre de la tabla que deseas exportar

# Cadena de conexión
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Crear una conexión usando SQLAlchemy
engine = create_engine(connection_string)

# Leer datos de la tabla
query = f'SELECT * FROM {table_name}'
df = pd.read_sql(query, engine)

# Exportar los datos a un archivo CSV
output_file = 'C:/Users/julio.cardenas/BTRLRO_MC_CCA_v4.csv'  # Nombre del archivo CSV de salida
df.to_csv(output_file, sep=';',index=False)

print(f"Datos exportados exitosamente a {output_file}")