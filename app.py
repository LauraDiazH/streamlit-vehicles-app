iimport streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('🚗 Análisis de Anuncios de Vehículos Usados en EE.UU.')

# Botón para mostrar histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Distribución del odómetro (km):')
    fig_hist = px.histogram(df, x='odometer', title='Distribución del odómetro (km)')
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para mostrar gráfico de dispersión
if st.button('Mostrar dispersión precio vs odómetro'):
    st.write('Relación entre precio y kilometraje:')
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Precio vs Odómetro')
    st.plotly_chart(fig_scatter, use_container_width=True)