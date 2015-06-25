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
from scipy.optimize import curve_fit

homedir = os.path.expanduser('~')

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = gpd.read_file('%s/github/RIPS_kircheis/data/shp/Electric_Retail_Service_Ter.shp' % homedir)

census_shp = '%s/github/RIPS_kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp' % homedir

census_path = '%s/github/RIPS_kircheis/data/census/' % homedir

acs_path = '%s/github/RIPS_kircheis/data/census/ACS_5y/' % homedir

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

util_to_eia = pd.read_csv('%s/github/RIPS_kircheis/RIPS/crosswalk/util_eia_id.csv' % homedir, index_col=0)

#### QUICK FIXES

rid = pd.read_csv('%s/github/RIPS_kircheis/data/eia_form_714/active/form714-database/form714-database/Respondent IDs.csv' % homedir)

util_to_eia.loc[2149, 'company_id'] = 2507     #Burbank
util_to_eia.loc[2046, 'company_id'] = 16868    #Seattle City Lights
util_to_eia.loc[2157, 'company_id'] = 17609    #Southern California Edison
util_to_eia.loc[229, 'company_id'] = 5326      #PUD of Douglas County
util_to_eia.loc[520, 'company_id'] = 3989      #Colorado Springs Utilities
util_to_eia.loc[2296, 'company_id'] = 18429    #Tacoma
util_to_eia.loc[2566, 'company_id'] = 7294     #Glendale
util_to_eia.loc[2155, 'company_id'] = 16088    #Riverside
util_to_eia.loc[2298, 'company_id'] = 15500    #Puget Sound

# util_to_eia.loc[589, 'company_id'] =           #Farmington | FARM
# util_to_eia.loc[533, 'company_id'] =           #Los Alamos | LOS
# util_to_eia.loc[627, 'company_id'] =           #Navajo Tribal | NTUA
# util_to_eia.loc[1008, 'company_id'] = 16534    #Redding | RDNG
# util_to_eia.loc[2148, 'company_id'] =          #Vernon | VER

# util_to_eia.loc[ , 'company_id'] = 229         #CAISO | CISO
# util_to_eia.loc[ , 'company_id'] = 12397       #MWD of SC | MWD

####

j90 = pd.read_csv('%s/github/RIPS_kircheis/data/util_join_1990.csv' % homedir, index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')

j00 = pd.read_csv('%s/github/RIPS_kircheis/data/util_join_2000.csv' % homedir, index_col=0).set_index('UNIQUE_ID')['GEOID_2000'].astype(str).str.pad(11, side='left', fillchar='0')

j14 = pd.read_csv('%s/github/RIPS_kircheis/data/util_join_2014.csv' % homedir, index_col=0).set_index('UNIQUE_ID')['GEOID_2014'].astype(str).str.pad(11, side='left', fillchar='0')

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

    c_load = pd.read_csv('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (homedir, idno), index_col=0, parse_dates=True)
    c_load = c_load.resample('M').interpolate()

    cat = pd.concat([cT, c_load, demdata], axis=1)
    return cat

def plot_curvefit(xdata, ydata):
    xy = np.vstack([xdata,ydata])
    z = scipy.stats.gaussian_kde(xy)(xy)
    plt.scatter(xdata, ydata, c=z, s=100, edgecolor='')

def curve_type(x, a, b, c):
    return abs(a*x**2) + b*x + c

def fit_data_no_linreg(idno, plot_output=False):
    data = cat_load_census(idno)[['load', 'pop', 'lforce_001', 'mHHI_001']].dropna()
    data = data[data.index.year!=2005]
    datasummer = data[np.in1d(data.index.month, [6,7,8])]

    c_load = pd.read_csv('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (homedir, idno), index_col=0, parse_dates=True)
    c_load = c_load.groupby(c_load.index.date).max()

    norm_load = (1000000*c_load['load']/(data['pop'].reindex_like(c_load).interpolate())).dropna()
    norm_load.index = pd.to_datetime(norm_load.index)
    norm_load = norm_load[np.in1d(norm_load.index.month, [6,7,8])]

    dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

    dem_util = dem_ua.set_index('eia_code').sort_index().loc[idno]

    util_d = {}
    hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

    if isinstance(dem_util, pd.DataFrame):
        for i in range(len(dem_util.index)):
            data_name = dem_util.iloc[i]['grid_cell']
            lat = float(data_name.split('_')[1])
            lon = float(data_name.split('_')[2])
            pop = int(dem_util.iloc[i]['POP'])
            if data_name in os.listdir(hist_path):
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            else:
                lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
                lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
                latlons = pd.DataFrame(np.column_stack([lats, lons]))
                newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
                data_name = 'data_%s_%s' % (newdata[0], newdata[1])
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
            df = df[np.in1d(df.index.month, [6,7,8])]
            if not data_name in util_d.keys():
                util_d.update({data_name : {}})
                util_d[data_name].update({'pop' : pop})
                util_d[data_name].update({'data' : df})
            else:
                util_d[data_name]['pop'] += pop
    elif isinstance(dem_util, pd.Series):
        data_name = dem_util['grid_cell']
        lat = float(data_name.split('_')[1])
        lon = float(data_name.split('_')[2])
        pop = int(dem_util['POP'])
        if data_name in os.listdir(hist_path):
            df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        else:
            lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
            lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
            latlons = pd.DataFrame(np.column_stack([lats, lons]))
            newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
            data_name = 'data_%s_%s' % (newdata[0], newdata[1])
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
    if isinstance(tempcat[4], pd.DataFrame):
        tmax = tempcat[4].sum(axis=1)/totpop
        tmin = tempcat[5].sum(axis=1)/totpop
    elif isinstance(tempcat[4], pd.Series):
        tmax = tempcat[4]/totpop
        tmin = tempcat[5]/totpop

    peak = pd.concat([norm_load, tmax], axis=1).dropna()
    peak = peak[peak.index.weekday <= 4]    #BUSINESS DAYS ONLY
    if idno in man_fixes:
        peak = peak.loc[man_fixes[idno][0]:man_fixes[idno][1]]

    # linreg = scipy.stats.linregress(peak[1], peak[0])
    # coeffs = np.polyfit(peak[1].values, peak[0].values, 2)

    x = peak[1].values
    y = peak[0].values

    coeffs = curve_fit(curve_type, x, y)[0]

    # p = np.poly1d(coeffs)
    p = curve_type
    s = p(x, *coeffs)
    R_2 = 1 - sum((s-y)**2)/sum((y-np.mean(y))**2)

    if plot_output:
        # linreg = scipy.stats.linregress(peak[1], peak[0])
        
        fig, ax = plt.subplots(1)
        plot_curvefit(peak[1], peak[0])
        x_mm = np.linspace(x.min(), x.max())
        plt.plot(x_mm, p(x_mm, *coeffs))
    
        util_name = util_to_eia.dropna().set_index('company_id').loc[idno, 'utility_name']
        plt.title('%s, %s' % (util_name, idno))
        plt.ylabel('Load (W per capita)')
        plt.xlabel('Air Temperature ($^\circ$C)')
        textstr = '$\\alpha=%.2f$\n$\\beta=%.2f$\n$\\gamma=%.2f$\n$n=%s$\n$r2=%.2f$' % (coeffs[0], coeffs[1], coeffs[2],  len(peak), R_2)
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', linespacing=1.25, bbox=props)
        plt.savefig('%s.png' % (idno), bbox_inches='tight')
        plt.clf()
    
    return coeffs, R_2


man_fixes = {
        3413 : ('1993', '2000'),
        5326 : ('2000', None),
        5701 : ('1993', '2004'),
        14328 : ('1997', None),
        14354 : ('1999', '2004'),
        15466 : ('1993', '2001'),
        15473 : ('1993', '2004'),
        17166 : ('1998', None),
        19281 : ('1993', '2004'),
        19545 : ('1997', '2004'),
        20169 : ('2006', '2010'),
        24211 : ('1993', '2004')}


reg_d = {}

for fn in os.listdir('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc' % homedir):
    if fn.endswith('csv'):
        i = int(fn.split('.')[0])
        try:
            reg_d.update({i : fit_data_no_linreg(i)})
        except:
            print(i)


#### Future projections

import netCDF4


def project_reg_vect(yr, idno):

    nc = call_reg.nc
    dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

    latpos = pd.Series(np.arange(len(nc[yr].variables['latitude'][:])), index=nc[yr].variables['latitude'][:])
    lonpos = pd.Series(np.arange(len(nc[yr].variables['longitude'][:])), index=nc[yr].variables['longitude'][:] - 360)
    latlon = pd.Series(dem_ua['grid_cell'].dropna().unique()).str.split('_').str[1:].apply(pd.Series).astype(float)
    latlonix = pd.concat([latpos[latlon[0].values].reset_index(), lonpos[latlon[1].values].reset_index()], axis=1).dropna()
    latlonix.columns = ['lat', 'latix', 'lon', 'lonix']
    latlonix['latix'] = latlonix['latix'].astype(int)
    latlonix['lonix'] = latlonix['lonix'].astype(int)
    latlonix['lat'] = latlonix['lat'].astype(str)
    latlonix['lon'] = latlonix['lon'].astype(str)

    cat = np.ma.filled(nc[yr].variables['tasmax'][:,:,:], np.iinfo(np.int32).min)[:, latlonix['latix'].values, latlonix['lonix'].values]
    cat[cat == cat.min()] = np.nan

    outdf = pd.DataFrame()

    for code_n in idno:
        dem_util = dem_ua.set_index('eia_code').sort_index().loc[code_n]
        data_name = pd.Series(dem_util['grid_cell'])
        util_ll = data_name.str.split('_').str[1:].apply(pd.Series)
        util_ll.columns = ['lat', 'lon']
        util_ll = pd.merge(util_ll, latlonix.reset_index(), on=['lat', 'lon'])
        pop = dem_util['POP'] 
        if dem_util.ndim > 1:
            nantest = np.isnan(cat[:, util_ll['index'].values][0])
            if nantest.any():
                nanpos = np.where(nantest)[0]
                pop.iloc[nanpos] = np.nan
            projtemp = np.nansum((cat[:, util_ll['index'].values] * pop.values), axis=1)/pop.sum()
        else:
            projtemp = cat[:, util_ll['index'].values].ravel()
        outdf[code_n] = projtemp

    outdf.index = pd.date_range(start=datetime.date(yr, 1, 1), freq='d', periods=len(outdf))
    return outdf


idno = [int(i.split('.')[0]) for i in os.listdir('%s/Dropbox/NSF WSC AZ WEN Team Share/Electricity Demand/plots' % homedir)]


def call_reg(model, scen, directory):
    call_reg.nc = {}
    curdir = '%s/%s/%s' % (directory, model, scen)
    for fn in os.listdir(curdir):
        call_reg.nc.update({ int(fn.split('_')[-1].split('-')[0][:4]) : netCDF4.Dataset('%s/%s' % (curdir, fn))})
    for y in call_reg.nc.keys():
        project_reg_vect(y, idno).to_csv('%s-%s-%s' % (model, scen, y))
        call_reg.nc[y].close()

default_dir = '%s/CMIP5' % homedir

for subdir in os.listdir(default_dir):
    scendir = '%s/%s' % (default_dir, subdir)
    for sc in ['rcp26', 'rcp45', 'rcp85']:
        if sc in os.listdir(scendir):
            call_reg(subdir, sc, default_dir)


historical_dir = '%s/temp_regression/historical/hist_util_temps' % (homedir)
projection_dir = '%s/temp_regression/projection' % (homedir)

def combine_scenario(model, scenario, histpath, projdir):
    proj_li = []
    hist_df = pd.read_csv(histpath, index_col=0)
    for i in os.listdir(projdir):
        if ('%s-%s' % (model, scenario)) in i:
            proj_li.append(pd.read_csv('%s/%s' % (projdir, i), index_col=0))
    out_df = pd.concat(proj_li)
    out_df = pd.concat([hist_df, out_df]).sort_index()
    out_df.index = pd.to_datetime(out_df.index)
    out_df.columns = np.asarray(out_df.columns).astype(int)
    return out_df

def util_hist_temp(idno):

    out_df = pd.DataFrame()

    dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

    for code_n in idno:
        dem_util = dem_ua.set_index('eia_code').sort_index().loc[code_n]

        util_d = {}
        hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

        if isinstance(dem_util, pd.DataFrame):
            for i in range(len(dem_util.index)):
                data_name = dem_util.iloc[i]['grid_cell']
                lat = float(data_name.split('_')[1])
                lon = float(data_name.split('_')[2])
                pop = int(dem_util.iloc[i]['POP'])
                if data_name in os.listdir(hist_path):
                    df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
                else:
                    lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
                    lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
                    latlons = pd.DataFrame(np.column_stack([lats, lons]))
                    newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
                    data_name = 'data_%s_%s' % (newdata[0], newdata[1])
                    df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
                df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
                if not data_name in util_d.keys():
                    util_d.update({data_name : {}})
                    util_d[data_name].update({'pop' : pop})
                    util_d[data_name].update({'data' : df})
                else:
                    util_d[data_name]['pop'] += pop
        elif isinstance(dem_util, pd.Series):
            data_name = dem_util['grid_cell']
            lat = float(data_name.split('_')[1])
            lon = float(data_name.split('_')[2])
            pop = int(dem_util['POP'])
            if data_name in os.listdir(hist_path):
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            else:
                lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
                lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
                latlons = pd.DataFrame(np.column_stack([lats, lons]))
                newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
                data_name = 'data_%s_%s' % (newdata[0], newdata[1])
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
            if not data_name in util_d.keys():
                util_d.update({data_name : {}})
                util_d[data_name].update({'pop' : pop})
                util_d[data_name].update({'data' : df})
            else:
                util_d[data_name]['pop'] += pop

        totpop = sum([util_d[i]['pop'] for i in util_d.keys()])
        tempcat = pd.concat([util_d[i]['pop']*util_d[i]['data'] for i in util_d.keys()], axis=1)
        if isinstance(tempcat[4], pd.DataFrame):
            tmax = tempcat[4].sum(axis=1)/totpop
        elif isinstance(tempcat[4], pd.Series):
            tmax = tempcat[4]/totpop
        out_df[code_n] = tmax
    return out_df.sort_index()

def apply_demand_reg(idno, temp_df):
    p = reg_d[idno][0]
    x = temp_df[idno][np.in1d(temp_df.index.month, [6,7,8])]
    y = pd.Series(np.polyval(p, x.values), index=x.index)
    y.name = idno
    return y

#Create output files of regression in directory ./regress

dirlist = pd.Series([k.split('rcp') for k in os.listdir(projection_dir)]).apply(pd.Series)
dirlist[0] = dirlist[0].str[:-1]
dirlist[1] = 'rcp' + dirlist[1].str.split('-').str[0]

for i in dirlist.index.values:
    model = dirlist.loc[i, 0]
    proj = dirlist.loc[i, 1]
    temp_df = combine_scenario(model, proj, historical_dir, projection_dir)
    reg_results = pd.DataFrame()
    for j in reg_d.keys():
        result = apply_demand_reg(j, temp_df)
        reg_results[j] = result
    reg_results.to_csv('demand_%s_%s' % (model, proj))


# Combine output files in a pandas panel
