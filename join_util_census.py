import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime
import os

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = '/home/kircheis/data/shp/Electric_Retail_Service_Ter.shp'

census_shp = '/home/kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp'

census_path = '/home/kircheis/data/census/'

acs_path = '/home/kircheis/data/census/ACS_5y/'

#### IMPORT SOCIAL EXPLORER POPULATION DATA

all_pop = {}

all_dem = {}

c = {
'1990': None,
'2000': None,
'2010': None,
}

for i in c.keys():
    if ('census_tract_pop_%s' % i) in os.listdir(census_path):
        all_pop[i] = pd.read_csv((census_path + 'census_tract_pop_' + i), sep='\t', encoding='iso-8859-1')
        all_pop[i]['Geo_FIPS'] = all_pop[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')
    if ('census_tract_dem_%s' % i) in os.listdir(census_path):
        all_dem[i] = pd.read_csv((census_path + 'census_tract_dem_' + i), sep='\t', encoding='iso-8859-1')
        all_dem[i]['Geo_FIPS'] = all_dem[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')

#### OPTIONALLY IMPORT ACS POPULATION DATA

acs = {
'2007' : {'r': '2005_2009'},
'2008': {'r': '2006_2010'},
'2009': {'r': '2007_2011'},
'2010': {'r': '2008_2012'},
'2011': {'r': '2009_2013'}
}

####

for i in acs.keys():
    if not i in all_pop.keys():
        all_pop[i] = pd.read_csv((acs_path + 'ACS_' + acs[i]['r'] + '_pop'), sep='\t', encoding='iso-8859-1')
        all_pop[i]['Geo_FIPS'] = all_pop[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')
    if not i in all_dem.keys():
        all_dem[i] = pd.read_csv((acs_path + 'ACS_' + acs[i]['r'] + '_dem'), sep='\t', encoding='iso-8859-1')
        all_dem[i]['Geo_FIPS'] = all_dem[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')

#### PROCESS DATA

pop_yrs = pd.concat([all_pop[i].set_index('Geo_FIPS').rename(columns={'SE_T001_001':i})[i] for i in all_pop.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

cnames = {
        '1990': {'SE_T043' : 'mHHI', 'SE_T074' : 'occ',
                 'SE_T077' : 'vint', 'SE_T028' : 'lforce'},
        '2000': {'SE_T093' : 'mHHI', 'SE_T157' : 'occ',
                 'SE_T160' : 'vint', 'SE_T072' : 'lforce'},
        '2007': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'}, 
        '2008': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        '2009': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        '2010': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        '2011': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        }

for i in cnames.keys():
    cols = pd.Series(all_dem[i].columns)
    newcols = cols[cols.str.contains('Geo_FIPS|SE_T')]
    df = all_dem[i][newcols.values]
    for j in cnames[i].keys():
        newcols = newcols.str.replace(j, cnames[i][j])
    newcols[1:] = i + '_' + newcols[1:]
    df.columns = newcols.values
    all_dem[i] = df

dem_yrs = pd.concat([all_dem[i].set_index('Geo_FIPS') for i in all_dem.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

dem_d = {}

ucols = pd.Series(dem_yrs.columns).str.split('_').str[1:].apply('_'.join).unique()

for i in ucols:
    cols = pd.Series(dem_yrs.columns)
    newcols = cols[cols.str.contains(i)]
    df = dem_yrs[newcols.values]
    newcols = newcols.str.split('_').str[0]
    df.columns = newcols.values
    dem_d.update({i : df})

####

util_to_eia = pd.read_csv('/home/kircheis/github/RIPS/crosswalk/util_eia_id.csv', index_col=0)


j90 = pd.read_csv('util_join_1990.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')

j00 = pd.read_csv('util_join_2000.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2000'].astype(str).str.pad(11, side='left', fillchar='0')

j14 = pd.read_csv('util_join_2014.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2014'].astype(str).str.pad(11, side='left', fillchar='0')

util_to_c = pd.concat([j90, j00, j14]).drop_duplicates().reset_index()
util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'])
util_to_c = util_to_c.dropna().rename(columns={0:'GEOID'}).set_index('company_id')

def cat_load_census(idno):
    u = util_to_c.loc[idno]
    cT = pop_yrs.loc[u['GEOID'].values].sum()
    cT.index = cT.index.to_datetime()
    cT = cT.resample('A').interpolate()
    cT.name = 'pop'

    demdata = []

    for m in dem_d.keys():
        if m.split('_')[0] in ('lforce', 'occ'):
            dT = dem_d[m].loc[u['GEOID'].values].sum()
        elif m.split('_')[0] in ('vint', 'mHHI'):
            dT = dem_d[m].loc[u['GEOID'].values].median()
        dT.index = dT.index.to_datetime()
        dT = dT.resample('A').interpolate()
        dT.name = m
        demdata.append(dT)

    demdata = pd.concat(demdata, axis=1)

    c_load = pd.read_csv('/home/kircheis/github/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    c_load = c_load.resample('A').interpolate()

    cat = pd.concat([cT, c_load, demdata], axis=1)
    return cat

####
# INCONSISTENT FIELDS BETWEEN YEARS; 1990 lforce2 == 2000 lforce1, etc.
####
#OLD

def return_pop_load(idno):
    u = util_to_c.loc[idno]
    cT = pop_yrs.loc[u['GEOID'].values].sum()
    cT.index = cT.index.to_datetime()
    cT = cT.resample('A').interpolate()
    c_load = pd.read_csv('/home/kircheis/github/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    cat = pd.concat([cT, c_load.resample('A').interpolate()], axis=1).dropna().rename(columns={0:'pop'})
    return cat

#### OLD
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
