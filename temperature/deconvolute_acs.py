import pandas as pd
import os

d = {}

for fn in os.listdir('/home/kircheis/data/census/ACS_5y'):
    df = pd.read_csv(fn, sep='\t', encoding='iso-8859-1')
    df['Geo_FIPS'] = df['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')
    df = df.set_index('Geo_FIPS').iloc[:,-1]
    df.name = fn.split('_')[1]
    d.update({fn.split('_')[1] : df})

acs = pd.concat([i for i in d.values()], axis=1)

d10 = pd.read_csv('/home/kircheis/data/census/census_tract_pop_2010', encoding='iso-8859-1', sep='\t')
d10['Geo_FIPS'] = d10['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')

cat = pd.concat([acs, d10.set_index('Geo_FIPS').iloc[:,-1]], axis=1)

est_2005 = (5*cat['2005'] - 5*cat['2006'] + cat['SE_T001_001']).reset_index().rename(columns={'index':'Geo_FIPS', 0:'SE_T001_001'})

est_2005.to_csv('census_tract_pop_2005', sep='\t', encoding='iso-8859-1')
