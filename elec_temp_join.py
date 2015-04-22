import datetime
import os
import numpy as np
import pandas as pd
from shapely import geometry
import geopandas as gpd
from geopandas import tools
import sys
sys.path.append('/home/kircheis/github/RIPS')
from rect_grid import rect_grid

#### DECLARE FILE PATHS

utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'
util = gpd.read_file(utility) 

urbarea = '/home/kircheis/data/shp/census/cb_2013_us_ua10_500k/cb_2013_us_ua10_500k.shp'
ua = gpd.read_file(urbarea)
ua = ua.to_crs(util.crs)

urbpop = '/home/kircheis/data/census/ua/ua_list_all.txt'
uapop = pd.read_fwf(urbpop, colspecs=[(0,5), (10,70), (75,84), (89,98), (103,117), (122,131), (136,150), (155,164), (169,178), (183,185)], names=['UACE', 'NAME', 'POP', 'HU', 'AREALAND', 'AREALANDSQMI', 'AREAWATER', 'AREAWATERSQMI', 'POPDEN', 'LSADC'], skiprows=1)
uapop['UACE'] = uapop['UACE'].astype(str).str.pad(5, side='left', fillchar='0')
uapop = uapop.set_index('UACE')
#### FIND WHICH URBAN AREAS ARE IN WHICH UTILITY SERVICE AREAS

j = tools.sjoin(util, ua)

#### ALLOCATE GRID FOR TEMPERATURE FORCINGS

g = rect_grid((-130, 24, -65, 50), 0.125) 

coords = g.centroid.apply(lambda x: x.coords[0])
coordstr = coords.apply(lambda x: 'data_%s_%s' % (x[1], x[0]))

g = gpd.GeoDataFrame(geometry=g.geometry, index=g.index)
g.crs = util.crs
g['coordstr'] = coordstr

#### JOIN UTILITY SERVICE AREAS WITH TEMPERATURE FORCINGS

ua_g = tools.sjoin(ua, g)
ua_g['grid_geom'] = ua_g['index_right'].map(g['geometry'])
ua_g['dist'] = ua_g.apply(lambda x: (x['geometry'].centroid).distance(x['grid_geom'].centroid), axis=1)

ua_g_out = ua_g.reset_index().loc[ua_g.reset_index().groupby('index').idxmin('dist')['dist'].values].set_index('index')


#### MAP COORDINATE STRING TO ORIGINAL JOIN

j['grid_cell'] = j['index_right'].map(ua_g_out['coordstr'])
j['POP'] = j['UACE10'].map(uapop['POP']) 

eia_to_util = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_eia_id.csv', index_col=0)

j['eia_code'] = j['UNIQUE_ID'].map(eia_to_util['company_id'])

#### WRITE TO CSV

#j[['UNIQUE_ID', 'NAME', 'CITY', 'index_right', 'AFFGEOID10', 'UACE10', 'NAME10', 'grid_cell', 'POP', 'eia_code']].to_csv('util_demand_to_met_ua')

#### FOR UTILITIES WITH NO URBAN AREA

non_ua = util[~np.in1d(util['UNIQUE_ID'].values, j['UNIQUE_ID'].unique())]
non_ua_c = non_ua.centroid

dirlist = pd.Series(os.listdir('/home/kircheis/data/source_hist_forcings/'))

distlist = gpd.GeoSeries(dirlist.str.split('_').str[::-1].str[:-1].apply(lambda x: geometry.Point(float(x[0]), float(x[1]))))

non_ua['grid_cell'] = non_ua.centroid.apply(lambda x: dirlist[list(distlist.sindex.nearest(x.coords[0], objects='raw'))[0]])

non_ua['eia_code'] = non_ua['UNIQUE_ID'].map(eia_to_util['company_id'])

#### WRITE TO CSV
#non_ua[['UNIQUE_ID', 'NAME', 'grid_cell', 'eia_code']].to_csv('util_demand_to_met_nonua')
