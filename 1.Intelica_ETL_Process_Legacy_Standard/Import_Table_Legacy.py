import pandas as pd
from sqlalchemy import create_engine

# Paso 1: Leer el archivo CSV
input_file = 'C:/Users/julio.cardenas/clearing_and_settlement_advice_ep733f.csv'  # Nombre del archivo CSV de entrada
df = pd.read_csv(input_file, delimiter=',')

# Paso 2: Configuración de la conexión a la nueva base de datos SQL Server
new_server = '10.0.4.100'  # Reemplaza con el nombre de tu nuevo servidor
new_database = 'ITLCMN'  # Reemplaza con el nombre de tu nueva base de datos
new_username = 'SoporteITX'  # Reemplaza con tu nuevo usuario
new_password = 'kSN^3xrW7Mw0'  # Reemplaza con tu nueva contraseña
new_table_name = 'clearing_settlement_ep733f'  # Reemplaza con el nombre de la nueva tabla


# Cadena de conexión a SQL Server
new_connection_string = f'mssql+pyodbc://{new_username}:{new_password}@{new_server}/{new_database}?driver=ODBC+Driver+17+for+SQL+Server'

# Crear una conexión usando SQLAlchemy
new_engine = create_engine(new_connection_string)

# Paso 3: Cargar los datos en la nueva tabla de la nueva base de datos SQL Server
df.to_sql(new_table_name, new_engine, if_exists='replace', index=False)

print(f"Datos cargados exitosamente en la tabla {new_table_name} de la base de datos {new_database}")
