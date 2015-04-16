import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'

census_shp = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp'

census_pop = '/home/kircheis/data/census/census_tract_pop_'

util = gpd.read_file(utility)
census = gpd.read_file(census_shp)
census.crs = {'init': 'epsg:4269'}
census = census.to_crs(util.crs)

#### JOIN UTILITY SHAPEFILE WITH CENSUS TRACT SHAPEFILE

c_u = tools.sjoin(util, census)

#### IMPORT SOCIAL EXPLORER POPULATION DATA

c = {
'1990': None,
'2000': None,
'2010': None,
}

for i in c.keys():
    c[i] = pd.read_csv((census_pop + i), sep='\t', encoding='iso-8859-1')
    c[i]['Geo_FIPS'] = c[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')
    c[i]['Geo_TRACT'] = c[i]['Geo_TRACT'].astype(str).str.pad(6, side='left', fillchar='0')

c_yrs = pd.concat([c[i].set_index('Geo_FIPS').rename(columns={'SE_T001_001':i})[i] for i in c.keys()], axis=1).sort(axis=1).replace(0, np.nan)

cT = c_yrs.T
cT.index = pd.date_range(start=datetime.date(1990,1,1), end=datetime.date(2010,12,31), freq='10A')
cT = cT.asfreq('A').interpolate()

#### JOIN SOCIAL EXPLORER DATA WITH SPATIAL CENSUS DATA
cjoin = pd.merge(census, c_yrs, left_on='GEOID', right_index=True, how='inner')

#### MERGE CROSSWALKS

util_to_c = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_to_ctract.csv', index_col=0)
util_to_eia = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_eia_id.csv', index_col=0)

util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'].dropna())


######## TEST ##########
########################
########################
########################

aps_test = util_to_c.dropna().set_index('company_id').loc[803]
aps_test['GEOID'] = aps_test['GEOID'].astype(str).str.pad(11, side='left', fillchar='0')

### VV LOSE 3/4 of census tracts during dropna
c_aps = c_yrs.loc[aps_test['GEOID'].values].dropna()
cT = c_aps.T
cT.index = pd.date_range(start=datetime.date(1990,1,1), end=datetime.date(2010,12,31), freq='10A')
cT = cT.asfreq('A').interpolate()
cT_sum = cT.sum(axis=1)

aps_load = pd.read_csv('/home/kircheis/github/RIPS/data/hourly_load/wecc/aps', index_col=0, parse_dates=True)

cat = pd.concat([cT_sum, aps_load.resample('A')], axis=1).dropna()
