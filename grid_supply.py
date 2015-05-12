import pandas as pd
import numpy as np
import geopandas as gpd
from shapely import geometry
from scipy import spatial

#### SPECIFY SHAPEFILES

substations = '/home/akagi/Desktop/electricity_data/Substations.shp'
s = gpd.read_file(substations)

#STATIC

generation = '/home/akagi/Desktop/electricity_data/Generation.shp'
g_sta = gpd.read_file(generation)

# DYNAMIC
plant_860 = pd.read_excel('/home/akagi/Documents/EIA_form_data/eia8602012/PlantY2012.xlsx', header=1)
gen_860 = pd.read_excel('/home/akagi/Documents/EIA_form_data/eia8602012/GeneratorY2012.xlsx', sheetname='Operable', header=1)

plant_cap = pd.merge(plant_860, gen_860, on='Plant Code').groupby('Plant Code').sum()[['Summer Capacity (MW)', 'Winter Capacity (MW)', 'Nameplate Capacity (MW)']]
plant_chars = plant_860.set_index('Plant Code')[['Plant Name', 'Utility ID', 'NERC Region', 'Grid Voltage (kV)', 'Latitude', 'Longitude']]
g_dyn = pd.concat([plant_cap, plant_chars], axis=1).dropna(subset=['Longitude', 'Latitude'])


#### FIND NEAREST NEIGHBORS

tree = spatial.cKDTree(np.vstack(s.geometry.apply(lambda x: x.coords[0]).values))

node_query_sta = tree.query(np.vstack(g_sta.geometry.apply(lambda x: x.coords[0]).values)) 
node_query_dyn = tree.query(np.vstack(g_dyn[['Longitude', 'Latitude']].values)) 

sta_crosswalk = pd.DataFrame(np.column_stack([g_sta[['UNIQUE_ID', 'S_CAP_MW']].values, s.iloc[node_query_sta[1]]['UNIQUE_ID'].values.astype(int)]), columns=['GEN_ID', 'S_CAP_MW', 'SUB_ID'])

sta_crosswalk = sta_crosswalk[['GEN_ID', 'SUB_ID', 'S_CAP_MW']]

sta_crosswalk.to_csv('gen_to_sub_static.csv')
