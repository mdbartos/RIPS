import rasterstats
import rasterio
import fiona
from rasterio.warp import reproject
import pandas as pd
import geopandas as gpd

srp = '/home/akagi/srp_voronoi.shp'
pop_dens = '/home/akagi/Desktop/rastercopy.tif'

gdf = gpd.GeoDataFrame.from_file(srp)
rast = rasterio.open(pop_dens)

zones = gdf['geometry'].to_crs(rast.crs) 

rstats = pd.DataFrame.from_dict(rasterstats.zonal_stats(zones, pop_dens, stats=['sum', 'mean']))

gdf['colors'] = rstats['sum']
gdf.plot(column='colors')
