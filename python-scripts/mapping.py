import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

#dfAsia = pd.read_csv('C:/Users/tyler/APL Projects/Data Combiner/Locational Data/fishy files take on Asia.csv')
#print("Read Asia")
dfEurope = pd.read_csv('C:/Users/tyler/APL Projects/Data Combiner/Locational Data/fishy files trip to small Europe.csv')
print("Read Small Europe")

#lat_lon_Asia = dfAsia[["cell_ll_lat", "cell_ll_lon"]]
#print("Sorted Asia")
lat_lon_Europe = dfEurope[["cell_ll_lat", "cell_ll_lon"]]
print("Sorted Small Europe")

from shapely.geometry.base import geometry_type_name
#geometry_Asia = [Point(xy) for xy in zip(lat_lon_Asia["cell_ll_lon"], lat_lon_Asia["cell_ll_lat"])]
#print("Geometry Asia Formed")
geometry_Europe = [Point(xy) for xy in zip(lat_lon_Europe["cell_ll_lon"], lat_lon_Europe["cell_ll_lat"])]
print("Geometry Asia Formed")

#gdf_Asia = GeoDataFrame(lat_lon_Asia, geometry = geometry_Asia)
#print("GDF Asia Fromed")
gdf_Europe = GeoDataFrame(lat_lon_Europe, geometry = geometry_Europe)
print("GDF Europe Fromed")

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
print("File read")

#gdf_Asia.plot(ax=world.plot(figsize=(15,15)), marker = 'o', color = 'red', markersize = 4)
#print("Asia Map Created")

gdf_Europe.plot(ax=world.plot(figsize=(15,15)), marker = 'o', color = 'red', markersize = 4)
print("Small Europe Map Created")