from config.configuration import db, collection
import pandas as pd



def restaurantes(ciudad, precio, tipo_cocina):
    lst = list(collection.find({"Cuisine Style": {"$regex": f".*{tipo_cocina}.*"}, 'Price Range': precio, 'City': ciudad}, {"Name": 1, 'web_restaurant': 1, 'Rating':1, "_id": 0}))
    df = pd.DataFrame(lst)
    return df.loc[0:4]


def enlace_restaurantes():
    lst = list(collection.find({"Cuisine Style": {"$regex": f".*{tipo_cocina}.*"}, 'Price Range': precio, 'City': ciudad}, {"Name": 1, 'web_restaurant': 1, 'Rating':1, "_id": 0}))
    df = pd.DataFrame(lst)
    df.loc[0:4]
    for i in range(0,5):
        url = df.loc[0:4].web_restaurant[i]
        if st.button(f'{df.loc[0:4].Name[i]}'):
            return webbrowser.open_new_tab(url)
def n():
    return '2'