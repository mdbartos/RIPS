import numpy as np
import pandas as pd
import os

homedir = os.path.expanduser('~')
datadir = 'github/RIPS_kircheis/data/eia_form_714/processed/'
fulldir = homedir + '/' + datadir

li = []

for d1 in os.listdir('.'):
    for fn in os.listdir('./%s' % d1):
        li.append(fn)

dir_u = pd.Series(li).str[:-2].order().unique()

###### NPCC
# BECO: 1998
# BHE: 1179
# CELC: 2886
# CHGE: 3249
# CMP: 3266
# COED: 4226
# COEL: 4089
# CVPS: 3292
# EUA: 5618
# GMP: 7601
# ISONY: 13501
# LILC: 11172
# MMWE: 11806
# NEES: 13433
# NEPOOL: 13435
# NMPC: 13573
# NU: 13556
# NYPA: 15296
# NYPP: 13501
# NYS: 13511
# OR: 14154
# RGE: 16183
# UI: 19497

npcc = {
    1998 : {
        1993 : pd.read_fwf('./1993/BECO93', header=None, skipfooter=1).loc[:, 2:].values.ravel(),
        1994 : pd.read_csv('./1994/BECO94', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[4].values,
        1995 : pd.read_csv('./1995/BECO95', sep =' ', skipinitialspace=True,  header=None)[4].values,
        1996 : pd.read_csv('./1996/BECO96', sep =' ', skipinitialspace=True,  header=None)[4].values,
        1997 : pd.read_csv('./1997/BECO97', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[4].values,
        1998 : pd.read_csv('./1998/BECO98', sep =' ', skipinitialspace=True,  header=None)[4].values,
        1999 : pd.read_csv('./1999/BECO99', sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2000 : pd.read_csv('./2000/BECO00', sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2001 : pd.read_csv('./2001/BECO01', sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2002 : pd.read_csv('./2002/BECO02', sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2003 : pd.read_csv('./2003/BECO03', sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2004 : pd.read_csv('./2004/BECO04', sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values
    },
    1179 : {
            1993 : pd.read_csv('./1993/BHE93', sep=' ', skiprows=2, skipinitialspace=True).loc[:, '0000':].values.ravel(),
            1994 : pd.read_csv('./1994/BHE94').dropna(how='all').loc[:729, '1/13':'12/24'].values.ravel(),
            1995 : pd.read_fwf('./1995/BHE95').loc[:729, '1/13':'1224'].values.ravel(),
            2001 : pd.read_excel('./2001/BHE01', skiprows=2).iloc[:, 1:24].values.ravel(),
            2003 : pd.read_excel('./2003/BHE03', skiprows=3).iloc[:, 1:24].values.ravel()
    },
    2886 = {
            1999 : pd.read_csv('./1999/CELC99', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2000 : pd.read_csv('./2000/CELC00', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2001 : pd.read_csv('./2001/CELC01', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2002 : pd.read_csv('./2002/CELC02', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2003 : pd.read_csv('./2003/CELC03', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2004 : pd.read_csv('./2004/CELC04', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values
    },
    3249 = {
            1993 : pd.read_csv('./1993/CHGE93', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[2].values,
            1994 : pd.read_fwf('./1994/CHGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('./1995/CHGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('./1996/CHGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1997 : pd.read_csv('./1997/CHGE97', sep ='\s', skipinitialspace=True,  header=None, skipfooter=1).iloc[:, 4:].values.ravel(),
            1998 : pd.read_excel('./1998/CHGE98', skipfooter=1, header=None).iloc[:, 2:].values.ravel(),
    },
    3266 = {
            1993 : pd.read_fwf('./1993/CMP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1994 : pd.read_fwf('./1994/CMP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('./1995/CMP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('./1996/CMP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('./1997/CMP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1999 : pd.read_fwf('./1999/CMP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            2002 : pd.read_fwf('./2002/CMP02', header=None).iloc[:, 1:].values.ravel(),
            2003 : pd.read_fwf('./2003/CMP03', header=None).iloc[:, 1:].values.ravel()
    },
    4226 = {
        1993 : pd.read_csv('./1993/COED93', skipfooter=1, skiprows=11, header=None, skipinitialspace=True, sep=' ')[2].values,
        1994 : pd.read_fwf('./1994/COED94', skipfooter=1, header=None)[1].values,
        1995 : pd.read_csv('./1995/COED95', skiprows=3, header=None),
        1996 : pd.read_excel('./1996/COED96').iloc[:, -1].values.ravel(),
        1997 : pd.read_excel('./1997/COED97', skiprows=1).iloc[:, -1].values.ravel(),
        1998 : pd.read_excel('./1998/COED98', skiprows=1).iloc[:, -1].values.ravel(),
        1999 : pd.read_csv('./1999/COED99', skiprows=1, sep='\t').iloc[:, -1].str.replace(',', '').astype(int).values.ravel(),
        2000 : pd.read_csv('./2000/COED00', sep='\t')[' Load '].dropna().str.replace(',', '').astype(int).values.ravel(),
        2001 : pd.read_csv('./2001/COED01', sep='\t', skipfooter=1)['Load'].dropna().str.replace(',', '').astype(int).values.ravel(),
        2002 : pd.read_csv('./2002/COED02', sep='\t', skipfooter=1, skiprows=1)['Load'].dropna().str.replace(',', '').astype(int).values.ravel(),
        2003 : pd.read_csv('./2003/COED03', sep='\t')['Load'].dropna().astype(int).values.ravel(),
        2004 : pd.read_csv('./2004/COED04', header=None).iloc[:, -1].str.replace('[A-Z,]', '').str.replace('\s', '0').astype(int).values.ravel()
    },
    4089 = {
        1993 : pd.read_fwf('./1993/COEL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/COEL95', header=None).iloc[:, 1:].values.ravel(), 
        1996 : pd.read_csv('./1996/COEL96', sep=' ', skipinitialspace=True, header=None)[3].values,
        1997 : pd.read_csv('./1997/COEL97', sep=' ', skipinitialspace=True, header=None)[4].values,
        1998 : pd.read_csv('./1998/COEL98', sep=' ', skipinitialspace=True, header=None)[4].values,
        1999 : pd.read_csv('./1999/COEL99', sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2000 : pd.read_csv('./2000/COEL00', sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2001 : pd.read_csv('./2001/COEL01', sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2002 : pd.read_csv('./2002/COEL02', sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2003 : pd.read_csv('./2003/COEL03', sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2004 : pd.read_csv('./2004/COEL04', sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values
    },
    3292 = {
        1995 : pd.read_fwf('./1995/CVPS95', header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('./1996/CVPS96', header=None, skipfooter=1)[1].values,
        1997 : pd.read_csv('./1997/CVPS97', header=None)[2].values,
        1998 : pd.read_csv('./1998/CVPS98', header=None, skipfooter=1)[4].values,
        1999 : pd.read_csv('./1999/CVPS99')['Load'].values
    },
    5618 = {
            1993 : pd.read_fwf('./1993/EUA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1994 : pd.read_fwf('./1994/EUA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('./1995/EUA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('./1996/EUA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('./1997/EUA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1999 : pd.read_fwf('./1999/EUA99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    7601 = {
        1993 : pd.read_csv('./1993/GMP93', sep=' ', skipinitialspace=True, header=None, skiprows=4)[0].values,
        1994 : pd.read_fwf('./1994/GMP94', header=None)[0].values,
        1995 : pd.read_csv('./1995/GMP95', sep=' ', skipinitialspace=True, header=None)[0].values,
        1996 : pd.read_csv('./1996/GMP96', sep='\t', skipinitialspace=True, header=None)[0].values,
        1997 : pd.read_csv('./1997/GMP97', sep='\t', skipinitialspace=True, header=None)[0].values,
        1998 : pd.read_csv('./1998/GMP98', sep='\t', skipinitialspace=True, header=None)[0].values,
        1999 : pd.read_csv('./1999/GMP99', sep=' ', skipinitialspace=True, header=None, skipfooter=1).iloc[:8760, 0].values,
        2002 : pd.read_excel('./2002/GMP02', skiprows=6, skipfooter=1).iloc[:, 0].values,
        2003 : pd.read_excel('./2003/GMP03', skiprows=6, skipfooter=1).iloc[:, 0].values,
        2004 : pd.read_csv('./2004/GMP04', skiprows=13, sep='\s').iloc[:, 0].values
    },
    13501 = {
        2002 : pd.read_csv('./2002/ISONY02', sep='\t')['mw'].values,
        2003 : pd.read_excel('./2003/ISONY03')['Load'].values,
        2004 : pd.read_excel('./2004/ISONY04').loc[:, 'HR1':].values.ravel()
    },
    11172 = {
            1994 : pd.read_fwf('./1994/LILC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('./1995/LILC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('./1997/LILC97', skiprows=4, widths=[8,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
    },
    11806 = {
        1998 : pd.read_fwf('./1998/MMWE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/MMWE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('./2000/MMWE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('./2001/MMWE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('./2002/MMWE02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2003 : pd.read_fwf('./2003/MMWE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2004 : pd.read_fwf('./2004/MMWE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel()
    },
    13433 = {
        1993 : pd.read_fwf('./1993/NEES93', widths=(8,7), header=None, skipfooter=1)[1].values,
        1994 : pd.read_csv('./1994/NEES94', header=None, skipfooter=1, sep=' ', skipinitialspace=True)[3].values
    },
    13435 = {
        1993 : pd.read_fwf('./1993/NEPOOL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/NEPOOL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/NEPOOL95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=3).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('./1996/NEPOOL96', sep=' ', skipinitialspace=True, header=None)[1].values,
        1997 : pd.read_fwf('./1997/NEPOOL97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_excel('./1998/NEPOOL98', header=None).iloc[:, 5:17].values.ravel(),
        1999 : pd.read_csv('./1999/NEPOOL99', engine='python', skiprows=1).iloc[:, 0].values,
        2000 : pd.read_fwf('./2000/NEPOOL00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('./2001/NEPOOL01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('./2002/NEPOOL02', sep='\t').iloc[:, 3:].values.ravel(),
        2003 : pd.read_fwf('./2003/NEPOOL03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2004 : pd.read_csv('./2004/NEPOOL04', sep='\t', header=None, skiprows=10).iloc[:, 5:].values.ravel()
    },
    13573 = {
            1993 : pd.read_csv('./1993/NMPC93', skiprows=11, header=None, sep=' ', skipinitialspace=True).iloc[:, 3:27].values.ravel(), 
            1995 : pd.read_fwf('./1995/NMPC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('./1996/NMPC96', header=None).iloc[:, 2:14].astype(int).values.ravel(),
            1998 : pd.read_fwf('./1998/NMPC98', header=None).iloc[:, 2:].astype(int).values.ravel(),
            1999 : pd.read_fwf('./1999/NMPC99', header=None).iloc[:, 2:14].astype(int).values.ravel(),
            2000 : pd.read_excel('./2000/NMPC00', sheetname=1, skiprows=10, skipfooter=3).iloc[:, 1:].values.ravel(),
            2002 : pd.read_excel('./2002/NMPC02', sheetname=1, skiprows=2, header=None).iloc[:, 2:].values.ravel(),
            2003 : pd.concat([pd.read_excel('./2003/NMPC03', sheetname=i, skiprows=1, header=None) for i in range(1,13)]).iloc[:, 2:].values.ravel()
    },
    13556 = {
            1993 : pd.read_fwf('./1993/NU93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1994 : pd.read_excel('./1994/NU94', header=None, skipfooter=1).iloc[:, 3:].values.ravel(),
            1995 : pd.read_excel('./1995/NU95', header=None, skipfooter=5).dropna(how='any').iloc[:, 3:].values.ravel(),
            1996 : pd.read_excel('./1996/NU96', header=None, skipfooter=1).iloc[:, 5:].values.ravel(),
            1997 : pd.read_excel('./1997/NU97', header=None, skipfooter=4).iloc[:, 5:].values.ravel(),
            1998 : pd.read_excel('./1998/NU98', header=None).iloc[:, 5:].values.ravel(),
            1999 : pd.read_excel('./1999/NU99', header=None).iloc[:, 5:].values.ravel(),
            2000 : pd.read_csv('./2000/NU00', sep='\t', header=None).iloc[:, 5:].values.ravel(),
            2001 : pd.read_excel('./2001/NU01').iloc[:, -1].values,
            2002 : pd.read_excel('./2002/NU02').iloc[:, -1].values,
            2003 : pd.read_excel('./2003/NU03', skipfooter=1).iloc[:, -1].values 
    },
    15296 = {
        1993 : pd.read_csv('./1993/NYPA93', engine='python', header=None).values,
        1994 : pd.read_csv('./1994/NYPA94', engine='python', header=None).values,
        1995 : pd.read_csv('./1995/NYPA95', engine='python', header=None).values,
        1996 : pd.read_csv('./1996/NYPA96', engine='python', header=None).values,
        1997 : pd.read_csv('./1997/NYPA97', engine='python', header=None).values,
        1998 : pd.read_csv('./1998/NYPA98', engine='python', header=None).values,
        1999 : pd.read_excel('./1999/NYPA99', header=None).values,
        2000 : pd.read_csv('./2000/NYPA00', engine='python', header=None).values,
        2001 : pd.read_csv('./2001/NYPA01', engine='python', header=None).values,
        2002 : pd.read_csv('./2002/NYPA02', engine='python', header=None).values,
        2003 : pd.read_csv('./2003/NYPA03', engine='python', header=None).values
    },
    13501 = {
            1993 : pd.read_fwf('./1993/NYPP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    13511 = {
            1996 : pd.read_fwf('./1996/NYS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('./1997/NYS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1999 : pd.read_excel('./1999/NYS99').iloc[:, 1:].values.ravel(),
            2000 : pd.read_csv('./2000/NYS00', sep='\t').iloc[:, -1].values,
            2001 : pd.read_csv('./2001/NYS01', sep='\t', skiprows=3).dropna(how='all').iloc[:, -1].values,
            2002 : pd.read_csv('./2002/NYS02', sep='\t', skiprows=3).iloc[:, -1].values,
            2003 : pd.read_csv('./2003/NYS03', sep=' ', skipinitialspace=True, skiprows=5, header=None).iloc[:, -1].values,
            2004 : pd.read_csv('./2004/NYS04', sep=' ', skipinitialspace=True, skiprows=5, header=None).dropna(how='all').iloc[:, -1].values
    },
    14154 = {
        1993 : pd.read_csv('./1993/OR93', skiprows=5, header=None).iloc[:, 2:26].values.ravel(),
        1995 : pd.read_csv('./1995/OR95', header=None).iloc[:, 1:25].values.ravel(),
        1996 : pd.read_csv('./1996/OR96', header=None).iloc[:, 1:25].values.ravel(),
        1997 : pd.read_csv('./1997/OR97', header=None).iloc[:, 1:25].values.ravel(),
        1998 : pd.read_fwf('./1998/OR98', skiprows=1, header=None).dropna(axis=1, how='all').iloc[:, 1:].values.ravel(),
        1999 : pd.read_csv('./1999/OR99', sep='\t', skiprows=1, header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_csv('./2000/OR00', sep='\t').iloc[:, -1].values.astype(int).ravel(),
        2002 : pd.read_csv('./2002/OR02', sep='\t', skiprows=2).iloc[:, -1].dropna().values.astype(int).ravel(),
        2003 : pd.read_csv('./2003/OR03', sep='\t').iloc[:, -1].dropna().values.astype(int).ravel(),
        2004 : pd.read_csv('./2004/OR04', header=None).iloc[:, -1].values.astype(int).ravel()
    },
    16183 = {
            1994 : pd.read_fwf('./1994/RGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('./1995/RGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('./1996/RGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            2002 : pd.read_csv('./2002/RGE02', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values,
            2003 : pd.read_csv('./2003/RGE03', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values,
            2004 : pd.read_csv('./2004/RGE04', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values
    },
    19497 = {
        1993 : pd.read_fwf('./1993/UI93', header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/UI94', header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/UI95', header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/UI96', header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/UI97', header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_excel('./1998/UI98')['MW'].values,
        1999 : pd.read_excel('./1999/UI99').loc[:, 'HR1':'HR24'].values.ravel(),
        2001 : pd.read_excel('./2001/UI01', sheetname=0).ix[:-2, 'HR1':'HR24'],
        2002 : pd.read_excel('./2002/UI02', sheetname=0).ix[:-2, 'HR1':'HR24'],
        2003 : pd.read_excel('./2003/UI03', sheetname=0, skipfooter=2).ix[:, 'HR1':'HR24'],
        2004 : pd.read_excel('./2004/UI04', sheetname=0, skipfooter=1).ix[:, 'HR1':'HR24']
    }
}
npcc[4226][1995] = pd.concat([npcc[4226][1995][2].dropna(), npcc[4226][1995][6]]).values.ravel()

###### ERCOT
# AUST: 1015
# CPL: 3278
# HLP: 8901
# LCRA: 11269
# NTEC: 13670
# PUB: 2409
# SRGT: 40233
# STEC: 17583
# TUEC: 44372
# TMPP: 18715
# TXLA: 18679
# WTU: 20404

ercot = {
    1015 : {
        1993 : pd.read_fwf('./1993/AUST93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/AUST94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/AUST95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/AUST96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/AUST97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['AENX'].loc[2:].astype(float)/1000).values,
        1999 : (pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['AENX'].astype(float)/1000).values,
        2000 : (pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[3].str.replace(',', '').astype(float)/1000).values
    },
    3278 : {
        1993 : pd.read_fwf('./1993/CPL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/CPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/CPL96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/CPL97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['CPLC'].loc[2:].astype(int)/1000).values
    },
    8901 : {
        1993 : pd.read_fwf('./1993/HLP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/HLP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/HLP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/HLP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/HLP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['HLPC'].loc[2:].astype(int)/1000).values
    },
    11269: {
        1993 : pd.read_fwf('./1993/LCRA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_csv('./1994/LCRA94', skiprows=4).iloc[:, -1].values,
        1995 : pd.read_fwf('./1995/LCRA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/LCRA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/LCR97', header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['LCRA'].loc[2:].astype(int)/1000).values,
        1999 : (pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['LCRA'].astype(float)/1000).values,
        2000 : (pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[6].str.replace(',', '').astype(float)/1000).values
    },
    13670 : {
        1993 : pd.read_csv('./1993/NTEC93', sep=' ', skipinitialspace=True, header=None)[1].values,
        1994 : pd.read_fwf('./1994/NTEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/NTEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/NTEC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/NTEC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('./2001/NTEC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    2409 : {
        1993 : pd.read_fwf('./1993/PUB93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/PUB94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/PUB95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/PUB96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/PUB97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['PUBX'].loc[2:].astype(int)/1000).values,
        1999 : (pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['PUBX'].astype(float)/1000).values,
        2000 : (pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[7].str.replace(',', '').astype(float)/1000).values
    },
    40233 : {
        1993 : pd.read_csv('./1993/SRGT93', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        1994 : pd.read_fwf('./1994/SRGT94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/SRGT95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/SRGT96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/SRGT97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    17583 : {
        1993 : pd.read_fwf('./1993/STEC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['STEC'].loc[2:].astype(int)/1000).values,
        1999 : (pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['STEC'].astype(float)/1000).values,
        2000 : (pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[9].str.replace(',', '').astype(float)/1000).values
    },
    44372 : {
        1993 : pd.read_fwf('./1993/TUEC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/TUEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/TUEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/TUE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/TUE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['TUEC'].loc[2:].astype(int)/1000).values
    },
    18715 : {
        1993 : pd.read_fwf('./1993/TMPP93', skiprows=6, header=None).dropna(how='all'),
        1995 : pd.read_fwf('./1995/TMPP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/TMPP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1999 : (pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['TMPP'].astype(float)/1000).values,
        2000 : (pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[10].str.replace(',', '').astype(float)/1000).values
    },
    18679 : {
        1993 : pd.read_csv('./1993/TEXLA93', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        1995 : pd.read_fwf('./1995/TXLA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/TXLA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/TXLA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['TXLA'].loc[2:].astype(int)/1000).values
    },
    20404 : {
        1993 : pd.read_fwf('./1993/WTU93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].astype(str).apply(lambda x: x.str.replace('\s', '0')).astype(float).values.ravel(),
        1994 : pd.read_fwf('./1994/WTU94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/WTU96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/WTU97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('./1998/FERC714.xls', skiprows=3)['WTUC'].loc[2:].astype(int)/1000).values
    }
}

###### FRCC
# GAIN: 6909
# LAKE: 10623
# FMPA: 6567
# FPC: 6455
# FPL: 6452
# JEA: 9617
# KUA: 10376
# OUC: 14610
# TECO: 18454

frcc = {
    6909 : {
        1993 : pd.read_fwf('./1993/GAIN93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_csv('./1994/GAIN94', header=None, sep=' ', skipinitialspace=True, skipfooter=2, skiprows=5).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/GAIN95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('./1996/GAIN96', sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/GAIN97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/GAIN98', sep=' ', skipinitialspace=True, skiprows=3, header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/GAIN99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('./2000/GAIN00', header=None).iloc[:, 4:].values.ravel(),
        2002 : pd.read_excel('./2002/GAIN02', sheetname=1, skiprows=3, header=None).iloc[:730, 8:20].values.ravel(),
        2003 : pd.read_excel('./2003/GAIN03', sheetname=2, skiprows=3, header=None).iloc[:730, 8:20].values.ravel(),
        2004 : pd.read_excel('./2004/GAIN04', sheetname=0, header=None).iloc[:, 8:].values.ravel()
    },
    10623: {
        1993 : pd.read_fwf('./1993/LAKE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/LAKE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/LAKE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/LAKE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/LAKE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('./1998/LAKE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/LAKE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('./2000/LAKE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('./2001/LAKE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('./2002/LAKE02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    6567 : {
        1993 : pd.read_fwf('./1993/FMPA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/FMPA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/FMPA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/FMPA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/FMPA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('./1998/FMPA98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/FMPA99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        2001 : pd.read_csv('./2001/FMPA01', header=None, sep=' ', skipinitialspace=True, skiprows=6).iloc[:, 2:-1].values.ravel(),
        2002 : pd.read_csv('./2002/FMPA02', header=None, sep='\t', skipinitialspace=True, skiprows=7).iloc[:, 1:].values.ravel(),
        2003 : pd.read_csv('./2003/FMPA03', header=None, sep='\t', skipinitialspace=True, skiprows=7).iloc[:, 1:].values.ravel(),
        2004 : pd.read_csv('./2004/FMPA04', header=None, sep=' ', skipinitialspace=True, skiprows=6, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    6455 : {
        1993 : pd.read_csv('./1993/FPC93', sep=' ', skipinitialspace=True, header=None)[1].values,
        1994 : pd.read_csv('./1994/FPC94', sep=' ', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
        1995 : pd.read_csv('./1995/FPC95', engine='python', header=None).values,
        1996 : pd.read_excel('./1996/FPC96', header=None, skiprows=2, skipfooter=1).iloc[:, 6:].values.ravel(),
        1998 : pd.read_excel('./1998/FPC98', header=None, skiprows=5).iloc[:, 7:].values.ravel(),
        1999 : pd.read_excel('./1999/FPC99', header=None, skiprows=4).iloc[:, 7:].values.ravel(),
        2000 : pd.read_excel('./2000/FPC00', header=None, skiprows=4).iloc[:, 7:].values.ravel(),
        2001 : pd.read_excel('./2001/FPC01', header=None, skiprows=5).iloc[:, 7:].values.ravel(),
        2002 : pd.read_excel('./2002/FPC02', header=None, skiprows=4).iloc[:, 7:].values.ravel(),
        2004 : pd.read_excel('./2004/FPC04', header=None, skiprows=4).iloc[:, 7:].values.ravel()
    },
    6452 : {
        1993 : pd.DataFrame([i.split('\t') for i in open('./1993/FPL93', 'r').readlines()]).iloc[:365, :24].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1994 : pd.DataFrame([i.split('\t') for i in open('./1994/FPL94', 'r').readlines()]).iloc[3:, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1995 : pd.DataFrame([i.split('\t') for i in open('./1995/FPL95', 'r').readlines()[3:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1996 : pd.DataFrame([i.split('\t') for i in open('./1996/FPL96', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1997 : pd.DataFrame([i.split('\t') for i in open('./1997/FPL97', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1998 : pd.DataFrame([i.split('\t') for i in open('./1998/FPL98', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split('\t') for i in open('./1999/FPL99', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split('\t') for i in open('./2000/FPL00', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2001 : pd.DataFrame([i.split('\t') for i in open('./2001/FPL01', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2002 : pd.DataFrame([i.split('\t') for i in open('./2002/FPL02', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2003 : pd.DataFrame([i.split('\t') for i in open('./2003/FPL03', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2004 : pd.DataFrame([i.split('\t') for i in open('./2004/FPL04', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
    },
    9617 : {
        1993 : pd.read_csv('./1993/JEA93', sep=' ', skipinitialspace=True, header=None)[2].values,
        1994 : pd.read_csv('./1994/JEA94', sep=' ', skipinitialspace=True, header=None)[2].values,
        1996 : pd.read_fwf('./1996/JEA96', header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/JEA97', header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/JEA98', sep='\t', header=None)[2].values,
        1999 : pd.read_csv('./1999/JEA99', sep='\t', header=None)[2].values,
        2000 : pd.read_excel('./2000/JEA00', header=None)[2].values,
        2001 : pd.read_excel('./2001/JEA01', header=None, skiprows=2)[2].values,
        2002 : pd.read_excel('./2002/JEA02', header=None, skiprows=1)[2].values,
        2003 : pd.read_excel('./2003/JEA03', header=None, skiprows=1)[2].values,
        2004 : pd.read_excel('./2004/JEA04', header=None, skiprows=1)[2].values
    },
    10376 : {
        1994 : pd.read_csv('./1994/KUA94', sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_csv('./1995/KUA95', sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('./1997/KUA97', sep='\t', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
        2001 : pd.read_csv('./2001/KUA01', skiprows=1, header=None, sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('./2002/KUA02', skipfooter=1, header=None, sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel()
    },
    14610 : {
        1993 : pd.read_fwf('./1993/OUC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/OUC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/OUC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/OUC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/OUC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('./1998/OUC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/OUC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('./2000/OUC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('./2001/OUC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('./2002/OUC02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    18454 : {
        1993 : pd.read_fwf('./1993/TECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/TECO94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/TECO98', engine='python', skiprows=3, header=None)[0].values,
        1999 : pd.read_csv('./1999/TECO99', engine='python', skiprows=3, header=None)[0].values,
        2000 : pd.read_csv('./2000/TECO00', engine='python', skiprows=3, header=None)[0].str[:4].astype(int).values,
        2001 : pd.read_csv('./2001/TECO01', skiprows=3, header=None)[0].values,
        2002 : pd.read_csv('./2002/TECO02', sep='\t').loc[:, 'HR1':].values.ravel(),
        2003 : pd.read_csv('./2003/TECO03', skiprows=2, header=None, sep=' ', skipinitialspace=True).iloc[:, 2:].values.ravel()
    }
}

###### ECAR
# AEP: 829
# APS: 538
# AMPO: 40577
# BREC: 1692
# BPI: 7004
# CEI: 3755
# CGE: 3542
# CP: 4254
# DPL: 4922
# DECO: 5109
# DLCO: 5487
# EKPC: 5580
# HEC: 9267
# IPL: 9273
# KUC: 10171
# LGE: 11249
# NIPS: 13756
# OE: 13998
# OVEC: 14015
# PSI: 15470
# SIGE: 17633
# TE: 18997
# WVPA: 40211
# CINRGY: 3260
# FE: 
# MCCP:

ecar = {
    829 : {
        1993 : pd.read_fwf('./1993/AEP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/AEP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/AEP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/AEP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/AEP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/AEP98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/AEP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/AEP00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/AEP01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/AEP02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/AEP03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/AEP04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    538 : {
        1993 : pd.read_fwf('./1993/APS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/APS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/APS95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    40577 : {
        2001 : pd.read_fwf('./2001/AMPO01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/AMPO02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/AMPO03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/AMPO04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    1692 : {
        1993 : pd.read_fwf('./1993/BREC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/BREC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/BREC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/BREC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/BREC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/BREC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/BREC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/BREC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/BREC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/BREC02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/BREC03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/BREC04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    7004 : {
        1994 : pd.read_fwf('./1994/BPI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/BPI99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/BPI00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/BPI01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/BPI02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/BPI03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/BPI04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    3755 : {
        1993 : pd.read_fwf('./1993/CEI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/CEI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/CEI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/CEI96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    3542 : {
        1993 : pd.read_fwf('./1993/CEI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/CEI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/CEI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    4254 : {
        1993 : pd.read_fwf('./1993/CP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/CP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/CP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/CP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    4922 : {
        1993 : pd.read_fwf('./1993/DPL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/DPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/DPL95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/DPL96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/DPL97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/DPL98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/DPL99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/DPL00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/DPL01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/DPL02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/DPL03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/DPL04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    5109 : {
        1993 : pd.read_fwf('./1993/DECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/DECO94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/DECO95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/DECO96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/DECO97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/DECO98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/DECO99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/DECO00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/DECO01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/DECO02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/DECO03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/DECO04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    5487 : {
        1993 : pd.read_fwf('./1993/DLCO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/DLCO94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/DLCO95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/DLCO96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/DLCO97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/DLCO98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/DLCO99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/DLCO00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/DLCO01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/DLCO02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/DLCO03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/DLCO04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    5580 : {
        1993 : pd.read_fwf('./1993/EKPC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/EKPC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/EKPC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/EKPC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/EKPC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/EKPC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/EKPC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/EKPC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/EKPC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/EKPC02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/EKPC03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/EKPC04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9267 : {
        1993 : pd.read_fwf('./1993/HEC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/HEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/HEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/HEC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/HEC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/HEC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/HEC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/HEC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/HEC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/HEC02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/HEC03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/HEC04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9273 : {
        1993 : pd.read_fwf('./1993/IPL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/IPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/IPL95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/IPL96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/IPL97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/IPL98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/IPL99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/IPL00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/IPL01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/IPL02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/IPL03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/IPL04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    10171 : {
        1993 : pd.read_fwf('./1993/KUC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/KUC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/KUC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/KUC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/KUC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    11249 : {
        1993 : pd.read_fwf('./1993/LGE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/LGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/LGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/LGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/LGE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/LGEE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/LGEE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/LGEE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/LGEE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/LGEE02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/LGEE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/LGEE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13756 : {
        1993 : pd.read_fwf('./1993/NIPS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/NIPS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/NIPS95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/NIPS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/NIPS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/NIPS98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/NIPS99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/NIPS00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/NIPS01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/NIPS02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/NIPS03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/NIPS04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13998 : {
        1993 : pd.read_fwf('./1993/OES93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/OES94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/OES95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/OES96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    14015 : {
        1993 : pd.read_fwf('./1993/OVEC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/OVEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/OVEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/OVEC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/OVEC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/OVEC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/OVEC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/OVEC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/OVEC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/OVEC02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/OVEC03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/OVEC04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    15470 : {
        1993 : pd.read_fwf('./1993/PSI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/PSI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/PSI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    17633 : {
        1993 : pd.read_fwf('./1993/SIGE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/SIGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/SIGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/SIGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/SIGE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/SIGE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/SIGE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/SIGE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/SIGE02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/SIGE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/SIGE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    18997 : {
        1993 : pd.read_fwf('./1993/TECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/TECO94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/TECO95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/TECO96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    40211 : {
        1994 : pd.read_fwf('./1994/WVPA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('./2003/WVPA03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/WVPA04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    3260 : {
        1996 : pd.read_fwf('./1996/CIN96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/CIN97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/CIN98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/CIN99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/CIN00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/CIN01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/CIN02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/CIN03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/CIN04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    'FE' : {
        1997 : pd.read_fwf('./1997/FE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('./1998/FE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('./1999/FE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/FE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/FE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/FE02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/FE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/FE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    'MCCP' : {
        1993 : pd.read_fwf('./1993/MCCP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/MCCP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/MCCP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('./2000/MCCP00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('./2001/MCCP01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('./2002/MCCP02', header=None)[1].values,
        2003 : pd.read_fwf('./2003/MCCP03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('./2004/MCCP04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    }
}

###### MAIN
# CECO : 4110
# CILC: 3252
# CIPS: 3253
# IPC: 9208
# MGE: 11479
# SIPC: 17632
# SPIL: 17828
# UE: 19436
# WEPC: 20847
# WPL: 20856
# WPS: 20860
# UPP: 19578
# WPPI: 20858
# AMER: 19436
# CWL: 4045

main = {
    4110 : {
        1993 : pd.read_fwf('./1993/CECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_csv('./1995/CECO95', skiprows=3, header=None)[0].values,
        1996 : pd.read_csv('./1996/CECO96', skiprows=4, header=None)[1].values,
        1997 : pd.read_csv('./1997/CECO97', sep=' ', skipinitialspace=True, skiprows=4, header=None)[3].values,
        1998 : pd.read_csv('./1998/CECO98', sep='\s', skipinitialspace=True, skiprows=5, header=None)[5].values,
        1999 : pd.read_csv('./1999/CECO99', sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values,
        2000 : pd.read_csv('./2000/CECO00', sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values,
        2001 : pd.read_csv('./2001/CECO01', sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values,
        2002 : pd.read_csv('./2002/CECO02', sep=' ', skipinitialspace=True, skiprows=5, header=None)[2].values
    }
    3252 : {
        1993 : pd.read_fwf('./1993/CILC93', header=None).iloc[:, 2:].values.ravel(),
        1994 : pd.read_fwf('./1994/CILC94', header=None).iloc[:, 2:].values.ravel(),
        1995 : pd.read_fwf('./1995/CILC95', header=None).iloc[:, 2:].values.ravel(),
        1996 : pd.read_fwf('./1996/CILC96', header=None).iloc[:, 2:].values.ravel(),
        1997 : pd.read_fwf('./1997/CILC97', header=None).iloc[:, 2:].values.ravel(),
        1998 : pd.read_fwf('./1998/CILC98', header=None).iloc[:, 2:].values.ravel(),
        1999 : pd.read_fwf('./1999/CILC99', header=None).iloc[:, 2:].values.ravel(),
        2000 : pd.read_excel('./2000/CILC00', skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel(),
        2001 : pd.read_excel('./2001/CILC01', skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel(),
        2002 : pd.read_excel('./2002/CILC02', skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel(),
        2003 : pd.read_csv('./2003/CILC03', skiprows=1, sep='\t').iloc[:, -1].values
    },
    3253 : {
        1993 : pd.read_fwf('./1993/CIPS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/CIPS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/CIPS95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('./1996/CIPS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('./1997/CIPS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9208 : {
        1993 : pd.read_csv('./1993/IPC93', skipfooter=1, header=None)[2].values,
        1994 : pd.read_csv('./1994/IPC94', skipfooter=1, header=None)[2].values,
        1995 : pd.read_csv('./1995/IPC95', skipfooter=1, header=None)[4].astype(str).str.replace('.', '0').astype(float).values,
        1996 : pd.read_csv('./1996/IPC96').iloc[:, -1].values,
        1997 : pd.read_csv('./1997/IPC97').iloc[:, -1].values,
        1998 : pd.read_excel('./1998/IPC98').iloc[:, -1].values,
        1999 : pd.read_csv('./1999/IPC99', skiprows=2, header=None)[1].values,
        2000 : pd.read_excel('./2000/IPC00', skiprows=1).iloc[:, -1].values,
        2001 : pd.read_excel('./2001/IPC01', skiprows=1).iloc[:, -1].values,
        2002 : pd.read_excel('./2002/IPC02', skiprows=4).iloc[:, -1].values,
        2003 : pd.read_excel('./2003/IPC03', skiprows=1).iloc[:, -1].values,
        2004 : pd.read_excel('./2004/IPC04', skiprows=1).iloc[:, -1].values
    },
    11479 : {
        1993 : pd.read_fwf('./1993/MGE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=4).iloc[:, 1:].dropna().astype(float).values.ravel(),
        1995 : pd.read_csv('./1995/MGE95', sep=' ', skipinitialspace=True, header=None)[2].values,
        1997 : pd.read_csv('./1997/MGE97', sep=' ', skipinitialspace=True, skiprows=12, header=None).iloc[:-1, 2].astype(float).values,
        1998 : pd.read_csv('./1998/MGE98', sep=' ', skipinitialspace=True).iloc[:-1]['LOAD'].astype(float).values,
        1999 : pd.read_csv('./1999/MGE99', sep=' ', skiprows=2, header=None, skipinitialspace=True).iloc[:-2, 2].astype(float).values,
        2000 : pd.read_csv('./2000/MGE00', sep=' ', skiprows=2, header=None, skipinitialspace=True).iloc[:-2, 2].astype(float).values,
        2000 : pd.read_fwf('./2000/MGE00', skiprows=2)['VMS_DATE'].iloc[:-2].str.split().str[-1].astype(float).values,
        2001 : pd.read_fwf('./2001/MGE01', skiprows=1, header=None).iloc[:-2, 2].values,
        2002 : pd.read_fwf('./2002/MGE02', skiprows=4, header=None).iloc[:-1, 0].str.split().str[-1].astype(float).values
    },
    17632 : {
        1994 : pd.read_csv('./1994/SIPC94', engine='python', skipfooter=1, header=None)[0].values,
        1996 : pd.read_csv('./1996/SIPC96', engine='python', header=None)[0].values,
        1997 : pd.read_csv('./1997/SIPC97', engine='python', header=None)[0].values,
        1998 : pd.read_csv('./1998/SIPC98', engine='python', header=None)[0].values,
        1999 : pd.read_csv('./1999/SIPC99', engine='python', header=None)[0].replace('no data', '0').astype(float).values,
        2000 : pd.read_csv('./2000/SIPC00', engine='python', header=None)[0].astype(str).str[:3].astype(float).values,
        2001 : pd.read_csv('./2001/SIPC01', engine='python', header=None)[0].str.strip().str[:3].astype(float).values,
        2002 : pd.read_csv('./2002/SIPC02', sep='\t', skiprows=3, header=None)[1].values,
        2003 : pd.read_csv('./2003/SIPC03', engine='python', header=None)[0].str.strip().str[:3].astype(float).values,
        2004 : pd.read_csv('./2004/SIPC04', engine='python', header=None)[0].str.strip().str[:3].astype(float).values
    },
    17828 : {
        1993 : pd.read_csv('./1993/SPIL93', sep=' ', skipinitialspace=True, skiprows=4, header=None).iloc[:, 3:].values.ravel(),
        1994 : pd.read_csv('./1994/SPIL94', sep=' ', skipinitialspace=True, skiprows=6, header=None).iloc[:, 3:].values.ravel(),
        1995 : pd.read_csv('./1995/SPIL95', sep=' ', skipinitialspace=True, skiprows=7, header=None).iloc[:, 3:].values.ravel(),
        1996 : pd.read_csv('./1996/SPIL96', sep=' ', skipinitialspace=True, skiprows=5, header=None).iloc[:366, 3:].astype(float).values.ravel(),
        1997 : pd.read_csv('./1997/SPIL97', sep=' ', skipinitialspace=True, skiprows=7, header=None).iloc[:, 3:].values.ravel(),
        1998 : pd.read_csv('./1998/SPIL98', sep='\t', skipinitialspace=True, skiprows=8, header=None).iloc[:, 4:].values.ravel(),
        1999 : pd.read_csv('./1999/SPIL99', skiprows=4, header=None)[0].values,
        2000 : pd.read_csv('./2000/SPIL00', skiprows=4, header=None)[0].values,
        2001 : pd.read_csv('./2001/SPIL01', sep='\t', skipinitialspace=True, skiprows=7, header=None).iloc[:, 5:-1].values.ravel(),
        2002 : pd.read_excel('./2002/SPIL02', sheetname=2, skiprows=5).iloc[:, 3:].values.ravel(),
        2003 : pd.read_excel('./2003/SPIL03', sheetname=2, skiprows=5).iloc[:, 3:].values.ravel(),
        2004 : pd.read_excel('./2004/SPIL04', sheetname=0, skiprows=5).iloc[:, 3:].values.ravel()
    },
    19436 : {
        1995 : pd.read_fwf('./1995/UE95', header=None)[2].values,
        1996 : pd.read_fwf('./1996/UE96', header=None)[2].values,
        1997 : pd.read_fwf('./1997/UE97', header=None)[2].values
    },
    20847 : {
        1993 : pd.read_csv('./1993/WEPC93', engine='python', skipfooter=1, header=None)[0].values,
        1994 : pd.read_csv('./1994/WEPC94', engine='python', skipfooter=1, header=None)[0].values,
        1995 : pd.read_csv('./1995/WEPC95', engine='python', skipfooter=1, header=None)[0].values,
        1996 : pd.read_csv('./1996/WEPC96', engine='python', header=None)[0].values,
        1997 : pd.read_excel('./1997/WEPC97', header=None)[0].astype(str).str.strip().replace('NA', '0').astype(float).values,
        1998 : pd.read_csv('./1998/WEPC98', engine='python', header=None)[0].str.strip().replace('NA', 0).astype(float).values,
        1999 : pd.read_excel('./1999/WEPC99', header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_excel('./2000/WEPC00', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2001 : pd.read_excel('./2001/WEPC01', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_excel('./2002/WEPC02', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2003 : pd.read_excel('./2003/WEPC03', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2004 : pd.read_excel('./2004/WEPC04', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    20856 : {
        1993 : pd.read_fwf('./1993/WPL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('./1994/WPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('./1995/WPL95', header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('./1996/WPL96', header=None, sep='\t').iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('./1997/WPL97', sep=' ', skipinitialspace=True, skiprows=1, header=None)[2].str.replace(',', '').astype(float).values
    },
    20860 : {
        1993 : pd.read_csv('./1993/WPS93', sep=' ', header=None, skipinitialspace=True, skipfooter=1).values.ravel(),
        1994 : (pd.read_csv('./1994/WPS94', sep=' ', header=None, skipinitialspace=True, skipfooter=1).iloc[:, 1:-1]/100).values.ravel(),
        1995 : pd.read_csv('./1995/WPS95', sep=' ', skipinitialspace=True, skiprows=8, header=None, skipfooter=7)[2].values,
        1996 : pd.read_csv('./1996/WPS96', sep='\t', skiprows=2).loc[:365, '100':'2400'].astype(float).values.ravel(),
        1997 : pd.read_csv('./1997/WPS97', sep='\s', header=None, skipfooter=1)[2].values,
        1998 : pd.read_csv('./1998/WPS98', sep='\s', header=None)[2].values,
        1999 : pd.read_excel('./1999/WPS99', skiprows=8, skipfooter=8, header=None)[1].values,
        2000 : pd.read_excel('./2000/WPS00', sheetname=1, skiprows=5, skipfooter=8, header=None)[2].values,
        2001 : pd.read_excel('./2001/WPS01', sheetname=0, skiprows=5, header=None)[2].values,
        2002 : pd.read_csv('./2002/WPS02', sep='\s', header=None, skiprows=5)[2].values,
        2003 : pd.read_excel('./2003/WPS03', sheetname=1, skiprows=6, header=None)[2].values
    },
    19578 : {
        1996 : pd.read_csv('./1996/UPP96', header=None, skipfooter=1).iloc[:, -1].values,
        2004 : pd.read_excel('./2004/UPP04').iloc[:, -1].values
    },
    20858 : {
        1997 : pd.read_csv('./1997/WPPI97', skiprows=5, sep=' ', skipinitialspace=True, header=None).iloc[:, 1:-1].values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('./1999/WPPI99').readlines()[5:]]).iloc[:, 1:-1].astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split() for i in open('./2000/WPPI00').readlines()[5:]]).iloc[:, 1:-1].astype(float).values.ravel(),
        2001 : pd.read_excel('./2001/WPPI01', sheetname=1, skiprows=4).iloc[:, 1:-1].values.ravel(),
        2002 : pd.read_excel('./2002/WPPI02', sheetname=1, skiprows=4).iloc[:, 1:-1].values.ravel()
    },
    19436 : {
        1998 : pd.read_csv('./1998/AMER98', sep='\t').iloc[:, -1].str.strip().replace('na', 0).astype(float).values,
        1999 : pd.read_csv('./1999/AMER99', sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2000 : pd.read_csv('./2000/AMER00', sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2001 : pd.read_csv('./2001/AMER01', sep='\t').iloc[:, -1].astype(str).str.strip().replace('n/a', 0).astype(float).values,
        2002 : pd.read_csv('./2002/AMER02', sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2003 : pd.read_csv('./2003/AMER03', sep='\t', skiprows=1).iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2004 : pd.read_csv('./2004/AMER04', sep='\t', skiprows=1).iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values
    },
    4045 : {
        2000 : pd.read_excel('./2000/CWL00', skiprows=2).iloc[:, 1:].values.ravel(),
        2001 : pd.read_excel('./2001/CWL01', skiprows=1).iloc[:, 0].values,
        2002 : pd.read_excel('./2002/CWL02', header=None).iloc[:, 0].values,
        2003 : pd.read_excel('./2003/CWL03', header=None).iloc[:, 0].values
    }
}

# EEI
# Bizarre formatting until 1998

###### MAAC
# AE: 963
# BC: 1167
# DPL: 5027
# PU: 7088
# PN: 14715
# PE: 14940
# PEP: 15270
# PS: 15477
# PJM: 14725

# ALL UTILS

maac93 = pd.read_fwf('./1993/PJM93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
maac94 = pd.read_fwf('./1994/PJM94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
maac95 = pd.read_csv('./1995/PJM95', sep='\t', header=None, skipfooter=1)
maac96 = pd.read_csv('./1996/PJM96', sep='\t', header=None, skipfooter=1)

maac = {
    963 : {
            1993 : maac93[maac93[0].str.contains('AE')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('AE')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('AE')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('AE')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='ACE_LOAD').iloc[:, 1:25].values.ravel()
    },
    1167 : {
            1993 : maac93[maac93[0].str.contains('BC')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('BC')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('BC')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('BC')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='BC_LOAD').iloc[:, 1:25].values.ravel()
    },
    5027 : {
            1993 : maac93[maac93[0].str.contains('DP')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('DP')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('DP')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('DP')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='DPL_LOAD').iloc[:366, 1:25].values.ravel()
    },
    7088 : {
            1993 : maac93[maac93[0].str.contains('PU')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PU')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PU')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PU')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='GPU_LOAD').iloc[:366, 1:25].values.ravel()
    }
    14715 : {
            1997 : pd.read_excel('./1997/PJM97', sheetname='PN_LOAD').iloc[:366, 1:25].values.ravel()
    },
    14940 : {
            1993 : maac93[maac93[0].str.contains('PE$')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PE$')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PE$')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PE$')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='PE_Load').iloc[:366, 1:25].values.ravel()
    },
    15270 : {
            1993 : maac93[maac93[0].str.contains('PEP')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PEP')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PEP')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PEP')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='PEP_LOAD').iloc[:366, 1:25].values.ravel()
    },
    15477 : {
            1993 : maac93[maac93[0].str.contains('PS')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PS')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PS')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PS')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='PS_Load').iloc[:366, 1:25].values.ravel()
    },
    14725 : {
            1993 : maac93[maac93[0].str.contains('PJM')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PJM')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PJM')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PJM')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('./1997/PJM97', sheetname='PJM_LOAD').iloc[:366, 1:25].values.ravel(),
            1998 : pd.read_csv('./1998/PJM98', sep=' ', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
            1999 : pd.read_excel('./1999/PJM99', header=None)[2].values,
            2000 : pd.read_excel('./2000/PJM00', header=None)[2].values
    }
}

###### SERC
# AEC: 189
# CPL: 3046
# CEPC: 40218
# CEPB: 3408
# MEMP: 12293
# DUKE: 5416
# FPWC: 6235 *
# FLINT: 6411
# GUC: 7639
# LCEC: 10857
# NPL: 13204
# OPC: 13994
# SCEG: 17539
# SCPS: 17543
# SMEA: 17568
# TVA: 18642
# VIEP: 19876
# WEMC: 20065
# DU: 4958
# AECI: 924
# ODEC-D: 40229D
# ODEC-V: 40229V
# SOCO-APCO: 18195AL
# SOCO-GPCO: 18195GP
# SOCO-GUCO: 18195GU
# SOCO-MPCO: 18195MP
# SOCO-SECO: 18195SE

serc = {
    189 : {
        1993 : pd.read_csv('./1993/AEC93', sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_csv('./1994/AEC94', sep=' ', skipinitialspace=True, header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1995 : pd.read_csv('./1995/AEC95', sep=' ', skipinitialspace=True, header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('./1996/AEC96', sep=' ', skipinitialspace=True, header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('./1997/AEC97', sep=' ', skipinitialspace=True, header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/AEC98', sep=' ', skipinitialspace=True, header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1999 : pd.read_csv('./1999/AEC99', sep='\t', skipinitialspace=True, header=None, skiprows=3).iloc[:, 1:].values.ravel(),
        2000 : pd.read_csv('./2000/AEC00', sep='\t', skipinitialspace=True, header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        2001 : pd.read_csv('./2001/AEC01', sep='\t', skipinitialspace=True, header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('./2002/AEC02', sep='\t', skipinitialspace=True, header=None, skiprows=4).iloc[:, 1:].values.ravel(),
        2004 : pd.read_csv('./2004/AEC04', sep=' ', skipinitialspace=True, header=None, skiprows=4).iloc[:, 1:].values.ravel()
    },
    3046 : {
        1994 : pd.read_csv('./1994/CPL94', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        1995 : pd.read_csv('./1995/CPL95', sep=' ', skipinitialspace=True, header=None, skiprows=5)[1].values,
        1996 : pd.DataFrame([i.split() for i in open('./1996/CEPL96').readlines()[1:]])[2].astype(float).values,
        1997 : pd.DataFrame([i.split() for i in open('./1997/CPL97').readlines()[1:]])[2].astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('./1998/CPL98').readlines()[1:]])[2].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('./1999/CPL99').readlines()[1:]])[2].astype(float).values,
        2000 : pd.read_excel('./2000/CPL00')['Load'].values,
        2001 : pd.read_excel('./2001/CPL01')['Load'].values,
        2002 : pd.read_excel('./2002/CPL02')['Load'].values,
        2003 : pd.read_excel('./2003/CPL03')['Load'].values,
        2004 : pd.read_excel('./2004/CPL04')['Load'].values
    },
    40218 : {
        1993 : pd.read_fwf('./1993/CEPC93', header=None).iloc[:, 1:-1].values.ravel(),
        1994 : pd.read_csv('./1994/CEPC94', sep=' ', skipinitialspace=True, header=None, skiprows=1).iloc[:, 1:-1].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_csv('./1995/CEPC95', sep=' ', skipinitialspace=True, header=None).iloc[:, 1:-1].replace('.', '0').astype(float).values.ravel(),
        1996 : (pd.read_fwf('./1996/CEPC96').iloc[:-1, 1:]/1000).values.ravel(),
        1997 : (pd.DataFrame([i.split() for i in open('./1997/CEPC97').readlines()[5:]]).iloc[:-1, 1:].astype(float)/1000).values.ravel(),
        1998 : (pd.DataFrame([i.split() for i in open('./1998/CEPC98').readlines()]).iloc[:, 1:].astype(float)).values.ravel(),
        2000 : pd.read_excel('./2000/CEPC00', sheetname=1, skiprows=3)['MW'].values,
        2001 : pd.read_excel('./2001/CEPC01', sheetname=1, skiprows=3)['MW'].values,
        2002 : pd.read_excel('./2002/CEPC02', sheetname=0, skiprows=5)['MW'].values,
        2002 : pd.read_excel('./2002/CEPC02', sheetname=0, skiprows=5)['MW'].values
    },
    3408 : {
        1993 : (pd.DataFrame([i.split() for i in open('./1993/CEPB93').readlines()[12:]])[1].astype(float)/1000).values,
        1994 : (pd.DataFrame([i.split() for i in open('./1994/CEPB94').readlines()[10:]])[1].astype(float)).values,
        1995 : (pd.DataFrame([i.split() for i in open('./1995/CEPB95').readlines()[6:]])[2].astype(float)).values,
        1996 : (pd.DataFrame([i.split() for i in open('./1996/CEPB96').readlines()[10:]])[2].astype(float)).values,
        1997 : (pd.DataFrame([i.split() for i in open('./1997/CEPB97').readlines()[9:]])[2].astype(float)).values,
        1998 : (pd.DataFrame([i.split() for i in open('./1998/CEPB98').readlines()[9:]])[2].astype(float)).values,
        1999 : (pd.DataFrame([i.split() for i in open('./1999/CEPB99').readlines()[8:]])[2].astype(float)).values,
        2000 : (pd.DataFrame([i.split() for i in open('./2000/CEPB00').readlines()[11:]])[2].astype(float)).values,
        2001 : (pd.DataFrame([i.split() for i in open('./2001/CEPB01').readlines()[8:]])[2].astype(float)).values,
        2002 : (pd.DataFrame([i.split() for i in open('./2002/CEPB02').readlines()[6:]])[4].astype(float)).values,
        2003 : (pd.DataFrame([i.split() for i in open('./2003/CEPB03').readlines()[6:]])[2].astype(float)).values
    },
    12293 : {
        2000 : (pd.read_csv('./2000/MEMP00').iloc[:, -1]/1000).values,
        2001 : (pd.DataFrame([i.split() for i in open('./2001/MEMP01').readlines()[1:]])[3].str.replace(',', '').astype(float)/1000).values,
        2002 : (pd.read_csv('./2002/MEMP02', sep='\t').iloc[:, -1].str.replace(',', '').astype(float)/1000).values,
        2003 : pd.read_csv('./2003/MEMP03').iloc[:, -1].str.replace(',', '').astype(float).values
    },
    5416 : {
        1999 : pd.DataFrame([i.split() for i in open('./1999/DUKE99').readlines()[4:]])[2].astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('./2000/DUKE00').readlines()[5:]])[2].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('./2001/DUKE01').readlines()[5:]])[2].astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('./2002/DUKE02').readlines()[5:]])[2].astype(float).values,
        2003 : pd.DataFrame([i.split() for i in open('./2003/DUKE03').readlines()[5:-8]])[2].astype(float).values,
        2004 : pd.DataFrame([i.split() for i in open('./2004/DUKE04').readlines()[5:]])[2].astype(float).values
    },
    6411 : {
        1993 : (pd.DataFrame([i.split() for i in open('./1993/FLINT93').readlines()])[6].astype(float)/1000).values,
        1994 : ((pd.DataFrame([i.split() for i in open('./1994/FLINT94').readlines()[:-1]])).iloc[:, -1].astype(float)/1000).values,
        1995 : ((pd.DataFrame([i.split() for i in open('./1995/FLINT95').readlines()[1:]]))[3].astype(float)/1000).values,
        1996 : (pd.DataFrame([i.split() for i in open('./1996/FLINT96').readlines()[3:-2]]))[2].astype(float).values,
        1997 : (pd.DataFrame([i.split() for i in open('./1997/FLINT97').readlines()[6:]]))[3].astype(float).values,
        1998 : (pd.DataFrame([i.split() for i in open('./1998/FLINT98').readlines()[4:]]))[2].astype(float).values,
        1999 : (pd.DataFrame([i.split() for i in open('./1999/FLINT99').readlines()[1:]]))[1].astype(float).values,
        2000 : (pd.DataFrame([i.split() for i in open('./2000/FLINT00').readlines()[2:]]))[4].astype(float).values
    },
    7639 : {
        1993 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1993', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1993', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1994 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1994', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1994', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1995 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1995', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1995', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1996 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1996', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1996', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1997 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1997', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1997', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1998 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1998', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1998', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1999 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='1999', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='1999', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        2000 : np.concatenate([pd.read_excel('./2000/GUC00', sheetname='2000', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('./2000/GUC00', sheetname='2000', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
    },
    10857 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/LCEC93').readlines()[:-1]]).iloc[:, 3:].astype(float).values.ravel(),
        1994 : pd.DataFrame([i.split() for i in open('./1994/LCEC94').readlines()[:-1]]).iloc[:, 3:].astype(float).values.ravel()
    },
    13204 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/NPL93').readlines()[6:]])[2].astype(float).values,
        1994 : pd.read_fwf('./1994/NPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    13994 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/OPC93').readlines()[4:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1995 : pd.DataFrame([i.split() for i in open('./1995/OPC95').readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1996 : pd.DataFrame([i.split() for i in open('./1996/OPC96').readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1997 : pd.DataFrame([i.split() for i in open('./1997/OPC97').readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1998 : pd.DataFrame([i.split() for i in open('./1998/OPC98').readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('./1999/OPC99').readlines()[18:]])[2].astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('./2000/OPC00').readlines()[19:]])[2].astype(float).values
    },
    17539 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/SCEG93').readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1995 : pd.DataFrame([i.split() for i in open('./1995/SCEG95').readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1996 : pd.DataFrame([i.split() for i in open('./1996/SCEG96').readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1997 : pd.DataFrame([i.split() for i in open('./1997/SCEG97').readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('./1998/SCEG98').readlines()[:]]).iloc[:, -1].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('./1999/SCEG99').readlines()[:]]).iloc[:, -1].astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('./2000/SCEG00').readlines()[:]]).iloc[:, -1].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('./2001/SCEG01').readlines()[:]]).iloc[:, -1].astype(float).values
    },
    17543 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/SCPS93').readlines()[:]]).iloc[:, 1:].astype(float).values.ravel(),
        1996 : pd.DataFrame([i.split() for i in open('./1996/SCPS96').readlines()[:-1]]).astype(float).values.ravel(),
        1997 : pd.DataFrame([i.split() for i in open('./1997/SCPS97').readlines()[1:-3]]).iloc[:, 4:-1].astype(float).values.ravel(),
        1998 : pd.DataFrame([i.split() for i in open('./1998/SCPS98').readlines()[:-1]]).iloc[:, 1:].replace('NA', '0').astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('./1999/SCPS99').readlines()[1:-1]]).iloc[:, 2:-1].replace('NA', '0').astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split() for i in open('./2000/SCPS00').readlines()[:]]).iloc[:, 2:].replace('NA', '0').astype(float).values.ravel(),
        2001 : pd.DataFrame([i.split() for i in open('./2001/SCPS01').readlines()[:]]).iloc[:, 2:].replace('NA', '0').astype(float).values.ravel(),
        2002 : pd.read_excel('./2002/SCPS02', header=None).dropna(axis=1, how='all').iloc[:, 2:-1].values.ravel(),
        2003 : pd.DataFrame([i.split() for i in open('./2003/SCPS03').readlines()[:]]).iloc[:, 2:].replace('NA', '0').astype(float).values.ravel(),
        2004 : pd.DataFrame([i.split() for i in open('./2004/SCPS04').readlines()[1:]]).iloc[:, 1:-1].replace('NA', '0').astype(float).values.ravel()
    },
    17568 : {
        1993 : (pd.DataFrame([i.split() for i in open('./1993/SMEA93').readlines()[5:]])[2].astype(float)/1000).values.ravel(),
        1994 : (pd.DataFrame([i.split() for i in open('./1994/SMEA94').readlines()[5:]]).iloc[:, -1].astype(float)).values,
        1996 : ((pd.DataFrame([i.split() for i in open('./1996/SMEA96').readlines()[:]])).iloc[:, -24:].astype(float)/1000).values.ravel(),
        1997 : pd.read_excel('./1997/SMEA97', sheetname=1, header=None, skiprows=1).iloc[:, 1:].values.ravel(,
        1998 : pd.DataFrame([i.split() for i in open('./1998/SMEA98').readlines()[1:]])[2].astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('./1999/SMEA99').readlines()[1:]])[2].astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split() for i in open('./2000/SMEA00').readlines()[1:]])[2].astype(float).values.ravel(),
        2002 : pd.DataFrame([i.split() for i in open('./2002/SMEA02').readlines()[2:]])[2].astype(float).values.ravel(),
        2003 : pd.DataFrame([i.split() for i in open('./2003/SMEA03').readlines()[1:]])[2].astype(float).values.ravel()
    },
    18642 : {
        1993 : (pd.DataFrame([i.split() for i in open('./1993/TVA93').readlines()[:-1]])[2].astype(float)).values.ravel(),
        1994 : (pd.DataFrame([i.split() for i in open('./1994/TVA94').readlines()[:-1]])[2].astype(float)).values.ravel(),
        1995 : (pd.DataFrame([i.split() for i in open('./1995/TVA95').readlines()[:-1]])[2].astype(float)).values.ravel(),
        1996 : (pd.DataFrame([i.split() for i in open('./1996/TVA96').readlines()[:-1]])[2].astype(float)).values.ravel(),
        1997 : (pd.DataFrame([i.split() for i in open('./1997/TVA97').readlines()[:-1]])[2].astype(float)).values.ravel(),
        1998 : (pd.DataFrame([i.split() for i in open('./1998/TVA98').readlines()[:-1]])[2].astype(float)).values.ravel(),
        1999 : pd.read_excel('./1999/TVA99').iloc[:, 2].astype(float).values,
        2000 : pd.read_excel('./2000/TVA00').iloc[:, 2].astype(float).values,
        2001 : pd.read_excel('./2001/TVA01', header=None, skiprows=3).iloc[:, 2].astype(float).values,
        2003 : pd.read_excel('./2003/TVA03').iloc[:, -1].values
    },
    19876 : {
        1993 : pd.read_fwf('./1993/VIEP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/VIEP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/VIEP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/VIEP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/VIEP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('./1998/VIEP98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/VIEP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2000 : (pd.DataFrame([i.split() for i in open('./2000/VIEP00').readlines()[1:]])[2].astype(float)).values.ravel(),
        2001 : (pd.DataFrame([i.split() for i in open('./2001/VIEP01').readlines()[1:]])[2].astype(float)).values.ravel(),
        2002 : (pd.DataFrame([i.split() for i in open('./2002/VIEP02').readlines()[1:]])[2].astype(float)).values.ravel(),
        2003 : (pd.DataFrame([i.split() for i in open('./2003/VIEP03').readlines()[2:]])[3].astype(float)).values.ravel(),
        2004 : (pd.DataFrame([i.split() for i in open('./2004/VIEP04').readlines()[:]])[3].astype(float)).values.ravel()
    },
    20065 : {
        1993 : pd.read_fwf('./1993/WEMC93', header=None).iloc[:, 1:].values.ravel(),
        1995 : (pd.read_csv('./1995/WEMC95', skiprows=1, header=None, sep=' ', skipinitialspace=True)[3]/1000).values,
        1996 : (pd.read_excel('./1996/WEMC96')['Load']/1000).values,
        1997 : pd.read_excel('./1997/WEMC97', skiprows=4)['MW'].values,
        1998 : pd.concat([pd.read_excel('./1998/WEMC98', sheetname=i).iloc[:, -1] for i in range(12)]),
        1999 : pd.read_excel('./1999/WEMC99')['mwh'].values,
        2000 : (pd.read_excel('./2000/WEMC00').iloc[:, -1]/1000).values,
        2001 : (pd.read_excel('./2001/WEMC01', header=None)[0]/1000).values
    },
    4958 : {
        1999 : (pd.DataFrame([i.split() for i in open('./1999/DU99').readlines()[1:]]).iloc[:-1, 2:].apply(lambda x: x.str.replace('[,"]', '').str.strip()).astype(float)/1000).values.ravel(),
        2000 : (pd.DataFrame([i.split() for i in open('./2000/DU00').readlines()[1:]]).iloc[:-1, 2:].apply(lambda x: x.str.replace('[,"]', '').str.strip()).astype(float)/1000).values.ravel(),
        2003 : pd.read_excel('./2003/DU03').iloc[:, -1].values
    },
    924 : {
        1999 : pd.read_excel('./1999/AECI99')['CALoad'].values,
        2001 : pd.read_excel('./2001/AECI01').iloc[:, -1].values,
        2002 : pd.Series(pd.read_excel('./2002/AECI02', skiprows=3).loc[:, 'Jan':'Dec'].values.ravel(order='F')).dropna().values
    },
    '40229D' : {
        1996 : pd.Series(pd.DataFrame([i.split() for i in open('./1996/ODECD96').readlines()[3:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1997 : pd.Series(pd.DataFrame([i.split() for i in open('./1997/ODECD97').readlines()[4:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1998 : pd.Series(pd.DataFrame([i.split() for i in open('./1998/ODECD98').readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1999 : pd.Series(pd.DataFrame([i.split() for i in open('./1999/ODECD99').readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('./2000/ODECD00').readlines()[3:]])[4].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('./2001/ODECD01').readlines()[3:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('./2002/ODECD02').readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2003 : pd.DataFrame([i.split() for i in open('./2003/ODECD03').readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2004 : pd.DataFrame([i.split() for i in open('./2004/ODECD04').readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values
    },
    '40229V' : {
        1996 : pd.Series(pd.DataFrame([i.split() for i in open('./1996/ODECV96').readlines()[3:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1997 : pd.Series(pd.DataFrame([i.split() for i in open('./1997/ODECV97').readlines()[4:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1998 : pd.Series(pd.DataFrame([i.split() for i in open('./1998/ODECV98').readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1999 : pd.Series(pd.DataFrame([i.split() for i in open('./1999/ODECV99').readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('./2000/ODECV00').readlines()[3:]])[4].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('./2001/ODECV01').readlines()[3:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('./2002/ODECV02').readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2003 : pd.DataFrame([i.split() for i in open('./2003/ODECV03').readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2004 : pd.DataFrame([i.split() for i in open('./2004/ODECV04').readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values
    },
    '18195AL' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('./1993/APCO93').readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('./1994/APCO94').readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('./1999/SOCO99')['Alabama'].dropna().values,
        2000 : pd.read_excel('./2000/SOCO00', skiprows=1).iloc[:, 2].values,
        2001 : pd.read_excel('./2001/SOCO01')['Alabama'].values,
        2002 : pd.read_excel('./2002/SOCO02', skiprows=1).iloc[:, 2].values,
        2003 : pd.read_excel('./2003/SOCO03').iloc[:, 2].values,
        2004 : pd.read_excel('./2004/SOCO04', skiprows=1).iloc[:, 1].values
    },
    '18195GP' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('./1993/GPCO93').readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('./1994/GPCO94').readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('./1999/SOCO99')['Georgia'].dropna().values,
        2000 : pd.read_excel('./2000/SOCO00', skiprows=1).iloc[:, 3].values,
        2001 : pd.read_excel('./2001/SOCO01')['Georgia'].values,
        2002 : pd.read_excel('./2002/SOCO02', skiprows=1).iloc[:, 3].values,
        2003 : pd.read_excel('./2003/SOCO03').iloc[:, 3].values,
        2004 : pd.read_excel('./2004/SOCO04', skiprows=1).iloc[:, 2].values
    },
    '18195GU' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('./1993/GUCO93').readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('./1994/GUCO94').readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('./1999/SOCO99')['Gulf'].dropna().values,
        2000 : pd.read_excel('./2000/SOCO00', skiprows=1).iloc[:, 4].values,
        2001 : pd.read_excel('./2001/SOCO01')['Gulf'].values,
        2002 : pd.read_excel('./2002/SOCO02', skiprows=1).iloc[:, 4].values,
        2003 : pd.read_excel('./2003/SOCO03').iloc[:, 4].values,
        2004 : pd.read_excel('./2004/SOCO04', skiprows=1).iloc[:, 3].values
    },
    '18195MP' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('./1993/MPCO93').readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('./1994/MPCO94').readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('./1999/SOCO99')['Mississippi'].dropna().values,
        2000 : pd.read_excel('./2000/SOCO00', skiprows=1).iloc[:, 5].values,
        2001 : pd.read_excel('./2001/SOCO01')['Mississippi'].values,
        2002 : pd.read_excel('./2002/SOCO02', skiprows=1).iloc[:, 5].values,
        2003 : pd.read_excel('./2003/SOCO03').iloc[:, 5].values,
        2004 : pd.read_excel('./2004/SOCO04', skiprows=1).iloc[:, 4].values
    },
    '18195SE' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('./1993/SECO93').readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('./1994/SECO94').readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('./1999/SOCO99')['Savannah'].dropna().values,
        2000 : pd.read_excel('./2000/SOCO00', skiprows=1).iloc[:, 6].values,
        2001 : pd.read_excel('./2001/SOCO01')['Savannah'].values,
        2002 : pd.read_excel('./2002/SOCO02', skiprows=1).iloc[:, 6].values,
        2003 : pd.read_excel('./2003/SOCO03').iloc[:, 6].values,
        2004 : pd.read_excel('./2004/SOCO04', skiprows=1).iloc[:, 5].values
    }
}

###### SPP
# AECC: 807
# CAJN: 2777
# CLEC: 3265
# EMDE: 5860
# ENTR: 12506
# KCPU: 9996
# LEPA: 26253
# LUS: 9096
# GSU: 7806
# MPS: 12699
# OKGE: 14063
# OMPA: 14077
# PSOK: 15474
# SEPC: 18315
# WFEC: 20447
# WPEK: 20391
# CSWS: 3283
# SRGT: 40233
# GSEC: 7349

spp = {
    807 : {
        1993 : pd.read_csv('./1993/AECC93', skiprows=6, skipfooter=1, header=None).iloc[:, -1].values,
        1994 : pd.read_csv('./1994/AECC94', skiprows=8, skipfooter=1, header=None).iloc[:, -1].values,
        1995 : pd.read_csv('./1995/AECC95', skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1996 : pd.read_csv('./1996/AECC96', skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1997 : pd.read_csv('./1997/AECC97', skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1998 : pd.read_csv('./1998/AECC98', skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1999 : pd.read_csv('./1999/AECC99', skiprows=5, skipfooter=1, header=None).iloc[:, -1].values,
        2003 : pd.read_csv('./2003/AECC03', skiprows=5, skipfooter=1, header=None).iloc[:, -2].values,
        2004 : pd.read_csv('./2004/AECC04', skiprows=5, header=None).iloc[:, -2].values
    },
    2777 : {
        1998 : pd.read_excel('./1998/CAJN98', skiprows=4).iloc[:365, 1:].values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('./1999/CAJN99').readlines()[:]])[2].astype(float).values
    },
    3265 : {
        1994 : pd.read_fwf('./1994/CLEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.DataFrame([i.split() for i in open('./1996/CLEC96').readlines()[:]])[0].astype(float).values,
        1997 : pd.read_csv('./1997/CLEC97').iloc[:, 2].str.replace(',', '').astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('./1998/CLEC98').readlines()[:]])[1].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('./1999/CLEC99').readlines()[1:]]).iloc[:, 0].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('./2001/CLEC01').readlines()[:]])[4].replace('NA', '0').astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('./2002/CLEC02').readlines()[:]])[4].replace('NA', '0').astype(float).values
    },
    5860 : {
        1997 : pd.DataFrame([i.split() for i in open('./1997/EMDE97').readlines()[:]])[3].astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('./1998/EMDE98').readlines()[2:-2]])[2].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('./1999/EMDE99').readlines()[3:8763]])[2].astype(float).values,
        2001 : pd.read_excel('./2001/EMDE01')['Load'].dropna().values,
        2002 : pd.read_excel('./2002/EMDE02')['Load'].dropna().values,
        2003 : pd.read_excel('./2003/EMDE03')['Load'].dropna().values,
        2004 : pd.read_excel('./2004/EMDE04', skiprows=2).iloc[:8784, -1].values
    },
    12506 : {
        1994 : pd.DataFrame([i.split() for i in open('./1994/ENTR94').readlines()[:]]).iloc[:, 1:-1].astype(float).values.ravel(),
        1995 : pd.DataFrame([i.split() for i in open('./1995/ENTR95').readlines()[1:-2]]).iloc[:, 1:-1].astype(float).values.ravel(),
        1997 : pd.read_csv('./1997/ENTR97', header=None).iloc[:, 1:-1].astype(float).values.ravel(),
        1998 : pd.read_csv('./1998/ENTR98', header=None)[2].astype(float).values,
        1999 : pd.read_excel('./1999/ENTR99').iloc[:, -1].values,
        2000 : pd.DataFrame([i.split() for i in open('./2000/ENTR00').readlines()[4:]]).iloc[:, 3:].astype(float).values.ravel(),
        2001 : pd.read_fwf('./2001/ENTR01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    9996 : {
        1994 : pd.read_fwf('./1994/KCPU94', skiprows=4, header=None).astype(str).apply(lambda x: x.str[-3:]).astype(float).values.ravel(),
        1997 : pd.read_csv('./1997/KCPU97', engine='python', header=None)[0].values,
        1998 : pd.read_csv('./1998/KCPU98', engine='python', header=None)[0].values,
        1999 : pd.read_csv('./1999/KCPU99', skiprows=1, engine='python', header=None)[0].values,
        2000 : pd.read_csv('./2000/KCPU00', engine='python', header=None)[0].values,
        2002 : pd.read_excel('./2002/KCPU02').iloc[:, -1].values,
        2003 : pd.read_csv('./2003/KCPU03', engine='python', header=None)[0].values,
        2004 : pd.read_csv('./2004/KCPU04', engine='python', header=None)[0].values
    },
    26253 : {
        1993 : pd.read_csv('./1993/LEPA93', skiprows=3, header=None)[0].values,
        1994 : pd.read_csv('./1994/LEPA94', skiprows=3, header=None)[0].values,
        1995 : pd.read_csv('./1995/LEPA95', sep='\t', skiprows=1, header=None)[2].values,
        1996 : pd.read_csv('./1996/LEPA96', sep='\t', skiprows=1, header=None)[2].values,
        1997 : pd.read_csv('./1997/LEPA97', engine='python', header=None)[0].values,
        1998 : pd.read_csv('./1998/LEPA98', sep=' ', skipinitialspace=True, skiprows=2, header=None),
        1998 : pd.Series(pd.read_csv('./1998/LEPA98', sep=' ', skipinitialspace=True, skiprows=2, header=None)[[1,3]].values.ravel(order='F')).dropna().values,
        1999 : pd.read_csv('./1999/LEPA99', sep='\t')['Load'].values,
        2001 : pd.read_csv('./2001/LEPA01', engine='python', sep='\t', header=None)[1].values,
        2002 : pd.read_csv('./2002/LEPA02', engine='python', sep='\t', header=None)[1].values,
        2003 : pd.read_excel('./2003/LEPA03', header=None)[1].values
    },
    9096 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/LUS93').readlines()[3:-1]]).iloc[:, -1].astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('./1994/LUS94').readlines()[3:-1]]).iloc[:, -1].astype(float).values,
        1995 : pd.DataFrame([i.split() for i in open('./1995/LUS95').readlines()[4:-1]]).iloc[:, -1].astype(float).values,
        1996 : pd.DataFrame([i.split() for i in open('./1996/LUS96').readlines()[4:-1]]).iloc[:, -1].astype(float).values,
        1997 : pd.DataFrame([i.split('\t') for i in open('./1997/LUS97').readlines()[3:-2]]).iloc[:, -1].astype(float).values,
        1998 : pd.DataFrame([i.split('\t') for i in open('./1998/LUS98').readlines()[4:]]).iloc[:, -1].astype(float).values,
        1999 : pd.DataFrame([i.split('  ') for i in open('./1999/LUS99').readlines()[4:]]).iloc[:, -1].astype(float).values,
        2000 : pd.read_csv('./2000/LUS00', skiprows=3, skipfooter=1, header=None).iloc[:, -1].values,
        2001 : pd.read_csv('./2001/LUS01', skiprows=3, header=None).iloc[:, -1].values,
        2002 : pd.read_csv('./2002/LUS02', skiprows=3, header=None).iloc[:, -1].values,
        2003 : pd.read_csv('./2003/LUS03', skiprows=3, header=None).iloc[:, -1].values,
        2004 : pd.read_csv('./2004/LUS04', skiprows=4, header=None).iloc[:, -1].values
    },
    7806 : {
        1993 : pd.read_csv('./1993/GSU93', engine='python', header=None)[0].values
    },
    12699 : {
        1993 : pd.read_csv('./1993/MPS93', sep=' ', skipinitialspace=True)['TOTLOAD'].values,
        1996 : pd.read_excel('./1996/MPS96', skiprows=6, header=None).iloc[:, -1].values,
        1998 : pd.read_csv('./1998/MPS98', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2000 : pd.read_csv('./2000/MPS00', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2001 : pd.read_csv('./2001/MPS01', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2002 : pd.read_csv('./2002/MPS02', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2003 : pd.read_excel('./2003/MPS03').iloc[:, 1:].values.ravel()
    },
    14063 : {
        1994 : pd.read_csv('./1994/OKGE94', header=None).iloc[:, 1:13].values.ravel()
    },
    14077 : {
        1993 : pd.read_csv('./1993/OMPA93', skiprows=2, header=None, sep=' ', skipinitialspace=True, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('./1997/OMPA97', engine='python', header=None)[0].values,
        1998 : pd.read_csv('./1998/OMPA98', skiprows=2, engine='python', header=None)[0].str.replace('\*', '').astype(float).values,
        2000 : pd.read_csv('./2000/OMPA00', skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2001 : pd.read_csv('./2001/OMPA01', skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2002 : pd.read_csv('./2002/OMPA02', skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2003 : pd.read_csv('./2003/OMPA03', skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2004 : pd.read_csv('./2004/OMPA04', skiprows=2, engine='python', header=None)[0].astype(float).values/1000
    },
    15474 : {
        1993 : pd.read_fwf('./1993/PSOK93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    18315 : {
        1993 : pd.read_csv('./1993/SEPC93', header=None).iloc[:, 1:].astype(str).apply(lambda x: x.str.replace('NA', '').str.strip()).replace('', '0').astype(float).values.ravel(),
        1997 : (pd.read_fwf('./1997/SEPC97', skiprows=1, header=None)[5]/1000).values,
        1999 : pd.read_csv('./1999/SEPC99', sep='\t', skipinitialspace=True, header=None)[3].str.strip().replace('#VALUE!', '0').astype(float).values,
        2000 : pd.read_csv('./2000/SEPC00', sep='\t', skipinitialspace=True, header=None)[3].apply(lambda x: 0 if len(x) > 3 else x).astype(float).values,
        2001 : pd.read_csv('./2001/SEPC01', sep='\t', skipinitialspace=True, header=None)[3].apply(lambda x: 0 if len(x) > 3 else x).astype(float).values,
        2002 : (pd.read_fwf('./2002/SEPC02', skiprows=1, header=None)[6]).str.replace('"', '').str.strip().astype(float).values,
        2004 : pd.read_csv('./2004/SEPC04', header=None, sep='\t')[5].values
    },
    20447 : {
        1993 : pd.read_csv('./1993/WFEC93').iloc[:, 0].values,
        2000 : pd.read_csv('./2000/WFEC00', header=None, sep=' ', skipinitialspace=True)[0].values
    },
    20391 : {
        1993 : pd.DataFrame([i.split() for i in open('./1993/WPEK93').readlines()[:]]).iloc[:365, 1:25].astype(float).values.ravel(),
        1996 : pd.read_excel('./1996/WPEK96', skiprows=2).dropna().iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/WPEK98', header=None, sep=' ', skipinitialspace=True)[6].values,
        2000 : pd.read_csv('./2000/WPEK00', header=None, sep=' ', skipinitialspace=True)[6].values,
        2001 : pd.read_csv('./2001/WPEK01', header=None, sep=' ', skipinitialspace=True)[6].values,
        2002 : pd.read_csv('./2002/WPEK02', header=None, sep=' ', skipinitialspace=True)[4].values
    },
    3283 : {
        1997 : pd.read_fwf('./1997/CSWS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/CSWS98', skiprows=4, sep=' ', skipinitialspace=True, header=None)[2].values,
        1999 : pd.read_csv('./1999/CSWS99', skiprows=3, sep=' ', skipinitialspace=True, header=None)[2].values,
        2000 : pd.read_csv('./2000/CSWS00', skiprows=5, sep=' ', skipinitialspace=True, header=None)[2].values
    },
    40233 : {
        2000 : pd.read_fwf('./2000/SRGT00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2001 : pd.read_fwf('./2001/SRGT01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    7349 : {
        1997 : pd.read_csv('./1997/GSEC97', sep=' ', skipinitialspace=True, skiprows=2, header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('./1998/GSEC98', sep=' ', skipinitialspace=True, skiprows=2, header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_csv('./1999/GSEC99', sep='\s', skipinitialspace=True, skiprows=2, header=None)[17].dropna().values,
        2000 : pd.read_csv('./2000/GSEC00', skiprows=1, engine='python', header=None)[0].values,
        2001 : pd.DataFrame([i.split() for i in open('./2001/GSEC01').readlines()[1:]])[0].astype(float).values,
        2002 : pd.read_csv('./2002/GSEC02', sep=' ', skipinitialspace=True, skiprows=2, header=None)[5].values,
        2003 : pd.read_csv('./2003/GSEC03', header=None)[2].values,
        2004 : (pd.read_csv('./2004/GSEC04', sep=' ', skipinitialspace=True, skiprows=1, header=None)[5]/1000).values
    }
}

###### MAPP
# CIPC: 3258
# CP: 4322
# CBPC: 4363
# DPC: 4716
# HUC: 9130
# IES: 9219
# IPW: 9392
# IIGE: 9438
# LES: 11018
# MPL: 12647
# MPC: 12658
# MDU: 12819
# MEAN: 21352
# MPW: 13143
# NPPD: 13337
# NSP: 13781
# NWPS: 13809
# OPPD: 14127
# OTP: 14232
# SMMP: 40580
# UPA: 19514
# WPPI: 20858
# MEC: 9435
# CPA: 4322
# MWPS: 23333

mapp = {
3258 : {
    1998 : pd.read_fwf('./1998/CIPC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
4322 : {
    1993 : pd.read_fwf('./1993/CP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/CP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/CP96', header=None).iloc[:, 2:].values.ravel()
},
4363 : {
    1993 : pd.read_fwf('./1993/CBPC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/CBPC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/CBPC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/CBPC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/CBPC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/CB02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
},
4716 : {
    1993 : pd.read_fwf('./1993/DPC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/DPC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_csv('./1996/DPC96', sep='\t', skipinitialspace=True, header=None).iloc[:, 6:].values.ravel()
},
9130 : {
    1993 : pd.read_fwf('./1993/HUC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/HUC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_fwf('./1996/HUC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1997 : pd.read_fwf('./1997/HUC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1998 : pd.read_fwf('./1998/HUC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1999 : pd.read_fwf('./1999/HUC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2002 : pd.read_fwf('./2002/HUC02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/HUC03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
9219 : {
    1993 : pd.read_fwf('./1993/IESC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/IES94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/IESC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/IES97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/IESC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
9392 : {
    1993 : pd.read_fwf('./1993/IPW93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/IPW94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1995 : pd.read_fwf('./1995/IPW95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_fwf('./1996/IPW96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1997 : pd.read_fwf('./1997/IPW97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, range(1,13)+range(14,26)].values.ravel(),
    1998 : pd.read_fwf('./1998/IPW98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
9438 : {
    1993 : pd.read_fwf('./1993/IIGE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/IIGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_fwf('./1995/IIGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
},
11018 : {
    1993 : pd.read_fwf('./1993/LES93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/LES94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1995 : pd.read_csv('./1995/LES95').iloc[:, 1:].values.ravel(),
    1996 : pd.read_fwf('./1996/LES96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1997 : pd.read_fwf('./1997/LES97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1998 : pd.read_fwf('./1998/LES98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1999 : pd.read_fwf('./1999/LES99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2000 : pd.read_excel('./2000/LES00', skipfooter=3).iloc[:, 1:].values.ravel(),
    2001 : pd.read_excel('./2001/LES01', skipfooter=3).iloc[:, 1:].values.ravel(),
    2002 : pd.read_fwf('./2002/LES02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/LES03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
12647 : {
    1995 : pd.read_fwf('./1995/MPL95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2000 : pd.read_fwf('./2000/MPL00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2001 : pd.read_fwf('./2001/MPL01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
},
12658 : {
    1993 : pd.read_fwf('./1993/MPC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/MPC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1995 : pd.read_fwf('./1995/MPC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_fwf('./1996/MPC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/MPC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/MPC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/MPC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/MPC02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/MPC03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
12819 : {
    1993 : pd.read_fwf('./1993/MDU93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/MDU94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, range(1,13)+range(14,26)].values.ravel(),
    1995 : pd.read_fwf('./1995/MDU95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_fwf('./1996/MDU96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1997 : pd.read_fwf('./1997/MDU97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1998 : pd.read_fwf('./1998/MDU98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1999 : pd.read_fwf('./1999/MDU99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2002 : pd.read_fwf('./2002/MDU02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/MDU03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
21352 : {
    1993 : pd.read_fwf('./1993/MEAN93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_fwf('./1995/MEAN95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
    1996 : pd.read_fwf('./1996/MEAN96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
    1997 : pd.read_fwf('./1997/MEAN97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
    1998 : pd.read_fwf('./1998/MEAN98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
    1999 : pd.read_fwf('./1999/MEAN99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
    2002 : pd.read_fwf('./2002/MEAN02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/MEAN03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
13143 : {
    1993 : pd.read_fwf('./1993/MPW93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/MPW94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1995 : pd.read_fwf('./1995/MPW95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_fwf('./1996/MPW96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1997 : pd.read_fwf('./1997/MPW97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, range(1,13)+range(14,26)].values.ravel(),
    1998 : pd.read_fwf('./1998/MPW98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1999 : pd.read_fwf('./1999/MPW99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2002 : pd.read_fwf('./2002/MPW02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/MPW03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
13337 : {
    1993 : pd.read_fwf('./1993/NPPD93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/NPPD94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_fwf('./1995/NPPD95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/NPPD96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/NPPD97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/NPPD98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/NPPD99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2000 : pd.read_fwf('./2000/NPPD00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=9, skipfooter=1).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2001 : pd.read_fwf('./2001/NPPD01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=9, skipfooter=1).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_csv('./2002/NPPD02', sep='\t', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
    2003 : pd.read_fwf('./2003/NPPD03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
13781 : {
    1993 : pd.read_fwf('./1993/NSP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1994 : pd.read_fwf('./1994/NSP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1996 : pd.read_fwf('./1996/NSP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1997 : pd.read_fwf('./1997/NSP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/NSP98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    1999 : pd.read_fwf('./1999/NSP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2000 : pd.read_csv('./2000/NSP00', sep='\t', skipinitialspace=True, skiprows=2, header=None, skipfooter=1)[2].values
},
13809 : {
    1993 : pd.read_fwf('./1993/NWPS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_fwf('./1995/NWPS95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/NWPS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/NWPS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/NWPS98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/NWPS99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/NWPS02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/NWPS03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
},
14127 : {
    1993 : pd.read_fwf('./1993/OPPD93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/OPPD94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_csv('./1995/OPPD95', sep='\t', skipinitialspace=True, header=None).iloc[:, 7:].values.ravel(),
    1996 : pd.read_fwf('./1996/OPPD96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/OPPD97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/OPPD98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/OPPD99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/OPPD02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
    2003 : pd.read_fwf('./2003/OPPD03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
},
14232 : {
    1993 : pd.read_fwf('./1993/OTP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/OTP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_csv('./1995/OTP95', header=None).iloc[:, -2].values.ravel(),
    1996 : pd.read_fwf('./1996/OTP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/OTP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/OTP98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/OTP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2000 : pd.read_fwf('./2000/OTP00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/OTP02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    2003 : pd.read_fwf('./2003/OTP03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
},
40580 : {
    1993 : pd.read_fwf('./1993/SMMP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1994 : pd.read_fwf('./1994/SMP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/SMMP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/SMMP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1998 : pd.read_fwf('./1998/SMMP98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/SMMPA99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2000 : pd.read_csv('./2000/SMMP00').iloc[:-1, 3].values,
    2001 : pd.read_csv('./2001/SMMP01', header=None).iloc[:, 2].values,
    2002 : pd.read_fwf('./2002/SMMPA02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    2003 : pd.read_fwf('./2003/SMMPA03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
},
19514 : {
    1993 : pd.read_fwf('./1993/UPA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1994 : pd.read_fwf('./1994/UPA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1996 : pd.read_fwf('./1996/UPA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1997 : pd.read_fwf('./1997/UPA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1998 : pd.read_fwf('./1998/UPA98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
},
20858 : {
    1993 : pd.read_fwf('./1993/WPPI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1994 : pd.read_fwf('./1994/WPPI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1996 : pd.read_fwf('./1996/WPPI96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_csv('./1997/WPPI97', sep=' ', skipinitialspace=True, header=None).iloc[:, 2:-1].values.ravel(),
    1998 : pd.read_fwf('./1998/WPPI98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/WPPI99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/WPPI02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    2003 : pd.read_fwf('./2003/WPPI03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
},
9435 : {
    1995 : pd.read_fwf('./1995/MEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/MEC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1997 : pd.read_fwf('./1997/MEC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    1998 : pd.read_fwf('./1998/MEC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1999 : pd.read_fwf('./1999/MEC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2000 : pd.read_fwf('./2000/MEC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    2002 : pd.read_fwf('./2002/MEC02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
    2003 : pd.read_fwf('./2003/MEC_ALL03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
},
4322 : {
    1993 : pd.read_fwf('./1993/CP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/CP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1996 : pd.read_fwf('./1996/CP96', header=None).iloc[:, 2:].values.ravel()
},
23333 : {
    1993 : pd.read_fwf('./1993/MPSI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1994 : pd.read_fwf('./1994/MPSI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
    1995 : pd.read_fwf('./1995/MPSI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
}
}
