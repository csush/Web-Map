import os
import json
import folium
import pandas as pd

#Loading data as dataframes using pandas
unemployment_data = os.path.join('data', 'us-unemployment.csv')
emp_data = pd.read_csv(unemployment_data)

state_geo = os.path.join('data', 'us-states.json')
geo_data = json.load(open(state_geo))

#Create base map
map = folium.Map(location=[37,-100], zoom_start = 4)

folium.Choropleth(
	geo_data=geo_data,
	data=emp_data,
	name='Unemployment Rate',
	columns=['State', 'Unemployment'],
	key_on='feature.id',
	fill_color='YlGn',
	fill_opacity=0.7,
	line_opacity=0.2,
	legend_name='Unemployment Rate (%)'
).add_to(map)

#Save the map
map.save("us-unemployment-map.html")