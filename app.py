import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de coches')

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Histograma de odómetro')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Gráfico de dispersión: odómetro vs precio')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True) 