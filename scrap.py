from selenium import webdriver
from time import sleep
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


def scrap2(pagina):
    driver = webdriver.Chrome("./chromedriver")
    sleep(1)
    try:
        driver.get(pagina)
        img = driver.find_element_by_css_selector('img.rAA8XwlX')
        string = img.get_attribute("src")
        x = re.findall('([+-]?(\d+.\d+),([+-]?(\d+.\d+)))', string)
        lat_long = x[0][0]
        lat_lon = lat_long.split(',')
        lat = float(lat_lon[0])
        long = float(lat_lon[1])
    except:
        return [0,0]
    return [lat, long]


def scrap1(pagina):
    driver = webdriver.Chrome("./chromedriver")
    sleep(1)
    try:
        driver.get(pagina)
        sleep(1)
        img = driver.find_element_by_css_selector('img.rAA8XwlX')
        string = img.get_attribute("src")
        x = re.findall('[+-]?((9[0]?|[0-8][0-9]?([.,][0-9]+)?))', string)
        lat = float(x[6][1])
        long = float(x[7][1])
    except:
        return [0,0]
    return [lat, long]



def geocode(address):
    """
    Saca las coordenadas de una dirección que le des.
    """
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":[float(data["longt"]),float(data["latt"])]}
    except:
        return data






def mapa(ciudad):
    local_ini = geocode(ciudad)
    map_1 = Map(location= [local_ini.get('coordinates')[1], local_ini.get('coordinates')[0]], zoom_start = 15)

    return folium_static(map_1)
