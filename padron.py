import streamlit as st
import pandas as pd

# URL del archivo Excel en GitHub (asegúrate de tener el enlace correcto)
url = "https://github.com/iterAR-eco/padron/raw/refs/heads/main/Padron.xlsx"

@st.cache
def cargar_datos(url):
    # Cargar el archivo Excel desde GitHub usando el motor openpyxl
    df = pd.read_excel(url, engine='openpyxl')
    return df

# Cargar los datos
df = cargar_datos(url)

# Título de la aplicación
st.title("Votá LISTA 15 - PABLO NICOLETTI Presidente")
st.title("Búsqueda por DNI")

# Input para ingresar el DNI
dni_input = st.text_input("Introduce el DNI (Sin puntos):", "")

# Si se ingresa un DNI, buscar la fila correspondiente
if dni_input:
    # Convertir el input a entero si es necesario
    try:
        dni_input = int(dni_input)
        fila = df[df['DNI'] == dni_input]
        
        # Si se encuentra el DNI, mostrar la fila
        if not fila.empty:
            st.write("Resultado para el DNI:", dni_input)
            st.write(fila)
        else:
            st.write("No se encontró ningún resultado para el DNI ingresado.")
    except ValueError:
        st.write("Por favor, introduce un número válido de DNI.")
