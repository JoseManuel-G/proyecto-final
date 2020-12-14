import pandas as pd

restaurants = pd.read_csv('data/df_restaurants.csv')

firs_option = list(restaurants.City.unique())

second_option = list(restaurants['Price Range'].unique())

lista_comidas = ['Mediterranean', 'Contemporary', 'Asian', 'Fast Food', 'Healthy', 'Vegetarian', 'Indian', 'Argentinean', 'Seafood', 'Chienese', 'Italian', 'Grill', 'Sushi', 'Vegan', 'Pizza', 'Mexican', 'Spanish']