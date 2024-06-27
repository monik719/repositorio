import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Anuncios de ventas de coches') # titulo
st.header('Aqui puedes encontrar toda la informacion y las caracteristicas de cada vehiculo en venta')

car_data = pd.read_csv('./data/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

# Crear un grafico de dispersion
grafico_button= st.button('Construir grafico de dispersion')
if grafico_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de ventas de coches')
    
    #crea un grafico
    graf= px.scatter(car_data, x="odometer")

    #mostrar el grafico
    st.plotly_chart(graf, use_container_width=True)

        