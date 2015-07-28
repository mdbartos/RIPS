import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import tools
import datetime
import os
import statsmodels.api as sm
import sys
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

homedir = os.path.expanduser('~')

#### IMPORT CENSUS AND UTILITY SHAPEFILES
utility = gpd.read_file('%s/github/RIPS_kircheis/data/shp/Electric_Retail_Service_Ter.shp' % homedir)

census_shp = '%s/github/RIPS_kircheis/data/shp/census/census_tracts_all/census_tracts_us.shp' % homedir

census_path = '%s/github/RIPS_kircheis/data/census/' % homedir

acs_path = '%s/github/RIPS_kircheis/data/census/ACS_5y/' % homedir

#### IMPORT SOCIAL EXPLORER POPULATION DATA

all_pop = {}

all_dem = {}

c = {
'1990': None,
'2000': None,
'2010': None,
}

for i in c.keys():
    if ('census_tract_pop_%s' % i) in os.listdir(census_path):
        all_pop[i] = pd.read_csv((census_path + 'census_tract_pop_' + i), sep='\t', encoding='iso-8859-1')
        all_pop[i]['Geo_FIPS'] = all_pop[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')
    if ('census_tract_dem_%s' % i) in os.listdir(census_path):
        all_dem[i] = pd.read_csv((census_path + 'census_tract_dem_' + i), sep='\t', encoding='iso-8859-1')
        all_dem[i]['Geo_FIPS'] = all_dem[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')

#### OPTIONALLY IMPORT ACS POPULATION DATA

acs = {
'2007' : {'r': '2005_2009'},
'2008': {'r': '2006_2010'},
'2009': {'r': '2007_2011'},
'2010': {'r': '2008_2012'},
'2011': {'r': '2009_2013'}
}

####

for i in acs.keys():
    if not i in all_pop.keys():
        all_pop[i] = pd.read_csv((acs_path + 'ACS_' + acs[i]['r'] + '_pop'), sep='\t', encoding='iso-8859-1')
        all_pop[i]['Geo_FIPS'] = all_pop[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')
    if not i in all_dem.keys():
        all_dem[i] = pd.read_csv((acs_path + 'ACS_' + acs[i]['r'] + '_dem'), sep='\t', encoding='iso-8859-1')
        all_dem[i]['Geo_FIPS'] = all_dem[i]['Geo_FIPS'].astype(str).str.pad(11, side='left', fillchar='0')

#### PROCESS DATA

pop_yrs = pd.concat([all_pop[i].set_index('Geo_FIPS').rename(columns={'SE_T001_001':i})[i] for i in all_pop.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

cnames = {
        '1990': {'SE_T043' : 'mHHI', 'SE_T074' : 'occ',
                 'SE_T077' : 'vint', 'SE_T028' : 'lforce'},
        '2000': {'SE_T093' : 'mHHI', 'SE_T157' : 'occ',
                 'SE_T160' : 'vint', 'SE_T072' : 'lforce'},
        '2007': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'}, 
        '2008': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        '2009': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        '2010': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        '2011': {'SE_T057' : 'mHHI', 'SE_T095' : 'occ',
                 'SE_T098' : 'vint', 'SE_T036' : 'lforce'},
        }

for i in cnames.keys():
    cols = pd.Series(all_dem[i].columns)
    newcols = cols[cols.str.contains('Geo_FIPS|SE_T')]
    df = all_dem[i][newcols.values]
    for j in cnames[i].keys():
        newcols = newcols.str.replace(j, cnames[i][j])
    newcols[1:] = i + '_' + newcols[1:]
    df.columns = newcols.values
    all_dem[i] = df

dem_yrs = pd.concat([all_dem[i].set_index('Geo_FIPS') for i in all_dem.keys()], axis=1).sort(axis=1).replace(0, np.nan).dropna(how='all')

dem_d = {}

ucols = pd.Series(dem_yrs.columns).str.split('_').str[1:].apply('_'.join).unique()

for i in ucols:
    cols = pd.Series(dem_yrs.columns)
    newcols = cols[cols.str.contains(i)]
    df = dem_yrs[newcols.values]
    newcols = newcols.str.split('_').str[0]
    df.columns = newcols.values
    dem_d.update({i : df})

####

util_to_eia = pd.read_csv('%s/github/RIPS_kircheis/RIPS/crosswalk/util_eia_id.csv' % homedir, index_col=0)

#### QUICK FIXES

rid = pd.read_csv('%s/github/RIPS_kircheis/data/eia_form_714/active/form714-database/form714-database/Respondent IDs.csv' % homedir)

util_to_eia.loc[2149, 'company_id'] = 2507     #Burbank
util_to_eia.loc[2046, 'company_id'] = 16868    #Seattle City Lights
util_to_eia.loc[2157, 'company_id'] = 17609    #Southern California Edison
util_to_eia.loc[229, 'company_id'] = 5326      #PUD of Douglas County
util_to_eia.loc[520, 'company_id'] = 3989      #Colorado Springs Utilities
util_to_eia.loc[2296, 'company_id'] = 18429    #Tacoma
util_to_eia.loc[2566, 'company_id'] = 7294     #Glendale
util_to_eia.loc[2155, 'company_id'] = 16088    #Riverside
util_to_eia.loc[2298, 'company_id'] = 15500    #Puget Sound
# util_to_eia.loc[589, 'company_id'] =           #Farmington | FARM
# util_to_eia.loc[533, 'company_id'] =           #Los Alamos | LOS
# util_to_eia.loc[627, 'company_id'] =           #Navajo Tribal | NTUA
# util_to_eia.loc[1008, 'company_id'] = 16534    #Redding | RDNG
# util_to_eia.loc[2148, 'company_id'] =          #Vernon | VER
# util_to_eia.loc[ , 'company_id'] = 12397       #MWD of SC | MWD

# NPCC
util_to_eia.loc[2183, 'company_id'] = 2886     #Cambridge (CELC)
util_to_eia.loc[2739, 'company_id'] = 4089     #Commonwealth Edison (COEL) ##DOUBLECHECK
util_to_eia.loc[1586, 'company_id'] = 11172     #Long Island Light (LILC)
util_to_eia.loc[2727, 'company_id'] = 7601     # Green Mountain Power
#util_to_eia.loc[ , 'company_id'] = 15296     #New York Power Authority
util_to_eia.loc[3084, 'company_id'] = 1998     #Boston Edison Co  #Part of NSTAR
#util_to_eia.loc[ , 'company_id'] = 5618     #Eastern Utilities
#util_to_eia.loc[ , 'company_id'] = 13433     #New England Electric Co
#util_to_eia.loc[2723 , 'company_id'] = 3292     #Central Vermont Public Service (CVPS)

# SERC
#util_to_eia.loc[, 'company_id'] = 13204     #Nantahala Power and Light

# ECAR
util_to_eia.loc[2348, 'company_id'] = 5109     #Detroit Edison Co #DTE Energy Co
util_to_eia.loc[2683, 'company_id'] = 3260     #CINERGY (NOW PART OF DUKE) # POSSIBLY UID 2683, Duke Energy Ohio
#util_to_eia.loc[, 'company_id'] = 14015     #Ohio Valley Elec. Coop
#util_to_eia.loc[, 'company_id'] = 538     #Allegheny (Now part of FirstEnergy)
#util_to_eia.loc[, 'company_id'] = 9267     #Hoosier Energy REC
#util_to_eia.loc[, 'company_id'] =      #Municipal Coop Coord Pool

# MAIN
util_to_eia.loc[2667, 'company_id'] = 17632     #Southern Illinois Power Coop
#util_to_eia.loc[, 'company_id'] = 3253     #Central Illinois Pub Serv # Now part of AMEREN #Prob 3105
#util_to_eia.loc[, 'company_id'] = 3252     #Central Illinois Light Co # Also part of AMEREN
#util_to_eia.loc[, 'company_id'] = 9208     #Illinois Power Co # Also part of AMEREN

# SPP
util_to_eia.loc[933, 'company_id'] = 20391     #Westplains Energy - Kansas
util_to_eia.loc[3095, 'company_id'] = 7806     #Gulf State Utilities # Now ENTERGY Gulf States # May want to get all in TX and LA
#util_to_eia.loc[, 'company_id'] = 807     #Arkansas Electric Coop # Members here: http://www.aecc.com/distribution-cooperatives
#util_to_eia.loc[, 'company_id'] = 40233     #Sam Rayburn
#util_to_eia.loc[, 'company_id'] = 12699     #Missouri Public Service # Now Part of Aquila/Black Hills

#ERCOT
util_to_eia.loc[795, 'company_id'] = 8901     #Houston Lighting And Power #Probably 795
util_to_eia.loc[3108, 'company_id'] = 3278     #Central Power and Light #Probably AEP Texas Central Co
#util_to_eia.loc[, 'company_id'] = 18715    #Texas Municipal Power Pool
#util_to_eia.loc[, 'company_id'] = 20404    #West Texas Utilities
#util_to_eia.loc[, 'company_id'] = 11269    #Lower Colorado River Auth
#util_to_eia.loc[, 'company_id'] = 44372    #Texas Utilities Elec # TXU
#util_to_eia.loc[, 'company_id'] = 17583    #South Texas Electric Coop # Possibly 272

#MAPP
util_to_eia.loc[1695, 'company_id'] = 9435     #MidAmerican Energy Co
util_to_eia.loc[1608, 'company_id'] = 4363     #Corn Belt Power Cooperative
#util_to_eia.loc[, 'company_id'] = 9219     #IES Industries #Interstate Power and Light
#util_to_eia.loc[, 'company_id'] = 4716     #Dairyland Power Coop
#util_to_eia.loc[, 'company_id'] = 4322     #Cooperative Power Assoc #Part of Great River
#util_to_eia.loc[, 'company_id'] = 21352     #Municipal Energy Agency NE
#util_to_eia.loc[, 'company_id'] = 9438     #Iowa-Illinois Gas and Electric
#util_to_eia.loc[, 'company_id'] = 40580     #Southern Minnesota Municipal PA #Could be Minn. Muni. Power Agency
#util_to_eia.loc[, 'company_id'] = 13809     #Northwestern Public Service #Probably part of Norhwestern Energy
#util_to_eia.loc[, 'company_id'] = 23333     #Midwest Power Systems Inc
#util_to_eia.loc[, 'company_id'] = 12819     #Montana-Dakota Utilities
#util_to_eia.loc[, 'company_id'] = 19514     #United Power Association #Part of "Great River"
#util_to_eia.loc[, 'company_id'] = 3258     #Central Iowa Power Coop
#util_to_eia.loc[, 'company_id'] = 9392     #Interstate Power Company

####

j90 = pd.read_csv('%s/github/RIPS_kircheis/data/util_join_1990.csv' % homedir, index_col=0).set_index('UNIQUE_ID')['GEOID_1990'].astype(str).str.pad(11, side='left', fillchar='0')

j00 = pd.read_csv('%s/github/RIPS_kircheis/data/util_join_2000.csv' % homedir, index_col=0).set_index('UNIQUE_ID')['GEOID_2000'].astype(str).str.pad(11, side='left', fillchar='0')

j14 = pd.read_csv('%s/github/RIPS_kircheis/data/util_join_2014.csv' % homedir, index_col=0).set_index('UNIQUE_ID')['GEOID_2014'].astype(str).str.pad(11, side='left', fillchar='0')

util_to_c = pd.concat([j90, j00, j14]).drop_duplicates().reset_index()
util_to_c['company_id'] = util_to_c['UNIQUE_ID'].map(util_to_eia['company_id'])
util_to_c = util_to_c.dropna().rename(columns={0:'GEOID'}).set_index('company_id')

####

dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

#### ADD ADDITIONAL ENTRIES TO util_to_c

multi_d = {
        'AEPC' : {'company_id' : 796, 'UNIQUE_ID' : None, 'geom' : None},
        'APS' : {'company_id' : 803, 'UNIQUE_ID' : None, 'geom' : None},
        'TEP' : {'company_id' : 24211, 'UNIQUE_ID' : None, 'geom' : None},
        'SRP' : {'company_id' : 16572, 'UNIQUE_ID' : None, 'geom' : None},
        'PNM' : {'company_id' : 15473, 'UNIQUE_ID' : None, 'geom' : None},
        'PSC' : {'company_id' : 15466, 'UNIQUE_ID' : None, 'geom' : None},
        'AVA' : {'company_id' : 20169, 'UNIQUE_ID' : None, 'geom' : None},
        'PRPA' : {'company_id' : 15143, 'UNIQUE_ID' : None, 'geom' : None},
        'SPP' : {'company_id' : 17166, 'UNIQUE_ID' : None, 'geom' : None},
        'CISO' : {'company_id' : 99999, 'UNIQUE_ID' : None, 'geom' : None},
        'BPA' : {'company_id' : 1738, 'UNIQUE_ID' : None, 'geom' : None},
        'WALC' : {'company_id' : 19610, 'UNIQUE_ID' : None, 'geom' : None},
        'WACM' : {'company_id' : 28503, 'UNIQUE_ID' : None, 'geom' : None},
        'TSGTCW' : {'company_id' : 99998, 'UNIQUE_ID' : None, 'geom' : None},
        'TSGTNM' : {'company_id' : 99997, 'UNIQUE_ID' : None, 'geom' : None},
        'MMWE' : {'company_id' : 11806, 'UNIQUE_ID' : None, 'geom' : None},
        'NEPOOL' : {'company_id' : 13435, 'UNIQUE_ID' : None, 'geom' : None},
        'NYISO' : {'company_id' : 13501, 'UNIQUE_ID' : None, 'geom' : None},
        'NU' : {'company_id' : 13556, 'UNIQUE_ID' : None, 'geom' : None},
        'SOCO' : {'company_id' : 18195, 'UNIQUE_ID' : None, 'geom' : None},
        'OTP' : {'company_id' : 13994, 'UNIQUE_ID' : None, 'geom' : None},
        }

#TODO
# NPCC
#util_to_eia.loc[, 'company_id'] = 11806     #Mass. Muni Wholesale # Contains Multiple *
#util_to_eia.loc[ , 'company_id'] = 13435     #New England Power Pool/NE ISO *
#util_to_eia.loc[ , 'company_id'] = 13501     #New York Power Pool/NY ISO *
#util_to_eia.loc[ , 'company_id'] = 13556     #Northeast Utilities # (HOLD_CO) 

#SERC
#util_to_eia.loc[, 'company_id'] = 18195     #Southern Company (CTRL_AREA)
#util_to_eia.loc[, 'company_id'] = 13994     #Oglethorp Power Corp (PLAN_AREA)
#util_to_eia.loc[, 'company_id'] = 3046     #Carolina P&L/Progress Energy Carolina
#util_to_eia.loc[, 'company_id'] = 924     #Associated Electric Coop
#util_to_eia.loc[, 'company_id'] = 40218     #Central Electric Power Coop (PLAN_AREA)
#util_to_eia.loc[, 'company_id'] = 17568     #South Mississippi El. Pow. Assoc. (CTRL/PLAN_AREA)
#util_to_eia.loc[, 'company_id'] = 189     #Alabama Electric Coop #POWERSOUTH?
#util_to_eia.loc[, 'company_id'] = 40229     #Old Dominion #VA | #DE,MA
#

#ECAR
#util_to_eia.loc[, 'company_id'] = 5580     #East Kentucky Power Coop
#util_to_eia.loc[, 'company_id'] = 7004     #Buckeye (PLAN_AREA)
#util_to_eia.loc[, 'company_id'] = 40577     #American Municipal Power OH
#util_to_eia.loc[, 'company_id'] = 1692     #Big Rivers Electric Corp: Members are Jackson Purchase Energy Corporation, Kenergy Corporation, and Meade County Rural Electric Cooperative Corporation.
#util_to_eia.loc[, 'company_id'] = 829     #American Electric Power
#util_to_eia.loc[, 'company_id'] =      #FirstEnergy (HOLD_CO)

#MAIN
#util_to_eia.loc[, 'company_id'] = 20858     #Wisconsin Public Power #WPPI Energy (PLAN_AREA)

#MAAC
#util_to_eia.loc[, 'company_id'] = 14725     #PJM
#util_to_eia.loc[, 'company_id'] = 7088     #General Public Utilities # Part of First Energy # Contains Jersey Central Power and Light; Pennsylvania Electric Company (Penelec); Metropolitan Edison (Met-Ed)

#SPP
#util_to_eia.loc[, 'company_id'] = 20447     #Western Farmer's Electric Coop (CTRL|PLAN_AREA)
#util_to_eia.loc[, 'company_id'] = 12506     #Entergy System Power Pool (CTRL|PLAN AREA)
#util_to_eia.loc[, 'company_id'] = 14077     #Oklahoma Muni Power Auth
#util_to_eia.loc[, 'company_id'] = 7349     #Golden Spread
#util_to_eia.loc[, 'company_id'] = 18315     #Sunflower Electric Power Corp
#util_to_eia.loc[, 'company_id'] = 2777     #Cajun Electric Power Coop # Probably Louisiana Generating LLC
#util_to_eia.loc[, 'company_id'] = 3283     #Central and SouthWest Serv # American Electric Power West
#util_to_eia.loc[, 'company_id'] = 26253     #LA Energy and Power Authority

#FRCC
#util_to_eia.loc[, 'company_id'] = 6567     #Florida Municipal Power Agency

# ERCOT
#util_to_eia.loc[, 'company_id'] = 13670     #Northeast Texas Elec Coop
#util_to_eia.loc[, 'company_id'] = 40233     #Sam Rayburn
#util_to_eia.loc[, 'company_id'] = 18679    #Tex La Elec Coop

#MAPP
#util_to_eia.loc[, 'company_id'] = 12658     #Minnkota Power Coop Inc
#util_to_eia.loc[, 'company_id'] = 20858     #Wisconsin Public Power Inc # Also in MAIN
#TODO

###### WECC
# AEPC

multi_d['AEPC']['UNIQUE_ID'] = 9990
multi_d['AEPC']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[[1, 106, 108, 109, 1130, 2111]].dropna().reset_index().set_index('company_id')
multi_d['AEPC']['census'].index = np.repeat(multi_d['AEPC']['company_id'], len(multi_d['AEPC']['census']))
multi_d['AEPC']['census']['UNIQUE_ID'] = multi_d['AEPC']['UNIQUE_ID']
multi_d['AEPC']['geom'] = utility[utility['UNIQUE_ID'].isin([1, 106, 108, 109, 1130, 2111])].unary_union
multi_d['AEPC']['comp_UID'] = [1, 106, 108, 109, 1130, 2111]

util_to_eia.loc[multi_d['AEPC']['UNIQUE_ID']] = [100, multi_d['AEPC']['company_id'], 'Arizona Electric Power Cooperative', 'Arizona Electric Power Cooperative']
util_to_c = pd.concat([util_to_c, multi_d['AEPC']['census']])
multi_d['AEPC']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['AEPC']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['AEPC']['ua']['UNIQUE_ID'] = multi_d['AEPC']['UNIQUE_ID'] 
multi_d['AEPC']['ua']['eia_code'] = multi_d['AEPC']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['AEPC']['ua']])

# Platte River Power Authority

multi_d['PRPA']['UNIQUE_ID'] = 9991
multi_d['PRPA']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['PLAN_AREA'].str.contains('Platte River')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['PRPA']['census'].index = np.repeat(multi_d['PRPA']['company_id'], len(multi_d['PRPA']['census']))
multi_d['PRPA']['census']['UNIQUE_ID'] = multi_d['PRPA']['UNIQUE_ID']
multi_d['PRPA']['geom'] = utility[utility['PLAN_AREA'].str.contains('Platte River')].unary_union
multi_d['PRPA']['comp_UID'] = utility[utility['PLAN_AREA'].str.contains('Platte River')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['PRPA']['UNIQUE_ID']] = [100, multi_d['PRPA']['company_id'], 'Platte River Power Authority', 'Platte River Power Authority']
util_to_c = pd.concat([util_to_c, multi_d['PRPA']['census']])
multi_d['PRPA']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['PRPA']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['PRPA']['ua']['UNIQUE_ID'] = multi_d['PRPA']['UNIQUE_ID'] 
multi_d['PRPA']['ua']['eia_code'] = multi_d['PRPA']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['PRPA']['ua']])

# CAISO

multi_d['CISO']['UNIQUE_ID'] = 9992
multi_d['CISO']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('California Independent System Operator')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['CISO']['census'].index = np.repeat(multi_d['CISO']['company_id'], len(multi_d['CISO']['census']))
multi_d['CISO']['census']['UNIQUE_ID'] = multi_d['CISO']['UNIQUE_ID']
multi_d['CISO']['geom'] = utility[utility['CTRL_AREA'].str.contains('California Independent System Operator')].unary_union
multi_d['CISO']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('California Independent System Operator')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['CISO']['UNIQUE_ID']] = [100, multi_d['CISO']['company_id'], 'California ISO', 'California ISO']
util_to_c = pd.concat([util_to_c, multi_d['CISO']['census']])
multi_d['CISO']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['CISO']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['CISO']['ua']['UNIQUE_ID'] = multi_d['CISO']['UNIQUE_ID'] 
multi_d['CISO']['ua']['eia_code'] = multi_d['CISO']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['CISO']['ua']])

# Bonneville Power Administration
# No Fit?
multi_d['BPA']['UNIQUE_ID'] = 9993
multi_d['BPA']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Bonneville')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['BPA']['census'].index = np.repeat(multi_d['BPA']['company_id'], len(multi_d['BPA']['census']))
multi_d['BPA']['census']['UNIQUE_ID'] = multi_d['BPA']['UNIQUE_ID']
multi_d['BPA']['geom'] = utility[utility['CTRL_AREA'].str.contains('Bonneville')].unary_union
multi_d['BPA']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Bonneville')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['BPA']['UNIQUE_ID']] = [100, multi_d['BPA']['company_id'], 'Bonneville Power Administration', 'Bonneville Power Administration']
util_to_c = pd.concat([util_to_c, multi_d['BPA']['census']])
multi_d['BPA']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['BPA']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['BPA']['ua']['UNIQUE_ID'] = multi_d['BPA']['UNIQUE_ID'] 
multi_d['BPA']['ua']['eia_code'] = multi_d['BPA']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['BPA']['ua']])

# WAPA Desert Southwest
# No fit
multi_d['WALC']['UNIQUE_ID'] = 9994
multi_d['WALC']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('WAPA Desert')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['WALC']['census'].index = np.repeat(multi_d['WALC']['company_id'], len(multi_d['WALC']['census']))
multi_d['WALC']['census']['UNIQUE_ID'] = multi_d['WALC']['UNIQUE_ID']
multi_d['WALC']['geom'] = utility[utility['CTRL_AREA'].str.contains('WAPA Desert')].unary_union
multi_d['WALC']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('WAPA Desert')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['WALC']['UNIQUE_ID']] = [100, multi_d['WALC']['company_id'], 'WAPA Desert Southwest', 'WAPA Desert Southwest']
util_to_c = pd.concat([util_to_c, multi_d['WALC']['census']])
multi_d['WALC']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['WALC']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['WALC']['ua']['UNIQUE_ID'] = multi_d['WALC']['UNIQUE_ID'] 
multi_d['WALC']['ua']['eia_code'] = multi_d['WALC']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['WALC']['ua']])

# WAPA Rocky Mountain
# No fit

multi_d['WACM']['UNIQUE_ID'] = 9995
multi_d['WACM']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('WAPA Rocky')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['WACM']['census'].index = np.repeat(multi_d['WACM']['company_id'], len(multi_d['WACM']['census']))
multi_d['WACM']['census']['UNIQUE_ID'] = multi_d['WACM']['UNIQUE_ID']
multi_d['WACM']['geom'] = utility[utility['CTRL_AREA'].str.contains('WAPA Rocky')].unary_union
multi_d['WACM']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('WAPA Rocky')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['WACM']['UNIQUE_ID']] = [100, multi_d['WACM']['company_id'], 'WAPA Desert Southwest', 'WAPA Desert Southwest']
util_to_c = pd.concat([util_to_c, multi_d['WACM']['census']])
multi_d['WACM']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['WACM']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['WACM']['ua']['UNIQUE_ID'] = multi_d['WACM']['UNIQUE_ID'] 
multi_d['WACM']['ua']['eia_code'] = multi_d['WACM']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['WACM']['ua']])

# Tri-state generation (CO and WY)

TSGTCW_ID = [1598, 24, 988, 1318, 820, 1222, 1673, 551, 1320, 677, 978, 1562, 1753, 462, 763, 3116, 1164, 775, 606, 10, 17, 1644, 1599, 12, 15, 1554, 1096, 1145, 1717, 9, 1253]

multi_d['TSGTCW']['UNIQUE_ID'] = 9996
multi_d['TSGTCW']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('WAPA Rocky')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['TSGTCW']['census'].index = np.repeat(multi_d['TSGTCW']['company_id'], len(multi_d['TSGTCW']['census']))
multi_d['TSGTCW']['census']['UNIQUE_ID'] = multi_d['TSGTCW']['UNIQUE_ID']
multi_d['TSGTCW']['geom'] = utility[utility['UNIQUE_ID'].isin(TSGTCW_ID)].unary_union
multi_d['TSGTCW']['comp_UID'] = TSGTCW_ID

util_to_eia.loc[multi_d['TSGTCW']['UNIQUE_ID']] = [100, multi_d['TSGTCW']['company_id'], 'Tri State Generation CO WY', 'Tri State Generation CO WY']
util_to_c = pd.concat([util_to_c, multi_d['TSGTCW']['census']])
multi_d['TSGTCW']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['TSGTCW']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['TSGTCW']['ua']['UNIQUE_ID'] = multi_d['TSGTCW']['UNIQUE_ID'] 
multi_d['TSGTCW']['ua']['eia_code'] = multi_d['TSGTCW']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['TSGTCW']['ua']])

# Tri-state generation (NM)

TSGTNM_ID = [311, 308, 315, 532, 317, 319, 318, 2172, 1003, 1147, 309, 321, 1094]

multi_d['TSGTNM']['UNIQUE_ID'] = 9997
multi_d['TSGTNM']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('WAPA Rocky')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['TSGTNM']['census'].index = np.repeat(multi_d['TSGTNM']['company_id'], len(multi_d['TSGTNM']['census']))
multi_d['TSGTNM']['census']['UNIQUE_ID'] = multi_d['TSGTNM']['UNIQUE_ID']
multi_d['TSGTNM']['geom'] = utility[utility['UNIQUE_ID'].isin(TSGTNM_ID)].unary_union
multi_d['TSGTNM']['comp_UID'] = TSGTNM_ID

util_to_eia.loc[multi_d['TSGTNM']['UNIQUE_ID']] = [100, multi_d['TSGTNM']['company_id'], 'Tri State Generation CO WY', 'Tri State Generation CO WY']
util_to_c = pd.concat([util_to_c, multi_d['TSGTNM']['census']])
multi_d['TSGTNM']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['TSGTNM']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['TSGTNM']['ua']['UNIQUE_ID'] = multi_d['TSGTNM']['UNIQUE_ID'] 
multi_d['TSGTNM']['ua']['eia_code'] = multi_d['TSGTNM']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['TSGTNM']['ua']])

# # APS
# # NEED TO TAKE CARE OF EXISTING APS
# multi_d['APS']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Arizona Public Service Co')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['APS']['census'].index = np.repeat(803, len(multi_d['APS']['census']))
# multi_d['APS']['census']['UNIQUE_ID'] = 9991
# multi_d['APS']['UNIQUE_ID'] = 9991
# multi_d['APS']['geom'] = utility[utility['CTRL_AREA'].str.contains('Arizona Public Service Co')].unary_union
# multi_d['APS']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Arizona Public Service Co')]['UNIQUE_ID'].unique().tolist()

# util_to_c = pd.concat([util_to_c, multi_d['APS']['census']])

# # TEP
# # NEED TO TAKE CARE OF EXISTING TEP
# multi_d['TEP']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Tucson')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['TEP']['census'].index = np.repeat(24211, len(multi_d['TEP']['census']))
# multi_d['TEP']['UNIQUE_ID'] = 9992
# multi_d['TEP']['geom'] = utility[utility['CTRL_AREA'].str.contains('Tucson')].unary_union
# multi_d['TEP']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Tucson')]['UNIQUE_ID'].unique().tolist()

# # SRP
# # NEED TO TAKE CARE OF EXISTING SRP
# multi_d['SRP']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Salt River')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['SRP']['census'].index = np.repeat(16572, len(multi_d['SRP']['census']))
# multi_d['SRP']['UNIQUE_ID'] = 9993
# multi_d['SRP']['geom'] = utility[utility['CTRL_AREA'].str.contains('Salt River')].unary_union
# multi_d['SRP']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Salt River')]['UNIQUE_ID'].unique().tolist()

# # Public Service Co of NM
# # NEED TO TAKE CARE OF EXISTING PNM
# multi_d['PNM']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Public Service Co of New Mexico')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['PNM']['census'].index = np.repeat(15473, len(multi_d['PNM']['census']))
# multi_d['PNM']['UNIQUE_ID'] = 9994
# multi_d['PNM']['geom'] = utility[utility['CTRL_AREA'].str.contains('Public Service Co of New Mexico')].unary_union
# multi_d['PNM']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Public Service Co of New Mexico')]['UNIQUE_ID'].unique().tolist()

# # Public Service Co of CO
# # NEED TO TAKE CARE OF EXISTING PSC
# multi_d['PSC']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Public Service Co of Colorado')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['PSC']['census'].index = np.repeat(15466, len(multi_d['PSC']['census']))
# multi_d['PSC']['UNIQUE_ID'] = 9995
# multi_d['PSC']['geom'] = utility[utility['CTRL_AREA'].str.contains('Public Service Co of Colorado')].unary_union
# multi_d['PSC']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Public Service Co of Colorado')]['UNIQUE_ID'].unique().tolist()

# # Avista
# # NEED TO TAKE CARE OF EXISTING AVISTA
# multi_d['AVA']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Avista')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['AVA']['census'].index = np.repeat(20169, len(multi_d['AVA']['census']))
# multi_d['AVA']['UNIQUE_ID'] = 9996
# multi_d['AVA']['geom'] = utility[utility['CTRL_AREA'].str.contains('Avista')].unary_union
# multi_d['AVA']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Avista')]['UNIQUE_ID'].unique().tolist()

# # Sierra Pacific
# # NEED TO TAKE CARE OF EXISTING SPP
# multi_d['SPP']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Sierra Pacific')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
# multi_d['SPP']['census'].index = np.repeat(17166, len(multi_d['SPP']['census']))
# multi_d['SPP']['UNIQUE_ID'] = 9998
# multi_d['SPP']['geom'] = utility[utility['CTRL_AREA'].str.contains('Sierra Pacific')].unary_union
# multi_d['SPP']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Sierra Pacific')]['UNIQUE_ID'].unique().tolist()

###### NPCC
# MMWE 

multi_d['MMWE']['UNIQUE_ID'] = 9998
multi_d['MMWE']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['PLAN_AREA'].str.contains('Massachusetts Municipal')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['MMWE']['census'].index = np.repeat(multi_d['MMWE']['company_id'], len(multi_d['MMWE']['census']))
multi_d['MMWE']['census']['UNIQUE_ID'] = multi_d['MMWE']['UNIQUE_ID']
multi_d['MMWE']['geom'] = utility[utility['PLAN_AREA'].str.contains('Massachusetts Municipal')].unary_union
multi_d['MMWE']['comp_UID'] = utility[utility['PLAN_AREA'].str.contains('Massachusetts Municipal')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['MMWE']['UNIQUE_ID']] = [100, multi_d['MMWE']['company_id'], 'Mass Muni Wholesale', 'Mass Muni Wholesale']
util_to_c = pd.concat([util_to_c, multi_d['MMWE']['census']])
multi_d['MMWE']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['MMWE']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['MMWE']['ua']['UNIQUE_ID'] = multi_d['MMWE']['UNIQUE_ID'] 
multi_d['MMWE']['ua']['eia_code'] = multi_d['MMWE']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['MMWE']['ua']])

# NEPOOL 

multi_d['NEPOOL']['UNIQUE_ID'] = 9999
multi_d['NEPOOL']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['PLAN_AREA'].str.contains('New England ISO')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['NEPOOL']['census'].index = np.repeat(multi_d['NEPOOL']['company_id'], len(multi_d['NEPOOL']['census']))
multi_d['NEPOOL']['census']['UNIQUE_ID'] = multi_d['NEPOOL']['UNIQUE_ID']
multi_d['NEPOOL']['geom'] = utility[utility['PLAN_AREA'].str.contains('New England ISO')].unary_union
multi_d['NEPOOL']['comp_UID'] = utility[utility['PLAN_AREA'].str.contains('New England ISO')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['NEPOOL']['UNIQUE_ID']] = [100, multi_d['NEPOOL']['company_id'], 'Mass Muni Wholesale', 'Mass Muni Wholesale']
util_to_c = pd.concat([util_to_c, multi_d['NEPOOL']['census']])
multi_d['NEPOOL']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['NEPOOL']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['NEPOOL']['ua']['UNIQUE_ID'] = multi_d['NEPOOL']['UNIQUE_ID'] 
multi_d['NEPOOL']['ua']['eia_code'] = multi_d['NEPOOL']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['NEPOOL']['ua']])

# NYISO 

multi_d['NYISO']['UNIQUE_ID'] = 9909
multi_d['NYISO']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('New York ISO')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['NYISO']['census'].index = np.repeat(multi_d['NYISO']['company_id'], len(multi_d['NYISO']['census']))
multi_d['NYISO']['census']['UNIQUE_ID'] = multi_d['NYISO']['UNIQUE_ID']
multi_d['NYISO']['geom'] = utility[utility['CTRL_AREA'].str.contains('New York ISO')].unary_union
multi_d['NYISO']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('New York ISO')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['NYISO']['UNIQUE_ID']] = [100, multi_d['NYISO']['company_id'], 'Mass Muni Wholesale', 'Mass Muni Wholesale']
util_to_c = pd.concat([util_to_c, multi_d['NYISO']['census']])
multi_d['NYISO']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['NYISO']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['NYISO']['ua']['UNIQUE_ID'] = multi_d['NYISO']['UNIQUE_ID'] 
multi_d['NYISO']['ua']['eia_code'] = multi_d['NYISO']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['NYISO']['ua']])

# NU 

multi_d['NU']['UNIQUE_ID'] = 9919
multi_d['NU']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['HOLD_CO'].str.contains('Northeast Util')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['NU']['census'].index = np.repeat(multi_d['NU']['company_id'], len(multi_d['NU']['census']))
multi_d['NU']['census']['UNIQUE_ID'] = multi_d['NU']['UNIQUE_ID']
multi_d['NU']['geom'] = utility[utility['HOLD_CO'].str.contains('Northeast Util')].unary_union
multi_d['NU']['comp_UID'] = utility[utility['HOLD_CO'].str.contains('Northeast Util')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['NU']['UNIQUE_ID']] = [100, multi_d['NU']['company_id'], 'Mass Muni Wholesale', 'Mass Muni Wholesale']
util_to_c = pd.concat([util_to_c, multi_d['NU']['census']])
multi_d['NU']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['NU']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['NU']['ua']['UNIQUE_ID'] = multi_d['NU']['UNIQUE_ID'] 
multi_d['NU']['ua']['eia_code'] = multi_d['NU']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['NU']['ua']])

###### SERC

# SOCO
multi_d['SOCO']['UNIQUE_ID'] = 9929
multi_d['SOCO']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['CTRL_AREA'].str.contains('Southern Co')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['SOCO']['census'].index = np.repeat(multi_d['SOCO']['company_id'], len(multi_d['SOCO']['census']))
multi_d['SOCO']['census']['UNIQUE_ID'] = multi_d['SOCO']['UNIQUE_ID']
multi_d['SOCO']['geom'] = utility[utility['CTRL_AREA'].str.contains('Southern Co')].unary_union
multi_d['SOCO']['comp_UID'] = utility[utility['CTRL_AREA'].str.contains('Southern Co')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['SOCO']['UNIQUE_ID']] = [100, multi_d['SOCO']['company_id'], 'Mass Muni Wholesale', 'Mass Muni Wholesale']
util_to_c = pd.concat([util_to_c, multi_d['SOCO']['census']])
multi_d['SOCO']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['SOCO']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['SOCO']['ua']['UNIQUE_ID'] = multi_d['SOCO']['UNIQUE_ID'] 
multi_d['SOCO']['ua']['eia_code'] = multi_d['SOCO']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['SOCO']['ua']])

#OTP
multi_d['OTP']['UNIQUE_ID'] = 9939
multi_d['OTP']['census'] = util_to_c.reset_index().set_index('UNIQUE_ID').loc[utility[utility['PLAN_AREA'].str.contains('Oglethorp')]['UNIQUE_ID'].values.astype(int)].dropna().reset_index().set_index('company_id')
multi_d['OTP']['census'].index = np.repeat(multi_d['OTP']['company_id'], len(multi_d['OTP']['census']))
multi_d['OTP']['census']['UNIQUE_ID'] = multi_d['OTP']['UNIQUE_ID']
multi_d['OTP']['geom'] = utility[utility['PLAN_AREA'].str.contains('Oglethorp')].unary_union
multi_d['OTP']['comp_UID'] = utility[utility['PLAN_AREA'].str.contains('Oglethorp')]['UNIQUE_ID'].unique().tolist()

util_to_eia.loc[multi_d['OTP']['UNIQUE_ID']] = [100, multi_d['OTP']['company_id'], 'Mass Muni Wholesale', 'Mass Muni Wholesale']
util_to_c = pd.concat([util_to_c, multi_d['OTP']['census']])
multi_d['OTP']['ua'] = dem_ua[dem_ua['UNIQUE_ID'].isin(multi_d['OTP']['comp_UID'])].drop_duplicates(subset=['UACE10'])
multi_d['OTP']['ua']['UNIQUE_ID'] = multi_d['OTP']['UNIQUE_ID'] 
multi_d['OTP']['ua']['eia_code'] = multi_d['OTP']['company_id'] 
dem_ua = pd.concat([dem_ua, multi_d['OTP']['ua']])


################################################################################

def cat_load_census(idno):
    u = util_to_c.loc[idno]
    cT = pop_yrs.loc[u['GEOID'].values].sum()
    cT.index = cT.index.to_datetime()
    cT = cT.resample('M').interpolate()
    cT.name = 'pop'

    demdata = []

    for m in dem_d.keys():
        if m.split('_')[0] in ('lforce', 'occ'):
            dT = dem_d[m].loc[u['GEOID'].values].sum()
        elif m.split('_')[0] in ('vint', 'mHHI'):
            dT = dem_d[m].loc[u['GEOID'].values].median()
        dT.index = dT.index.to_datetime()
        dT = dT.resample('M').interpolate()
        dT.name = m
        demdata.append(dT)

    demdata = pd.concat(demdata, axis=1)

    nonames = {99999 : 'ciso', 99998 : 'tsgtcw', 99997 : 'tsgtnm'}
    if idno in nonames.keys():
        c_load = pd.read_csv('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s' % (homedir, nonames[idno]), index_col=0, parse_dates=True)
    else:
        c_load = pd.read_csv('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (homedir, idno), index_col=0, parse_dates=True)
    c_load = c_load.resample('M').interpolate()

    cat = pd.concat([cT, c_load, demdata], axis=1)
    return cat

def plot_curvefit(xdata, ydata):
    xy = np.vstack([xdata,ydata])
    z = scipy.stats.gaussian_kde(xy)(xy)
    plt.scatter(xdata, ydata, c=z, s=100, edgecolor='')

def curve_type(x, a, b, c):
    return abs(a*x**2) + b*x + c

def fit_data_no_linreg(idno, plot_output=False):
    data = cat_load_census(idno)[['load', 'pop', 'lforce_001', 'mHHI_001']].dropna()
    data = data[data.index.year!=2005]
    datasummer = data[np.in1d(data.index.month, [6,7,8])]

    nonames = {99999 : 'ciso', 99998 : 'tsgtcw', 99997 : 'tsgtnm'}
    if idno in nonames.keys():
        c_load = pd.read_csv('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s' % (homedir, nonames[idno]), index_col=0, parse_dates=True)
    else:
        c_load = pd.read_csv('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc/%s.csv' % (homedir, idno), index_col=0, parse_dates=True)
    c_load = c_load.groupby(c_load.index.date).max()

    norm_load = (1000000*c_load['load']/(data['pop'].reindex_like(c_load).interpolate())).dropna()
    norm_load.index = pd.to_datetime(norm_load.index)
    norm_load = norm_load[np.in1d(norm_load.index.month, [6,7,8])]

#    dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

    dem_util = dem_ua.set_index('eia_code').sort_index().loc[idno]

    util_d = {}
    hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

    if isinstance(dem_util, pd.DataFrame):
        for i in range(len(dem_util.index)):
            data_name = dem_util.iloc[i]['grid_cell']
            lat = float(data_name.split('_')[1])
            lon = float(data_name.split('_')[2])
            pop = int(dem_util.iloc[i]['POP'])
            if data_name in os.listdir(hist_path):
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            else:
                lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
                lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
                latlons = pd.DataFrame(np.column_stack([lats, lons]))
                newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
                data_name = 'data_%s_%s' % (newdata[0], newdata[1])
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
            df = df[np.in1d(df.index.month, [6,7,8])]
            if not data_name in util_d.keys():
                util_d.update({data_name : {}})
                util_d[data_name].update({'pop' : pop})
                util_d[data_name].update({'data' : df})
            else:
                util_d[data_name]['pop'] += pop
    elif isinstance(dem_util, pd.Series):
        data_name = dem_util['grid_cell']
        lat = float(data_name.split('_')[1])
        lon = float(data_name.split('_')[2])
        pop = int(dem_util['POP'])
        if data_name in os.listdir(hist_path):
            df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        else:
            lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
            lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
            latlons = pd.DataFrame(np.column_stack([lats, lons]))
            newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
            data_name = 'data_%s_%s' % (newdata[0], newdata[1])
            df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
        df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
        df = df[np.in1d(df.index.month, [6,7,8])]
        if not data_name in util_d.keys():
            util_d.update({data_name : {}})
            util_d[data_name].update({'pop' : pop})
            util_d[data_name].update({'data' : df})
        else:
            util_d[data_name]['pop'] += pop

    totpop = sum([util_d[i]['pop'] for i in util_d.keys()])
    tempcat = pd.concat([util_d[i]['pop']*util_d[i]['data'] for i in util_d.keys()], axis=1)
    if isinstance(tempcat[4], pd.DataFrame):
        tmax = tempcat[4].sum(axis=1)/totpop
        tmin = tempcat[5].sum(axis=1)/totpop
    elif isinstance(tempcat[4], pd.Series):
        tmax = tempcat[4]/totpop
        tmin = tempcat[5]/totpop

    peak = pd.concat([norm_load, tmax], axis=1).dropna()
    peak = peak[peak.index.weekday <= 4]    #BUSINESS DAYS ONLY
    if idno in man_fixes:
        peak = peak.loc[man_fixes[idno][0]:man_fixes[idno][1]]

    # linreg = scipy.stats.linregress(peak[1], peak[0])
    # coeffs = np.polyfit(peak[1].values, peak[0].values, 2)

    x = peak[1].values
    y = peak[0].values

    coeffs = curve_fit(curve_type, x, y)[0]

    # p = np.poly1d(coeffs)
    p = curve_type
    s = p(x, *coeffs)
    R_2 = 1 - sum((s-y)**2)/sum((y-np.mean(y))**2)

    if plot_output:
        # linreg = scipy.stats.linregress(peak[1], peak[0])
        
        fig, ax = plt.subplots(1)
        plot_curvefit(peak[1], peak[0])
        x_mm = np.linspace(x.min(), x.max())
        plt.plot(x_mm, p(x_mm, *coeffs))
    
        util_name = util_to_eia.dropna().set_index('company_id').loc[idno, 'utility_name']
        plt.title('%s, %s' % (util_name, idno))
        plt.ylabel('Load (W per capita)')
        plt.xlabel('Air Temperature ($^\circ$C)')
        textstr = '$\\alpha=%.2f$\n$\\beta=%.2f$\n$\\gamma=%.2f$\n$n=%s$\n$r2=%.2f$' % (coeffs[0], coeffs[1], coeffs[2],  len(peak), R_2)
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', linespacing=1.25, bbox=props)
        plt.savefig('%s.png' % (idno), bbox_inches='tight')
        plt.clf()
    
    return coeffs, R_2


man_fixes = {
        3413 : ('1993', '2000'),
        5326 : ('2000', None),
        5701 : ('1993', '2004'),
        14328 : ('1997', None),
        14354 : ('1999', '2004'),
        15466 : ('1993', '2001'),
        15473 : ('1993', '2004'),
        17166 : ('1998', None),
        19281 : ('1993', '2004'),
        19545 : ('1997', '2004'),
        20169 : ('2006', '2010'),
        24211 : ('1993', '2004'),
        796 : ('1999', '2004'),
        1738 : ('2002', None),
        19610 : ('2001', '2007'),
        28503 : ('1993', '1996'),
        15143 : ('1998', None)
        }

reg_d = {}

readlist = [int(i.split('.')[0]) for i in os.listdir('%s/github/RIPS_kircheis/RIPS/data/hourly_load/wecc' % homedir) if i.endswith('csv')] + [99999, 99998, 99997]

for i in readlist:
#    i = int(fn.split('.')[0])
    try:
        reg_d.update({i : fit_data_no_linreg(i, plot_output=True)})
    except:
        print(i)


#### Future projections

import netCDF4


def project_reg_vect(yr, idno):

    nc = call_reg.nc
    dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

    latpos = pd.Series(np.arange(len(nc[yr].variables['latitude'][:])), index=nc[yr].variables['latitude'][:])
    lonpos = pd.Series(np.arange(len(nc[yr].variables['longitude'][:])), index=nc[yr].variables['longitude'][:] - 360)
    latlon = pd.Series(dem_ua['grid_cell'].dropna().unique()).str.split('_').str[1:].apply(pd.Series).astype(float)
    latlonix = pd.concat([latpos[latlon[0].values].reset_index(), lonpos[latlon[1].values].reset_index()], axis=1).dropna()
    latlonix.columns = ['lat', 'latix', 'lon', 'lonix']
    latlonix['latix'] = latlonix['latix'].astype(int)
    latlonix['lonix'] = latlonix['lonix'].astype(int)
    latlonix['lat'] = latlonix['lat'].astype(str)
    latlonix['lon'] = latlonix['lon'].astype(str)

    cat = np.ma.filled(nc[yr].variables['tasmax'][:,:,:], np.iinfo(np.int32).min)[:, latlonix['latix'].values, latlonix['lonix'].values]
    cat[cat == cat.min()] = np.nan

    outdf = pd.DataFrame()

    for code_n in idno:
        dem_util = dem_ua.set_index('eia_code').sort_index().loc[code_n]
        data_name = pd.Series(dem_util['grid_cell'])
        util_ll = data_name.str.split('_').str[1:].apply(pd.Series)
        util_ll.columns = ['lat', 'lon']
        util_ll = pd.merge(util_ll, latlonix.reset_index(), on=['lat', 'lon'])
        pop = dem_util['POP'] 
        if dem_util.ndim > 1:
            nantest = np.isnan(cat[:, util_ll['index'].values][0])
            if nantest.any():
                nanpos = np.where(nantest)[0]
                pop.iloc[nanpos] = np.nan
            projtemp = np.nansum((cat[:, util_ll['index'].values] * pop.values), axis=1)/pop.sum()
        else:
            projtemp = cat[:, util_ll['index'].values].ravel()
        outdf[code_n] = projtemp

    outdf.index = pd.date_range(start=datetime.date(yr, 1, 1), freq='d', periods=len(outdf))
    return outdf


idno = [int(i.split('.')[0]) for i in os.listdir('%s/Dropbox/NSF WSC AZ WEN Team Share/Electricity Demand/plots' % homedir)]


def call_reg(model, scen, directory):
    call_reg.nc = {}
    curdir = '%s/%s/%s' % (directory, model, scen)
    for fn in os.listdir(curdir):
        call_reg.nc.update({ int(fn.split('_')[-1].split('-')[0][:4]) : netCDF4.Dataset('%s/%s' % (curdir, fn))})
    for y in call_reg.nc.keys():
        project_reg_vect(y, idno).to_csv('%s-%s-%s' % (model, scen, y))
        call_reg.nc[y].close()

default_dir = '%s/CMIP5' % homedir

for subdir in os.listdir(default_dir):
    scendir = '%s/%s' % (default_dir, subdir)
    for sc in ['rcp26', 'rcp45', 'rcp85']:
        if sc in os.listdir(scendir):
            call_reg(subdir, sc, default_dir)


historical_dir = '%s/temp_regression/historical/hist_util_temps' % (homedir)
projection_dir = '%s/temp_regression/projection' % (homedir)

def combine_scenario(model, scenario, histpath, projdir):
    proj_li = []
    hist_df = pd.read_csv(histpath, index_col=0)
    for i in os.listdir(projdir):
        if ('%s-%s' % (model, scenario)) in i:
            proj_li.append(pd.read_csv('%s/%s' % (projdir, i), index_col=0))
    out_df = pd.concat(proj_li)
    out_df = pd.concat([hist_df, out_df]).sort_index()
    out_df.index = pd.to_datetime(out_df.index)
    out_df.columns = np.asarray(out_df.columns).astype(int)
    return out_df

def util_hist_temp(idno):

    out_df = pd.DataFrame()

    dem_ua = pd.read_csv('%s/github/RIPS_kircheis/data/util_demand_to_met_ua' % homedir)

    for code_n in idno:
        dem_util = dem_ua.set_index('eia_code').sort_index().loc[code_n]

        util_d = {}
        hist_path = '/home/chesterlab/Bartos/pre/source_hist_forcings/master'

        if isinstance(dem_util, pd.DataFrame):
            for i in range(len(dem_util.index)):
                data_name = dem_util.iloc[i]['grid_cell']
                lat = float(data_name.split('_')[1])
                lon = float(data_name.split('_')[2])
                pop = int(dem_util.iloc[i]['POP'])
                if data_name in os.listdir(hist_path):
                    df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
                else:
                    lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
                    lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
                    latlons = pd.DataFrame(np.column_stack([lats, lons]))
                    newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
                    data_name = 'data_%s_%s' % (newdata[0], newdata[1])
                    df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
                df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
                if not data_name in util_d.keys():
                    util_d.update({data_name : {}})
                    util_d[data_name].update({'pop' : pop})
                    util_d[data_name].update({'data' : df})
                else:
                    util_d[data_name]['pop'] += pop
        elif isinstance(dem_util, pd.Series):
            data_name = dem_util['grid_cell']
            lat = float(data_name.split('_')[1])
            lon = float(data_name.split('_')[2])
            pop = int(dem_util['POP'])
            if data_name in os.listdir(hist_path):
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            else:
                lats = np.asarray([float(i.split('_')[1]) for i in os.listdir(hist_path)])
                lons = np.asarray([float(i.split('_')[2]) for i in os.listdir(hist_path)])
                latlons = pd.DataFrame(np.column_stack([lats, lons]))
                newdata = latlons.loc[latlons.apply(lambda x: ((x[0] - lat)**2 + (x[1] - lon)**2)**0.5, axis=1).idxmin()]
                data_name = 'data_%s_%s' % (newdata[0], newdata[1])
                df = pd.read_csv('%s/%s' % (hist_path, data_name), sep='\t', header=None)[[4,5]]
            df.index = pd.date_range(start=datetime.date(1949, 1, 1), freq='d', periods=len(df))
            if not data_name in util_d.keys():
                util_d.update({data_name : {}})
                util_d[data_name].update({'pop' : pop})
                util_d[data_name].update({'data' : df})
            else:
                util_d[data_name]['pop'] += pop

        totpop = sum([util_d[i]['pop'] for i in util_d.keys()])
        tempcat = pd.concat([util_d[i]['pop']*util_d[i]['data'] for i in util_d.keys()], axis=1)
        if isinstance(tempcat[4], pd.DataFrame):
            tmax = tempcat[4].sum(axis=1)/totpop
        elif isinstance(tempcat[4], pd.Series):
            tmax = tempcat[4]/totpop
        out_df[code_n] = tmax
    return out_df.sort_index()

def apply_demand_reg(idno, temp_df):
    p = reg_d[idno][0]
    x = temp_df[idno][np.in1d(temp_df.index.month, [6,7,8])]
    y = pd.Series(np.polyval(p, x.values), index=x.index)
    y.name = idno
    return y

#Create output files of regression in directory ./regress

dirlist = pd.Series([k.split('rcp') for k in os.listdir(projection_dir)]).apply(pd.Series)
dirlist[0] = dirlist[0].str[:-1]
dirlist[1] = 'rcp' + dirlist[1].str.split('-').str[0]

for i in dirlist.index.values:
    model = dirlist.loc[i, 0]
    proj = dirlist.loc[i, 1]
    temp_df = combine_scenario(model, proj, historical_dir, projection_dir)
    reg_results = pd.DataFrame()
    for j in reg_d.keys():
        result = apply_demand_reg(j, temp_df)
        reg_results[j] = result
    reg_results.to_csv('demand_%s_%s' % (model, proj))


# Combine output files in a pandas panel
