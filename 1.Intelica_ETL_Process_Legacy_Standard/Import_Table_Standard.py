import pandas as pd
from sqlalchemy import create_engine

# Paso 1: Leer el archivo CSV
input_file = 'C:/Users/julio.cardenas/exchange_rate_20240801_visa.csv'  # Ruta del archivo CSV
df = pd.read_csv(input_file, delimiter=';')  # Leer CSV con delimitador ';'

# Paso 2: Configuración de la conexión a PostgreSQL
host = '10.0.4.200'  # Reemplaza con la IP o nombre del host de tu servidor PostgreSQL
port = '5432'  # Reemplaza con el puerto de PostgreSQL (el valor por defecto es 5432)
database = 'ITLCMN'  # Reemplaza con el nombre de tu base de datos en PostgreSQL
username = 'SoporteITX'  # Reemplaza con tu usuario de PostgreSQL
password = 'kSN^3xrW7Mw0'  # Reemplaza con tu contraseña de PostgreSQL
new_table_name = 'EXCHANGE_RATE_20240801_VISA'  # Reemplaza con el nombre de la tabla en PostgreSQL

# Cadena de conexión a PostgreSQL
pg_connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Crear una conexión usando SQLAlchemy
pg_engine = create_engine(pg_connection_string)

# Paso 3: Cargar los datos en la nueva tabla de PostgreSQL
df.to_sql(new_table_name, pg_engine, if_exists='replace', index=False)

print(f"Datos cargados exitosamente en la tabla {new_table_name} de la base de datos {database}")
