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
#sub_to_util['SUB_INT'] = sub_to_util['UNIQUE_ID'].map(pd.Series(sub_db.set_index('UNIQUE_ID')['SUB_INT']))
sub_to_util['UTIL_INT'] = sub_to_util['UTIL_ID'].map(pd.Series(util_db.index, index=util_db['UNIQUE_ID']))

#### VECTORIZE POLYGON FUNCTION

class vectorize_polygon():
    def __init__(self, shp, convert_crs=0):
        print 'START: %s' % (str(datetime.now()))
        print 'loading files...'        
        
        print 'getting geometry type info...'
        
        self.shapes={'shp':{}}


        self.shapes['shp'].update({'file' : fiona.open(shp, 'r')})
        self.shapes['shp'].update({'crs': self.shapes['shp']['file'].crs})
        self.shapes['shp'].update({'types': self.geom_types(self.shapes['shp']['file']).dropna()}) 
        self.shapes['shp'].update({'shp' : self.homogenize_inputs('shp', range(len(self.shapes['shp']['file'])))})
        self.shapes['shp'].update({'poly' : self.poly_return('shp')})
        
        print 'END: %s' % (str(datetime.now()))


    def file_chunks(self, l, n):
        """ Yield successive n-sized chunks from l.
        """
        for i in xrange(0, len(l), n):
            yield np.array(l[i:i+n])
        
    def homogenize_inputs(self, shp, chunk):
        print 'homogenizing inputs for %s...' % (shp)
        
        d = {}
        
        bv = self.poly_vectorize(self.shapes[shp]['file'], chunk).dropna()
        gtypes = self.shapes[shp]['types'].loc[bv.index]

        poly = bv.loc[gtypes=='Polygon'] 
        mpoly = bv.loc[gtypes=='MultiPolygon'] 

        apoly = poly.apply(lambda x: list(chain(*x)))
        a_mpoly = mpoly.apply(lambda x: list(chain(*x)))
        
        #### HOMOGENIZE POLYGONS

        if len(poly) > 0:
            polyarrays = pd.Series(apoly.apply(lambda x: np.array(x)))
            p_x_arrays = polyarrays.apply(lambda x: np.array(x)[:,0])
            p_y_arrays = polyarrays.apply(lambda x: np.array(x)[:,1])
            p_trans_arrays = pd.concat([p_x_arrays, p_y_arrays], axis=1)

            d['p_geom'] = pd.Series(zip(p_trans_arrays[0], p_trans_arrays[1]), index=p_trans_arrays.index).apply(np.column_stack)
            d['p_geom'] = d['p_geom'][d['p_geom'].apply(lambda x: x.shape[0]>=4)]

        #### HOMOGENIZE MULTIPOLYGONS
        
        if len(mpoly) > 0:            
            mpolydims = a_mpoly.apply(lambda x: np.array(x).ndim)

            ##ndim==1

            if (mpolydims==1).any():
                m_x_arrays_1 = a_mpoly[mpolydims==1].apply(pd.Series).stack().apply(lambda x: np.array(x)[:,0])
                m_y_arrays_1 = a_mpoly[mpolydims==1].apply(pd.Series).stack().apply(lambda x: np.array(x)[:,1])

                mp = pd.concat([m_x_arrays_1, m_y_arrays_1], axis=1)

                m_geom_1_s = pd.Series(zip(mp[0], mp[1])).apply(np.column_stack)

                empty_s = pd.Series(range(len(mp)), index=mp.index)
                empty_s = empty_s.reset_index()
                empty_s[0] = m_geom_1_s
                empty_s = empty_s[empty_s[0].apply(lambda x: x.shape[0]>=4)]

                d['m_geom_1'] = empty_s.groupby('level_0').apply(lambda x: tuple(list(x[0])))

            ##ndim==3

            if (mpolydims==3).any():
                m_arrays_3 = a_mpoly[mpolydims==3].apply(pd.Series).stack().apply(lambda x: np.array(x)[:,[0,1]])
                m_arrays_3 = m_arrays_3[m_arrays_3.apply(lambda x: x.shape[0]>=4)]

                d['m_geom_3'] = m_arrays_3.reset_index().groupby('level_0').apply(lambda x: tuple(list(x[0])))
        
        returndf = pd.concat(d.values()).sort_index()
        return returndf

        
    def convert_crs(self, shp, crsfrom, crsto, chunk):
        print 'converting coordinate reference system of %s...' % (shp)
        
        crsfrom = Proj(crsfrom, preserve_units=True)
        crsto = Proj(crsto, preserve_units=True)
        
        d = {}
        
        bv = self.poly_vectorize(self.shapes[shp]['file'], chunk).dropna()
        gtypes = self.shapes[shp]['types'].loc[bv.index]

        poly = bv.loc[gtypes=='Polygon'] 
        mpoly = bv.loc[gtypes=='MultiPolygon'] 

        apoly = poly.apply(lambda x: list(chain(*x)))
        a_mpoly = mpoly.apply(lambda x: list(chain(*x)))
        
        #### CONVERT POLYGONS
        
        if len(poly) > 0:
            polyarrays = pd.Series(apoly.apply(lambda x: np.array(x)))
            p_x_arrays = polyarrays.apply(lambda x: np.array(x)[:,0])
            p_y_arrays = polyarrays.apply(lambda x: np.array(x)[:,1])
            p_trans_arrays = pd.concat([p_x_arrays, p_y_arrays], axis=1).apply(lambda x: transform(crsfrom, crsto, x[0], x[1]), axis=1)
        
            d['p_trans_geom'] = p_trans_arrays.apply(np.array).apply(np.column_stack)
            d['p_trans_geom'] = d['p_trans_geom'][d['p_trans_geom'].apply(lambda x: x.shape[0]>=4)]
        
        #### CONVERT MULTIPOLYGONS
        
        if len(mpoly) > 0:
            mpolydims = a_mpoly.apply(lambda x: np.array(x).ndim)
        
            ##ndim==1
            
            if (mpolydims==1).any():
                m_x_arrays_1 = a_mpoly[mpolydims==1].apply(pd.Series).stack().apply(lambda x: np.array(x)[:,0])
                m_y_arrays_1 = a_mpoly[mpolydims==1].apply(pd.Series).stack().apply(lambda x: np.array(x)[:,1])
                mp = pd.concat([m_x_arrays_1, m_y_arrays_1], axis=1)
                m_x_flat_arrays_1 = pd.Series([j[:,0] for j in [np.column_stack(i) for i in np.column_stack([mp[0].values, mp[1].values])]])
                m_y_flat_arrays_1 = pd.Series([j[:,0] for j in [np.column_stack(i) for i in np.column_stack([mp[0].values, mp[1].values])]])
                m_trans_arrays_1 = pd.concat([m_x_flat_arrays_1, m_y_flat_arrays_1], axis=1).apply(lambda x: transform(crsfrom, crsto, x[0], x[1]), axis=1)
                m_trans_geom_1_s = m_trans_arrays_1.apply(np.array).apply(np.column_stack)
                empty_s = pd.Series(range(len(mp)), index=mp.index).reset_index()
                empty_s[0] = m_trans_geom_1_s
                empty_s = empty_s[empty_s[0].apply(lambda x: x.shape[0]>=4)]

                d['m_trans_geom_1'] = empty_s.groupby('level_0').apply(lambda x: tuple(list(x[0])))
        
            ##ndim==3
            if (mpolydims==3).any():
                m_trans_arrays_3 = a_mpoly[mpolydims==3].apply(pd.Series).stack().apply(lambda x: np.array(x)[:,[0,1]]).apply(lambda x: transform(crsfrom, crsto, x[:,0], x[:,1]))

                m_trans_geom_3 = m_trans_arrays_3.apply(np.array).apply(np.column_stack)
                m_trans_geom_3 = m_trans_geom_3[m_trans_geom_3.apply(lambda x: x.shape[0]>=4)]
                m_trans_geom_3_u = m_trans_geom_3.unstack()

                d['m_trans_geom_3'] = pd.Series(zip(m_trans_geom_3_u[0], m_trans_geom_3_u[1]), index=m_trans_geom_3_u.index)
        
        return pd.concat(d.values()).sort_index()
    
    
    def poly_vectorize(self, shpfile, chunk):
        s = pd.Series(chunk, index=chunk)
        
        def return_coords(x):
            try:
                return shpfile[x]['geometry']['coordinates']
            except:
                return np.nan
            
        return s.apply(return_coords)
    
    def handle_topo_err(self, k):
        if k.is_valid:
            return k
        else:
            return k.boundary.convex_hull
   
    def handle_empty(self, k):
        if k.is_empty:
            return np.nan
        elif type(k) != geometry.polygon.Polygon:
            return np.nan
        else:
            return k

    def try_union(self, k):
        try:
    	    return ops.cascaded_union(k)
        except:
            try:
    	        u = k[0]
    	        for z in range(len(k))[1:]:
    	            u = u.union(k[z])
    	        return u
            except:
                return geometry.Polygon(np.vstack(pd.Series(k).apply(lambda x: x.boundary.coords).apply(np.array))).convex_hull

    def poly_return(self, shp):
        print 'creating polygons for %s...' % (shp)
        poly_df = pd.Series(index=self.shapes[shp]['shp'].index)

        geomtypes = self.shapes[shp]['types'].loc[poly_df.index]
        
#        print 'making p'
        if (geomtypes=='Polygon').any():
            p = self.shapes[shp]['shp'].loc[geomtypes=='Polygon'].apply(lambda x: geometry.Polygon(x))#.apply(self.handle_empty) 
    #        print 'setting polydf with p'
            poly_df.loc[p.index] = p.copy()
        
#        print 'making mp'
        if (geomtypes=='MultiPolygon').any():
            mp = self.shapes[shp]['shp'].loc[geomtypes == 'MultiPolygon'].apply(lambda x: (pd.Series(list(x)))).stack().apply(geometry.Polygon)
	    
	    if mp.apply(lambda x: not x.is_valid).any():
	        mp = mp.apply(self.handle_topo_err).apply(self.handle_empty).dropna()
		
	    mp = mp.reset_index().groupby('level_0').apply(lambda x: list(x[0])).apply(self.try_union)
            
    #        print 'setting poly df with mp'
            poly_df.loc[mp.index] = mp.copy()

#        print 'making nullgeom'
        nullgeom = poly_df[poly_df.isnull()].index

#        print 'dropping nullgeom from polydf'
        poly_df = poly_df.drop(nullgeom)
        
#        print 'dropping nullgeom from selp.shapes.shp'
        self.shapes[shp]['shp'] = self.shapes[shp]['shp'].drop(nullgeom)
        
        return poly_df
            
    def geom_types(self, shp):
        s = pd.Series(range(len(shp)))
        def return_geom(x):
            try:
                return shp[x]['geometry']['type']
            except:
                return np.nan
        return s.apply(return_geom)
      
#### WORK AREA

b = vectorize_polygon('/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp')

b.shapes['shp']['poly'][~b.shapes['shp']['poly'].apply(lambda x: x.is_valid)] = b.shapes['shp']['poly'][~b.shapes['shp']['poly'].apply(lambda x: x.is_valid)].apply(lambda x: x.buffer(0))

op_db = pd.merge(sub_to_util.set_index('UTIL_ID').loc[869].reset_index(), sub_db.rename(columns={'UNIQUE_ID':'SUB_ID'}), on='SUB_ID')[['UTIL_ID', 'SUB_ID', 'LONG_LON', 'LONG_LAT', 'UTIL_INT', 'SUB_INT']].set_index('SUB_INT').sort_index()

vor = spatial.Voronoi(op_db[['LONG_LON', 'LONG_LAT']].values)

reg, vert = voronoi_finite_polygons_2d(vor,1)

srp_poly = b.shapes['shp']['poly'][344]

v_poly = pd.Series(reg).apply(lambda x: geometry.Polygon(vert[x])).apply(lambda x: srp_poly.intersection(x))

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
