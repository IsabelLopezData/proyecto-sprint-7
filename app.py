import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los

st.header("Análisis de venta de autos usados")

hist_button = st.button('Construir histograma')  # crear un botón


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data,
                       x="odometer",
                       title="Distribución del kilometraje de los vehículos",
                       labels={"odometer": "Kilometraje"}
                       )
    fig.update_layout(yaxis_title="Cantidad de autos")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_scatter:  # si la casilla de verificación está seleccionada

    st.write("Creando gráfico de Dispersión")

    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre Kilometraje y Precio",
                     labels={"odometer": "Kilometraje",
                             "price": "Precio"}
                     )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
