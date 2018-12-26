import folium

import pandas as pd

data = pd.read_csv("us-volcanoes.txt")
Lat = data['LAT']
Lon = data['LON']
Elevation = data['ELEV']

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles ="Mapbox bright")

for lat, lon, elevation in zip(Lat, Lon, Elevation):
	folium.Marker(location=[lat, lon], popup=str(elevation) + " m", icon=folium.Icon(color = 'red')).add_to(map)

#Save the map
map.save("map1.html")