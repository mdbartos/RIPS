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

grid_shape = (nc[2010].variables['latitude'][:].size, nc[2010].variables['longitude'][:].size)


#### Data Size

datasize = nc[2010].variables['tasmax'].size * nc[2010].variables['tasmax'][0,0,0].nbytes
memsize = psutil.virtual_memory()[1]

#### For historical data

hist = {}

hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/color'

hist = {}
hist.update({'tmax_summer_mean' : {}})
hist.update({'wind_summer_mean' : {}})

for i in phx_ix:
    lat = i[1]
    lon = i[0]
    data_name = 'data_%s_%s' % (lat, lon)
    df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)
    df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
    df = df[np.in1d(df.index.month, [6,7,8])]
    for j in hist.keys():
        if not lat in hist[j].keys():
            hist[j].update({lat : {}})
        hist[j][lat].update({lon : None})
    hist['tmax_summer_mean'][lat][lon] = df[4].mean()
    hist['wind_summer_mean'][lat][lon] = df[6].mean()

for i in hist.keys():
    hist[i] = pd.DataFrame.from_dict(hist[i], orient='index').sort_index().sort_index(axis=1)

#### For future data

fut = {}

for k in nc:
    cat = np.ma.filled(nc[k].variables['tasmax'][:,:,:], np.iinfo(np.int32).min)
    cat = pd.Panel(cat, items=pd.date_range(datetime.date(k,1,1), freq='d', periods=nc[k].variables['tasmax'].shape[0]), major_axis=nc[k].variables['latitude'][:], minor_axis=nc[k].variables['longitude'][:] - 360)
    cat = cat[np.in1d(cat.items.month, [6,7,8])]
    tmax_mean = cat.mean(axis=0)
    fut.update({ k : {}})
    fut[k]['tmax_summer_mean'] = tmax_mean.sort_index().sort_index(axis=1)
