import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime
import os
import statsmodels.api as sm
import sys
import scipy
import matplotlib.pyplot as plt

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = '/home/akagi/github/RIPS_kircheis/data/shp/Electric_Retail_Service_Ter.shp'

census_shp = '/home/akagi/github/RIPS_kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp'

census_path = '/home/akagi/github/RIPS_kircheis/data/census/'

acs_path = '/home/akagi/github/RIPS_kircheis/data/census/ACS_5y/'

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

util_to_eia = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/crosswalk/util_eia_id.csv', index_col=0)


j90 = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_join_1990.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')

j00 = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_join_2000.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2000'].astype(str).str.pad(11, side='left', fillchar='0')

j14 = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_join_2014.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_2014'].astype(str).str.pad(11, side='left', fillchar='0')

util_to_c = pd.concat([j90, j00, j14]).drop_duplicates().reset_index()
util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'])
util_to_c = util_to_c.dropna().rename(columns={0:'GEOID'}).set_index('company_id')

def cat_load_census(idno):
    u = util_to_c.loc[idno]
    cT = pop_yrs.loc[u['GEOID'].values].sum()
    cT.index = cT.index.to_datetime()
    cT = cT.resample('M').interpolate()
    cT.name = 'pop'

    demdata = []

    for m in dem_d.keys():
        if m.split('_')[0] in ('lforce', 'occ'):
            dT = dem_d[m].loc[u['GEOID'].values].sum()
        elif m.split('_')[0] in ('vint', 'mHHI'):
            dT = dem_d[m].loc[u['GEOID'].values].median()
        dT.index = dT.index.to_datetime()
        dT = dT.resample('M').interpolate()
        dT.name = m
        demdata.append(dT)

    demdata = pd.concat(demdata, axis=1)

    c_load = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    c_load = c_load.resample('M').interpolate()

    cat = pd.concat([cT, c_load, demdata], axis=1)
    return cat

def plot_curvefit(xdata, ydata):
    xy = np.vstack([xdata,ydata])
    z = scipy.stats.gaussian_kde(xy)(xy)
    plt.scatter(xdata, ydata, c=z, s=100, edgecolor='')

def fit_data(idno):
    data = cat_load_census(idno)[['load', 'pop', 'lforce_001', 'mHHI_001']].dropna()
    data = data[data.index.year!=2005]
    datasummer = data[np.in1d(data.index.month, [6,7,8])]
    y = datasummer['load']
    X = datasummer[['pop', 'lforce_001', 'mHHI_001']]
    X = sm.add_constant(X)
    est = sm.OLS(y, X).fit()

    c_load = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    resampled = pd.Series(est.predict(), index=data.index[np.in1d(data.index.month, [6,7,8])]).resample('h').interpolate()

    norm_load = (c_load - resampled).dropna()

    dem_ua = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_demand_to_met_ua')

    dem_util = dem_ua.set_index('eia_code').sort_index().loc[idno]

    util_d = {}
    hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

    for i in range(len(dem_util.index)):
        data_name = dem_util.iloc[i]['grid_cell']
        lat = float(data_name.split('_')[1])
        lon = float(data_name.split('_')[2])
        pop = int(dem_util.iloc[i]['POP'])
        df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
        df = df[np.in1d(df.index.month, [6,7,8])]
        if not data_name in util_d.keys():
            util_d.update({data_name : {}})
            util_d[data_name].update({'pop' : pop})
            util_d[data_name].update({'data' : df})
        else:
            util_d[data_name]['pop'] += pop

    totpop = sum([util_d[i]['pop'] for i in util_d.keys()])
    tempcat = pd.concat([util_d[i]['pop']*util_d[i]['data'] for i in util_d.keys()], axis=1)
    tmax = tempcat[4].sum(axis=1)/totpop
    tmin = tempcat[5].sum(axis=1)/totpop

    max_loads = norm_load.groupby(norm_load.index.date).max()
    max_loads.index = pd.to_datetime(max_loads.index)
    max_loads = max_loads.resample('h', loffset='12H')

    peak = pd.concat([max_loads, tmax.resample('h', loffset='12H')], axis=1).dropna()
    peak = peak[peak.index.weekday <= 4]    #BUSINESS DAYS ONLY

    linfit = np.polyfit(peak[0], peak['load'], 1)

    tot_load = c_load.groupby(c_load.index.date).max()
    tot_load.index = pd.to_datetime(tot_load.index)

    load_anom = (peak['load'].resample('d')/tot_load['load']).dropna()

    linreg = scipy.stats.linregress(peak[0], load_anom)

    fig, ax = plt.subplots(1)
    plot_curvefit(peak[0], load_anom)
    plt.plot(np.arange(peak[0].min(), peak[0].max()), linreg[0]*np.arange(peak[0].min(), peak[0].max()) + linreg[1])

    util_name = util_to_eia.dropna().set_index('company_id').loc[idno, 'utility_name']
    plt.title('%s, %s' % (util_name, idno))
    plt.ylabel('Load Anomaly')
    plt.xlabel('Air Temperature ($^\circ$C)')
    textstr = '$\\alpha=%.2f$\n$\\beta=%.2f$\n$n=%s$\n$r=%.2f$' % (linreg[0], linreg[1], len(peak), linreg[2])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', linespacing=1.25, bbox=props)
    plt.savefig('%s.png' % (idno), bbox_inches='tight')
    plt.clf()


for fn in os.listdir('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc'):
    if fn.endswith('csv'):
        i = int(fn.split('.')[0])
        try:
            fit_data(i)
        except:
            print(i)




def fit_data_no_linreg(idno):
    data = cat_load_census(idno)[['load', 'pop', 'lforce_001', 'mHHI_001']].dropna()
    data = data[data.index.year!=2005]
    datasummer = data[np.in1d(data.index.month, [6,7,8])]
    # y = datasummer['load']
    # X = datasummer[['pop', 'lforce_001', 'mHHI_001']]
    # X = sm.add_constant(X)
    # est = sm.OLS(y, X).fit()

    c_load = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    c_load = c_load.groupby(c_load.index.date).max()

    norm_load = (1000000*c_load['load']/(data['pop'].reindex_like(c_load).interpolate())).dropna()
    norm_load.index = pd.to_datetime(norm_load.index)
    norm_load = norm_load[np.in1d(norm_load.index.month, [6,7,8])]

#    norm_load = pd.Series(1000000*datasummer['load']/datasummer['pop'], index=data.index[np.in1d(data.index.month, [6,7,8])]).resample('h').interpolate()

#    norm_load = (c_load - resampled).dropna()

    dem_ua = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_demand_to_met_ua')

    dem_util = dem_ua.set_index('eia_code').sort_index().loc[idno]

    util_d = {}
    hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

    for i in range(len(dem_util.index)):
        data_name = dem_util.iloc[i]['grid_cell']
        lat = float(data_name.split('_')[1])
        lon = float(data_name.split('_')[2])
        pop = int(dem_util.iloc[i]['POP'])
        df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
        df = df[np.in1d(df.index.month, [6,7,8])]
        if not data_name in util_d.keys():
            util_d.update({data_name : {}})
            util_d[data_name].update({'pop' : pop})
            util_d[data_name].update({'data' : df})
        else:
            util_d[data_name]['pop'] += pop

    totpop = sum([util_d[i]['pop'] for i in util_d.keys()])
    tempcat = pd.concat([util_d[i]['pop']*util_d[i]['data'] for i in util_d.keys()], axis=1)
    tmax = tempcat[4].sum(axis=1)/totpop
    tmin = tempcat[5].sum(axis=1)/totpop

#    max_loads = norm_load.groupby(norm_load.index.date).max()
#    max_loads.index = pd.to_datetime(max_loads.index)
#    max_loads = max_loads.resample('h', loffset='12H')

    peak = pd.concat([norm_load, tmax], axis=1).dropna()
    peak = peak[peak.index.weekday <= 4]    #BUSINESS DAYS ONLY

#    linfit = np.polyfit(peak[1], peak[0], 1)

#    tot_load = c_load.groupby(c_load.index.date).max()
#    tot_load.index = pd.to_datetime(tot_load.index)

#    load_anom = (peak[0].resample('d')/tot_load['load']).dropna()

    linreg = scipy.stats.linregress(peak[1], peak[0])

    fig, ax = plt.subplots(1)
    plot_curvefit(peak[1], peak[0])
    plt.plot(np.arange(peak[1].min(), peak[1].max()), linreg[0]*np.arange(peak[1].min(), peak[1].max()) + linreg[1])

    util_name = util_to_eia.dropna().set_index('company_id').loc[idno, 'utility_name']
    plt.title('%s, %s' % (util_name, idno))
    plt.ylabel('Load (W per capita)')
    plt.xlabel('Air Temperature ($^\circ$C)')
    textstr = '$\\alpha=%.2f$\n$\\beta=%.2f$\n$n=%s$\n$r=%.2f$' % (linreg[0], linreg[1], len(peak), linreg[2])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', linespacing=1.25, bbox=props)
    plt.savefig('%s.png' % (idno), bbox_inches='tight')
    plt.clf()


for fn in os.listdir('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc'):
    if fn.endswith('csv'):
        i = int(fn.split('.')[0])
        try:
            fit_data_no_linreg(i)
        except:
            print(i)








# idno = 803
# data = cat_load_census(idno)[['load', 'pop', 'lforce_001', 'mHHI_001']].dropna()
# data = data[data.index.year!=2005]
# datasummer = data[np.in1d(data.index.month, [6,7,8])]
# y = datasummer['load']
# X = datasummer[['pop', 'lforce_001', 'mHHI_001']]
# X = sm.add_constant(X)
# est = sm.OLS(y, X).fit()

# c_load = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
# resampled = pd.Series(est.predict(), index=data.index[np.in1d(data.index.month, [6,7,8])]).resample('h').interpolate()

# norm_load = (c_load - resampled).dropna()

# dem_ua = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_demand_to_met_ua')

# dem_aps = dem_ua.set_index('eia_code').sort_index().loc[803]

# aps_d = {}
# hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/color'

# for i in range(len(dem_aps.index)):
#     data_name = dem_aps.iloc[i]['grid_cell']
#     lat = float(data_name.split('_')[1])
#     lon = float(data_name.split('_')[2])
#     pop = int(dem_aps.iloc[i]['POP'])
#     df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
#     df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
#     df = df[np.in1d(df.index.month, [6,7,8])]
#     if not data_name in aps_d.keys():
#         aps_d.update({data_name : {}})
#         aps_d[data_name].update({'pop' : pop})
#         aps_d[data_name].update({'data' : df})
#     else:
#         aps_d[data_name]['pop'] += pop

# totpop = sum([aps_d[i]['pop'] for i in aps_d.keys()])
# tempcat = pd.concat([aps_d[i]['pop']*aps_d[i]['data'] for i in aps_d.keys()], axis=1)
# tmax = tempcat[4].sum(axis=1)/totpop
# tmin = tempcat[5].sum(axis=1)/totpop

# max_loads = norm_load.groupby(norm_load.index.date).max()
# max_loads.index = pd.to_datetime(max_loads.index)
# max_loads = max_loads.resample('h', loffset='12H')

# peak = pd.concat([max_loads, tmax.resample('h', loffset='12H')], axis=1).dropna()

# linfit = np.polyfit(peak[0], peak['load'], 1)

# tot_load = c_load.groupby(c_load.index.date).max()
# tot_load.index = pd.to_datetime(tot_load.index)

# load_anom = (peak['load'].resample('d')/tot_load['load']).dropna()

# linreg = scipy.stats.linregress(peak[0], load_anom)

# plot_curvefit(peak[0], load_anom)
# plot(np.arange(peak[0].min(), peak[0].max()), linreg[0]*np.arange(peak[0].min(), peak[0].max()) + linreg[1])


####
# INCONSISTENT FIELDS BETWEEN YEARS; 1990 lforce2 == 2000 lforce1, etc.
####
#OLD

def return_pop_load(idno):
    u = util_to_c.loc[idno]
    cT = pop_yrs.loc[u['GEOID'].values].sum()
    cT.index = cT.index.to_datetime()
    cT = cT.resample('A').interpolate()
    c_load = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    cat = pd.concat([cT, c_load.resample('A').interpolate()], axis=1).dropna().rename(columns={0:'pop'})
    return cat










#### OLD
c_yrs = pd.concat([c[i].set_index('Geo_FIPS').rename(columns={'SE_T001_001':i})[i] for i in c.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

util_to_eia = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/crosswalk/util_eia_id.csv', index_col=0)


j90 = pd.read_csv('home/akagi/util_join_1990.csv', index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')

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
