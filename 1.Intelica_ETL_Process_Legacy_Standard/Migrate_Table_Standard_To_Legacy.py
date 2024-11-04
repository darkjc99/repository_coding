import pandas as pd
from sqlalchemy import create_engine
import psycopg2  # Para la conexión a PostgreSQL
import pyodbc  # Para la conexión a SQL Server

# Paso 1: Configuración de la conexión a PostgreSQL
pg_host = 'app-interchange-aurora-priv-cluster-prd.cf3zxr6zcsiz.us-east-1.rds.amazonaws.com'  # Dirección de tu servidor PostgreSQL
pg_port = '5432'  # Puerto de PostgreSQL
pg_database = 'interchange'  # Base de datos de PostgreSQL
pg_username = 'root'  # Usuario de PostgreSQL
pg_password = 'p5JBBBq>2&p`C]l%'  # Contraseña de PostgreSQL
pg_table_name = 'public.exchange_rate_20240729_20240810_visa'  # Nombre de la tabla en PostgreSQL

# Cadena de conexión a PostgreSQL
pg_connection_string = f'postgresql://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'

# Crear una conexión usando SQLAlchemy
pg_engine = create_engine(pg_connection_string)

# Paso 2: Leer los datos desde PostgreSQL
query = f'SELECT * FROM {pg_table_name}'
df = pd.read_sql(query, pg_engine)

# Paso 3: Configuración de la conexión a SQL Server
sql_server = '10.0.4.100'  # Dirección de tu servidor SQL Server
sql_database = 'ITLCMN'  # Base de datos de SQL Server
sql_username = 'SoporteITX'  # Usuario de SQL Server
sql_password = 'kSN^3xrW7Mw0'  # Contraseña de SQL Server
sql_table_name = 'exchange_rate_20240729_20240810_visa'  # Nombre de la tabla en SQL Server

# Cadena de conexión a SQL Server
sql_connection_string = f'mssql+pyodbc://{sql_username}:{sql_password}@{sql_server}/{sql_database}?driver=ODBC+Driver+17+for+SQL+Server'

# Crear una conexión usando SQLAlchemy
sql_engine = create_engine(sql_connection_string)

# Paso 4: Migrar los datos a SQL Server
df.to_sql(sql_table_name, sql_engine, if_exists='replace', index=False)

print(f"Datos migrados exitosamente de PostgreSQL a SQL Server en la tabla {sql_table_name}")
