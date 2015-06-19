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

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = gpd.read_file('/home/akagi/github/RIPS_kircheis/data/shp/Electric_Retail_Service_Ter.shp')

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

#### QUICK FIXES

rid = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/eia_form_714/active/form714-database/form714-database/Respondent IDs.csv')

util_to_eia.loc[2149, 'company_id'] = 2507     #Burbank
util_to_eia.loc[2046, 'company_id'] = 16868    #Seattle City Lights
util_to_eia.loc[2157, 'company_id'] = 17609    #Southern California Edison
util_to_eia.loc[229, 'company_id'] = 5326      #PUD of Douglas County
util_to_eia.loc[520, 'company_id'] = 3989      #Colorado Springs Utilities
util_to_eia.loc[3296, 'company_id'] = 18429    #Tacoma
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

def curve_type(x, a, b, c):
    return abs(a*x**2) + b*x + c

def fit_data_no_linreg(idno, plot_output=True):
    data = cat_load_census(idno)[['load', 'pop', 'lforce_001', 'mHHI_001']].dropna()
    data = data[data.index.year!=2005]
    datasummer = data[np.in1d(data.index.month, [6,7,8])]

    c_load = pd.read_csv('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (idno), index_col=0, parse_dates=True)
    c_load = c_load.groupby(c_load.index.date).max()

    norm_load = (1000000*c_load['load']/(data['pop'].reindex_like(c_load).interpolate())).dropna()
    norm_load.index = pd.to_datetime(norm_load.index)
    norm_load = norm_load[np.in1d(norm_load.index.month, [6,7,8])]

    dem_ua = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_demand_to_met_ua')

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

for fn in os.listdir('/home/akagi/github/RIPS_kircheis/RIPS/data/hourly_load/wecc'):
    if fn.endswith('csv'):
        i = int(fn.split('.')[0])
        try:
            reg_d.update({i : fit_data_no_linreg(i)})
        except:
            print(i)


#### Future projections


nc = {}

for fn in os.listdir('%s/CMIP5/rcp45' % homedir):
    nc.update({ int(fn.split('_')[-1].split('-')[0][:4]) : netCDF4.Dataset('%s/CMIP5/rcp45/%s' % (homedir, fn))})


def project_reg(idno, yr):

    latpos = pd.Series(np.arange(len(nc[yr].variables['latitude'][:])), index=nc[yr].variables['latitude'][:])
    lonpos = pd.Series(np.arange(len(nc[yr].variables['longitude'][:])), index=nc[yr].variables['longitude'][:] - 360)

    dem_ua = pd.read_csv('/home/akagi/github/RIPS_kircheis/data/util_demand_to_met_ua')

    dem_util = dem_ua.set_index('eia_code').sort_index().loc[idno]

    util_d = {}

    if isinstance(dem_util, pd.DataFrame):
        tasproj = np.zeros(nc[yr].variables['tasmax'].shape[0])
        for i in range(len(dem_util.index)):
            data_name = dem_util.iloc[i]['grid_cell']
            lat = float(data_name.split('_')[1])
            lon = float(data_name.split('_')[2])
	    pop = dem_util.iloc[i]['POP']
	    if (lat in latpos.index.values) and (lon in lonpos.index.values):
                latint = latpos[lat]
                lonint = lonpos[lon]
            else:
                lat = latpos.index.values[np.argmin(lat - latpos.index.values)]
                lon = lonpos.index.values[np.argmin(lon - lonpos.index.values)]
                latint = latpos[lat]
                lonint = lonpos[lon]

            tasproj += pop*(nc[yr].variables['tasmax'][:, latint, lonint])

        tasproj = tasproj/dem_util['POP'].astype(float).sum()    
        tasproj = pd.Series(tasproj, index=pd.date_range(start=datetime.date(yr, 1, 1), freq='d', periods=len(tasproj)))
        tasproj = tasproj[np.in1d(tasproj.index.month, [6,7,8])]
        tasproj = tasproj[tasproj.index.weekday <= 4]
        return tasproj

    elif isinstance(dem_util, pd.Series):
        tasproj = np.zeros(nc[yr].variables['tasmax'].shape[0])
        data_name = dem_util['grid_cell']
        lat = float(data_name.split('_')[1])
        lon = float(data_name.split('_')[2])
        if (lat in latpos.index.values) and (lon in lonpos.index.values):
            latint = latpos[lat]
            lonint = lonpos[lon]
        else:
            lat = latpos.index.values[np.argmin(lat - latpos.index.values)]
            lon = lonpos.index.values[np.argmin(lon - lonpos.index.values)]
            latint = latpos[lat]
            lonint = lonpos[lon]
        tasproj = nc[yr].variables['tasmax'][:, latint, lonint])

        tasproj = pd.Series(tasproj, index=pd.date_range(start=datetime.date(yr, 1, 1), freq='d', periods=len(tasproj)))
        tasproj = tasproj[np.in1d(tasproj.index.month, [6,7,8])]
        tasproj = tasproj[tasproj.index.weekday <= 4]
        return tasproj

	# return curve_type(tasproj.values, *reg_d[idno][0]), tasproj

            # if data_name in os.listdir(hist_path):
            #     df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            # else:
            #     lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
            #     lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
            #     latlons = pd.DataFrame(np.column_stack([lats, lons]))
            #     newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
            #     data_name = 'data_%s_%s' % (newdata[0], newdata[1])
            #     df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            # df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
            # df = df[np.in1d(df.index.month, [6,7,8])]
            # if not data_name in util_d.keys():
            #     util_d.update({data_name : {}})
            #     util_d[data_name].update({'pop' : pop})
            #     util_d[data_name].update({'data' : df})
            # else:
            #     util_d[data_name]['pop'] += pop
    # elif isinstance(dem_util, pd.Series):
        # data_name = dem_util['grid_cell']
        # lat = float(data_name.split('_')[1])
        # lon = float(data_name.split('_')[2])
        # pop = int(dem_util['POP'])
        # if data_name in os.listdir(hist_path):
            # df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        # else:
            # lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
            # lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
            # latlons = pd.DataFrame(np.column_stack([lats, lons]))
            # newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
            # data_name = 'data_%s_%s' % (newdata[0], newdata[1])
            # df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        # df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
        # df = df[np.in1d(df.index.month, [6,7,8])]
        # if not data_name in util_d.keys():
            # util_d.update({data_name : {}})
            # util_d[data_name].update({'pop' : pop})
            # util_d[data_name].update({'data' : df})
        # else:
            # util_d[data_name]['pop'] += pop

proj_d = {}

for k in nc.keys():
	proj_d.update({ k : project_reg(803, k)})
