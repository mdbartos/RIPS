import datetime
import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import sys
sys.path.append('/home/kircheis/github/RIPS')
from rect_grid import rect_grid

utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'
util = gpd.read_file(utility) 

urbarea = '/home/kircheis/data/shp/census/cb_2013_us_ua10_500k/cb_2013_us_ua10_500k.shp'
ua = gpd.read_file(urbarea)

ua = ua.to_crs(util.crs)

j = tools.sjoin(util, ua)

g = rect_grid((-130, 24, -65, 50), 0.125) 

coords = g.centroid.apply(lambda x: x.coords[0])
coordstr = coords.apply(lambda x: 'data_%s_%s' % (x[1], x[0]))
g['coordstr'] = coordstr

ua_g = tools.sjoin(ua, g)
ua_g['grid_geom'] = ua_g['index_right'].map(g['geometry'])
ua_g.apply(lambda x: (x['geometry'].centroid).distance(x['grid_geom'].centroid), axis=1)

ua_g = ua_g.reset_index().loc[ua_g.reset_index().groupby('index').idxmin('dist')['FID'].values].set_index('index')

j['grid_cell'] = j['index_right'].map(ua_g['coordstr'])

eia_to_util = pd.read_csv('./crosswalk/util_eia_id.csv', index_col=0)

j['eia_code'] = j['UNIQUE_ID'].map(eia_to_util['company_id'])

j = j.dropna(subset=['eia_code']).set_index('eia_code').sort_index()

## LADWP ID: 11208

la1 = pd.read_csv('/home/kircheis/data/source_hist_forcings/data_33.5625_-117.9375', sep='\t', names=['year', 'month', 'day', 'prcp', 'tmax', 'tmin', 'wspd'])
la1.index = pd.date_range(start=datetime.date(1949,1,1), end=datetime.date(2010,12,31), freq='D')

la2 = pd.read_csv('/home/kircheis/data/source_hist_forcings/data_37.3125_-118.4375', sep='\t', names=['year', 'month', 'day', 'prcp', 'tmax', 'tmin', 'wspd'])
la2.index = pd.date_range(start=datetime.date(1949,1,1), end=datetime.date(2010,12,31), freq='D')
