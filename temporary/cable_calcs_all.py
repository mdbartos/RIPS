import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import os
import netCDF4
import datetime
import sys
import psutil

homedir = os.path.expanduser('~')
sys.path.append('%s/github/RIPS/tools' % homedir)
sys.path.append('%s/github/RIPS/transmission' % homedir)

import rect_grid
import cable

t = gpd.read_file('%s/Desktop/electricity_data/Transmission_Lines.shp' % homedir)

#### Initialize cable classes

cable_classes = {
    525 : {0 : ['Cardinal', 'acsr'],
           1 : ['Bluebird', 'acsr']},
    345 : {0 : ['Cardinal', 'acsr']},
    230 : {0 : ['Martin', 'acsr'],
           1 : ['Bluebird', 'acss'],
           2 : ['Tern', 'acsr']},
    115 : {0 : ['Condor', 'acsr'],
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

template_nc =  netCDF4.Dataset('%s/CMIP5/mpi-esm-lr/rcp45/BCCA_0.125deg_tasmax_day_MPI-ESM-LR_rcp45_r2i1p1_20100101-20191231.nc' % homedir)

bbox = np.array([
            template_nc.variables['longitude'][:].min() - 360, template_nc.variables['latitude'][:].min(),
            template_nc.variables['longitude'][:].max() - 360, template_nc.variables['latitude'][:].max()
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
datanames = 'data_' + pd.Series(grid_ix[:, 1].astype(str)) + '_' + pd.Series(grid_ix[:, 0].astype(str))
join['dataname'] = pd.Series(join['index_right'].values, index=join['index_right'].values).map(datanames).values

#join[['index', 'UNIQUE_ID', 'index_right', 'dataname']].to_csv('line_to_gridcell.csv')

grid_shape = (template_nc.variables['latitude'][:].size, template_nc.variables['longitude'][:].size)


#### Data Size

datasize = template_nc.variables['tasmax'].size * template_nc.variables['tasmax'][0,0,0].nbytes
memsize = psutil.virtual_memory()[1]

template_nc.close()

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

#hist['tmax_summer_mean'].to_csv('hist_tmax_summer_mean_1949-2010.csv')
#hist['wind_summer_mean'].to_csv('hist_wind_summer_mean_1949-2010.csv')

#### For future data

fut_tmax_dir = 'github/RIPS/output/transmission/fut_met'

for model in os.listdir('%s/CMIP5' % homedir):
    print model
    for scen in os.listdir('%s/CMIP5/%s' % (homedir, model)):
        print scen
        nc = {}
        for fn in os.listdir('%s/CMIP5/%s/%s' % (homedir, model, scen)):
            nc.update({ int(fn.split('_')[-1].split('-')[0][:4]) : netCDF4.Dataset('%s/CMIP5/%s/%s/%s' % (homedir, model, scen, fn))})

#            fut = {}

        for k in nc.keys():
            print k
            cat = np.ma.filled(nc[k].variables['tasmax'][:,:,:], np.iinfo(np.int32).min)
            cat = pd.Panel(cat, items=pd.date_range(datetime.date(k,1,1), freq='d', periods=nc[k].variables['tasmax'].shape[0]), major_axis=nc[k].variables['latitude'][:], minor_axis=nc[k].variables['longitude'][:] - 360)
            cat = cat[np.in1d(cat.items.month, [6,7,8])]
#    tmax_mean = cat.mean(axis=0)
            tmax_mean = cat.groupby(cat.items.year, axis=0).mean()
            for j in tmax_mean.items:
                tmax_mean.loc[j].sort_index().sort_index(axis=1).to_csv('%s/%s/fut_tmax_%s_%s_%s' % (homedir, fut_tmax_dir, model, scen, j))
            nc[k].close()
            print k, ' closed'

#### Import csvs
#### Start here when input files are created

join = pd.read_csv('%s/github/RIPS/crosswalk/line_to_gridcell.csv' % (homedir))
hist_tmax = pd.read_csv('%s/github/RIPS/output/transmission/hist_tmax_summer_mean_1949-2010.csv' % (homedir), index_col=0)

join['VOLTAGE'] = join['UNIQUE_ID'].map(t.set_index('UNIQUE_ID')['VOLTAGE'])


def combine_fut_met(fut_met_path, yr_range, model, scen):
    fut_d = {}

    for fn in os.listdir(fut_met_path):
        splitpath = fn.split('_')[2:]
        if (splitpath[0] == model) and (splitpath[1] == scen) and (int(splitpath[2]) in range(*yr_range)):
            df = pd.read_csv('%s/%s' % (fut_met_path, fn), index_col=0).replace(-2147483648, np.nan)
            df.columns = df.columns.values.astype(float)
	    df.index = df.index.values.astype(float)
	    df = df.sort_index().sort_index(axis=1)
            fut_d.update({ int(splitpath[2]) : df})
    return fut_d



join['h_tmax'] = join['index_right'].apply(lambda x: hist_tmax.values.flat[x]) 


join['CABLE_VOLT'] = join['VOLTAGE'].apply(lambda x: v_list[np.argmin(abs(x - v_list))])

join['h_mean_amps'] = join.apply(lambda x: instance_cables[x['CABLE_VOLT']].I(348, 273 + x['h_tmax'], 0.6096), axis=1)

##########

fut_met_path = '%s/github/RIPS/output/transmission/fut_met' % homedir
impact_dir = '%s/github/RIPS/output/transmission/impacts' % homedir


iter_list = pd.Series(os.listdir(fut_met_path)).str.split('_').str[2:].apply(pd.Series)[[0,1]].drop_duplicates(subset=[0,1]).sort(0).reset_index(drop=True)

for iter_comb in iter_list.index:
    model = iter_list.loc[iter_comb, 0]
    scen = iter_list.loc[iter_comb, 1]
    print model, scen

    fut_d = combine_fut_met(fut_met_path, (2010, 2090), model, scen)
    join_out = join.copy()
    join_out['cable_inst'] = join_out.apply(lambda x: instance_cables[x['CABLE_VOLT']], axis=1)

    for i in fut_d.keys():
        join_out['f_%s' % (i)] = join_out['index_right'].apply(lambda x: fut_d[i].values.flat[x])

    fcols = join_out.columns[pd.Series(join_out.columns).str.contains('^f_')]
    join_out = join_out.drop_duplicates(subset=['UNIQUE_ID']).dropna(subset=fcols)

    for i in fcols:
        join_out['f_mean_amps_%s' % i] = join_out.apply(lambda x: x['cable_inst'].I(348, 273 + x[i], 0.6096), axis=1)


    pct_decrease = -100*join_out.iloc[:, np.where(pd.Series(join_out.columns).str.contains('f_mean_amps'))[0]].sub(join_out['h_mean_amps'], 0).div(join_out['h_mean_amps'], 0)
    
    pct_decrease.columns = 'pd_' + pd.Series(pct_decrease.columns).str.extract('(\d+)')
    
    join_geom = t.set_index('UNIQUE_ID')['geometry'][join_out['UNIQUE_ID'].values].reset_index()['geometry']
 
    join_out = pd.concat([join_out.reset_index(drop=True), pct_decrease.reset_index(drop=True), join_geom], axis=1)
    
    join_out.dropna(subset=pct_decrease.columns, inplace=True)
    join_out.reset_index(drop=True, inplace=True)
    
    join_out = gpd.GeoDataFrame(join_out[join_out.columns[pd.Series(join_out.columns).str.contains('pd_')]], geometry=join_out.geometry.values).dropna()
    
    join_out.crs = t.crs
    
    # Get decadal averages
    
    decades = [[str(i) for i in range(2010, 2090) if int(str(i)[2]) == j] for j in list(set([int(str(k)[2]) for k in range(2010, 2090)]))]
    decade_keys = ['d' + str(i) for i in range(2010, 2090, 10)]
    
    decades = dict(zip(decade_keys, decades))
    
    jcols = pd.Series(join_out.columns)
    jcols = jcols[jcols.str.contains('\d')]
    
    for i in decades.keys():
        join_out['pd_%s' % (i)] = join_out[jcols[jcols.str.contains('|'.join(decades[i]))]].mean(axis=1)
    
    #### Output file
    
    join_out.to_file('%s/trans_impacts_%s_%s.shp' % (impact_dir, model, scen))


#### Combine scenarios

import os
import geopandas as gpd

homedir = os.path.expanduser('~')
impact_dir = '%s/github/RIPS/output/transmission/impacts' % homedir

for i in ['rcp26', 'rcp45', 'rcp85']:
    print i
    dlist = [j for j in os.listdir(impact_dir) if (i in j) and ('.shp' in j)]
    out_df = gpd.read_file('%s/%s' % (impact_dir, dlist[0]))
    cols = [col for col in out_df.columns if col != 'geometry']
    for fn in dlist[1:]:
        df = gpd.read_file('%s/%s' % (impact_dir, fn))
        out_df[cols] += df[cols]
    out_df[cols] = out_df[cols]/len(dlist)
    out_df.to_file('trans_impacts_%s_avg.shp' % (i))
