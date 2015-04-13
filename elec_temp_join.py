import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools

utility = '/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp'
util = gpd.read_file(utility) 

urbarea = '/home/akagi/GIS/census/cb_2013_us_ua10_500k/cb_2013_us_ua10_500k.shp'
ua = gpd.read_file(urbarea)

ua = ua.to_crs(util.crs)

j = tools.sjoin(util, ua)

grid = '/home/akagi/gridcells.shp'
g = gpd.read_file(grid)
coords = g.centroid.apply(lambda x: x.coords[0])
coordstr = coords.apply(lambda x: 'data_%s_%s' % (x[1], x[0]))
g['coordstr'] = coordstr

ua_g = tools.sjoin(ua, g)
ua_g['grid_geom'] = ua_g['index_right'].map(g['geometry'])
ua_g.apply(lambda x: (x['geometry'].centroid).distance(x['grid_geom'].centroid), axis=1)

ua_g = ua_g.reset_index().loc[ua_g.reset_index().groupby('index').idxmin('dist')['FID'].values].set_index('index')

j['grid_cell'] = j['index_right'].map(ua_g['coordstr'])
