import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools

census_old = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_1990.shp'
census_new = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_2014.shp'

df_90 = gpd.read_file(census_old)
df_14 = gpd.read_file(census_new)

df_14_c = df_14.copy()
df_14_c['geometry'] = df_14_c.centroid

j = tools.sjoin(df_90, df_14_c, op='contains')

#### FORMAT CENSUS TRACT NAMES

#### NONDECIMAL ENTRIES
j['TRACT_NAME'][~j['TRACT_NAME'].str.contains('\.')] = (j['TRACT_NAME'][~j['TRACT_NAME'].str.contains('\.')] + '00').str.pad(6, side='left', fillchar='0')

#### DECIMAL ENTRIES
j['TRACT_NAME'][j['TRACT_NAME'].str.contains('\.')] = j['TRACT_NAME'][j['TRACT_NAME'].str.contains('\.')].str.replace('.', '').str.pad(6, side='left', fillchar='0')

#### CREATE FIPS

j['GEOID_1990'] = j['ST'].astype(str).str.cat(j['CO'].astype(str)).str.cat(j['TRACT_NAME'])

j_cross = j.rename(columns={'GEOID':'GEOID_2014'})[['GEOID_1990', 'GEOID_2014']].sort('GEOID_1990')
