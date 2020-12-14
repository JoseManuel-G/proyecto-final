from config.configuration import db, collection
import pandas as pd



def restaurantes(ciudad, precio, tipo_cocina):
    lst = list(collection.find({"Cuisine Style": {"$regex": f".*{tipo_cocina}.*"}, 'Price Range': precio, 'City': ciudad}, {"Name": 1, 'Rating':1, "_id": 0}))
    df = pd.DataFrame(lst)
    return df.loc[0:4]
