import pandas as pd
import numpy as np
import fiona
from shapely import geometry
from shapely import ops
from itertools import chain
from pyproj import Proj, transform
from scipy import spatial
from matplotlib import path
import os
from datetime import datetime
import sys
import pysal as ps
import numpy as np
from scipy import spatial
import geopandas as gpd
from geopandas import tools


substations = '/home/akagi/Desktop/electricity_data/Substations.shp'
substations_db = '/home/akagi/Desktop/electricity_data/Substations.dbf'

utility = '/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp'
utility_db = '/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.dbf'

#### FINITE VORONOI REGIONS 

def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.

    """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()*2

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all([v >= 0 for v in vertices]):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    return new_regions, np.asarray(new_vertices)


b = gpd.GeoDataFrame.from_file('/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp')

#### LOOP THROUGH UTILITY SERVICE AREAS
sub = gpd.read_file(substations)
util = gpd.read_file(utility)

invalid_util = util[~util['geometry'].apply(lambda x: x.is_valid)]
util.loc[invalid_util.index, 'geometry'] = util.loc[invalid_util.index, 'geometry'].apply(lambda x: x.buffer(0))

sub_util = tools.sjoin(sub, util, op='within', how='left')

sub_xy = np.vstack(sub['geometry'].apply(lambda u: np.concatenate(u.xy)).values)

#util_poly = b.set_index('UNIQUE_ID')['geometry']
vor = spatial.Voronoi(sub_xy)
reg, vert = voronoi_finite_polygons_2d(vor,1)

v_poly = gpd.GeoSeries(pd.Series(reg).apply(lambda x: geometry.Polygon(vert[x])))

v_gdf = gpd.GeoDataFrame(pd.concat([sub.drop('geometry', axis=1), v_poly], axis=1)).rename(columns={0:'geometry'})
v_gdf.crs = sub.crs

j = tools.sjoin(util, v_gdf, op='intersects')
j['right_geom'] = j['UNIQUE_ID_right'].map(v_gdf.set_index('UNIQUE_ID')['geometry'])
j = j.dropna(subset=['geometry', 'right_geom']).set_index('UNIQUE_ID_left')

## BE CAREFUL WITH THIS: SLOW
j_inter = j.apply(lambda x: x['geometry'].intersection(x['right_geom']), axis=1)

## OUTFILE
outdf = gpd.GeoDataFrame(pd.concat([j[['UNIQUE_ID_right', 'SUMMERPEAK', 'WINTERPEAK']].reset_index(), j_inter.reset_index()[0]], axis=1), crs=sub.crs).rename(columns={0:'geometry', 'UNIQUE_ID_left':'UTIL_ID', 'UNIQUE_ID_right':'SUB_ID'})

#outdf.to_file('voronoi_intersect.shp')
