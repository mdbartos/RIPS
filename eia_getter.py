import numpy as np
import pandas as pd
import os
import re
import datetime
import time
import pysal as ps

basepath = '/home/akagi/Documents/EIA_form_data/wecc_form_714'

path_d = {
1993: '93WSCC1/WSCC',
1994: '94WSCC1/WSCC1994',
1995: '95WSCC1',
1996: '96WSCC1/WSCC1996',
1997: '97wscc1',
1998: '98WSCC1/WSCC1',
1999: '99WSCC1/WSCC1',
2000: '00WSCC1/WSCC1',
2001: '01WECC/WECC01/wecc01',
2002: 'WECCONE3/WECC One/WECC2002',
2003: 'WECC/WECC/WECC ONE/wecc03',
2004: 'WECC_2004/WECC/WECC One/ferc',
2006: 'form714-database_2006_2013/form714-database/Part 3 Schedule 2 - Planning Area Hourly Demand.csv'
}

#### GET UNIQUE UTILITIES AND UTILITIES BY YEAR

u_by_year = {}

for d in path_d:
    if d != 2006:
        full_d = basepath + '/' + path_d[d]
        l = [i.lower().split('.')[0][:-2] for i in os.listdir(full_d) if i.lower().endswith('dat')]
        u_by_year.update({d : sorted(l)})

unique_u = np.unique(np.concatenate([np.array(i) for i in u_by_year.values()]))

#### GET EIA CODES OF WECC UTILITIES

rm_d = {1993: {'rm': '93WSCC1/README2'},
1994: {'rm': '94WSCC1/README.TXT'},
1995: {'rm': '95WSCC1/README.TXT'},
1996: {'rm': '96WSCC1/README.TXT'},
1997: {'rm': '97wscc1/README.TXT'},
1998: {'rm': '98WSCC1/WSCC1/part.002'},
1999: {'rm': '99WSCC1/WSCC1/README.TXT'},
2000: {'rm': '00WSCC1/WSCC1/README.TXT'},
2001: {'rm': '01WECC/WECC01/wecc01/README.TXT'},
2002: {'rm': 'WECCONE3/WECC One/WECC2002/README.TXT'},
2003: {'rm': 'WECC/WECC/WECC ONE/wecc03/README.TXT'},
2004: {'rm': 'WECC_2004/WECC/WECC One/ferc/README.TXT'}}

for d in rm_d.keys():
    fn = basepath + '/' + rm_d[d]['rm']
    f = open(fn, 'r')
    r = f.readlines()
    f.close()
    for i in range(len(r)):
        if 'FILE NAME' in r[i]:
            rm_d[d].update({'op': i})
        if 'FERC' and 'not' in r[i]:
            rm_d[d].update({'ed': i})

unique_u_ids = {}

for u in unique_u:
    regex = re.compile('^ *%s\d\d.dat' % u, re.IGNORECASE)
    for d in rm_d.keys():
        fn = basepath + '/' + rm_d[d]['rm']
        f = open(fn, 'r')
        r = f.readlines() #[rm_d[d]['op']:rm_d[d]['ed']]
        f.close()
        for line in r:
            result = re.search(regex, line)
            if result:
#                print line
                code = line.split()[1]
                nm = line.split(code)[1].strip()
                unique_u_ids.update({u : {'code':code, 'name':nm}})
                break
            else:
                continue
        if u in unique_u_ids:
            break
        else:
            continue

id_2006 = pd.read_csv('/home/akagi/Documents/EIA_form_data/wecc_form_714/form714-database_2006_2013/form714-database/Respondent IDs.csv') 
id_2006 = id_2006.drop_duplicates('eia_code').set_index('eia_code').sort_index()

ui = pd.DataFrame.from_dict(unique_u_ids, orient='index')
ui = ui.loc[ui['code'] != '*'].drop_duplicates('code')
ui['code'] = ui['code'].astype(int)
ui = ui.set_index('code')

eia_to_r = pd.concat([ui, id_2006], axis=1).dropna()

# util = {
# 'aps' : 803,
# 'srp' : 16572,
# 'ldwp' : 11208
#         }
# util_2006 = {
# 'aps' : 116,
# 'srp' : 244,
# 'ldwp' : 194
# }

resp_ids = '/home/akagi/Documents/EIA_form_data/wecc_form_714/form714-database_2006_2013/form714-database/Respondent IDs.csv'

df_path_d = {}

def build_paths():
    for y in path_d.keys():
        if y < 2006:
            pathstr = basepath + '/' + path_d[y]
            dirstr = ' '.join(os.listdir(pathstr))
#            print dirstr
            for u in u_by_year[y]:
                if not u in df_path_d:
                    df_path_d.update({u : {}})
                srcstr = '%s\d\d.dat' % (u)
 #               print srcstr
                match = re.search(srcstr, dirstr, re.I)
#                print type(match.group())
                rpath = pathstr + '/' + match.group()
                df_path_d[u].update({y : rpath})
        elif y == 2006:
            pathstr = basepath + '/' + path_d[y]
            for u in unique_u:
                if not u in df_path_d:
                    df_path_d.update({u : {}})
                df_path_d[u].update({y : pathstr})

df_d = {}

def build_df(u):
        print u
        df = pd.DataFrame()
        for y in sorted(df_path_d[u].keys()):
            print y
            if y < 2006:
                f = open(df_path_d[u][y], 'r')
                r = f.readlines()
                f.close()
                #### DISCARD BINARY-ENCODED FILES
                try:
                    enc = r[0].decode()
                except:
                    enc = None
                    pass
                if enc:
                    r = [g.replace('\t', '      ') for g in r if len(g) > 70]
                    if not str.isdigit(r[0][0]):
                        for line in range(len(r)):
                            try:
                                chk = int(''.join(r[line].rstrip().split()))
                                if chk:
                                    # print line, r[line]
                                    r = r[line:]
                                    break
                            except:
                                continue
                    for i in range(0, len(r)-1, 2):
                        # print i
                        entry = [r[i], r[i+1]]
                        mo = int(r[i][:2])
                        day = int(r[i][2:4])
                        yr = y
    #                    yr = r[i][4:6]
    #                    if yr[0] == '0':
    #                        yr = int('20' + yr)
    #                    else:
    #                        yr = int('19' + yr)

                        if (len(entry[0].rstrip()) + len(entry[1].rstrip())) == 160:
                            try:
                                am = [int(j) if j.strip() != '' else None for j in re.findall('.{5}', entry[0][20:].rstrip())]
                                pm = [int(j) if j.strip() != '' else None for j in re.findall('.{5}', entry[1][20:].rstrip())]
                                assert(len(am)==12)
                                assert(len(pm)==12)
                            except:
                                am = [int(j) for j in entry[0][20:].rstrip().split()]
                                pm = [int(j) for j in entry[1][20:].rstrip().split()]
                                assert(len(am)==12)
                                assert(len(pm)==12)
                        else:
                            try:
                                am = [int(j) for j in entry[0][20:].rstrip().split()]
                                pm = [int(j) for j in entry[1][20:].rstrip().split()]
                                assert(len(am)==12)
                                assert(len(pm)==12)
                            except:
                                try:
                                    am = [int(j) if j.strip() != '' else None for j in re.findall('.{5}', entry[0][20:].rstrip())]
                                    pm = [int(j) if j.strip() != '' else None for j in re.findall('.{5}', entry[1][20:].rstrip())]
                                    if len(am) < 12:
                                        am_arr = np.array(am)
                                        am = np.pad(am_arr, (0, (12 - np.array(am).shape[0])), mode='symmetric').tolist()
                                    if len(pm) < 12:
                                        pm_arr = np.array(pm)
                                        pm = np.pad(pm_arr, (0, (12 - np.array(pm).shape[0])), mode='symmetric').tolist()
                                    if len(am) > 12:
                                        am = am[:12] 
                                    if len(pm) > 12:
                                        pm = pm[:12]
                                except:
                                    print 'Cannot read line'
                                    am = np.repeat(np.nan, 12).tolist()
                                    pm = np.repeat(np.nan, 12).tolist()

                        ampm = am + pm
                        entry_df = pd.DataFrame()
                        try:
                            dt_ix = pd.date_range(start=datetime.datetime(yr, mo, day, 0), end=datetime.datetime(yr, mo, day, 23), freq='H')
                            entry_df['load'] = ampm
        #                    print entry_df
                            entry_df.index = dt_ix
                            df = df.append(entry_df)
                        except:
                            entry_df['load'] = ampm
                            yest = df.index.to_pydatetime()[-1]
                            dt_ix = pd.date_range(start=(yest + datetime.timedelta(hours=1)), end=(yest + datetime.timedelta(hours=24)), freq='H') 
                            entry_df.index = dt_ix
                            df = df.append(entry_df)

                elif y == 2006:
                    f = pd.read_csv('%s/%s' % (basepath, path_d[y]))
                    if u in eia_to_r.index.values:
                        f = f.loc[f['respondent_id'] == eia_to_r.loc[u, 'respondent_id'], [u'plan_date', u'hour01', u'hour02', u'hour03', u'hour04', u'hour05', u'hour06', u'hour07', u'hour08', u'hour09', u'hour10', u'hour11', u'hour12', u'hour13', u'hour14', u'hour15', u'hour16', u'hour17', u'hour18', u'hour19', u'hour20', u'hour21', u'hour22', u'hour23', u'hour24']]
                        f['plan_date'] = f['plan_date'].str.split().apply(lambda x: x[0]).apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'))
                        f = f.set_index('plan_date').stack().reset_index().rename(columns={'level_1':'hour', 0:'load'})
                        f['hour'] = f['hour'].str.replace('hour','').astype(int)-1
                        f['date'] = f.apply(lambda x: datetime.datetime(x['plan_date'].year, x['plan_date'].month, x['plan_date'].day, x['hour']), axis=1)
                        f = pd.DataFrame(f.set_index('date')['load'])
                        df = pd.concat([df, f], axis=0)
            
        return df            

build_paths()

for x in unique_u:
    out_df = build_df(x)
    out_df.to_csv(x)
