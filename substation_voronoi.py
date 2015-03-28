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


substations = '/home/akagi/Desktop/electricity_data/Substations.shp'
substations_db = '/home/akagi/Desktop/electricity_data/Substations.dbf'

utility = '/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp'
utility_db = '/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.dbf'

#### FUNCTION TO IMPORT DBF

def open_dbf(fn):
    dbf = ps.open(fn)
    dbpass = {col: dbf.by_col(col) for col in dbf.header}
    return_df = pd.DataFrame(dbpass)
    return return_df

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

#### IMPORT SUBSTATION POINTS

sub = fiona.open(substations)
sub_db = open_dbf(substations_db)

sub_db['LONG_LAT'] = pd.Series(sub_db.index).apply(lambda x: sub[x]['geometry']['coordinates'][1])
sub_db['LONG_LON'] = pd.Series(sub_db.index).apply(lambda x: sub[x]['geometry']['coordinates'][0])
sub_db['SUB_INT'] = sub_db.index

#### IMPORT UTILITY REGIONS

util = fiona.open(utility)
util_db = open_dbf(utility_db)
util_db['UTIL_INT'] = util_db.index

#### IMPORT SUBSTATION TO UTILITY CORRESPONDENCE

sub_to_util = pd.read_csv('/home/akagi/Desktop/sub_util_qgis.csv')
sub_to_util['UTIL_INT'] = sub_to_util['UTIL_ID'].map(pd.Series(util_db.index, index=util_db['UNIQUE_ID']))

#### IMPORT UTILITY SERVICE AREAS

b = gpd.GeoDataFrame.from_file('/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp')

#### LOOP THROUGH UTILITY SERVICE AREAS

schema = {
    'geometry': 'Polygon',
    'properties': {'sub_id': 'int', 'util_id': 'int'},
}

with fiona.open('util_voronoi.shp', 'w', 'ESRI Shapefile', schema, crs=b.crs) as c:

    op_db = pd.merge(sub_to_util, sub_db.rename(columns={'UNIQUE_ID':'SUB_ID'}), on='SUB_ID')[['UTIL_ID', 'SUB_ID', 'LONG_LON', 'LONG_LAT', 'UTIL_INT', 'SUB_INT']].set_index('UTIL_ID').sort_index().drop_duplicates(subset=['LONG_LON', 'LONG_LAT'])
    
    for u in sub_to_util['UTIL_ID'].astype(int).unique():
        print u
        util_poly = b.set_index('UNIQUE_ID')['geometry'].loc[u]
        w_db = op_db.loc[u]
        
        if (len(w_db.shape) > 1) and (w_db.shape[0] > 2):
            
            w_db = w_db.set_index('SUB_INT').sort_index()
            
            vor = spatial.Voronoi(w_db[['LONG_LON', 'LONG_LAT']].values)

            reg, vert = voronoi_finite_polygons_2d(vor,1)


            v_poly = pd.Series(reg).apply(lambda x: geometry.Polygon(vert[x])).apply(lambda x: util_poly.intersection(x))
            
            for rec in range(len(v_poly)):
                if not v_poly[rec].is_empty:
                    c.write({
                        'geometry': geometry.mapping(v_poly[rec]),
                        'properties': {'sub_id': int(w_db.iloc[rec]['SUB_ID']), 'util_id': int(u)},
                    })

        elif (len(w_db.shape) > 1) and (w_db.shape[0] == 2):

            w_db = w_db.set_index('SUB_INT').sort_index()
            subs = list(w_db.index)
            slope = -1/((w_db.loc[subs[0]]['LONG_LAT'] - w_db.loc[subs[1]]['LONG_LAT'])/(w_db.loc[subs[0]]['LONG_LON'] - w_db.loc[subs[1]]['LONG_LON']))

            mid_x = (w_db.loc[subs[0]]['LONG_LON'] + w_db.loc[subs[1]]['LONG_LON'])/2
            mid_y = (w_db.loc[subs[0]]['LONG_LAT'] + w_db.loc[subs[1]]['LONG_LAT'])/2
            xc = np.linspace(util_poly.bounds[0], util_poly.bounds[2])
            yc = slope*(xc - mid_x) + mid_y

            result = list(ops.polygonize(ops.linemerge(list(util_poly.boundary.union(geometry.LineString(np.column_stack([xc, yc])))))))

            if result[0].contains(geometry.Point(w_db.loc[subs[0]][['LONG_LON', 'LONG_LAT']].values)):
                c.write({
                    'geometry': geometry.mapping(result[0]),
                    'properties': {'sub_id': int(subs[0]), 'util_id': int(u)},
                })

                c.write({
                    'geometry': geometry.mapping(result[1]),
                    'properties': {'sub_id': int(subs[1]), 'util_id': int(u)},
                })

            else:
                c.write({
                    'geometry': geometry.mapping(result[0]),
                    'properties': {'sub_id': int(subs[1]), 'util_id': int(u)},
                })

                c.write({
                    'geometry': geometry.mapping(result[1]),
                    'properties': {'sub_id': int(subs[0]), 'util_id': int(u)},
                })


        else:
            c.write({
                'geometry': geometry.mapping(util_poly),
                'properties': {'sub_id': int(w_db['SUB_ID']), 'util_id': int(u)},
            })



#### PLOTTING

plot(srp_poly.exterior.xy[0], srp_poly.exterior.xy[1])

scatter(op_db['LONG_LON'], op_db['LONG_LAT'])

for i in v_poly.index:
    try:
        p = v_poly[i].exterior.xy
        plot(p[0], p[1])
    except:
        pass

#### WRITE TO SHAPEFILE

schema = {
    'geometry': 'Polygon',
    'properties': {'id': 'int'},
}

with fiona.open('srp_voronoi.shp', 'w', 'ESRI Shapefile', schema, crs=b.shapes['shp']['crs']) as c:
    ## If there are multiple geometries, put the "for" loop here
    for rec in range(len(v_poly)):
        c.write({
            'geometry': geometry.mapping(v_poly[rec]),
            'properties': {'id': int(op_db.iloc[rec]['SUB_ID'])},
        })
