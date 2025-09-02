import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Conexão com PostgreSQL
engine = create_engine("postgresql://user:senha@localhost:5432/meubanco")

# Ler CSV
df = pd.read_csv("data/air_quality.csv")

# Carregar no PostgreSQL
df.to_sql("air_quality", engine, if_exists="replace", index=False)

print("Dados inseridos com sucesso!")
