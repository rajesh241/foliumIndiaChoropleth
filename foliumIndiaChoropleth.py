import folium
import pandas as pd
import os

states = os.path.join('data', 'india-states_nrega.json')
data = os.path.join('data', 'womenWorkForce.csv')
dtype_dic= { 'State':str }
state_data = pd.read_csv(data,dtype=dtype_dic)
m = folium.Map(location=[23.21, 79.51], zoom_start=5)

folium.Choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', 'Value'],
    key_on='feature.properties.nregaCode',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Women WorkForce %',
    highlight=True
).add_to(m)

folium.LayerControl().add_to(m)

m.save('indiaChoropleth.html')
