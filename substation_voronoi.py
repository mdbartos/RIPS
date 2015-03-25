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


substations = '/home/tabris/Desktop/electricity_data/Substations.shp'
substations_db = '/home/tabris/Desktop/electricity_data/Substations.dbf'

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

####


all_vert = b.shape['shp'].apply(list).apply(pd.Series).stack().apply(tuple).reset_index()[0]
trans_input = {'shp': all_vert, 'crs': b.shape['crs']}
h = quick_spatial_join(None, zipshp, man_input_1=trans_input, memsize=4800000) 

vert_to_zip = h.matches.copy()
vert_to_zip['zip'] = vert_to_zip[0].astype(int).apply(lambda x: h.shapes['shp2']['file'][x]['properties']['ZCTA5CE10'])
vertstack = b.shape['shp'].apply(list).apply(pd.Series).stack().reset_index().rename(columns={0:'coords'}) 
vert_to_zip = pd.concat([vert_to_zip, vertstack], axis=1).reset_index()
vert_to_zip = vert_to_zip.rename(columns={'index':'vert_id', 0:'zip_id'}).set_index('vert_id')
vert_to_zip['BUS_NAME'] = vert_to_zip['level_0'].map(trans_nodes['BUS_NAME'])
vert_to_zip['x'] = vert_to_zip['coords'].apply(lambda x: x[0])
vert_to_zip['y'] = vert_to_zip['coords'].apply(lambda x: x[1])
vert_to_zip['coords'] = vert_to_zip['coords'].astype(str)
mesa = vert_to_zip.loc[vert_to_zip['zip']==85210].drop_duplicates('coords')

testv = mesa[['x', 'y']].values
v = spatial.Voronoi(testv) 



reg, vert = voronoi_finite_polygons_2d(v,1)
s = pd.Series(range(len(mesa.index)))
iverts = s.apply(lambda x: vert[reg[x]])
iverts.index = mesa.index
mesa_verts = pd.concat([mesa, iverts], axis=1)
mesa_verts[0] = mesa_verts[0].apply(lambda x: np.vstack([x, x[0]]))

zipdfstr = '/home/tabris/GIS/census/cb_2013_us_zcta510_500k.dbf'  

dbf2 = ps.open(zipdfstr)
dbpass2 = {col: dbf2.by_col(col) for col in dbf2.header}
zipdf = pd.DataFrame(dbpass2)
zipdf[zipdf['ZCTA5CE10']=='85210'].index
zbounds_85210 = h.shapes['shp2']['shp'].at[zipdf[zipdf['ZCTA5CE10']=='85210'].index[0]]
poly_85210 = h.shapes['shp2']['poly'].at[zipdf[zipdf['ZCTA5CE10']=='85210'].index[0]]
mesa_verts['poly'] = mesa_verts[0].apply(geometry.Polygon)
mesa_util = mesa_verts.groupby('BUS_NAME')['poly'].apply(lambda x: ops.cascaded_union(x)).apply(lambda x: x.intersection(poly_85210))


xmin = zbounds_85210[:,0].min()
xmax = zbounds_85210[:,0].max()
ymin = zbounds_85210[:,1].min()
ymax = zbounds_85210[:,1].max()
xlim(xmin, xmax)
ylim(ymin, ymax)
