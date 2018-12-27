import folium
from folium.plugins import MarkerCluster

import pandas as pd

#Loading data as dataframes using pandas
data = pd.read_csv("us-volcanoes.txt")
Lat = data['LAT']
Lon = data['LON']
Elevation = data['ELEV']

#Color corresponding to elevation of volcanoes
def switch_color(elevation):
	if (elevation < 1000):
		return ('green')
	elif (1000 <= elevation < 3000):
		return ('orange')
	else: return ('red')

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles ="CartoDB dark_matter")

#Create cluster
marker_cluster = MarkerCluster().add_to(map)

for lat, lon, elevation in zip(Lat, Lon, Elevation):
	folium.CircleMarker(location=[lat, lon], radius=9, popup=str(elevation) + " m", fill_color=switch_color(elevation), color="gray", fill_opacity=0.9).add_to(marker_cluster)

#Save the map
map.save("us-volcanoes-map.html")