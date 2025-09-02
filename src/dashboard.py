import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Configuração da página
st.set_page_config(page_title="Dashboard IoT", layout="wide")

# Conexão com PostgreSQL
engine = create_engine("postgresql://user:senha@localhost:5432/meubanco")

# Carregar dados
df = pd.read_sql("SELECT * FROM air_quality", engine)

st.title(" Dashboard IoT - Qualidade do Ar")

# Gráfico 1: Histórico de poluentes
st.subheader("Histórico de Poluentes")
st.line_chart(df[["CO(GT)", "NOx(GT)", "NMHC(GT)"]])

# Gráfico 2: Distribuição de Temperatura
st.subheader("Distribuição de Temperatura")
st.bar_chart(df["T"])

# Gráfico 3: Umidade relativa
st.subheader("Umidade Relativa do Ar")
st.area_chart(df["RH"])
