import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'

census_shp_1990 = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_1990.shp'
census_shp_2000 = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_2000.shp'
census_shp_2014 = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_2014.shp'

util = gpd.read_file(utility)
c1990 = gpd.read_file(census_shp_1990)
c2000 = gpd.read_file(census_shp_2000)
c2014 = gpd.read_file(census_shp_2014)

c1990 = c1990.to_crs(util.crs)
c2000 = c2000.to_crs(util.crs)
c2014 = c2014.to_crs(util.crs)

j90 = tools.sjoin(util, c1990)
j00 = tools.sjoin(util, c2000)
j14 = tools.sjoin(util, c2014)

j90['TRACT_NAME'] = j90['TRACT_NAME'].astype(str)

j90['TRACT_NAME'][~j90['TRACT_NAME'].str.contains('\.')] = (j90['TRACT_NAME'][~j90['TRACT_NAME'].str.contains('\.')] + '00').str.pad(6, side='left', fillchar='0')

#### DECIMAL ENTRIES
j90['TRACT_NAME'][j90['TRACT_NAME'].str.contains('\.')] = j90['TRACT_NAME'][j90['TRACT_NAME'].str.contains('\.')].str.replace('.', '').str.pad(6, side='left', fillchar='0')

#### CREATE FIPS

j90['GEOID_1990'] = j90['ST'].astype(str).str.cat(j90['CO'].astype(str)).str.cat(j90['TRACT_NAME'])

####

j00['GEOID_2000'] = j00['CTIDFP00'].astype(str).str.pad(11, side='left', fillchar='0')

####

j14['GEOID_2014'] = j14['GEOID'].astype(str).str.pad(11, side='left', fillchar='0')

#j90[['UNIQUE_ID', 'GEOID_1990']].to_csv('util_join_1990.csv')
#j14[['UNIQUE_ID', 'GEOID_2014']].to_csv('util_join_2014.csv')
#j00[['UNIQUE_ID', 'GEOID_2000']].to_csv('util_join_2000.csv')
