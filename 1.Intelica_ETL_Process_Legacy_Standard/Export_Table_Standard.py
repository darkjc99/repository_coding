import pandas as pd
from sqlalchemy import create_engine

# Configuración de la conexión a PostgreSQL
host = 'app-interchange-aurora-priv-cluster-prd.cf3zxr6zcsiz.us-east-1.rds.amazonaws.com'  # Reemplaza con el nombre de tu host
port = '5432'  # Reemplaza con el puerto de tu base de datos (por defecto es 5432)
database = 'interchange'  # Reemplaza con el nombre de tu base de datos
username = 'root'  # Reemplaza con tu usuario
password = 'p5JBBBq>2&p`C]l%'  # Reemplaza con tu contraseña
table_name = 'public.exchange_rate_20240729_20240810_visa'  # Reemplaza con el nombre de la tabla que deseas exportar

# Cadena de conexión
connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Crear una conexión usando SQLAlchemy
engine = create_engine(connection_string)

# Leer datos de la tabla
query = f'SELECT * FROM {table_name}'
df = pd.read_sql(query, engine)

# Exportar los datos a un archivo CSV
output_file = 'C:/Users/julio.cardenas/exchange_rate_20240729_20240810_visa.csv'  # Nombre del archivo CSV de salida
df.to_csv(output_file, sep=';', index=False)

print(f"Datos exportados exitosamente a {output_file}")
