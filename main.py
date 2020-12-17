import streamlit as st
from PIL import Image
import options as op
import seaborn as sns
import matplotlib.pyplot as plt
import graficas as gr
import pandas as pd
import querys as qu
from config.configuration import db, collection
import webbrowser
import plotly.express as px
import scrap as sc
from selenium import webdriver
import pandas as pd
import re
import requests
import json
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
from time import sleep
from streamlit_folium import folium_static
import sys 




st.title("Bienvenido a tu recomendador de Restaurantes")

img = Image.open("imagen.jpg")
st.image(img,width=600,caption="Simple Image")

st.header('Puntuación ciudades')

gr.grafica1()

ciudad1 = st.selectbox('Ciudad donde buscas restaurante',op.firs_option) # elección de ciudad del cliente

st.write("you selected this option",ciudad1)

gr.precios_pais(ciudad1)


precio = st.selectbox('Cuánto te quieres gastar',op.second_option) #elección de cuánto se quiere gastar


tipo_cocina = st.selectbox("Qué te apetece comer?", op.lista_comidas) # elección de tipo de cocina qu quiere comer

gluten_free = st.selectbox("Gluten free?", ['Sí','No']) # elección si necesita opciones sin gluten o no


#query
if gluten_free == 'Sí':
    lst = list(collection.find({"Cuisine Style": {"$regex": f".*{tipo_cocina}.*"+".*Gluten.*"}, 'Price Range': precio, 'City': ciudad1}, {'Ranking':0, 'Price Range':0, 'Cuisine Style':0, "_id": 0}).sort("Rating", -1))
else:
    lst = list(collection.find({"Cuisine Style": {"$regex": f".*{tipo_cocina}.*"}, 'Price Range': precio, 'City': ciudad1}, {'Ranking':0, 'Price Range':0, 'Cuisine Style':0, "_id": 0}).sort("Rating", -1))


df = pd.DataFrame(lst)
try:
    df.loc[0:4]
    if st.button('BUSCAR UBICACIÓN'):
        try:
            web = list(df.loc[0:4].web_restaurant)
            
            lst_2 = []
            for i in web:
                lst_2.append(sc.scrap2(i))

            df_loc = pd.DataFrame(lst_2, columns=['long', 'lat'])

            concat_df = pd.concat([df_loc, df.loc[0:4]], axis=1,)
            


            local_ini = sc.geocode(ciudad1)
            map_1 = Map(location= [local_ini.get('coordinates')[1], local_ini.get('coordinates')[0]], zoom_start = 8)
            for i,row in concat_df.iterrows():
                #popup distrito
                distrito = {
                    "location" : [row["long"], row["lat"]],
                    "tooltip" : row["Name"]
                }
                icon = Icon( color = "blue",
                                prefix = "fa",
                                icon = "home",
                                icon_color = "black"
                    )
                Marker (**distrito).add_to(map_1)
            folium_static(map_1)

        except:
            st.header('No hemos podido encontrar la ubicación de los restaurantes, lo sentimos')
    
    


    st.header('Enlaces de los restaurantes')
    ## enlaces
    try:
        for i in range(0,df.shape[0]):
            url = df.loc[0:4].web_restaurant[i]
            if st.button(f'{df.loc[0:4].Name[i]}'):
                webbrowser.open_new_tab(url)
    except:
        st.header('')




    election = st.selectbox('Qué restaurante has elegido?', list(df.loc[0:4].Name))

    review = st.text_input('Danos tu opinión')



    if st.button('Enviar'):
        collection.update_one(
    {
        'Name': f'{election}',
    }, {
        '$push' : {
        'new_review': [f'{review}']
        }
    }
    )
except:
    st.header('No, hemos encontrado ningún restaurante con estas características')





