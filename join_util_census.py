import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'

census_shp = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp'

census_pop = '/home/kircheis/data/census/census_tract_pop_'

census_compat = '/home/kircheis/github/RIPS/crosswalk/c90_to_c10.csv'

util = gpd.read_file(utility)
census = gpd.read_file(census_shp)
census.crs = {'init': 'epsg:4269'}
census = census.to_crs(util.crs)

compat = pd.read_csv(census_compat, index_col=0).astype(str).apply(lambda x: x.str.pad(11, side='left', fillchar='0'))
compat = compat.append(pd.DataFrame({'GEOID_1990': compat['GEOID_1990'].values, 'GEOID_2014': compat['GEOID_1990'].values})).drop_duplicates('GEOID_2014')

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

c_yrs = pd.concat([c[i].set_index('Geo_FIPS').rename(columns={'SE_T001_001':i})[i] for i in c.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

#c_yrs['GEOID_1990'] = pd.Series(c_yrs.index, index=c_yrs.index).map(compat.set_index('GEOID_2014')['GEOID_1990'])

#c_yrs = c_yrs.groupby('GEOID_1990').sum()
#c_yrs = c_yrs.dropna(subset=['GEOID_1990']).set_index('GEOID_1990')

cT = c_yrs.T
cT.index = pd.date_range(start=datetime.date(1990,1,1), end=datetime.date(2010,12,31), freq='10A')
cT = cT.asfreq('A').interpolate()

#### JOIN SOCIAL EXPLORER DATA WITH SPATIAL CENSUS DATA
cjoin = pd.merge(census, c_yrs, left_on='GEOID', right_index=True, how='inner')

#### MERGE CROSSWALKS

#util_to_c = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_to_ctract.csv', index_col=0)
util_to_eia = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_eia_id.csv', index_col=0)

#util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'].dropna())
#util_to_c['GEOID'] = util_to_c['GEOID'].astype(str).str.pad(11, side='left', fillchar='0')

#util_to_c['GEOID_1990'] = util_to_c['GEOID'].astype(str).str.pad(11, side='left', fillchar='0').map(compat.set_index('GEOID_2014')['GEOID_1990'])
j90 = pd.read_csv('util_join_1990.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')
j00 = pd.read_csv('util_join_2000.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2000'].astype(str).str.pad(11, side='left', fillchar='0')
j14 = pd.read_csv('util_join_2014.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2014'].astype(str).str.pad(11, side='left', fillchar='0')
util_to_c = pd.concat([j90, j00, j14]).drop_duplicates().reset_index()
util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'])
util_to_c = util_to_c.dropna().rename(columns={0:'GEOID'}).set_index('company_id')
######## TEST ##########
########################
########################
########################

aps_test = util_to_c.loc[803]
c_aps = c_yrs.loc[aps_test['GEOID'].values].sum()
cT = c_aps.T
cT.index = pd.date_range(start=datetime.date(1990,1,1), end=datetime.date(2010,12,31), freq='10A')
cT = cT.resample('A').interpolate()
#cT_sum = cT.sum(axis=1)

aps_load = pd.read_csv('/home/kircheis/github/RIPS/data/hourly_load/wecc/803.csv', index_col=0, parse_dates=True)

cat = pd.concat([cT, aps_load.resample('A').interpolate()], axis=1).dropna()
