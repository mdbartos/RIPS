import numpy as np
import pandas as pd
import geopandas as gpd


class network_model():

    def __init__(self, lines, subs, util, gen, bbox=None, loads=None, pop_dens=None):
        self.lines = gpd.read_file(lines)
        self.subs = gpd.read_file(subs)
        self.util = gpd.read_file(util)
        self.gen = gpd.read_file(gen)

        if loads is None:
            if pop_dens is not None:
                loads = self.partition_loads(self.construct_voronoi(), pop_dens)

        if edges is None:
            edges = self.line_to_sub()
        if node_gen is None:
            node_gen = self.gen_to_sub()

        self.net = pd.concat([loads.groupby('SUB_ID').sum()['summer_loa'], gen.groupby('SUB_ID').sum()['S_CAP_MW'].fillna(0)], axis=1, join='outer')[['summer_loa', 'S_CAP_MW']].fillna(0)
        self.net = self.net['S_CAP_MW'] - self.net['summer_loa']

        if bbox is not None:
        self.nodes, self.edges, self.loads = self.set_bbox(*bbox)

        # Set up graph

        self.G = nx.Graph()
        
        for i in self.loads.index:
            self.G.add_node(i, load=self.loads[i])
        
        for i in self.edges.index:
            row = self.edges.loc[i]
            self.G.add_edge(*tuple(row[['SUB_1', 'SUB_2']].astype(int).values),
        		tot_kv=row['TOT_CAP_KV'],
        		num_lines=int(row['NUM_LINES']),
        		length=row['LENGTH'])

    def construct_voronoi(self):
        from scipy import spatial
        from geopandas import tools
        from shapely import geometry

        util = self.util
        sub = self.sub

        # Fix utility service areas with invalid geometry
        invalid_util = util[~util['geometry'].apply(lambda x: x.is_valid)]
        util.loc[invalid_util.index, 'geometry'] = util.loc[invalid_util.index, 'geometry'].apply(lambda x: x.buffer(0))
       
        # Spatially join substations with utility service territories
        sub_util = tools.sjoin(sub, util, op='within', how='left')
        
        # Construct voronoi polygons for each substation
        sub_xy = np.vstack(sub['geometry'].apply(lambda u: np.concatenate(u.xy)).values)
        vor = spatial.Voronoi(sub_xy)
        reg, vert = self.voronoi_finite_polygons_2d(vor,1)
       
        # Convert voronoi diagram to polygons and insert into GeoDataFrame
        v_poly = gpd.GeoSeries(pd.Series(reg).apply(lambda x: geometry.Polygon(vert[x])))
        v_gdf = gpd.GeoDataFrame(pd.concat([sub.drop('geometry', axis=1), v_poly], axis=1)).rename(columns={0:'geometry'})
        v_gdf.crs = sub.crs
        
        # Spatially join utility service areas with voronoi polygons
        j = tools.sjoin(util, v_gdf, op='intersects')
        j['right_geom'] = j['UNIQUE_ID_right'].map(v_gdf.set_index('UNIQUE_ID')['geometry'])
        j = j.dropna(subset=['geometry', 'right_geom']).set_index('UNIQUE_ID_left')
        
        # Clip voronoi polygons to utility service area
        j_inter = j.apply(lambda x: x['geometry'].intersection(x['right_geom']), axis=1)
        
        # Create output GeoDataFrame with relevant fields
        outdf = gpd.GeoDataFrame(pd.concat([j[['UNIQUE_ID_right', 'SUMMERPEAK', 'WINTERPEAK']].reset_index(), j_inter.reset_index()[0]], axis=1), crs=sub.crs).rename(columns={0:'geometry', 'UNIQUE_ID_left':'UTIL_ID', 'UNIQUE_ID_right':'SUB_ID'})

        return outdf

    def partition_loads(self, vor, pop_dens):
        # voronoi_stats.shp

        import rasterstats
        import rasterio
        
        #### FOR ICLUS, BEST PROJECTION IS EPSG 5070: NAD83/CONUS ALBERS
        # vor = '/home/akagi/voronoi_intersect.shp'
        # pop_dens = '/home/akagi/Desktop/rastercopy.tif' 
        # gdf = gpd.GeoDataFrame.from_file(vor)
        # rast = rasterio.open(pop_dens)

        if isinstance(vor, str):
            gdf = gpd.read_file(vor)
        if isinstance(pop_dens, str):
            pop_dens = rasterio.open(pop_dens)

        zones = gdf['geometry'].to_crs(pop_dens.crs)
        rstats = pd.DataFrame.from_dict(rasterstats.zonal_stats(zones, pop_dens, stats=['sum', 'mean']))

        util_stats = pd.concat([rstats, gdf], join='inner', axis=1)
        tot_util = util_stats.groupby('UTIL_ID').sum()['sum']
        util_stats['util_tot'] = util_stats['UTIL_ID'].map(tot_util)
        util_stats['load_frac'] = util_stats['sum']/util_stats['util_tot']
        util_stats['summer_load'] = util_stats['SUMMERPEAK']*util_stats['load_frac']
        util_stats['winter_load'] = util_stats['WINTERPEAK']*util_stats['load_frac']

        return util_stats

    def gen_to_sub(self):

        from shapely import geometry
        from scipy import spatial
       
        sub = self.sub
        gen = self.gen
  
        # Find nearest neighbors
        tree = spatial.cKDTree(np.vstack(sub.geometry.apply(lambda x: x.coords[0]).values))
        node_query = tree.query(np.vstack(gen.geometry.apply(lambda x: x.coords[0]).values)) 
        
        crosswalk = pd.DataFrame(np.column_stack([gen[['UNIQUE_ID', 'S_CAP_MW']].values, s.iloc[node_query[1]]['UNIQUE_ID'].values.astype(int)]), columns=['GEN_ID', 'S_CAP_MW', 'SUB_ID'])
        crosswalk = crosswalk[['GEN_ID', 'SUB_ID', 'S_CAP_MW']]
       
        return crosswalk
        #gen_to_sub_static.csv

    def line_to_sub(self):

        from shapely import geometry
        from scipy import spatial
        
        t = self.lines
        s = self.subs
        
        # Extract start and end nodes in networkK
        
        start = t.geometry[t.geometry.type=='LineString'].apply(lambda x: np.array([x.xy[0][0], x.xy[1][0]])).append(t.geometry[t.geometry.type=='MultiLineString'].apply(lambda x: np.hstack([i.xy for i in x])[:,0])).sort_index()
        
        end = t.geometry[t.geometry.type=='LineString'].apply(lambda x: np.array([x.xy[0][-1], x.xy[1][-1]])).append(t.geometry[t.geometry.type=='MultiLineString'].apply(lambda x: np.hstack([i.xy for i in x])[:,-1])).sort_index()
        
        # Find nearest neighbors
        
        tree = spatial.cKDTree(np.vstack(s.geometry.apply(lambda x: x.coords[0]).values))
        
        start_node_query = tree.query(np.vstack(start.values)) 
        end_node_query = tree.query(np.vstack(end.values)) 
        
        # Create crosswalk table
        
        crosswalk = pd.DataFrame(np.column_stack([t[['UNIQUE_ID', 'TOT_CAP_KV', 'NUM_LINES', 'Shape_Leng']].values, s.iloc[start_node_query[1]][['UNIQUE_ID', 'NAME']].values, start_node_query[0], s.iloc[end_node_query[1]][['UNIQUE_ID', 'NAME']].values, end_node_query[0]]), columns=['TRANS_ID', 'TOT_CAP_KV', 'NUM_LINES', 'LENGTH', 'SUB_1', 'NAME_1', 'ERR_1', 'SUB_2', 'NAME_2', 'ERR_2']) 
        crosswalk = crosswalk[['TRANS_ID', 'SUB_1', 'SUB_2', 'NAME_1', 'NAME_2',  'ERR_1', 'ERR_2', 'TOT_CAP_KV', 'NUM_LINES', 'LENGTH']]

        return crosswalk
        #edges.csv

    def set_bbox(self, xmin, ymin, xmax, ymax):

        t = self.lines
        s = self.subs
        edges = self.edges
        net = self.net

        bbox = tuple(xmin, ymin, xmax, ymax)
        bbox_poly = shapely.geometry.MultiPoint(np.vstack(np.dstack(np.meshgrid(*np.hsplit(bbox, 2)))).tolist()).convex_hull
        
        bbox_lines = t[t.intersects(bbox_poly)]['UNIQUE_ID'].astype(int).values
        bbox_edges = edges[edges['TRANS_ID'].isin(bbox_lines)]
        bbox_edges = bbox_edges[bbox_edges['SUB_1'] != bbox_edges['SUB_2']]
        bbox_nodes = np.unique(bbox_edges[['SUB_1', 'SUB_2']].values.astype(int).ravel())
        
        # Outer lines
        
        edgesubs = pd.merge(t[t.intersects(bbox_poly.boundary)], edges, left_on='UNIQUE_ID', right_on='TRANS_ID')[['SUB_1_y', 'SUB_2_y']].values.ravel().astype(int)
        
        # Nodes just outside of bbox (entering)
        outer_nodes = np.unique(edgesubs[~np.in1d(edgesubs, s[s.within(bbox_poly)]['UNIQUE_ID'].values.astype(int))])
        
        weights = s.loc[s['UNIQUE_ID'].astype(int).isin(edgesubs[~np.in1d(edgesubs, s[s.within(bbox_poly)]['UNIQUE_ID'].values.astype(int))])].set_index('UNIQUE_ID')['MAX_VOLT'].sort_index()
        transfers = -net[bbox_nodes].sum()*(weights/weights.sum()) 
        bbox_loads = net[bbox_nodes] + transfers.reindex(bbox_nodes).fillna(0)

        return bbox_nodes, bbox_edges, bbox_loads

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
