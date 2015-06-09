import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import os
import netCDF4
import datetime
import sys

sys.path.append('/home/akagi/github/RIPS_kircheis/RIPS')
import rect_grid
import cable

homedir = os.path.expanduser('~')
t = gpd.read_file('%s/Desktop/electricity_data/Transmission_Lines.shp' % homedir)


tmax1 = netCDF4.Dataset('%s/tmax_1.nc' % homedir)
tmax2 = netCDF4.Dataset('%s/tmax_2.nc' % homedir)
tmax5 = netCDF4.Dataset('%s/tmax_5.nc' % homedir)
tmax6 = netCDF4.Dataset('%s/tmax_6.nc' % homedir)

yrs = {
1: [2030,'la'],
2: [2010, 'la'],
3: [2050, 'phx'],
4: [2070, 'phx'],
5: [2010, 'phx'],
6: [2030, 'phx'],
7: [2050, 'la'],
8: [2070, 'la']
}

#### Initialize cable classes

cable_classes = {
    525 : {0 : ['Chukar', 'acsr'],
           1 : ['Bluebird', 'acsr']},
    345 : {0 : ['Tern', 'acsr']},
    230 : {0 : ['Bittern', 'acsr'],
           1 : ['Bluebird', 'acss'],
           2 : ['Tern', 'acsr']},
    115 : {0 : ['Bittern', 'acsr'],
           1 : ['Bluebird', 'acss'],
           2 : ['Tern', 'acsr']},
    69  : {0 : ['Tern', 'acss'],
           1 : ['Arbutus', 'aac'],
           2 : ['Linnet', 'acsr']}
    }

instance_cables = {
    525 : cable.cable(*cable_classes[525][0]),
    345 : cable.cable(*cable_classes[345][0]),
    230 : cable.cable(*cable_classes[230][0]),
    115 : cable.cable(*cable_classes[115][0]),
    69 :  cable.cable(*cable_classes[69][0])}

v_list = np.asarray(instance_cables.keys())

proj = pd.Series(tmax5.Projections.split(',')).str.strip()[:-1]
projsel = proj[proj.str.contains('csiro-mk3-6-0.5.rcp|mpi-esm-lr.2.rcp|gfdl-esm2g.1.rcp')]

#PHX

phx_bbox = np.array([
            tmax5.variables['longitude'][:].min() - 360, tmax5.variables['latitude'][:].min(),
            tmax5.variables['longitude'][:].max() - 360, tmax5.variables['latitude'][:].max()
            ])

phx_bbox[:2] -= 0.125/2
phx_bbox[2:] += 0.125/2

phx_grid = rect_grid.rect_grid(phx_bbox, 0.125)
phx_grid = gpd.GeoDataFrame(geometry=phx_grid, crs=t.crs)
phx_grid.crs = t.crs
phx_lines = t[t.intersects(phx_grid.unary_union)].reset_index()
phx_join = tools.sjoin(phx_lines, phx_grid)

phx_ix = np.column_stack(np.hstack(phx_grid.centroid.apply(lambda x: x.xy).values))

phx_shape = (tmax5.variables['latitude'][:].size, tmax5.variables['longitude'][:].size)

#### FOR HISTORICAL DATA

phx_d = {}

hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/color'

phx_d = {}
phx_d.update({'tmax_summer_mean' : {}})
phx_d.update({'tmax_summer_90th' : {}})
phx_d.update({'wind_summer_mean' : {}})
phx_d.update({'wind_summer_10th' : {}})

for i in phx_ix:
    lat = i[1]
    lon = i[0]
    data_name = 'data_%s_%s' % (lat, lon)
    df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)
    df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
    df = df[np.in1d(df.index.month, [6,7,8])]
    for j in phx_d.keys():
        if not lat in phx_d[j].keys():
            phx_d[j].update({lat : {}})
        phx_d[j][lat].update({lon : None})
    phx_d['tmax_summer_mean'][lat][lon] = df[4].mean()
    phx_d['tmax_summer_90th'][lat][lon] = df[4].quantile(0.9)
    phx_d['wind_summer_mean'][lat][lon] = df[6].mean()
    phx_d['wind_summer_10th'][lat][lon] = df[6].quantile(0.1)

for i in phx_d.keys():
    phx_d[i] = pd.DataFrame.from_dict(phx_d[i], orient='index').sort_index().sort_index(axis=1)


#### FOR FUTURE DATA

#PHX, 2010-2050

fut_phx = {}

for k, v in projsel.iteritems():
    cat = np.ma.filled(tmax6.variables['tasmax'][k,:,:,:], np.nan)
    p = pd.Panel(tmax6.variables['tasmax'][k,:,:,:], items=pd.date_range(datetime.date(2030,1,1), freq='d', periods=tmax6.variables['tasmax'].shape[1]), major_axis=tmax6.variables['latitude'][:], minor_axis=tmax6.variables['longitude'][:] - 360)
    ps = p[np.in1d(p.items.month, [6,7,8])]
    tmax_mean = ps.mean(axis=0)
    tmax_90 = ps.to_frame().quantile(0.9, axis=1).unstack()
    fut_phx.update({ k : {}})
    fut_phx[k]['tmax_summer_mean'] = tmax_mean.sort_index().sort_index(axis=1)
    fut_phx[k]['tmax_summer_90th'] = tmax_90.sort_index().sort_index(axis=1)


#### Get line temperatures

for i in phx_d.keys():
    phx_join['h_%s' % i] = phx_join['index_right'].apply(lambda x: phx_d[i].values.flat[x]) 

for i in fut_phx.keys():
    for j in fut_phx[i].keys():
        phx_join['f_%s_%s' % (i, j)] = phx_join['index_right'].apply(lambda x: fut_phx[i][j].values.flat[x])

phx_geom = phx_join.set_index('index').geometry.reset_index().drop_duplicates('index').set_index('index')

phx_join = phx_join.groupby('index').mean()        

phx_join['CABLE_VOLT'] = phx_join['VOLTAGE'].apply(lambda x: v_list[np.argmin(abs(x - v_list))])

phx_join['h_mean_amps'] = phx_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax_summer_mean'], 0.6096), axis=1)

phx_join['h_90th_amps'] = phx_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax_summer_90th'], 0.6096), axis=1)

for i in phx_join.columns[pd.Series(phx_join.columns).str.contains('^f_.*mean$')]:
    phx_join['f_mean_amps_%s' % i] = phx_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x[i], 0.6096), axis=1)

phx_pct_decrease = 100*phx_join.iloc[:, np.where(pd.Series(phx_join.columns).str.contains('f_mean_amps'))[0]].sub(phx_join['h_mean_amps'], 0).div(phx_join['h_mean_amps'], 0)

phx_pct_decrease.columns = 'pct_decrease_' + pd.Series(phx_pct_decrease.columns).str.extract('(\d+)')

phx_pct_decrease['pct_decrease_rcp26'] = phx_pct_decrease[['pct_decrease_39', 'pct_decrease_68', 'pct_decrease_113']].mean(axis=1)
phx_pct_decrease['pct_decrease_rcp45'] = phx_pct_decrease[['pct_decrease_49', 'pct_decrease_69', 'pct_decrease_116']].mean(axis=1)
phx_pct_decrease['pct_decrease_rcp85'] = phx_pct_decrease[['pct_decrease_59', 'pct_decrease_71', 'pct_decrease_119']].mean(axis=1)

phx_join = pd.concat([phx_join, phx_pct_decrease, phx_geom], axis=1)

phx_out = gpd.GeoDataFrame(phx_join[phx_join.columns[pd.Series(phx_join.columns).str.contains('pct_')]], geometry=phx_join.geometry.values)

phx_out.crs = t.crs

#### OUTPUT CABLE SHAPEFILE
phx_out.to_file('phx_cables.shp')

#### LOS ANGELES

# LA

la_bbox = np.array(
        (tmax1.variables['longitude'][:].min() - 360, tmax1.variables['latitude'][:].min(),
        tmax1.variables['longitude'][:].max() - 360, tmax1.variables['latitude'][:].max())
        )

la_bbox[:2] -= 0.125/2
la_bbox[2:] += 0.125/2

la_grid = rect_grid.rect_grid(la_bbox, 0.125)
la_grid = gpd.GeoDataFrame(geometry=la_grid, crs=t.crs)
la_grid.crs = t.crs
la_lines = t[t.intersects(la_grid.unary_union)].reset_index()
la_join = tools.sjoin(la_lines, la_grid)

la_ix = np.column_stack(np.hstack(la_grid.centroid.apply(lambda x: x.xy).values))

la_shape = (tmax1.variables['latitude'][:].size, tmax1.variables['longitude'][:].size)


#### FOR HISTORICAL DATA

la_d = {}

hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/cali'

la_d = {}
la_d.update({'tmax_summer_mean' : {}})
la_d.update({'tmax_summer_90th' : {}})
la_d.update({'wind_summer_mean' : {}})
la_d.update({'wind_summer_10th' : {}})

for i in la_ix:
    lat = i[1]
    lon = i[0]
    data_name = 'data_%s_%s' % (lat, lon)
    if data_name in os.listdir(hist_path):
        df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)
        df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
        df = df[np.in1d(df.index.month, [6,7,8])]
        for j in la_d.keys():
            if not lat in la_d[j].keys():
                la_d[j].update({lat : {}})
            la_d[j][lat].update({lon : None})
        la_d['tmax_summer_mean'][lat][lon] = df[4].mean()
        la_d['tmax_summer_90th'][lat][lon] = df[4].quantile(0.9)
        la_d['wind_summer_mean'][lat][lon] = df[6].mean()
        la_d['wind_summer_10th'][lat][lon] = df[6].quantile(0.1)
    else:
        for j in la_d.keys():
            if not lat in la_d[j].keys():
                la_d[j].update({lat : {}})
            la_d[j][lat].update({lon : None})
        la_d['tmax_summer_mean'][lat][lon] = np.nan
        la_d['tmax_summer_90th'][lat][lon] = np.nan
        la_d['wind_summer_mean'][lat][lon] = np.nan 
        la_d['wind_summer_10th'][lat][lon] = np.nan

for i in la_d.keys():
    la_d[i] = pd.DataFrame.from_dict(la_d[i], orient='index').sort_index().sort_index(axis=1)

#### FOR FUTURE DATA

fut_la = {}

for k, v in projsel.iteritems():
    cat = np.ma.filled(tmax1.variables['tasmax'][k,:,:,:], np.nan)
    p = pd.Panel(tmax1.variables['tasmax'][k,:,:,:], items=pd.date_range(datetime.date(2030,1,1), freq='d', periods=tmax1.variables['tasmax'].shape[1]), major_axis=tmax1.variables['latitude'][:], minor_axis=tmax1.variables['longitude'][:] - 360)
    ps = p[np.in1d(p.items.month, [6,7,8])]
    tmax_mean = ps.mean(axis=0)
    tmax_90 = ps.to_frame().quantile(0.9, axis=1).unstack()
    fut_la.update({ k : {}})
    fut_la[k]['tmax_summer_mean'] = tmax_mean.sort_index().sort_index(axis=1)
    fut_la[k]['tmax_summer_90th'] = tmax_90.sort_index().sort_index(axis=1)


#### Get line temperatures

for i in la_d.keys():
    la_join['h_%s' % i] = la_join['index_right'].apply(lambda x: la_d[i].values.flat[x]) 

for i in fut_la.keys():
    for j in fut_la[i].keys():
        la_join['f_%s_%s' % (i, j)] = la_join['index_right'].apply(lambda x: fut_la[i][j].values.flat[x])

la_geom = la_join.set_index('index').geometry.reset_index().drop_duplicates('index').set_index('index')

la_join = la_join.groupby('index').mean()        

la_join['CABLE_VOLT'] = la_join['VOLTAGE'].apply(lambda x: v_list[np.argmin(abs(x - v_list))])

la_join['h_mean_amps'] = la_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax_summer_mean'], 0.6096), axis=1)

la_join['h_90th_amps'] = la_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax_summer_90th'], 0.6096), axis=1)

for i in la_join.columns[pd.Series(la_join.columns).str.contains('^f_.*mean$')]:
    la_join['f_mean_amps_%s' % i] = la_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x[i], 0.6096), axis=1)


la_pct_decrease = 100*la_join.iloc[:, np.where(pd.Series(la_join.columns).str.contains('f_mean_amps'))[0]].sub(la_join['h_mean_amps'], 0).div(la_join['h_mean_amps'], 0)

la_pct_decrease.columns = 'pct_decrease_' + pd.Series(la_pct_decrease.columns).str.extract('(\d+)')

la_pct_decrease['pct_decrease_rcp26'] = la_pct_decrease[['pct_decrease_39', 'pct_decrease_68', 'pct_decrease_113']].mean(axis=1)
la_pct_decrease['pct_decrease_rcp45'] = la_pct_decrease[['pct_decrease_49', 'pct_decrease_69', 'pct_decrease_116']].mean(axis=1)
la_pct_decrease['pct_decrease_rcp85'] = la_pct_decrease[['pct_decrease_59', 'pct_decrease_71', 'pct_decrease_119']].mean(axis=1)

la_join = pd.concat([la_join, la_pct_decrease, la_geom], axis=1)

la_out = gpd.GeoDataFrame(la_join[la_join.columns[pd.Series(la_join.columns).str.contains('pct_')]], geometry=la_join.geometry.values)

la_out.crs = t.crs

la_out.fillna(0, inplace=True)

la_out.to_file('la_cables.shp')

######################################################


#### COMBINE WITH CENSUS TRACTS

census = gpd.read_file('/home/akagi/github/RIPS_kircheis/data/shp/census/census_tracts_all/census_tracts_2014.shp')

census_az = census[census['STATEFP'].astype(int) == 4]
census_line_join_phx = tools.sjoin(census_az.reset_index(), phx_out.to_crs(census_az.crs).reset_index())
census_line_join_phx.to_file('census_line_phx.shp')


census_ca = census[census['STATEFP'].astype(int) == 6]
census_line_join_la = tools.sjoin(census_ca.reset_index(), la_out.to_crs(census_ca.crs).reset_index())
census_line_join_la[['geometry', 'pct_decrease_rcp26', 'pct_decrease_rcp45', 'pct_decrease_rcp85']].to_file('census_line_la.shp')
