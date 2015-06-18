import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import os
import netCDF4
import datetime
import sys
import psutil

sys.path.append('/home/akagi/github/RIPS_kircheis/RIPS')
import rect_grid
import cable

homedir = os.path.expanduser('~')
t = gpd.read_file('%s/Desktop/electricity_data/Transmission_Lines.shp' % homedir)

nc = {}

for fn in os.listdir('%s/CMIP5/rcp45' % homedir):
    nc.update({ int(fn.split('_')[-1].split('-')[0][:4]) : netCDF4.Dataset('%s/CMIP5/rcp45/%s' % (homedir, fn))})

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

#### Grid and Lines

bbox = np.array([
            nc[2010].variables['longitude'][:].min() - 360, nc[2010].variables['latitude'][:].min(),
            nc[2010].variables['longitude'][:].max() - 360, nc[2010].variables['latitude'][:].max()
            ])

bbox[:2] -= 0.125/2
bbox[2:] += 0.125/2

grid = rect_grid.rect_grid(bbox, 0.125)
grid = gpd.GeoDataFrame(geometry=grid)
grid.crs = t.crs

lines = t[t.intersects(grid.unary_union)].reset_index()
join = tools.sjoin(lines, grid)

grid_ix = np.column_stack(np.hstack(grid.centroid.apply(lambda x: x.xy).values))

#grid_ix = pd.DataFrame(grid_ix)
#datanames = 'data_' + grid_ix[1].astype(str) + '_' + grid_ix[0].astype(str)
#join['dataname'] = pd.Series(join['index_right'].values, index=join['index_right'].values).map(datanames).values

grid_shape = (nc[2010].variables['latitude'][:].size, nc[2010].variables['longitude'][:].size)


#### Data Size

datasize = nc[2010].variables['tasmax'].size * nc[2010].variables['tasmax'][0,0,0].nbytes
memsize = psutil.virtual_memory()[1]

#### For historical data

hist = {}

hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

hist = {}
hist.update({'tmax_summer_mean' : {}})
hist.update({'wind_summer_mean' : {}})

for i in grid_ix:
    lat = i[1]
    lon = i[0]
    for j in hist.keys():
        if not lat in hist[j].keys():
            hist[j].update({lat : {}})
        hist[j][lat].update({lon : None})
    data_name = 'data_%s_%s' % (lat, lon)
    if data_name in os.listdir(hist_path):
        df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)
        df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
        df = df[np.in1d(df.index.month, [6,7,8])]
        hist['tmax_summer_mean'][lat][lon] = df[4].mean()
        hist['wind_summer_mean'][lat][lon] = df[6].mean()
    else:
        hist['tmax_summer_mean'][lat][lon] = np.nan
        hist['wind_summer_mean'][lat][lon] = np.nan


for i in hist.keys():
    hist[i] = pd.DataFrame.from_dict(hist[i], orient='index').sort_index().sort_index(axis=1)

#### For future data

fut = {}

for k in nc:
    cat = np.ma.filled(nc[k].variables['tasmax'][:,:,:], np.iinfo(np.int32).min)
    cat = pd.Panel(cat, items=pd.date_range(datetime.date(k,1,1), freq='d', periods=nc[k].variables['tasmax'].shape[0]), major_axis=nc[k].variables['latitude'][:], minor_axis=nc[k].variables['longitude'][:] - 360)
    cat = cat[np.in1d(cat.items.month, [6,7,8])]
    tmax_mean = cat.mean(axis=0)
    fut[k] = tmax_mean.sort_index().sort_index(axis=1)

#### Import csvs

join = pd.read_csv('line_to_gridcell.csv')
join['VOLTAGE'] = join['UNIQUE_ID'].map(t.set_index('UNIQUE_ID')['VOLTAGE'])

hist_tmax = pd.read_csv('hist_tmax_summer_mean.csv', index_col=0)

fut_d = {}

for fn in os.listdir('.'):
    if 'fut_tmax' in fn:
        df = pd.read_csv(fn, index_col=0).replace(-2147483648, np.nan)
        df.columns = df.columns.values.astype(float)
	df.index = df.index.values.astype(float)
	df = df.sort_index().sort_index(axis=1)
        fut_d.update({ int(fn.split('.')[0].split('_')[-1]) : df})


join['h_tmax'] = join['index_right'].apply(lambda x: hist_tmax.values.flat[x]) 

for i in fut_d.keys():
    join['f_%s' % (i)] = join['index_right'].apply(lambda x: fut_d[i].values.flat[x])


join['CABLE_VOLT'] = join['VOLTAGE'].apply(lambda x: v_list[np.argmin(abs(x - v_list))])

join['h_mean_amps'] = join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax'], 0.6096), axis=1)

for i in join.columns[pd.Series(join.columns).str.contains('^f_')]:
    join['f_mean_amps_%s' % i] = join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x[i], 0.6096), axis=1)


pct_decrease = 100*join.iloc[:, np.where(pd.Series(join.columns).str.contains('f_mean_amps'))[0]].sub(join['h_mean_amps'], 0).div(join['h_mean_amps'], 0)

pct_decrease.columns = 'pct_decrease_' + pd.Series(pct_decrease.columns).str.extract('(\d+)')

join_geom = t.set_index('UNIQUE_ID')['geometry'][join['UNIQUE_ID'].values].reset_index()['geometry']

join = pd.concat([join, pct_decrease, join_geom], axis=1)

join_out = gpd.GeoDataFrame(join[join.columns[pd.Series(join.columns).str.contains('pct_')]], geometry=join.geometry.values).dropna()

join_out.crs = t.crs

#### Output file

join_out.to_file('trans_impacts.shp')

#### Histogram

for i in np.arange(2020,2090,20):
    hist(join_out['pct_decrease_%s' % i].values, bins=250, alpha=0.8, linewidth=0, label=str(i))

legend()
title('Bidecadal percent reduction in Transmission Line Capacity,\nMPI-ESM-MR, RCP4.5')
xlabel('Rated Ampacity Reduction (%)')
ylabel('Count')
