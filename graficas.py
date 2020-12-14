import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



def grafica2():
    x = list()
    y = list()
    df_restaurants = pd.read_csv('data/df_restaurants.csv')
    for city in list(df_restaurants['City'].unique()):
        x.append(city)
        y.append(df_restaurants[df_restaurants['City'] == city]['Rating'].mean())
    fig, ax = plt.subplots(1,1,figsize=(17,7))
    ax.bar(x,y,color = 'cyan',edgecolor = 'black')
    ax.set_ylim(bottom=3.5)
    ax.set_xticklabels(labels = x, rotation = 45)
    ax.set_xlabel('City')
    ax.set_ylabel('Average Review Rating')
    return st.pyplot(fig)


def grafica_top_rating_mean():
    df_restaurants = pd.read_csv('data/df_restaurants.csv')
    rating_mean = df_restaurants.groupby('City').Rating.mean()
    sort_rating_mean = rating_mean.sort_values(ascending=False)
    sort_rating_mean = pd.DataFrame(sort_rating_mean)

    top_rating_mean = sort_rating_mean.head()
    fig, ax = plt.subplots()
    ax.scatter(x=top_rating_mean.index, y = top_rating_mean.Rating)
    return st.pyplot(fig)




def precios_pais(ciudad: str):
    colors = ['g', 'c', 'm']
    df_restaurants = pd.read_csv('data/df_restaurants.csv')
    df_ciudad = df_restaurants[df_restaurants.City == ciudad]
    fig, ax = plt.subplots()
    ax.hist(x=df_ciudad['Price Range'], color = 'g')
    return st.pyplot(fig)