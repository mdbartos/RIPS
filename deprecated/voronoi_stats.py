import rasterstats
import rasterio
import fiona
from rasterio.warp import reproject
import pandas as pd
import geopandas as gpd

#### FOR ICLUS, BEST PROJECTION IS EPSG 5070: NAD83/CONUS ALBERS
vor = '/home/akagi/voronoi_intersect.shp'
pop_dens = '/home/akagi/Desktop/rastercopy.tif'

gdf = gpd.GeoDataFrame.from_file(vor)
rast = rasterio.open(pop_dens)

zones = gdf['geometry'].to_crs(rast.crs) 

rstats = pd.DataFrame.from_dict(rasterstats.zonal_stats(zones, pop_dens, stats=['sum', 'mean']))

util_stats = pd.concat([rstats, gdf], join='inner', axis=1)
tot_util = util_stats.groupby('UTIL_ID').sum()['sum']
util_stats['util_tot'] = util_stats['UTIL_ID'].map(tot_util)
util_stats['load_frac'] = util_stats['sum']/util_stats['util_tot']
util_stats['summer_load'] = util_stats['SUMMERPEAK']*util_stats['load_frac']
util_stats['winter_load'] = util_stats['WINTERPEAK']*util_stats['load_frac']
#util_stats = pd.concat([rstats.set_index('__fid__'), gdf.set_index('SUB_ID')['UTIL_ID']], join='inner', axis=1).groupby('UTIL_ID').sum()

gdf['colors'] = rstats['sum']
gdf.plot(column='colors')
