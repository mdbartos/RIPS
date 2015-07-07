import pandas as pd
import numpy as np

d = {}
for i in range (2001, 2011):
    d.update({i : pd.read_excel('schedule6_%s.xls' % (i), skiprows=6)})

c = pd.concat([i[['NERC Region', 'Design (kV)', 'Size  (MCM)', 'Material']] for i in d.values()]).dropna()
c['NERC Region'] = c['NERC Region'].str.strip()
c['Material'] = c['Material'].str.replace('^ACSR.+', 'ACSR').str.replace('^ACSS.+', 'ACSS').str.replace('^CU.+', 'CU').replace('AA', 'AAC').replace('AL', 'AAC').replace('Copper', 'CU').replace('Aluminum', 'AAC')
c = c[c['Material'].isin(['ACSR', 'ACSS', 'AAC', 'CU'])]
c['Design (kV)'] = c['Design (kV)'].astype(str).str.replace('kV', '').str.replace('*', '').str.strip().replace('100-120', '115').replace('200-299', '230').replace('151-199', '161').replace('400-599', '500').replace('121-150', '138').replace('300-399', '345').replace('161/115', '161').replace('500/230', '500').astype(float)
c = c[c['Design (kV)'].isin([230, 115, 345, 500, 138, 161])]
c = c[c['Size  (MCM)'].apply(np.isreal)]
c['Size  (MCM)'] = c['Size  (MCM)'].astype(float)
c = c[(c['Size  (MCM)'] < 9999) & (c['Size  (MCM)'] > 0)]

s = c.groupby(['NERC Region', 'Design (kV)', 'Material'])['Size  (MCM)']
s.value_counts()

boxplot(np.asarray([c[c['Design (kV)'] == i]['Size  (MCM)'].values for i in sorted(c['Design (kV)'].unique().tolist())]), labels=sorted(c['Design (kV)'].unique().tolist()))
