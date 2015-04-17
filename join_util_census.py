import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'

census_shp = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp'

census_pop = '/home/kircheis/data/census/census_tract_pop_'


#### IMPORT SOCIAL EXPLORER POPULATION DATA

c = {
'1990': None,
'2000': None,
'2010': None,
}

for i in c.keys():
    c[i] = pd.read_csv((census_pop + i), sep='\t', encoding='iso-8859-1')
    c[i]['Geo_FIPS'] = c[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')

c_yrs = pd.concat([c[i].set_index('Geo_FIPS').rename(columns={'SE_T001_001':i})[i] for i in c.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

util_to_eia = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_eia_id.csv', index_col=0)


j90 = pd.read_csv('util_join_1990.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')

j00 = pd.read_csv('util_join_2000.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2000'].astype(str).str.pad(11, side='left', fillchar='0')

j14 = pd.read_csv('util_join_2014.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2014'].astype(str).str.pad(11, side='left', fillchar='0')

util_to_c = pd.concat([j90, j00, j14]).drop_duplicates().reset_index()
util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'])
util_to_c = util_to_c.dropna().rename(columns={0:'GEOID'}).set_index('company_id')


def return_pop_load(idno):
    u = util_to_c.loc[idno]
    c_ = c_yrs.loc[u['GEOID'].values].sum()
    cT = c_.T
    cT.index = pd.date_range(start=datetime.date(1990,1,1), end=datetime.date(2010,12,31), freq='10A')
    cT = cT.resample('A').interpolate()
    c_load = pd.read_csv('/home/kircheis/github/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    cat = pd.concat([cT, c_load.resample('A').interpolate()], axis=1).dropna().rename(columns={0:'pop'})
    return cat

######### TEST ##########
#########################
#########################
#########################
#
#aps_test = util_to_c.loc[803]
#c_aps = c_yrs.loc[aps_test['GEOID'].values].sum()
#cT = c_aps.T
#cT.index = pd.date_range(start=datetime.date(1990,1,1), end=datetime.date(2010,12,31), freq='10A')
#cT = cT.resample('A').interpolate()
##cT_sum = cT.sum(axis=1)
#
#aps_load = pd.read_csv('/home/kircheis/github/RIPS/data/hourly_load/wecc/803.csv', index_col=0, parse_dates=True)
#
#cat = pd.concat([cT, aps_load.resample('A').interpolate()], axis=1).dropna()
