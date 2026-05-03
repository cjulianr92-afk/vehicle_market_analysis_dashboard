import plotly.express as px
import streamlit as st
import pandas as pd


car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de vehículos usados')

build_hist = st.checkbox('Mostrar Histograma')
build_scatter = st.checkbox('Mostrar Dispersión')

if build_hist:
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Relación Precio vs Odómetro')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
