import pandas as pd
import numpy as np
from shapely import geometry
import geopandas as gpd
from geopandas import tools
import requests
import time

utility = '/home/akagi/Desktop/electricity_data/Electric_Retail_Service_Ter.shp'
util = gpd.read_file(utility)

#### GET DATA FROM NREL API
apikey = 'WTg8hkRAKuWtOj5L46NrHAa6rrlLm7ESslkEoDf6'

d = {}

util = util.set_index('UNIQUE_ID')

for i in util.index.values:
    rp = util.loc[i, 'geometry'].representative_point().coords[0]
    req = requests.get('https://developer.nrel.gov/api/utility_rates/v3.json?api_key=%s&lat=%s&lon=%s' % (apikey, rp[1], rp[0]))
    req_head = req.headers
    req_out = req.json()['outputs']['utility_info']
    d.update({i : req_out})
    if int(req_head['x-ratelimit-remaining']) == 10:
        time.sleep(3600)

#### SAVE DATA
#import pickle

#with open('util_verify.p', 'wb') as handle:
#    pickle.dump(d, handle)

#### SPLIT MATCHES INTO OVERLAPPING AND NON-OVERLAPPING
ds = {}
dm = {}

for i in d.keys():
    if len(d[i]) > 1:
        dm.update({i : d[i]})
    elif len(d[i]) == 1:
        ds.update({i : d[i]})

from fuzzywuzzy import fuzz, process

#### FIND BEST MATCH FOR OVERLAPPING UTILITY SERVICE AREAS
dm_r = {}

for i in dm.keys():
    df = pd.DataFrame.from_dict(d[i]).set_index('company_id')['utility_name']
    src_str = util.loc[i, 'NAME']
    m_df = df.apply(lambda x: fuzz.ratio(src_str, x))
    dm_r.update({i : {}})
    dm_r[i].update({'company_id': m_df.idxmax(), 'utility_name': df[m_df.idxmax()], 'search_name': src_str, 'match_ratio': m_df.max()})

#### CHECK MATCHES FOR NON-OVERLAPPING
ds_r = {}

for i in ds.keys():
    nm = ds[i][0]['utility_name']
    c_id = ds[i][0]['company_id']
    src_str = util.loc[i, 'NAME']
    fr = fuzz.ratio(src_str, nm)
    ds_r.update({i : {}})
    ds_r[i].update({'company_id': c_id, 'utility_name': nm, 'search_name': src_str, 'match_ratio': fr})

#### CONVERT TO DATAFRAMES
dm_df = pd.DataFrame.from_dict(dm_r, orient='index').sort('match_ratio')
ds_df = pd.DataFrame.from_dict(ds_r, orient='index').sort('match_ratio')

result = pd.concat([dm_df[dm_df['match_ratio'] > 60], ds_df[ds_df['match_ratio'] > 53]])
