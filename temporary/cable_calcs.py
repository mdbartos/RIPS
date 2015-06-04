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

# LA
tmax1 = netCDF4.Dataset('%s/tmax_1.nc' % homedir)
tmax2 = netCDF4.Dataset('%s/tmax_2.nc' % homedir)

#PHX
tmax5 = netCDF4.Dataset('%s/tmax_5.nc' % homedir)
tmax6 = netCDF4.Dataset('%s/tmax_6.nc' % homedir)

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
#pd.Series(phx_grid.index).apply(lambda x: np.unravel_index(x, phx_shape))
#phx_join['index_right'].apply(lambda x: np.unravel_index(x, phx_shape))


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


proj = pd.Series(tmax1.Projections.split(',')).str.strip()[:-1]
projsel = proj[proj.str.contains('csiro-mk3-6-0.5.rcp|mpi-esm-lr.2.rcp|gfdl-esm2g.1.rcp')]

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


phx_join = phx_join.groupby('index').mean()        

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

phx_join['CABLE_VOLT'] = phx_join['VOLTAGE'].apply(lambda x: v_list[np.argmin(abs(x - v_list))])

phx_join['h_mean_amps'] = phx_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax_summer_mean'], 0.6096), axis=1)

phx_join['h_90th_amps'] = phx_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax_summer_90th'], 0.6096), axis=1)

for i in phx_join.columns[pd.Series(phx_join.columns).str.contains('^f_.*mean$')]:
    phx_join['f_mean_amps_%s' % i] = phx_join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x[i], 0.6096), axis=1)

pct_decrease = 100*phx_join.iloc[:, np.where(pd.Series(phx_join.columns).str.contains('f_mean_amps'))[0]].sub(phx_join['h_mean_amps'], 0).div(phx_join['h_mean_amps'], 0)


#### LOS ANGELES


la_bbox = (tmax1.variables['longitude'][:].min() - 360, tmax1.variables['latitude'][:].min(),
            tmax1.variables['longitude'][:].max() - 360, tmax1.variables['latitude'][:].max())
