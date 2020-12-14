import streamlit as st
from PIL import Image
import options as op
import seaborn as sns
import matplotlib.pyplot as plt
import graficas as gr
import pandas as pd
import querys as qu
from config.configuration import db, collection

st.title("Bienvenido a tu recomendador de Restaurantes")

img = Image.open("imagen.jpg")
st.image(img,width=600,caption="Simple Image")

st.header('Puntuación ciudades')

gr.grafica2()

ciudad = st.selectbox('Ciudad donde buscas restaurante',op.firs_option)

st.write("you selected this option",ciudad)

gr.precios_pais(ciudad)


precio = st.selectbox('Cuánto te quieres gastar',op.second_option)




tipo_cocina = st.selectbox("Qué te apetece comer?", op.lista_comidas)



lst = list(collection.find({"Cuisine Style": {"$regex": f".*{tipo_cocina}.*"}, 'Price Range': precio, 'City': ciudad}, {"Name": 1, 'Rating':1, "_id": 0}))
df = pd.DataFrame(lst)

try:
    df.loc[0:4]
except:
    st.header('No, hemos encontrado ningún restaurante con estas características')























