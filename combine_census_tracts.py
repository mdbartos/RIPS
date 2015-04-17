import numpy as np
import pandas as pd
import geopandas as gpd
import psutil
import os

def combine_ct(directory):
    df = gpd.GeoDataFrame()
    memuse = psutil.phymem_usage()[0]

    for fn in os.listdir(directory):
        if fn.endswith('shp'):
            nd = gpd.read_file((directory + '/' + fn))
            df = df.append(nd)
            if not df.crs:
                if nd.crs:
                    df.crs = nd.crs
                else:
                    df.crs = {'init': 'epsg:4269'}
            if nd.crs:
                if df.crs != nd.crs:
                    print('Warning, CRS mismatch')
            if df.values.nbytes > 0.95*memuse:
                print('Memory warning!')
                break

    df = df.reset_index()
    del df['index']
    df = gpd.GeoDataFrame(df, crs=df.crs)
    return df


#### 1990 CT BOUNDARIES

c_1990 = '/home/kircheis/data/shp/census/census_tracts_all/src_data/c_1990'
df_1990 = combine_ct(c_1990)
df_1990.to_file('census_tracts_1990.shp')

#### 2000 CT BOUNDARIES

c_2000 = '/home/kircheis/data/shp/census/census_tracts_all/src_data/c_2000'
df_2000 = combine_ct(c_2000)
df_2000.to_file('census_tracts_2000.shp')

#### 2014 CT BOUNDARIES

c_2014 = '/home/kircheis/data/shp/census/census_tracts_all/src_data/c_2014'
df_2014 = combine_ct(c_2014)
df_2014.to_file('census_tracts_2014.shp')
