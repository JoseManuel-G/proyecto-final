import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


def precios_pais(ciudad: str):
    colors = ['g', 'c', 'm']
    df_restaurants = pd.read_csv('data/df_restaurants.csv')
    df_ciudad = df_restaurants[df_restaurants.City == ciudad]
    fig, ax = plt.subplots()
    ax.hist(x=df_ciudad['Price Range'], color = 'g')
    return st.pyplot(fig)

def grafica1():
    """
    Grafica que te devuelve la media de puntuación de los restaurantes por pais
    """
    x = list()
    y = list()
    df_restaurants = pd.read_csv('data/df_restaurants.csv')
    for city in list(df_restaurants['City'].unique()):
        x.append(city)
        y.append(df_restaurants[df_restaurants['City'] == city]['Rating'].mean())
    fig = px.bar(df_restaurants, x=x, y=y, color=df_restaurants['City'].unique(), barmode="stack")
    return st.plotly_chart(fig)

