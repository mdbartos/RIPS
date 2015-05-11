import pandas as pd
import numpy as np
import geopandas as gpd
from shapely import geometry
from scipy import spatial

#### SPECIFY SHAPEFILES

translines = '/home/akagi/Desktop/electricity_data/Transmission_Lines.shp'
t = gpd.read_file(translines)

substations = '/home/akagi/Desktop/electricity_data/Substations.shp'
s = gpd.read_file(substations)

#### EXTRACT START AND END POINTS IN NETWORK

start = t.geometry[t.geometry.type=='LineString'].apply(lambda x: np.array([x.xy[0][0], x.xy[1][0]])).append(t.geometry[t.geometry.type=='MultiLineString'].apply(lambda x: np.hstack([i.xy for i in x])[:,0])).sort_index()

end = t.geometry[t.geometry.type=='LineString'].apply(lambda x: np.array([x.xy[0][-1], x.xy[1][-1]])).append(t.geometry[t.geometry.type=='MultiLineString'].apply(lambda x: np.hstack([i.xy for i in x])[:,-1])).sort_index()

#### FIND NEAREST NEIGHBORS

tree = spatial.cKDTree(np.vstack(s.geometry.apply(lambda x: x.coords[0]).values))

start_node_query = tree.query(np.vstack(start.values)) 
end_node_query = tree.query(np.vstack(end.values)) 

#### CREATE CROSSWALK TABLE

crosswalk = pd.DataFrame(np.column_stack([t[['UNIQUE_ID', 'TOT_CAP_KV', 'NUM_LINES', 'Shape_Leng']].values, s.iloc[start_node_query[1]][['UNIQUE_ID', 'NAME']].values, start_node_query[0], s.iloc[end_node_query[1]][['UNIQUE_ID', 'NAME']].values, end_node_query[0]]), columns=['TRANS_ID', 'TOT_CAP_KV', 'NUM_LINES', 'LENGTH', 'SUB_1', 'NAME_1', 'ERR_1', 'SUB_2', 'NAME_2', 'ERR_2'])

crosswalk = crosswalk[['TRANS_ID', 'SUB_1', 'SUB_2', 'NAME_1', 'NAME_2',  'ERR_1', 'ERR_2', 'TOT_CAP_KV', 'NUM_LINES', 'LENGTH']]

# crosswalk.to_csv('edges.csv')
