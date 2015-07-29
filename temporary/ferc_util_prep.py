import numpy as np
import pandas as pd
import os
import datetime

homedir = os.path.expanduser('~')
datadir = 'github/RIPS_kircheis/data/eia_form_714/processed/'
fulldir = homedir + '/' + datadir

# li = []

# for d1 in os.listdir('.'):
#     for fn in os.listdir('./%s' % d1):
#         li.append(fn)

# dir_u = pd.Series(li).str[:-2].order().unique()

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
        1993 : pd.read_fwf('%s/npcc/1993/BECO93' % (fulldir), header=None, skipfooter=1).loc[:, 2:].values.ravel(),
        1994 : pd.read_csv('%s/npcc/1994/BECO94' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[4].values,
        1995 : pd.read_csv('%s/npcc/1995/BECO95' % (fulldir), sep =' ', skipinitialspace=True,  header=None)[4].values,
        1996 : pd.read_csv('%s/npcc/1996/BECO96' % (fulldir), sep =' ', skipinitialspace=True,  header=None)[4].values,
        1997 : pd.read_csv('%s/npcc/1997/BECO97' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[4].values,
        1998 : pd.read_csv('%s/npcc/1998/BECO98' % (fulldir), sep =' ', skipinitialspace=True,  header=None)[4].values,
        1999 : pd.read_csv('%s/npcc/1999/BECO99' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2000 : pd.read_csv('%s/npcc/2000/BECO00' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2001 : pd.read_csv('%s/npcc/2001/BECO01' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2002 : pd.read_csv('%s/npcc/2002/BECO02' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2003 : pd.read_csv('%s/npcc/2003/BECO03' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values,
        2004 : pd.read_csv('%s/npcc/2004/BECO04' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skiprows=3)[4].values
    },
    1179 : {
            1993 : pd.read_csv('%s/npcc/1993/BHE93' % (fulldir), sep=' ', skiprows=2, skipinitialspace=True).loc[:, '0000':].values.ravel(),
            1994 : pd.read_csv('%s/npcc/1994/BHE94' % (fulldir)).dropna(how='all').loc[:729, '1/13':'12/24'].values.ravel(),
            1995 : pd.read_fwf('%s/npcc/1995/BHE95' % (fulldir)).loc[:729, '1/13':'1224'].values.ravel(),
            2001 : pd.read_excel('%s/npcc/2001/BHE01' % (fulldir), skiprows=2).iloc[:, 1:24].values.ravel(),
            2003 : pd.read_excel('%s/npcc/2003/BHE03' % (fulldir), skiprows=3).iloc[:, 1:24].values.ravel()
    },
    2886 : {
            1999 : pd.read_csv('%s/npcc/1999/CELC99' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2000 : pd.read_csv('%s/npcc/2000/CELC00' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2001 : pd.read_csv('%s/npcc/2001/CELC01' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2002 : pd.read_csv('%s/npcc/2002/CELC02' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2003 : pd.read_csv('%s/npcc/2003/CELC03' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
            2004 : pd.read_csv('%s/npcc/2004/CELC04' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values
    },
    3249 : {
            1993 : pd.read_csv('%s/npcc/1993/CHGE93' % (fulldir), sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[2].values,
            1994 : pd.read_fwf('%s/npcc/1994/CHGE94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('%s/npcc/1995/CHGE95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('%s/npcc/1996/CHGE96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1997 : pd.read_csv('%s/npcc/1997/CHGE97' % (fulldir), sep ='\s', skipinitialspace=True,  header=None, skipfooter=1).iloc[:, 4:].values.ravel(),
            1998 : pd.read_excel('%s/npcc/1998/CHGE98' % (fulldir), skipfooter=1, header=None).iloc[:, 2:].values.ravel(),
    },
    3266 : {
            1993 : pd.read_fwf('%s/npcc/1993/CMP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1994 : pd.read_fwf('%s/npcc/1994/CMP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('%s/npcc/1995/CMP95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('%s/npcc/1996/CMP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('%s/npcc/1997/CMP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1999 : pd.read_fwf('%s/npcc/1999/CMP99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            2002 : pd.read_fwf('%s/npcc/2002/CMP02' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
            2003 : pd.read_fwf('%s/npcc/2003/CMP03' % (fulldir), header=None).iloc[:, 1:].values.ravel()
    },
    4226 : {
        1993 : pd.read_csv('%s/npcc/1993/COED93' % (fulldir), skipfooter=1, skiprows=11, header=None, skipinitialspace=True, sep=' ')[2].values,
        1994 : pd.read_fwf('%s/npcc/1994/COED94' % (fulldir), skipfooter=1, header=None)[1].values,
        1995 : pd.read_csv('%s/npcc/1995/COED95' % (fulldir), skiprows=3, header=None),
        1996 : pd.read_excel('%s/npcc/1996/COED96' % (fulldir)).iloc[:, -1].values.ravel(),
        1997 : pd.read_excel('%s/npcc/1997/COED97' % (fulldir), skiprows=1).iloc[:, -1].values.ravel(),
        1998 : pd.read_excel('%s/npcc/1998/COED98' % (fulldir), skiprows=1).iloc[:, -1].values.ravel(),
        1999 : pd.read_csv('%s/npcc/1999/COED99' % (fulldir), skiprows=1, sep='\t').iloc[:, -1].str.replace(',', '').astype(int).values.ravel(),
        2000 : pd.read_csv('%s/npcc/2000/COED00' % (fulldir), sep='\t')[' Load '].dropna().str.replace(',', '').astype(int).values.ravel(),
        2001 : pd.read_csv('%s/npcc/2001/COED01' % (fulldir), sep='\t', skipfooter=1)['Load'].dropna().str.replace(',', '').astype(int).values.ravel(),
        2002 : pd.read_csv('%s/npcc/2002/COED02' % (fulldir), sep='\t', skipfooter=1, skiprows=1)['Load'].dropna().str.replace(',', '').astype(int).values.ravel(),
        2003 : pd.read_csv('%s/npcc/2003/COED03' % (fulldir), sep='\t')['Load'].dropna().astype(int).values.ravel(),
        2004 : pd.read_csv('%s/npcc/2004/COED04' % (fulldir), header=None).iloc[:, -1].str.replace('[A-Z,]', '').str.replace('\s', '0').astype(int).values.ravel()
    },
    4089 : {
        1993 : pd.read_fwf('%s/npcc/1993/COEL93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/npcc/1995/COEL95' % (fulldir), header=None).iloc[:, 1:].values.ravel(), 
        1996 : pd.read_csv('%s/npcc/1996/COEL96' % (fulldir), sep=' ', skipinitialspace=True, header=None)[3].values,
        1997 : pd.read_csv('%s/npcc/1997/COEL97' % (fulldir), sep=' ', skipinitialspace=True, header=None)[4].values,
        1998 : pd.read_csv('%s/npcc/1998/COEL98' % (fulldir), sep=' ', skipinitialspace=True, header=None)[4].values,
        1999 : pd.read_csv('%s/npcc/1999/COEL99' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2000 : pd.read_csv('%s/npcc/2000/COEL00' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2001 : pd.read_csv('%s/npcc/2001/COEL01' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2002 : pd.read_csv('%s/npcc/2002/COEL02' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2003 : pd.read_csv('%s/npcc/2003/COEL03' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values,
        2004 : pd.read_csv('%s/npcc/2004/COEL04' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=3)[4].values
    },
    3292 : {
        1995 : pd.read_fwf('%s/npcc/1995/CVPS95' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('%s/npcc/1996/CVPS96' % (fulldir), header=None, skipfooter=1)[1].values,
        1997 : pd.read_csv('%s/npcc/1997/CVPS97' % (fulldir), header=None)[2].values,
        1998 : pd.read_csv('%s/npcc/1998/CVPS98' % (fulldir), header=None, skipfooter=1)[4].values,
        1999 : pd.read_csv('%s/npcc/1999/CVPS99' % (fulldir))['Load'].values
    },
    5618 : {
            1993 : pd.read_fwf('%s/npcc/1993/EUA93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1994 : pd.read_fwf('%s/npcc/1994/EUA94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('%s/npcc/1995/EUA95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('%s/npcc/1996/EUA96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('%s/npcc/1997/EUA97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1999 : pd.read_fwf('%s/npcc/1999/EUA99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    7601 : {
        1993 : pd.read_csv('%s/npcc/1993/GMP93' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=4)[0].values,
        1994 : pd.read_fwf('%s/npcc/1994/GMP94' % (fulldir), header=None)[0].values,
        1995 : pd.read_csv('%s/npcc/1995/GMP95' % (fulldir), sep=' ', skipinitialspace=True, header=None)[0].values,
        1996 : pd.read_csv('%s/npcc/1996/GMP96' % (fulldir), sep='\t', skipinitialspace=True, header=None)[0].values,
        1997 : pd.read_csv('%s/npcc/1997/GMP97' % (fulldir), sep='\t', skipinitialspace=True, header=None)[0].values,
        1998 : pd.read_csv('%s/npcc/1998/GMP98' % (fulldir), sep='\t', skipinitialspace=True, header=None)[0].values,
        1999 : pd.read_csv('%s/npcc/1999/GMP99' % (fulldir), sep=' ', skipinitialspace=True, header=None, skipfooter=1).iloc[:8760, 0].values,
        2002 : pd.read_excel('%s/npcc/2002/GMP02' % (fulldir), skiprows=6, skipfooter=1).iloc[:, 0].values,
        2003 : pd.read_excel('%s/npcc/2003/GMP03' % (fulldir), skiprows=6, skipfooter=1).iloc[:, 0].values,
        2004 : pd.read_csv('%s/npcc/2004/GMP04' % (fulldir), skiprows=13, sep='\s').iloc[:, 0].values
    },
    13501 : {
        2002 : pd.read_csv('%s/npcc/2002/ISONY02' % (fulldir), sep='\t')['mw'].values,
        2003 : pd.read_excel('%s/npcc/2003/ISONY03' % (fulldir))['Load'].values,
        2004 : pd.read_excel('%s/npcc/2004/ISONY04' % (fulldir)).loc[:, 'HR1':].values.ravel()
    },
    11172 : {
            1994 : pd.read_fwf('%s/npcc/1994/LILC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('%s/npcc/1995/LILC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('%s/npcc/1997/LILC97' % (fulldir), skiprows=4, widths=[8,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
    },
    11806 : {
        1998 : pd.read_fwf('%s/npcc/1998/MMWE98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('%s/npcc/1999/MMWE99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('%s/npcc/2000/MMWE00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('%s/npcc/2001/MMWE01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('%s/npcc/2002/MMWE02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2003 : pd.read_fwf('%s/npcc/2003/MMWE03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        2004 : pd.read_fwf('%s/npcc/2004/MMWE04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel()
    },
    13433 : {
        1993 : pd.read_fwf('%s/npcc/1993/NEES93' % (fulldir), widths=(8,7), header=None, skipfooter=1)[1].values,
        1994 : pd.read_csv('%s/npcc/1994/NEES94' % (fulldir), header=None, skipfooter=1, sep=' ', skipinitialspace=True)[3].values
    },
    13435 : {
        1993 : pd.read_fwf('%s/npcc/1993/NEPOOL93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/npcc/1994/NEPOOL94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/npcc/1995/NEPOOL95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=3).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('%s/npcc/1996/NEPOOL96' % (fulldir), sep=' ', skipinitialspace=True, header=None)[1].values,
        1997 : pd.read_fwf('%s/npcc/1997/NEPOOL97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_excel('%s/npcc/1998/NEPOOL98' % (fulldir), header=None).iloc[:, 5:17].values.ravel(),
        1999 : pd.read_csv('%s/npcc/1999/NEPOOL99' % (fulldir), engine='python', skiprows=1).iloc[:, 0].values,
        2000 : pd.read_fwf('%s/npcc/2000/NEPOOL00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('%s/npcc/2001/NEPOOL01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('%s/npcc/2002/NEPOOL02' % (fulldir), sep='\t').iloc[:, 3:].values.ravel(),
        2003 : pd.read_fwf('%s/npcc/2003/NEPOOL03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2004 : pd.read_csv('%s/npcc/2004/NEPOOL04' % (fulldir), sep='\t', header=None, skiprows=10).iloc[:, 5:].values.ravel()
    },
    13573 : {
            1993 : pd.read_csv('%s/npcc/1993/NMPC93' % (fulldir), skiprows=11, header=None, sep=' ', skipinitialspace=True).iloc[:, 3:27].values.ravel(), 
            1995 : pd.read_fwf('%s/npcc/1995/NMPC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('%s/npcc/1996/NMPC96' % (fulldir), header=None).iloc[:, 2:14].astype(int).values.ravel(),
            1998 : pd.read_fwf('%s/npcc/1998/NMPC98' % (fulldir), header=None).iloc[:, 2:].astype(int).values.ravel(),
            1999 : pd.read_fwf('%s/npcc/1999/NMPC99' % (fulldir), header=None).iloc[:, 2:14].astype(int).values.ravel(),
            2000 : pd.read_excel('%s/npcc/2000/NMPC00' % (fulldir), sheetname=1, skiprows=10, skipfooter=3).iloc[:, 1:].values.ravel(),
            2002 : pd.read_excel('%s/npcc/2002/NMPC02' % (fulldir), sheetname=1, skiprows=2, header=None).iloc[:, 2:].values.ravel(),
            2003 : pd.concat([pd.read_excel('%s/npcc/2003/NMPC03' % (fulldir), sheetname=i, skiprows=1, header=None) for i in range(1,13)]).iloc[:, 2:].values.ravel()
    },
    13556 : {
            1993 : pd.read_fwf('%s/npcc/1993/NU93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
            1994 : pd.read_excel('%s/npcc/1994/NU94' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(),
            1995 : pd.read_excel('%s/npcc/1995/NU95' % (fulldir), header=None, skipfooter=5).dropna(how='any').iloc[:, 3:].values.ravel(),
            1996 : pd.read_excel('%s/npcc/1996/NU96' % (fulldir), header=None, skipfooter=1).iloc[:, 5:].values.ravel(),
            1997 : pd.read_excel('%s/npcc/1997/NU97' % (fulldir), header=None, skipfooter=4).iloc[:, 5:].values.ravel(),
            1998 : pd.read_excel('%s/npcc/1998/NU98' % (fulldir), header=None).iloc[:, 5:].values.ravel(),
            1999 : pd.read_excel('%s/npcc/1999/NU99' % (fulldir), header=None).iloc[:, 5:].values.ravel(),
            2000 : pd.read_csv('%s/npcc/2000/NU00' % (fulldir), sep='\t', header=None).iloc[:, 5:].values.ravel(),
            2001 : pd.read_excel('%s/npcc/2001/NU01' % (fulldir)).iloc[:, -1].values,
            2002 : pd.read_excel('%s/npcc/2002/NU02' % (fulldir)).iloc[:, -1].values,
            2003 : pd.read_excel('%s/npcc/2003/NU03' % (fulldir), skipfooter=1).iloc[:, -1].values 
    },
    15296 : {
        1993 : pd.read_csv('%s/npcc/1993/NYPA93' % (fulldir), engine='python', header=None).values.ravel(),
        1994 : pd.read_csv('%s/npcc/1994/NYPA94' % (fulldir), engine='python', header=None).values.ravel(),
        1995 : pd.read_csv('%s/npcc/1995/NYPA95' % (fulldir), engine='python', header=None).values.ravel(),
        1996 : pd.read_csv('%s/npcc/1996/NYPA96' % (fulldir), engine='python', header=None).values.ravel(),
        1997 : pd.read_csv('%s/npcc/1997/NYPA97' % (fulldir), engine='python', header=None).values.ravel(),
        1998 : pd.read_csv('%s/npcc/1998/NYPA98' % (fulldir), engine='python', header=None).values.ravel(),
        1999 : pd.read_excel('%s/npcc/1999/NYPA99' % (fulldir), header=None).values.ravel(),
        2000 : pd.read_csv('%s/npcc/2000/NYPA00' % (fulldir), engine='python', header=None).values.ravel(),
        2001 : pd.read_csv('%s/npcc/2001/NYPA01' % (fulldir), engine='python', header=None).values.ravel(),
        2002 : pd.read_csv('%s/npcc/2002/NYPA02' % (fulldir), engine='python', header=None).values.ravel(),
        2003 : pd.read_csv('%s/npcc/2003/NYPA03' % (fulldir), engine='python', header=None).values.ravel()
    },
    13501 : {
            1993 : pd.read_fwf('%s/npcc/1993/NYPP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    13511 : {
            1996 : pd.read_fwf('%s/npcc/1996/NYS96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1997 : pd.read_fwf('%s/npcc/1997/NYS97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1999 : pd.read_excel('%s/npcc/1999/NYS99' % (fulldir)).iloc[:, 1:].values.ravel(),
            2000 : pd.read_csv('%s/npcc/2000/NYS00' % (fulldir), sep='\t').iloc[:, -1].values,
            2001 : pd.read_csv('%s/npcc/2001/NYS01' % (fulldir), sep='\t', skiprows=3).dropna(how='all').iloc[:, -1].values,
            2002 : pd.read_csv('%s/npcc/2002/NYS02' % (fulldir), sep='\t', skiprows=3).iloc[:, -1].values,
            2003 : pd.read_csv('%s/npcc/2003/NYS03' % (fulldir), sep=' ', skipinitialspace=True, skiprows=5, header=None).iloc[:, -1].values,
            2004 : pd.read_csv('%s/npcc/2004/NYS04' % (fulldir), sep=' ', skipinitialspace=True, skiprows=5, header=None).dropna(how='all').iloc[:, -1].values
    },
    14154 : {
        1993 : pd.read_csv('%s/npcc/1993/OR93' % (fulldir), skiprows=5, header=None).iloc[:, 2:26].values.ravel(),
        1995 : pd.read_csv('%s/npcc/1995/OR95' % (fulldir), header=None).iloc[:, 1:25].values.ravel(),
        1996 : pd.read_csv('%s/npcc/1996/OR96' % (fulldir), header=None).iloc[:, 1:25].values.ravel(),
        1997 : pd.read_csv('%s/npcc/1997/OR97' % (fulldir), header=None).iloc[:, 1:25].values.ravel(),
        1998 : pd.read_fwf('%s/npcc/1998/OR98' % (fulldir), skiprows=1, header=None).dropna(axis=1, how='all').iloc[:, 1:].values.ravel(),
        1999 : pd.read_csv('%s/npcc/1999/OR99' % (fulldir), sep='\t', skiprows=1, header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_csv('%s/npcc/2000/OR00' % (fulldir), sep='\t').iloc[:, -1].values.astype(int).ravel(),
        2002 : pd.read_csv('%s/npcc/2002/OR02' % (fulldir), sep='\t', skiprows=2).iloc[:, -1].dropna().values.astype(int).ravel(),
        2003 : pd.read_csv('%s/npcc/2003/OR03' % (fulldir), sep='\t').iloc[:, -1].dropna().values.astype(int).ravel(),
        2004 : pd.read_csv('%s/npcc/2004/OR04' % (fulldir), header=None).iloc[:, -1].values.astype(int).ravel()
    },
    16183 : {
            1994 : pd.read_fwf('%s/npcc/1994/RGE94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1995 : pd.read_fwf('%s/npcc/1995/RGE95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            1996 : pd.read_fwf('%s/npcc/1996/RGE96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
            2002 : pd.read_csv('%s/npcc/2002/RGE02' % (fulldir), skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values,
            2003 : pd.read_csv('%s/npcc/2003/RGE03' % (fulldir), skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values,
            2004 : pd.read_csv('%s/npcc/2004/RGE04' % (fulldir), skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values
    },
    19497 : {
        1993 : pd.read_fwf('%s/npcc/1993/UI93' % (fulldir), header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/npcc/1994/UI94' % (fulldir), header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/npcc/1995/UI95' % (fulldir), header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/npcc/1996/UI96' % (fulldir), header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/npcc/1997/UI97' % (fulldir), header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_excel('%s/npcc/1998/UI98' % (fulldir))['MW'].values,
        1999 : pd.read_excel('%s/npcc/1999/UI99' % (fulldir)).loc[:, 'HR1':'HR24'].values.ravel(),
        2001 : pd.read_excel('%s/npcc/2001/UI01' % (fulldir), sheetname=0).ix[:-2, 'HR1':'HR24'].values.ravel(),
        2002 : pd.read_excel('%s/npcc/2002/UI02' % (fulldir), sheetname=0).ix[:-2, 'HR1':'HR24'].values.ravel(),
        2003 : pd.read_excel('%s/npcc/2003/UI03' % (fulldir), sheetname=0, skipfooter=2).ix[:, 'HR1':'HR24'].values.ravel(),
        2004 : pd.read_excel('%s/npcc/2004/UI04' % (fulldir), sheetname=0, skipfooter=1).ix[:, 'HR1':'HR24'].values.ravel()
    }
}
npcc[4226][1995] = pd.concat([npcc[4226][1995][2].dropna(), npcc[4226][1995][6]]).values.ravel()

for k in npcc.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(npcc[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(npcc[k][i]))) for i in npcc[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./npcc/%s.csv' % k)

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
        1993 : pd.read_fwf('%s/ercot/1993/AUST93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/ercot/1994/AUST94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/AUST95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/AUST96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/AUST97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['AENX'].loc[2:].astype(float)/1000).values,
        1999 : (pd.read_excel('%s/ercot/1999/ERCOT99HRLD060800.xls' % (fulldir), skiprows=14)['AENX'].astype(float)/1000).values,
        2000 : (pd.read_csv('%s/ercot/2000/ERCOT00HRLD.txt' % (fulldir), skiprows=18, header=None, skipinitialspace=True, sep='\t')[3].str.replace(',', '').astype(float)/1000).values
    },
    3278 : {
        1993 : pd.read_fwf('%s/ercot/1993/CPL93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/ercot/1994/CPL94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/CPL96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/CPL97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['CPLC'].loc[2:].astype(int)/1000).values
    },
    8901 : {
        1993 : pd.read_fwf('%s/ercot/1993/HLP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/ercot/1994/HLP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/HLP95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/HLP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/HLP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['HLPC'].loc[2:].astype(int)/1000).values
    },
    11269: {
        1993 : pd.read_fwf('%s/ercot/1993/LCRA93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_csv('%s/ercot/1994/LCRA94' % (fulldir), skiprows=4).iloc[:, -1].values,
        1995 : pd.read_fwf('%s/ercot/1995/LCRA95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/LCRA96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/LCR97' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['LCRA'].loc[2:].astype(int)/1000).values,
        1999 : (pd.read_excel('%s/ercot/1999/ERCOT99HRLD060800.xls' % (fulldir), skiprows=14)['LCRA'].astype(float)/1000).values,
        2000 : (pd.read_csv('%s/ercot/2000/ERCOT00HRLD.txt' % (fulldir), skiprows=18, header=None, skipinitialspace=True, sep='\t')[6].str.replace(',', '').astype(float)/1000).values
    },
    13670 : {
        1993 : pd.read_csv('%s/ercot/1993/NTEC93' % (fulldir), sep=' ', skipinitialspace=True, header=None)[1].values,
        1994 : pd.read_fwf('%s/ercot/1994/NTEC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/NTEC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/NTEC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/NTEC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('%s/ercot/2001/NTEC01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    2409 : {
        1993 : pd.read_fwf('%s/ercot/1993/PUB93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/ercot/1994/PUB94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/PUB95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/PUB96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/PUB97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['PUBX'].loc[2:].astype(int)/1000).values,
        1999 : (pd.read_excel('%s/ercot/1999/ERCOT99HRLD060800.xls' % (fulldir), skiprows=14)['PUBX'].astype(float)/1000).values,
        2000 : (pd.read_csv('%s/ercot/2000/ERCOT00HRLD.txt' % (fulldir), skiprows=18, header=None, skipinitialspace=True, sep='\t')[7].str.replace(',', '').astype(float)/1000).values
    },
    40233 : {
        1993 : pd.read_csv('%s/ercot/1993/SRGT93' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        1994 : pd.read_fwf('%s/ercot/1994/SRGT94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/SRGT95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/SRGT96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/SRGT97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    17583 : {
        1993 : pd.read_fwf('%s/ercot/1993/STEC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['STEC'].loc[2:].astype(int)/1000).values,
        1999 : (pd.read_excel('%s/ercot/1999/ERCOT99HRLD060800.xls' % (fulldir), skiprows=14)['STEC'].astype(float)/1000).values,
        2000 : (pd.read_csv('%s/ercot/2000/ERCOT00HRLD.txt' % (fulldir), skiprows=18, header=None, skipinitialspace=True, sep='\t')[9].str.replace(',', '').astype(float)/1000).values
    },
    44372 : {
        1993 : pd.read_fwf('%s/ercot/1993/TUEC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/ercot/1994/TUEC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/TUEC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/TUE96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/TUE97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['TUEC'].loc[2:].astype(int)/1000).values
    },
    18715 : {
        1993 : pd.read_csv('%s/ercot/1993/TMPP93' % (fulldir), skiprows=7, header=None, sep=' ', skipinitialspace=True).iloc[:, 3:].values.ravel(),
        1995 : pd.read_fwf('%s/ercot/1995/TMPP95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/TMPP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1999 : (pd.read_excel('%s/ercot/1999/ERCOT99HRLD060800.xls' % (fulldir), skiprows=14)['TMPP'].astype(float)/1000).values,
        2000 : (pd.read_csv('%s/ercot/2000/ERCOT00HRLD.txt' % (fulldir), skiprows=18, header=None, skipinitialspace=True, sep='\t')[10].str.replace(',', '').astype(float)/1000).values
    },
    18679 : {
        1993 : pd.read_csv('%s/ercot/1993/TEXLA93' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        1995 : pd.read_fwf('%s/ercot/1995/TXLA95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/TXLA96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/TXLA97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['TXLA'].loc[2:].astype(int)/1000).values
    },
    20404 : {
        1993 : pd.read_fwf('%s/ercot/1993/WTU93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].astype(str).apply(lambda x: x.str.replace('\s', '0')).astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/ercot/1994/WTU94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/ercot/1996/WTU96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/ercot/1997/WTU97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : (pd.read_excel('%s/ercot/1998/FERC714.xls' % (fulldir), skiprows=3)['WTUC'].loc[2:].astype(int)/1000).values
    }
}

for k in ercot.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(ercot[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(ercot[k][i]))) for i in ercot[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./ercot/%s.csv' % k)

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
# SECI: 21554

frcc = {
    6909 : {
        1993 : pd.read_fwf('%s/frcc/1993/GAIN93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_csv('%s/frcc/1994/GAIN94' % (fulldir), header=None, sep=' ', skipinitialspace=True, skipfooter=2, skiprows=5).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/frcc/1995/GAIN95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('%s/frcc/1996/GAIN96' % (fulldir), sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/frcc/1997/GAIN97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/frcc/1998/GAIN98' % (fulldir), sep=' ', skipinitialspace=True, skiprows=3, header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('%s/frcc/1999/GAIN99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('%s/frcc/2000/GAIN00' % (fulldir), header=None).iloc[:, 4:].values.ravel(),
        2002 : pd.read_excel('%s/frcc/2002/GAIN02' % (fulldir), sheetname=1, skiprows=3, header=None).iloc[:730, 8:20].values.ravel(),
        2003 : pd.read_excel('%s/frcc/2003/GAIN03' % (fulldir), sheetname=2, skiprows=3, header=None).iloc[:730, 8:20].values.ravel(),
        2004 : pd.read_excel('%s/frcc/2004/GAIN04' % (fulldir), sheetname=0, header=None).iloc[:, 8:].values.ravel()
    },
    10623: {
        1993 : pd.read_fwf('%s/frcc/1993/LAKE93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/frcc/1994/LAKE94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/frcc/1995/LAKE95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/frcc/1996/LAKE96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/frcc/1997/LAKE97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('%s/frcc/1998/LAKE98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('%s/frcc/1999/LAKE99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('%s/frcc/2000/LAKE00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('%s/frcc/2001/LAKE01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('%s/frcc/2002/LAKE02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    6567 : {
        1993 : pd.read_fwf('%s/frcc/1993/FMPA93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/frcc/1994/FMPA94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/frcc/1995/FMPA95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/frcc/1996/FMPA96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/frcc/1997/FMPA97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('%s/frcc/1998/FMPA98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('%s/frcc/1999/FMPA99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        2001 : pd.read_csv('%s/frcc/2001/FMPA01' % (fulldir), header=None, sep=' ', skipinitialspace=True, skiprows=6).iloc[:, 2:-1].values.ravel(),
        2002 : pd.read_csv('%s/frcc/2002/FMPA02' % (fulldir), header=None, sep='\t', skipinitialspace=True, skiprows=7).iloc[:, 1:].values.ravel(),
        2003 : pd.read_csv('%s/frcc/2003/FMPA03' % (fulldir), header=None, sep='\t', skipinitialspace=True, skiprows=7).iloc[:, 1:].values.ravel(),
        2004 : pd.read_csv('%s/frcc/2004/FMPA04' % (fulldir), header=None, sep=' ', skipinitialspace=True, skiprows=6, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    6455 : {
        1993 : pd.read_csv('%s/frcc/1993/FPC93' % (fulldir), sep=' ', skipinitialspace=True, header=None)[1].values,
        1994 : pd.read_csv('%s/frcc/1994/FPC94' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
        1995 : pd.read_csv('%s/frcc/1995/FPC95' % (fulldir), engine='python', header=None)[0].values,
        1996 : pd.read_excel('%s/frcc/1996/FPC96' % (fulldir), header=None, skiprows=2, skipfooter=1).iloc[:, 6:].values.ravel(),
        1998 : pd.read_excel('%s/frcc/1998/FPC98' % (fulldir), header=None, skiprows=5).iloc[:, 7:].values.ravel(),
        1999 : pd.read_excel('%s/frcc/1999/FPC99' % (fulldir), header=None, skiprows=4).iloc[:, 7:].values.ravel(),
        2000 : pd.read_excel('%s/frcc/2000/FPC00' % (fulldir), header=None, skiprows=4).iloc[:, 7:].values.ravel(),
        2001 : pd.read_excel('%s/frcc/2001/FPC01' % (fulldir), header=None, skiprows=5).iloc[:, 7:].values.ravel(),
        2002 : pd.read_excel('%s/frcc/2002/FPC02' % (fulldir), header=None, skiprows=4).iloc[:, 7:].values.ravel(),
        2004 : pd.read_excel('%s/frcc/2004/FPC04' % (fulldir), header=None, skiprows=4).iloc[:, 7:].values.ravel()
    },
    6452 : {
        1993 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1993/FPL93' % (fulldir), 'r').readlines()]).iloc[:365, :24].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1994 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1994/FPL94' % (fulldir), 'r').readlines()]).iloc[3:, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1995 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1995/FPL95' % (fulldir), 'r').readlines()[3:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1996 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1996/FPL96' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1997 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1997/FPL97' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1998 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1998/FPL98' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/1999/FPL99' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/2000/FPL00' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2001 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/2001/FPL01' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2002 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/2002/FPL02' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2003 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/2003/FPL03' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel(),
        2004 : pd.DataFrame([i.split('\t') for i in open('%s/frcc/2004/FPL04' % (fulldir), 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
    },
    9617 : {
        1993 : pd.read_csv('%s/frcc/1993/JEA93' % (fulldir), sep=' ', skipinitialspace=True, header=None)[2].values,
        1994 : pd.read_csv('%s/frcc/1994/JEA94' % (fulldir), sep=' ', skipinitialspace=True, header=None)[2].values,
        1996 : pd.read_fwf('%s/frcc/1996/JEA96' % (fulldir), header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/frcc/1997/JEA97' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/frcc/1998/JEA98' % (fulldir), sep='\t', header=None)[2].values,
        1999 : pd.read_csv('%s/frcc/1999/JEA99' % (fulldir), sep='\t', header=None)[2].values,
        2000 : pd.read_excel('%s/frcc/2000/JEA00' % (fulldir), header=None)[2].values,
        2001 : pd.read_excel('%s/frcc/2001/JEA01' % (fulldir), header=None, skiprows=2)[2].values,
        2002 : pd.read_excel('%s/frcc/2002/JEA02' % (fulldir), header=None, skiprows=1)[2].values,
        2003 : pd.read_excel('%s/frcc/2003/JEA03' % (fulldir), header=None, skiprows=1)[2].values,
        2004 : pd.read_excel('%s/frcc/2004/JEA04' % (fulldir), header=None, skiprows=1)[2].values
    },
    10376 : {
        1994 : pd.read_csv('%s/frcc/1994/KUA94' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_csv('%s/frcc/1995/KUA95' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('%s/frcc/1997/KUA97' % (fulldir), sep='\t', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
        2001 : pd.read_csv('%s/frcc/2001/KUA01' % (fulldir), skiprows=1, header=None, sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('%s/frcc/2002/KUA02' % (fulldir), skipfooter=1, header=None, sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel()
    },
    14610 : {
        1993 : pd.read_fwf('%s/frcc/1993/OUC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/frcc/1994/OUC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/frcc/1995/OUC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/frcc/1996/OUC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/frcc/1997/OUC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('%s/frcc/1998/OUC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('%s/frcc/1999/OUC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_fwf('%s/frcc/2000/OUC00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2001 : pd.read_fwf('%s/frcc/2001/OUC01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('%s/frcc/2002/OUC02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    18454 : {
        1993 : pd.read_fwf('%s/frcc/1993/TECO93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/frcc/1994/TECO94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/frcc/1998/TECO98' % (fulldir), engine='python', skiprows=3, header=None)[0].values,
        1999 : pd.read_csv('%s/frcc/1999/TECO99' % (fulldir), engine='python', skiprows=3, header=None)[0].values,
        2000 : pd.read_csv('%s/frcc/2000/TECO00' % (fulldir), engine='python', skiprows=3, header=None)[0].str[:4].astype(int).values,
        2001 : pd.read_csv('%s/frcc/2001/TECO01' % (fulldir), skiprows=3, header=None)[0].values,
        2002 : pd.read_csv('%s/frcc/2002/TECO02' % (fulldir), sep='\t').loc[:, 'HR1':].values.ravel(),
        2003 : pd.read_csv('%s/frcc/2003/TECO03' % (fulldir), skiprows=2, header=None, sep=' ', skipinitialspace=True).iloc[:, 2:].values.ravel()
    },
    21554 : {
        1993 : pd.read_fwf('%s/frcc/1993/SECI93' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(),
	1994 : pd.read_fwf('%s/frcc/1994/SECI94' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(), 
	1995 : pd.read_fwf('%s/frcc/1995/SECI95' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(), 
	1996 : pd.read_fwf('%s/frcc/1996/SECI96' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(), 
	1997 : pd.read_fwf('%s/frcc/1997/SECI97' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(), 
	1999 : pd.read_fwf('%s/frcc/1999/SECI99' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(), 
	2000 : pd.read_fwf('%s/frcc/2000/SECI00' % (fulldir), header=None, skipfooter=1).iloc[:, 3:].values.ravel(),
	2002 : pd.read_fwf('%s/frcc/2002/SECI02' % (fulldir), header=None).iloc[:, 3:].values.ravel(),
	2004 : pd.read_fwf('%s/frcc/2004/SECI04' % (fulldir), header=None).iloc[:, 3:].values.ravel() 
    }
}

for k in frcc.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(frcc[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(frcc[k][i]))) for i in frcc[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./frcc/%s.csv' % k)

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
# FE: 32208
# MCCP:

ecar = {
    829 : {
        1993 : pd.read_fwf('%s/ecar/1993/AEP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/AEP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/AEP95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/AEP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/AEP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/AEP98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/AEP99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/AEP00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/AEP01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/AEP02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/AEP03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/AEP04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    538 : {
        1993 : pd.read_fwf('%s/ecar/1993/APS93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/APS94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/APS95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    40577 : {
        2001 : pd.read_fwf('%s/ecar/2001/AMPO01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/AMPO02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/AMPO03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/AMPO04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    1692 : {
        1993 : pd.read_fwf('%s/ecar/1993/BREC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/BREC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/BREC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/BREC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/BREC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/BREC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/BREC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/BREC00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/BREC01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/BREC02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/BREC03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/BREC04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    7004 : {
        1994 : pd.read_fwf('%s/ecar/1994/BPI94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/BPI99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/BPI00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/BPI01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/BPI02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/BPI03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/BPI04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    3755 : {
        1993 : pd.read_fwf('%s/ecar/1993/CEI93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/CEI94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/CEI95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/CEI96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    3542 : {
        1993 : pd.read_fwf('%s/ecar/1993/CEI93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/CEI94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/CEI95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    4254 : {
        1993 : pd.read_fwf('%s/ecar/1993/CP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/CP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/CP95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/CP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    4922 : {
        1993 : pd.read_fwf('%s/ecar/1993/DPL93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/DPL94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/DPL95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/DPL96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/DPL97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/DPL98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/DPL99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/DPL00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/DPL01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/DPL02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/DPL03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/DPL04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    5109 : {
        1993 : pd.read_fwf('%s/ecar/1993/DECO93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/DECO94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/DECO95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/DECO96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/DECO97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/DECO98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/DECO99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/DECO00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/DECO01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/DECO02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/DECO03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/DECO04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    5487 : {
        1993 : pd.read_fwf('%s/ecar/1993/DLCO93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/DLCO94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/DLCO95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/DLCO96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/DLCO97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/DLCO98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/DLCO99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/DLCO00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/DLCO01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/DLCO02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/DLCO03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/DLCO04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    5580 : {
        1993 : pd.read_fwf('%s/ecar/1993/EKPC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/EKPC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/EKPC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/EKPC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/EKPC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/EKPC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/EKPC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/EKPC00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/EKPC01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/EKPC02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/EKPC03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/EKPC04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9267 : {
        1993 : pd.read_fwf('%s/ecar/1993/HEC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/HEC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/HEC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/HEC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/HEC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/HEC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/HEC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/HEC00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/HEC01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/HEC02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/HEC03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/HEC04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9273 : {
        1993 : pd.read_fwf('%s/ecar/1993/IPL93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/IPL94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/IPL95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/IPL96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/IPL97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/IPL98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/IPL99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/IPL00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/IPL01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/IPL02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/IPL03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/IPL04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    10171 : {
        1993 : pd.read_fwf('%s/ecar/1993/KUC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/KUC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/KUC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/KUC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/KUC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    11249 : {
        1993 : pd.read_fwf('%s/ecar/1993/LGE93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/LGE94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/LGE95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/LGE96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/LGE97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/LGEE98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/LGEE99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/LGEE00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/LGEE01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/LGEE02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/LGEE03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/LGEE04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13756 : {
        1993 : pd.read_fwf('%s/ecar/1993/NIPS93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/NIPS94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/NIPS95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/NIPS96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/NIPS97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/NIPS98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/NIPS99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/NIPS00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/NIPS01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/NIPS02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/NIPS03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/NIPS04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13998 : {
        1993 : pd.read_fwf('%s/ecar/1993/OES93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/OES94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/OES95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/OES96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    14015 : {
        1993 : pd.read_fwf('%s/ecar/1993/OVEC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/OVEC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/OVEC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/OVEC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/OVEC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/OVEC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/OVEC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/OVEC00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/OVEC01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/OVEC02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/OVEC03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/OVEC04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    15470 : {
        1993 : pd.read_fwf('%s/ecar/1993/PSI93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/PSI94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/PSI95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    17633 : {
        1993 : pd.read_fwf('%s/ecar/1993/SIGE93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/SIGE94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/SIGE95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/SIGE96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/SIGE97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/SIGE98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/SIGE99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/SIGE01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/SIGE02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/SIGE03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/SIGE04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    18997 : {
        1993 : pd.read_fwf('%s/ecar/1993/TECO93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/ecar/1994/TECO94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/ecar/1995/TECO95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/TECO96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    40211 : {
        1994 : pd.read_fwf('%s/ecar/1994/WVPA94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/ecar/2003/WVPA03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/WVPA04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    3260 : {
        1996 : pd.read_fwf('%s/ecar/1996/CIN96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/CIN97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/CIN98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/CIN99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/CIN00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/CIN01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/CIN02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/CIN03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/CIN04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    32208 : {
        1997 : pd.read_fwf('%s/ecar/1997/FE97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/ecar/1998/FE98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/ecar/1999/FE99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/FE00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/FE01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/FE02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/FE03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/FE04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    'mccp' : {
        1993 : pd.read_fwf('%s/ecar/1993/MCCP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/ecar/1996/MCCP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/ecar/1997/MCCP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_fwf('%s/ecar/2000/MCCP00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2001 : pd.read_fwf('%s/ecar/2001/MCCP01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_csv('%s/ecar/2002/MCCP02' % (fulldir), header=None)[1].values,
        2003 : pd.read_fwf('%s/ecar/2003/MCCP03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2004 : pd.read_fwf('%s/ecar/2004/MCCP04' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    }
}

for k in ecar.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(ecar[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(ecar[k][i]))) for i in ecar[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./ecar/%s.csv' % k)

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
        1993 : pd.read_fwf('%s/main/1993/CECO93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_csv('%s/main/1995/CECO95' % (fulldir), skiprows=3, header=None)[0].values,
        1996 : pd.read_csv('%s/main/1996/CECO96' % (fulldir), skiprows=4, header=None)[1].values,
        1997 : pd.read_csv('%s/main/1997/CECO97' % (fulldir), sep=' ', skipinitialspace=True, skiprows=4, header=None)[3].values,
        1998 : pd.read_csv('%s/main/1998/CECO98' % (fulldir), sep='\s', skipinitialspace=True, skiprows=5, header=None)[5].values,
        1999 : pd.read_csv('%s/main/1999/CECO99' % (fulldir), sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values,
        2000 : pd.read_csv('%s/main/2000/CECO00' % (fulldir), sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values,
        2001 : pd.read_csv('%s/main/2001/CECO01' % (fulldir), sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values,
        2002 : pd.read_csv('%s/main/2002/CECO02' % (fulldir), sep=' ', skipinitialspace=True, skiprows=5, header=None)[2].values
    },
    3252 : {
        1993 : pd.read_fwf('%s/main/1993/CILC93' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        1994 : pd.read_fwf('%s/main/1994/CILC94' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        1995 : pd.read_fwf('%s/main/1995/CILC95' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        1996 : pd.read_fwf('%s/main/1996/CILC96' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        1997 : pd.read_fwf('%s/main/1997/CILC97' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        1998 : pd.read_fwf('%s/main/1998/CILC98' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        1999 : pd.read_fwf('%s/main/1999/CILC99' % (fulldir), header=None).iloc[:, 2:].values.ravel(),
        2000 : pd.read_excel('%s/main/2000/CILC00' % (fulldir), skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel(),
        2001 : pd.read_excel('%s/main/2001/CILC01' % (fulldir), skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel(),
        2002 : pd.read_excel('%s/main/2002/CILC02' % (fulldir), skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel(),
        2003 : pd.read_csv('%s/main/2003/CILC03' % (fulldir), skiprows=1, sep='\t').iloc[:, -1].values
    },
    3253 : {
        1993 : pd.read_fwf('%s/main/1993/CIPS93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/main/1994/CIPS94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/main/1995/CIPS95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/main/1996/CIPS96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/main/1997/CIPS97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9208 : {
        1993 : pd.read_csv('%s/main/1993/IPC93' % (fulldir), skipfooter=1, header=None)[2].values,
        1994 : pd.read_csv('%s/main/1994/IPC94' % (fulldir), skipfooter=1, header=None)[2].values,
        1995 : pd.read_csv('%s/main/1995/IPC95' % (fulldir), skipfooter=1, header=None)[4].astype(str).str.replace('.', '0').astype(float).values,
        1996 : pd.read_csv('%s/main/1996/IPC96' % (fulldir)).iloc[:, -1].values,
        1997 : pd.read_csv('%s/main/1997/IPC97' % (fulldir)).iloc[:, -1].values,
        1998 : pd.read_excel('%s/main/1998/IPC98' % (fulldir)).iloc[:, -1].values,
        1999 : pd.read_csv('%s/main/1999/IPC99' % (fulldir), skiprows=2, header=None)[1].values,
        2000 : pd.read_excel('%s/main/2000/IPC00' % (fulldir), skiprows=1).iloc[:, -1].values,
        2001 : pd.read_excel('%s/main/2001/IPC01' % (fulldir), skiprows=1).iloc[:, -1].values,
        2002 : pd.read_excel('%s/main/2002/IPC02' % (fulldir), skiprows=4).iloc[:, -1].values,
        2003 : pd.read_excel('%s/main/2003/IPC03' % (fulldir), skiprows=1).iloc[:, -1].values,
        2004 : pd.read_excel('%s/main/2004/IPC04' % (fulldir), skiprows=1).iloc[:, -1].values
    },
    11479 : {
        1993 : pd.read_fwf('%s/main/1993/MGE93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=4).iloc[:, 1:].dropna().astype(float).values.ravel(),
        1995 : pd.read_csv('%s/main/1995/MGE95' % (fulldir), sep=' ', skipinitialspace=True, header=None)[2].values,
        1997 : pd.read_csv('%s/main/1997/MGE97' % (fulldir), sep=' ', skipinitialspace=True, skiprows=12, header=None).iloc[:-1, 2].astype(float).values,
        1998 : pd.read_csv('%s/main/1998/MGE98' % (fulldir), sep=' ', skipinitialspace=True).iloc[:-1]['LOAD'].astype(float).values,
        1999 : pd.read_csv('%s/main/1999/MGE99' % (fulldir), sep=' ', skiprows=2, header=None, skipinitialspace=True).iloc[:-2, 2].astype(float).values,
        2000 : pd.read_csv('%s/main/2000/MGE00' % (fulldir), sep=' ', skiprows=3, header=None, skipinitialspace=True, skipfooter=2).iloc[:, 2].astype(float).values,
        2000 : pd.read_fwf('%s/main/2000/MGE00' % (fulldir), skiprows=2)['VMS_DATE'].iloc[:-2].str.split().str[-1].astype(float).values,
        2001 : pd.read_fwf('%s/main/2001/MGE01' % (fulldir), skiprows=1, header=None).iloc[:-2, 2].values,
        2002 : pd.read_fwf('%s/main/2002/MGE02' % (fulldir), skiprows=4, header=None).iloc[:-1, 0].str.split().str[-1].astype(float).values
    },
    17632 : {
        1994 : pd.read_csv('%s/main/1994/SIPC94' % (fulldir), engine='python', skipfooter=1, header=None)[0].values,
        1996 : pd.read_csv('%s/main/1996/SIPC96' % (fulldir), engine='python', header=None)[0].values,
        1997 : pd.read_csv('%s/main/1997/SIPC97' % (fulldir), engine='python', header=None)[0].values,
        1998 : pd.read_csv('%s/main/1998/SIPC98' % (fulldir), engine='python', header=None)[0].values,
        1999 : pd.read_csv('%s/main/1999/SIPC99' % (fulldir), engine='python', header=None)[0].replace('no data', '0').astype(float).values,
        2000 : pd.read_csv('%s/main/2000/SIPC00' % (fulldir), engine='python', header=None)[0].astype(str).str[:3].astype(float).values,
        2001 : pd.read_csv('%s/main/2001/SIPC01' % (fulldir), engine='python', header=None)[0].str.strip().str[:3].astype(float).values,
        2002 : pd.read_csv('%s/main/2002/SIPC02' % (fulldir), sep='\t', skiprows=3, header=None)[1].values,
        2003 : pd.read_csv('%s/main/2003/SIPC03' % (fulldir), engine='python', header=None)[0].str.strip().str[:3].astype(float).values,
        2004 : pd.read_csv('%s/main/2004/SIPC04' % (fulldir), engine='python', header=None)[0].str.strip().str[:3].astype(float).values
    },
    17828 : {
        1993 : pd.read_csv('%s/main/1993/SPIL93' % (fulldir), sep=' ', skipinitialspace=True, skiprows=4, header=None).iloc[:, 3:].values.ravel(),
        1994 : pd.read_csv('%s/main/1994/SPIL94' % (fulldir), sep=' ', skipinitialspace=True, skiprows=6, header=None).iloc[:, 3:].values.ravel(),
        1995 : pd.read_csv('%s/main/1995/SPIL95' % (fulldir), sep=' ', skipinitialspace=True, skiprows=7, header=None).iloc[:, 3:].values.ravel(),
        1996 : pd.read_csv('%s/main/1996/SPIL96' % (fulldir), sep=' ', skipinitialspace=True, skiprows=5, header=None).iloc[:366, 3:].astype(float).values.ravel(),
        1997 : pd.read_csv('%s/main/1997/SPIL97' % (fulldir), sep=' ', skipinitialspace=True, skiprows=7, header=None).iloc[:, 3:].values.ravel(),
        1998 : pd.read_csv('%s/main/1998/SPIL98' % (fulldir), sep='\t', skipinitialspace=True, skiprows=8, header=None).iloc[:, 4:].values.ravel(),
        1999 : pd.read_csv('%s/main/1999/SPIL99' % (fulldir), skiprows=4, header=None)[0].values,
        2000 : pd.read_csv('%s/main/2000/SPIL00' % (fulldir), skiprows=4, header=None)[0].values,
        2001 : pd.read_csv('%s/main/2001/SPIL01' % (fulldir), sep='\t', skipinitialspace=True, skiprows=7, header=None).iloc[:, 5:-1].values.ravel(),
        2002 : pd.read_excel('%s/main/2002/SPIL02' % (fulldir), sheetname=2, skiprows=5).iloc[:, 3:].values.ravel(),
        2003 : pd.read_excel('%s/main/2003/SPIL03' % (fulldir), sheetname=2, skiprows=5).iloc[:, 3:].values.ravel(),
        2004 : pd.read_excel('%s/main/2004/SPIL04' % (fulldir), sheetname=0, skiprows=5).iloc[:, 3:].values.ravel()
    },
    19436 : {
        1995 : pd.read_fwf('%s/main/1995/UE95' % (fulldir), header=None)[2].values,
        1996 : pd.read_fwf('%s/main/1996/UE96' % (fulldir), header=None)[2].values,
        1997 : pd.read_fwf('%s/main/1997/UE97' % (fulldir), header=None)[2].values
    },
    20847 : {
        1993 : pd.read_csv('%s/main/1993/WEPC93' % (fulldir), engine='python', skipfooter=1, header=None)[0].values,
        1994 : pd.read_csv('%s/main/1994/WEPC94' % (fulldir), engine='python', skipfooter=1, header=None)[0].values,
        1995 : pd.read_csv('%s/main/1995/WEPC95' % (fulldir), engine='python', skipfooter=1, header=None)[0].values,
        1996 : pd.read_csv('%s/main/1996/WEPC96' % (fulldir), engine='python', header=None)[0].values,
        1997 : pd.read_excel('%s/main/1997/WEPC97' % (fulldir), header=None)[0].astype(str).str.strip().replace('NA', '0').astype(float).values,
        1998 : pd.read_csv('%s/main/1998/WEPC98' % (fulldir), engine='python', header=None)[0].str.strip().replace('NA', 0).astype(float).values,
        1999 : pd.read_excel('%s/main/1999/WEPC99' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
        2000 : pd.read_excel('%s/main/2000/WEPC00' % (fulldir), header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2001 : pd.read_excel('%s/main/2001/WEPC01' % (fulldir), header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_excel('%s/main/2002/WEPC02' % (fulldir), header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2003 : pd.read_excel('%s/main/2003/WEPC03' % (fulldir), header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2004 : pd.read_excel('%s/main/2004/WEPC04' % (fulldir), header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    20856 : {
        1993 : pd.read_fwf('%s/main/1993/WPL93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/main/1994/WPL94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/main/1995/WPL95' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('%s/main/1996/WPL96' % (fulldir), header=None, sep='\t').iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('%s/main/1997/WPL97' % (fulldir), sep=' ', skipinitialspace=True, skiprows=1, header=None)[2].str.replace(',', '').astype(float).values
    },
    20860 : {
        1993 : pd.read_csv('%s/main/1993/WPS93' % (fulldir), sep=' ', header=None, skipinitialspace=True, skipfooter=1).values.ravel(),
        1994 : (pd.read_csv('%s/main/1994/WPS94' % (fulldir), sep=' ', header=None, skipinitialspace=True, skipfooter=1).iloc[:, 1:-1]/100).values.ravel(),
        1995 : pd.read_csv('%s/main/1995/WPS95' % (fulldir), sep=' ', skipinitialspace=True, skiprows=8, header=None, skipfooter=7)[2].values,
        1996 : pd.read_csv('%s/main/1996/WPS96' % (fulldir), sep='\t', skiprows=2).loc[:365, '100':'2400'].astype(float).values.ravel(),
        1997 : pd.read_csv('%s/main/1997/WPS97' % (fulldir), sep='\s', header=None, skipfooter=1)[2].values,
        1998 : pd.read_csv('%s/main/1998/WPS98' % (fulldir), sep='\s', header=None)[2].values,
        1999 : pd.read_excel('%s/main/1999/WPS99' % (fulldir), skiprows=8, skipfooter=8, header=None)[1].values,
        2000 : pd.read_excel('%s/main/2000/WPS00' % (fulldir), sheetname=1, skiprows=5, skipfooter=8, header=None)[2].values,
        2001 : pd.read_excel('%s/main/2001/WPS01' % (fulldir), sheetname=0, skiprows=5, header=None)[2].values,
        2002 : pd.read_csv('%s/main/2002/WPS02' % (fulldir), sep='\s', header=None, skiprows=5)[2].values,
        2003 : pd.read_excel('%s/main/2003/WPS03' % (fulldir), sheetname=1, skiprows=6, header=None)[2].values
    },
    19578 : {
        1996 : pd.read_csv('%s/main/1996/UPP96' % (fulldir), header=None, skipfooter=1).iloc[:, -1].values,
        2004 : pd.read_excel('%s/main/2004/UPP04' % (fulldir)).iloc[:, -1].values
    },
    20858 : {
        1997 : pd.read_csv('%s/main/1997/WPPI97' % (fulldir), skiprows=5, sep=' ', skipinitialspace=True, header=None).iloc[:, 1:-1].values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('%s/main/1999/WPPI99' % (fulldir)).readlines()[5:]]).iloc[:, 1:-1].astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split() for i in open('%s/main/2000/WPPI00' % (fulldir)).readlines()[5:]]).iloc[:, 1:-1].astype(float).values.ravel(),
        2001 : pd.read_excel('%s/main/2001/WPPI01' % (fulldir), sheetname=1, skiprows=4).iloc[:, 1:-1].values.ravel(),
        2002 : pd.read_excel('%s/main/2002/WPPI02' % (fulldir), sheetname=1, skiprows=4).iloc[:, 1:-1].values.ravel()
    },
    19436 : {
        1998 : pd.read_csv('%s/main/1998/AMER98' % (fulldir), sep='\t').iloc[:, -1].str.strip().replace('na', 0).astype(float).values,
        1999 : pd.read_csv('%s/main/1999/AMER99' % (fulldir), sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2000 : pd.read_csv('%s/main/2000/AMER00' % (fulldir), sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2001 : pd.read_csv('%s/main/2001/AMER01' % (fulldir), sep='\t').iloc[:, -1].astype(str).str.strip().replace('n/a', 0).astype(float).values,
        2002 : pd.read_csv('%s/main/2002/AMER02' % (fulldir), sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2003 : pd.read_csv('%s/main/2003/AMER03' % (fulldir), sep='\t', skiprows=1).iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values,
        2004 : pd.read_csv('%s/main/2004/AMER04' % (fulldir), sep='\t', skiprows=1).iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values
    },
    4045 : {
        2000 : pd.read_excel('%s/main/2000/CWL00' % (fulldir), skiprows=2).iloc[:, 1:].values.ravel(),
        2001 : pd.read_excel('%s/main/2001/CWL01' % (fulldir), skiprows=1).iloc[:, 0].values,
        2002 : pd.read_excel('%s/main/2002/CWL02' % (fulldir), header=None).iloc[:, 0].values,
        2003 : pd.read_excel('%s/main/2003/CWL03' % (fulldir), header=None).iloc[:, 0].values
    }
}

for k in main.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(main[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(main[k][i]))) for i in main[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./main/%s.csv' % k)

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

maac93 = pd.read_fwf('%s/maac/1993/PJM93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
maac94 = pd.read_fwf('%s/maac/1994/PJM94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
maac95 = pd.read_csv('%s/maac/1995/PJM95' % (fulldir), sep='\t', header=None, skipfooter=1)
maac96 = pd.read_csv('%s/maac/1996/PJM96' % (fulldir), sep='\t', header=None, skipfooter=1)

maac = {
    963 : {
            1993 : maac93[maac93[0].str.contains('AE')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('AE')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('AE')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('AE')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='ACE_LOAD').iloc[:, 1:25].values.ravel()
    },
    1167 : {
            1993 : maac93[maac93[0].str.contains('BC')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('BC')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('BC')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('BC')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='BC_LOAD').iloc[:, 1:25].values.ravel()
    },
    5027 : {
            1993 : maac93[maac93[0].str.contains('DP')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('DP')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('DP')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('DP')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='DPL_LOAD').iloc[:366, 1:25].values.ravel()
    },
    7088 : {
            1993 : maac93[maac93[0].str.contains('PU')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PU')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PU')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PU')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='GPU_LOAD').iloc[:366, 1:25].values.ravel()
    },
    14715 : {
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='PN_LOAD').iloc[:366, 1:25].values.ravel()
    },
    14940 : {
            1993 : maac93[maac93[0].str.contains('PE$')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PE$')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PE$')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PE$')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='PE_Load').iloc[:366, 1:25].values.ravel()
    },
    15270 : {
            1993 : maac93[maac93[0].str.contains('PEP')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PEP')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PEP')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PEP')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='PEP_LOAD').iloc[:366, 1:25].values.ravel()
    },
    15477 : {
            1993 : maac93[maac93[0].str.contains('PS')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PS')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PS')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PS')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='PS_Load').iloc[:366, 1:25].values.ravel()
    },
    14725 : {
            1993 : maac93[maac93[0].str.contains('PJM')].iloc[:, 1:].values.ravel(),
            1994 : maac94[maac94[0].str.contains('PJM')].iloc[:, 1:].values.ravel(),
            1995 : maac95[maac95[1].str.contains('PJM')].iloc[:, 2:].values.ravel(),
            1996 : maac96[maac96[1].str.contains('PJM')].iloc[:, 2:].values.ravel(),
            1997 : pd.read_excel('%s/maac/1997/PJM97' % (fulldir), sheetname='PJM_LOAD').iloc[:366, 1:25].values.ravel(),
            1998 : pd.read_csv('%s/maac/1998/PJM98' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
            1999 : pd.read_excel('%s/maac/1999/PJM99' % (fulldir), header=None)[2].values,
            2000 : pd.read_excel('%s/maac/2000/PJM00' % (fulldir), header=None)[2].values
    }
}

for k in maac.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(maac[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(maac[k][i]))) for i in maac[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./maac/%s.csv' % k)

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
# ODEC-D: 402290
# ODEC-V: 402291
# ODEC: 40229
# SOCO-APCO: 18195AL
# SOCO-GPCO: 18195GP
# SOCO-GUCO: 18195GU
# SOCO-MPCO: 18195MP
# SOCO-SECO: 18195SE

serc = {
    189 : {
        1993 : pd.read_csv('%s/serc/1993/AEC93' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel(),
        1994 : pd.read_csv('%s/serc/1994/AEC94' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1995 : pd.read_csv('%s/serc/1995/AEC95' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_csv('%s/serc/1996/AEC96' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('%s/serc/1997/AEC97' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/serc/1998/AEC98' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        1999 : pd.read_csv('%s/serc/1999/AEC99' % (fulldir), sep='\t', skipinitialspace=True, header=None, skiprows=3).iloc[:, 1:].values.ravel(),
        2000 : pd.read_csv('%s/serc/2000/AEC00' % (fulldir), sep='\t', skipinitialspace=True, header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        2001 : pd.read_csv('%s/serc/2001/AEC01' % (fulldir), sep='\t', skipinitialspace=True, header=None, skiprows=5).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('%s/serc/2002/AEC02' % (fulldir), sep='\t', skipinitialspace=True, header=None, skiprows=4).iloc[:, 1:].values.ravel(),
        2004 : pd.read_csv('%s/serc/2004/AEC04' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=4).iloc[:, 1:].values.ravel()
    },
    3046 : {
        1994 : pd.read_csv('%s/serc/1994/CPL94' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        1995 : pd.read_csv('%s/serc/1995/CPL95' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=5)[1].values,
        1996 : pd.DataFrame([i.split() for i in open('%s/serc/1996/CEPL96' % (fulldir)).readlines()[1:]])[2].astype(float).values,
        1997 : pd.DataFrame([i.split() for i in open('%s/serc/1997/CPL97' % (fulldir)).readlines()[1:]])[2].astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('%s/serc/1998/CPL98' % (fulldir)).readlines()[1:]])[2].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('%s/serc/1999/CPL99' % (fulldir)).readlines()[1:]])[2].astype(float).values,
        2000 : pd.read_excel('%s/serc/2000/CPL00' % (fulldir))['Load'].values,
        2001 : pd.read_excel('%s/serc/2001/CPL01' % (fulldir))['Load'].values,
        2002 : pd.read_excel('%s/serc/2002/CPL02' % (fulldir))['Load'].values,
        2003 : pd.read_excel('%s/serc/2003/CPL03' % (fulldir))['Load'].values,
        2004 : pd.read_excel('%s/serc/2004/CPL04' % (fulldir))['Load'].values
    },
    40218 : {
        1993 : pd.read_fwf('%s/serc/1993/CEPC93' % (fulldir), header=None).iloc[:, 1:-1].values.ravel(),
        1994 : pd.read_csv('%s/serc/1994/CEPC94' % (fulldir), sep=' ', skipinitialspace=True, header=None, skiprows=1).iloc[:, 1:-1].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_csv('%s/serc/1995/CEPC95' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 1:-1].replace('.', '0').astype(float).values.ravel(),
        1996 : (pd.read_fwf('%s/serc/1996/CEPC96' % (fulldir)).iloc[:-1, 1:]/1000).values.ravel(),
        1997 : (pd.DataFrame([i.split() for i in open('%s/serc/1997/CEPC97' % (fulldir)).readlines()[5:]]).iloc[:-1, 1:].astype(float)/1000).values.ravel(),
        1998 : (pd.DataFrame([i.split() for i in open('%s/serc/1998/CEPC98' % (fulldir)).readlines()]).iloc[:, 1:].astype(float)).values.ravel(),
        2000 : pd.read_excel('%s/serc/2000/CEPC00' % (fulldir), sheetname=1, skiprows=3)['MW'].values,
        2001 : pd.read_excel('%s/serc/2001/CEPC01' % (fulldir), sheetname=1, skiprows=3)['MW'].values,
        2002 : pd.read_excel('%s/serc/2002/CEPC02' % (fulldir), sheetname=0, skiprows=5)['MW'].values,
        2002 : pd.read_excel('%s/serc/2002/CEPC02' % (fulldir), sheetname=0, skiprows=5)['MW'].values
    },
    3408 : {
        1993 : (pd.DataFrame([i.split() for i in open('%s/serc/1993/CEPB93' % (fulldir)).readlines()[12:]])[1].astype(float)/1000).values,
        1994 : (pd.DataFrame([i.split() for i in open('%s/serc/1994/CEPB94' % (fulldir)).readlines()[10:]])[1].astype(float)).values,
        1995 : (pd.DataFrame([i.split() for i in open('%s/serc/1995/CEPB95' % (fulldir)).readlines()[6:]])[2].astype(float)).values,
        1996 : (pd.DataFrame([i.split() for i in open('%s/serc/1996/CEPB96' % (fulldir)).readlines()[10:]])[2].astype(float)).values,
        1997 : (pd.DataFrame([i.split() for i in open('%s/serc/1997/CEPB97' % (fulldir)).readlines()[9:]])[2].astype(float)).values,
        1998 : (pd.DataFrame([i.split() for i in open('%s/serc/1998/CEPB98' % (fulldir)).readlines()[9:]])[2].astype(float)).values,
        1999 : (pd.DataFrame([i.split() for i in open('%s/serc/1999/CEPB99' % (fulldir)).readlines()[8:]])[2].astype(float)).values,
        2000 : (pd.DataFrame([i.split() for i in open('%s/serc/2000/CEPB00' % (fulldir)).readlines()[11:]])[2].astype(float)).values,
        2001 : (pd.DataFrame([i.split() for i in open('%s/serc/2001/CEPB01' % (fulldir)).readlines()[8:]])[2].astype(float)).values,
        2002 : (pd.DataFrame([i.split() for i in open('%s/serc/2002/CEPB02' % (fulldir)).readlines()[6:]])[4].astype(float)).values,
        2003 : (pd.DataFrame([i.split() for i in open('%s/serc/2003/CEPB03' % (fulldir)).readlines()[6:]])[2].astype(float)).values
    },
    12293 : {
        2000 : (pd.read_csv('%s/serc/2000/MEMP00' % (fulldir)).iloc[:, -1]/1000).values,
        2001 : (pd.DataFrame([i.split() for i in open('%s/serc/2001/MEMP01' % (fulldir)).readlines()[1:]])[3].str.replace(',', '').astype(float)/1000).values,
        2002 : (pd.read_csv('%s/serc/2002/MEMP02' % (fulldir), sep='\t').iloc[:, -1].str.replace(',', '').astype(float)/1000).values,
        2003 : pd.read_csv('%s/serc/2003/MEMP03' % (fulldir)).iloc[:, -1].str.replace(',', '').astype(float).values
    },
    5416 : {
        1999 : pd.DataFrame([i.split() for i in open('%s/serc/1999/DUKE99' % (fulldir)).readlines()[4:]])[2].astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/DUKE00' % (fulldir)).readlines()[5:]])[2].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('%s/serc/2001/DUKE01' % (fulldir)).readlines()[5:]])[2].astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('%s/serc/2002/DUKE02' % (fulldir)).readlines()[5:]])[2].astype(float).values,
        2003 : pd.DataFrame([i.split() for i in open('%s/serc/2003/DUKE03' % (fulldir)).readlines()[5:-8]])[2].astype(float).values,
        2004 : pd.DataFrame([i.split() for i in open('%s/serc/2004/DUKE04' % (fulldir)).readlines()[5:]])[2].astype(float).values
    },
    6411 : {
        1993 : (pd.DataFrame([i.split() for i in open('%s/serc/1993/FLINT93' % (fulldir)).readlines()])[6].astype(float)/1000).values,
        1994 : ((pd.DataFrame([i.split() for i in open('%s/serc/1994/FLINT94' % (fulldir)).readlines()[:-1]])).iloc[:, -1].astype(float)/1000).values,
        1995 : ((pd.DataFrame([i.split() for i in open('%s/serc/1995/FLINT95' % (fulldir)).readlines()[1:]]))[3].astype(float)/1000).values,
        1996 : (pd.DataFrame([i.split() for i in open('%s/serc/1996/FLINT96' % (fulldir)).readlines()[3:-2]]))[2].astype(float).values,
        1997 : (pd.DataFrame([i.split() for i in open('%s/serc/1997/FLINT97' % (fulldir)).readlines()[6:]]))[3].astype(float).values,
        1998 : (pd.DataFrame([i.split() for i in open('%s/serc/1998/FLINT98' % (fulldir)).readlines()[4:]]))[2].astype(float).values,
        1999 : (pd.DataFrame([i.split() for i in open('%s/serc/1999/FLINT99' % (fulldir)).readlines()[1:]]))[1].astype(float).values,
        2000 : (pd.DataFrame([i.split() for i in open('%s/serc/2000/FLINT00' % (fulldir)).readlines()[2:]]))[4].astype(float).values
    },
    7639 : {
        1993 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1993', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1993', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1994 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1994', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1994', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1995 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1995', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1995', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1996 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1996', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1996', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1997 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1997', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1997', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1998 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1998', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1998', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        1999 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1999', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='1999', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
        2000 : np.concatenate([pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='2000', skiprows=7, header=None).iloc[:24, 1:183].values.ravel(order='F'), pd.read_excel('%s/serc/2000/GUC00' % (fulldir), sheetname='2000', skiprows=45, header=None).iloc[:24, 1:183].values.ravel(order='F')]).astype(float)/1000,
    },
    10857 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/serc/1993/LCEC93' % (fulldir)).readlines()[:-1]]).iloc[:, 3:].astype(float).values.ravel(),
        1994 : pd.DataFrame([i.split() for i in open('%s/serc/1994/LCEC94' % (fulldir)).readlines()[:-1]]).iloc[:, 3:].astype(float).values.ravel()
    },
    13204 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/serc/1993/NPL93' % (fulldir)).readlines()[6:]])[2].astype(float).values,
        1994 : pd.read_fwf('%s/serc/1994/NPL94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    13994 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/serc/1993/OPC93' % (fulldir)).readlines()[4:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1995 : pd.DataFrame([i.split() for i in open('%s/serc/1995/OPC95' % (fulldir)).readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1996 : pd.DataFrame([i.split() for i in open('%s/serc/1996/OPC96' % (fulldir)).readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1997 : pd.DataFrame([i.split() for i in open('%s/serc/1997/OPC97' % (fulldir)).readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1998 : pd.DataFrame([i.split() for i in open('%s/serc/1998/OPC98' % (fulldir)).readlines()[12:]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('%s/serc/1999/OPC99' % (fulldir)).readlines()[18:]])[2].astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/OPC00' % (fulldir)).readlines()[19:]])[2].astype(float).values
    },
    17539 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/serc/1993/SCEG93' % (fulldir)).readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1995 : pd.DataFrame([i.split() for i in open('%s/serc/1995/SCEG95' % (fulldir)).readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1996 : pd.DataFrame([i.split() for i in open('%s/serc/1996/SCEG96' % (fulldir)).readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1997 : pd.DataFrame([i.split() for i in open('%s/serc/1997/SCEG97' % (fulldir)).readlines()[:-1]]).iloc[:, -1].astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('%s/serc/1998/SCEG98' % (fulldir)).readlines()[:]]).iloc[:, -1].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('%s/serc/1999/SCEG99' % (fulldir)).readlines()[:]]).iloc[:, -1].astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/SCEG00' % (fulldir)).readlines()[:]]).iloc[:, -1].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('%s/serc/2001/SCEG01' % (fulldir)).readlines()[:]]).iloc[:, -1].astype(float).values
    },
    17543 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/serc/1993/SCPS93' % (fulldir)).readlines()[:]]).iloc[:, 1:].astype(float).values.ravel(),
        1996 : pd.DataFrame([i.split() for i in open('%s/serc/1996/SCPS96' % (fulldir)).readlines()[:-1]]).astype(float).values.ravel(),
        1997 : pd.DataFrame([i.split() for i in open('%s/serc/1997/SCPS97' % (fulldir)).readlines()[1:-3]]).iloc[:, 4:-1].astype(float).values.ravel(),
        1998 : pd.DataFrame([i.split() for i in open('%s/serc/1998/SCPS98' % (fulldir)).readlines()[:-1]]).iloc[:, 1:].replace('NA', '0').astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('%s/serc/1999/SCPS99' % (fulldir)).readlines()[1:-1]]).iloc[:, 2:-1].replace('NA', '0').astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/SCPS00' % (fulldir)).readlines()[:]]).iloc[:, 2:].replace('NA', '0').astype(float).values.ravel(),
        2001 : pd.DataFrame([i.split() for i in open('%s/serc/2001/SCPS01' % (fulldir)).readlines()[:]]).iloc[:, 2:].replace('NA', '0').astype(float).values.ravel(),
        2002 : pd.read_excel('%s/serc/2002/SCPS02' % (fulldir), header=None).dropna(axis=1, how='all').iloc[:, 2:-1].values.ravel(),
        2003 : pd.DataFrame([i.split() for i in open('%s/serc/2003/SCPS03' % (fulldir)).readlines()[:]]).iloc[:, 2:].replace('NA', '0').astype(float).values.ravel(),
        2004 : pd.DataFrame([i.split() for i in open('%s/serc/2004/SCPS04' % (fulldir)).readlines()[1:]]).iloc[:, 1:-1].replace('NA', '0').astype(float).values.ravel()
    },
    17568 : {
        1993 : (pd.DataFrame([i.split() for i in open('%s/serc/1993/SMEA93' % (fulldir)).readlines()[5:]])[2].astype(float)/1000).values.ravel(),
        1994 : (pd.DataFrame([i.split() for i in open('%s/serc/1994/SMEA94' % (fulldir)).readlines()[5:]]).iloc[:, -1].astype(float)).values,
        1996 : ((pd.DataFrame([i.split() for i in open('%s/serc/1996/SMEA96' % (fulldir)).readlines()[:]])).iloc[:, -24:].astype(float)/1000).values.ravel(),
        1997 : pd.read_excel('%s/serc/1997/SMEA97' % (fulldir), sheetname=1, header=None, skiprows=1).iloc[:, 1:].values.ravel(),
        1998 : pd.DataFrame([i.split() for i in open('%s/serc/1998/SMEA98' % (fulldir)).readlines()[1:]])[2].astype(float).values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('%s/serc/1999/SMEA99' % (fulldir)).readlines()[1:]])[2].astype(float).values.ravel(),
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/SMEA00' % (fulldir)).readlines()[1:]])[2].astype(float).values.ravel(),
        2002 : pd.DataFrame([i.split() for i in open('%s/serc/2002/SMEA02' % (fulldir)).readlines()[2:]])[2].astype(float).values.ravel(),
        2003 : pd.DataFrame([i.split() for i in open('%s/serc/2003/SMEA03' % (fulldir)).readlines()[1:]])[2].astype(float).values.ravel()
    },
    18642 : {
        1993 : (pd.DataFrame([i.split() for i in open('%s/serc/1993/TVA93' % (fulldir)).readlines()[:-1]])[2].astype(float)).values.ravel(),
        1994 : (pd.DataFrame([i.split() for i in open('%s/serc/1994/TVA94' % (fulldir)).readlines()[:-1]])[2].astype(float)).values.ravel(),
        1995 : (pd.DataFrame([i.split() for i in open('%s/serc/1995/TVA95' % (fulldir)).readlines()[:-1]])[2].astype(float)).values.ravel(),
        1996 : (pd.DataFrame([i.split() for i in open('%s/serc/1996/TVA96' % (fulldir)).readlines()[:-1]])[2].astype(float)).values.ravel(),
        1997 : (pd.DataFrame([i.split() for i in open('%s/serc/1997/TVA97' % (fulldir)).readlines()[:-1]])[2].astype(float)).values.ravel(),
        1998 : (pd.DataFrame([i.split() for i in open('%s/serc/1998/TVA98' % (fulldir)).readlines()[:-1]])[2].astype(float)).values.ravel(),
        1999 : pd.read_excel('%s/serc/1999/TVA99' % (fulldir)).iloc[:, 2].astype(float).values,
        2000 : pd.read_excel('%s/serc/2000/TVA00' % (fulldir)).iloc[:, 2].astype(float).values,
        2001 : pd.read_excel('%s/serc/2001/TVA01' % (fulldir), header=None, skiprows=3).iloc[:, 2].astype(float).values,
        2003 : pd.read_excel('%s/serc/2003/TVA03' % (fulldir)).iloc[:, -1].values
    },
    19876 : {
        1993 : pd.read_fwf('%s/serc/1993/VIEP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('%s/serc/1994/VIEP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('%s/serc/1995/VIEP95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/serc/1996/VIEP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('%s/serc/1997/VIEP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1998 : pd.read_fwf('%s/serc/1998/VIEP98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('%s/serc/1999/VIEP99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2000 : (pd.DataFrame([i.split() for i in open('%s/serc/2000/VIEP00' % (fulldir)).readlines()[1:]])[2].astype(float)).values.ravel(),
        2001 : (pd.DataFrame([i.split() for i in open('%s/serc/2001/VIEP01' % (fulldir)).readlines()[1:]])[2].astype(float)).values.ravel(),
        2002 : (pd.DataFrame([i.split() for i in open('%s/serc/2002/VIEP02' % (fulldir)).readlines()[1:]])[2].astype(float)).values.ravel(),
        2003 : (pd.DataFrame([i.split() for i in open('%s/serc/2003/VIEP03' % (fulldir)).readlines()[2:]])[3].astype(float)).values.ravel(),
        2004 : (pd.DataFrame([i.split() for i in open('%s/serc/2004/VIEP04' % (fulldir)).readlines()[:]])[3].astype(float)).values.ravel()
    },
    20065 : {
        1993 : pd.read_fwf('%s/serc/1993/WEMC93' % (fulldir), header=None).iloc[:, 1:].values.ravel(),
        1995 : (pd.read_csv('%s/serc/1995/WEMC95' % (fulldir), skiprows=1, header=None, sep=' ', skipinitialspace=True)[3]/1000).values,
        1996 : (pd.read_excel('%s/serc/1996/WEMC96' % (fulldir))['Load']/1000).values,
        1997 : pd.read_excel('%s/serc/1997/WEMC97' % (fulldir), skiprows=4)['MW'].values,
        1998 : pd.concat([pd.read_excel('%s/serc/1998/WEMC98' % (fulldir), sheetname=i).iloc[:, -1] for i in range(12)]).values,
        1999 : pd.read_excel('%s/serc/1999/WEMC99' % (fulldir))['mwh'].values,
        2000 : (pd.read_excel('%s/serc/2000/WEMC00' % (fulldir)).iloc[:, -1]/1000).values,
        2001 : (pd.read_excel('%s/serc/2001/WEMC01' % (fulldir), header=None)[0]/1000).values
    },
    4958 : {
        1999 : (pd.DataFrame([i.split() for i in open('%s/serc/1999/DU99' % (fulldir)).readlines()[1:]]).iloc[:-1, 2:].apply(lambda x: x.str.replace('[,"]', '').str.strip()).astype(float)/1000).values.ravel(),
        2000 : (pd.DataFrame([i.split() for i in open('%s/serc/2000/DU00' % (fulldir)).readlines()[1:]]).iloc[:-1, 2:].apply(lambda x: x.str.replace('[,"]', '').str.strip()).astype(float)/1000).values.ravel(),
        2003 : pd.read_excel('%s/serc/2003/DU03' % (fulldir)).iloc[:, -1].values
    },
    924 : {
        1999 : pd.read_excel('%s/serc/1999/AECI99' % (fulldir))['CALoad'].values,
        2001 : pd.read_excel('%s/serc/2001/AECI01' % (fulldir)).iloc[:, -1].values,
        2002 : pd.Series(pd.read_excel('%s/serc/2002/AECI02' % (fulldir), skiprows=3).loc[:, 'Jan':'Dec'].values.ravel(order='F')).dropna().values
    },
    402290 : {
        1996 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1996/ODECD96' % (fulldir)).readlines()[3:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1997 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1997/ODECD97' % (fulldir)).readlines()[4:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1998 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1998/ODECD98' % (fulldir)).readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1999 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1999/ODECD99' % (fulldir)).readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/ODECD00' % (fulldir)).readlines()[3:]])[4].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('%s/serc/2001/ODECD01' % (fulldir)).readlines()[3:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('%s/serc/2002/ODECD02' % (fulldir)).readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2003 : pd.DataFrame([i.split() for i in open('%s/serc/2003/ODECD03' % (fulldir)).readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2004 : pd.DataFrame([i.split() for i in open('%s/serc/2004/ODECD04' % (fulldir)).readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values
    },
    402291 : {
        1996 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1996/ODECV96' % (fulldir)).readlines()[3:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1997 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1997/ODECV97' % (fulldir)).readlines()[4:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1998 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1998/ODECV98' % (fulldir)).readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1999 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1999/ODECV99' % (fulldir)).readlines()[2:]]).iloc[:, 3:].values.ravel()).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        2000 : pd.DataFrame([i.split() for i in open('%s/serc/2000/ODECV00' % (fulldir)).readlines()[3:]])[4].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('%s/serc/2001/ODECV01' % (fulldir)).readlines()[3:]])[4].dropna().str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2002 : pd.DataFrame([i.split() for i in open('%s/serc/2002/ODECV02' % (fulldir)).readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2003 : pd.DataFrame([i.split() for i in open('%s/serc/2003/ODECV03' % (fulldir)).readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values,
        2004 : pd.DataFrame([i.split() for i in open('%s/serc/2004/ODECV04' % (fulldir)).readlines()[5:]])[4].str.replace('[N/A]', '').replace('', '0').astype(float).values
    },
    '18195AL' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1993/APCO93' % (fulldir)).readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('%s/serc/1994/APCO94' % (fulldir)).readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('%s/serc/1999/SOCO99' % (fulldir))['Alabama'].dropna().values,
        2000 : pd.read_excel('%s/serc/2000/SOCO00' % (fulldir), skiprows=1).iloc[:, 2].values,
        2001 : pd.read_excel('%s/serc/2001/SOCO01' % (fulldir))['Alabama'].values,
        2002 : pd.read_excel('%s/serc/2002/SOCO02' % (fulldir), skiprows=1).iloc[:, 2].values,
        2003 : pd.read_excel('%s/serc/2003/SOCO03' % (fulldir)).iloc[:, 2].values,
        2004 : pd.read_excel('%s/serc/2004/SOCO04' % (fulldir), skiprows=1).iloc[:, 1].values
    },
    '18195GP' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1993/GPCO93' % (fulldir)).readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('%s/serc/1994/GPCO94' % (fulldir)).readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('%s/serc/1999/SOCO99' % (fulldir))['Georgia'].dropna().values,
        2000 : pd.read_excel('%s/serc/2000/SOCO00' % (fulldir), skiprows=1).iloc[:, 3].values,
        2001 : pd.read_excel('%s/serc/2001/SOCO01' % (fulldir))['Georgia'].values,
        2002 : pd.read_excel('%s/serc/2002/SOCO02' % (fulldir), skiprows=1).iloc[:, 3].values,
        2003 : pd.read_excel('%s/serc/2003/SOCO03' % (fulldir)).iloc[:, 3].values,
        2004 : pd.read_excel('%s/serc/2004/SOCO04' % (fulldir), skiprows=1).iloc[:, 2].values
    },
    '18195GU' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1993/GUCO93' % (fulldir)).readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('%s/serc/1994/GUCO94' % (fulldir)).readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('%s/serc/1999/SOCO99' % (fulldir))['Gulf'].dropna().values,
        2000 : pd.read_excel('%s/serc/2000/SOCO00' % (fulldir), skiprows=1).iloc[:, 4].values,
        2001 : pd.read_excel('%s/serc/2001/SOCO01' % (fulldir))['Gulf'].values,
        2002 : pd.read_excel('%s/serc/2002/SOCO02' % (fulldir), skiprows=1).iloc[:, 4].values,
        2003 : pd.read_excel('%s/serc/2003/SOCO03' % (fulldir)).iloc[:, 4].values,
        2004 : pd.read_excel('%s/serc/2004/SOCO04' % (fulldir), skiprows=1).iloc[:, 3].values
    },
    '18195MP' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1993/MPCO93' % (fulldir)).readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('%s/serc/1994/MPCO94' % (fulldir)).readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('%s/serc/1999/SOCO99' % (fulldir))['Mississippi'].dropna().values,
        2000 : pd.read_excel('%s/serc/2000/SOCO00' % (fulldir), skiprows=1).iloc[:, 5].values,
        2001 : pd.read_excel('%s/serc/2001/SOCO01' % (fulldir))['Mississippi'].values,
        2002 : pd.read_excel('%s/serc/2002/SOCO02' % (fulldir), skiprows=1).iloc[:, 5].values,
        2003 : pd.read_excel('%s/serc/2003/SOCO03' % (fulldir)).iloc[:, 5].values,
        2004 : pd.read_excel('%s/serc/2004/SOCO04' % (fulldir), skiprows=1).iloc[:, 4].values
    },
    '18195SE' : {
        1993 : pd.Series(pd.DataFrame([i.split() for i in open('%s/serc/1993/SECO93' % (fulldir)).readlines()[:-1]]).iloc[:,-1].values).str.replace('[^\d]', '').replace('', '0').astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('%s/serc/1994/SECO94' % (fulldir)).readlines()[:-1]]).iloc[:, 1:].astype(float).values.ravel(),
        1999 : pd.read_excel('%s/serc/1999/SOCO99' % (fulldir))['Savannah'].dropna().values,
        2000 : pd.read_excel('%s/serc/2000/SOCO00' % (fulldir), skiprows=1).iloc[:, 6].values,
        2001 : pd.read_excel('%s/serc/2001/SOCO01' % (fulldir))['Savannah'].values,
        2002 : pd.read_excel('%s/serc/2002/SOCO02' % (fulldir), skiprows=1).iloc[:, 6].values,
        2003 : pd.read_excel('%s/serc/2003/SOCO03' % (fulldir)).iloc[:, 6].values,
        2004 : pd.read_excel('%s/serc/2004/SOCO04' % (fulldir), skiprows=1).iloc[:, 5].values
    },
    18195 : {
        1999 : pd.read_excel('%s/serc/1999/SOCO99' % (fulldir))['System'].dropna().values,
        2000 : pd.read_excel('%s/serc/2000/SOCO00' % (fulldir), skiprows=1).iloc[:, 7].values,
        2001 : pd.read_excel('%s/serc/2001/SOCO01' % (fulldir))['Southern'].values,
        2002 : pd.read_excel('%s/serc/2002/SOCO02' % (fulldir), skiprows=1).iloc[:, 7].values,
        2003 : pd.read_excel('%s/serc/2003/SOCO03' % (fulldir)).iloc[:, 8].values,
        2004 : pd.read_excel('%s/serc/2004/SOCO04' % (fulldir), skiprows=1).iloc[:, 7].values
    }
}

serc.update({40229 : {}})
for i in serc[402290].keys():
    serc[40229][i] = serc[402290][i] + serc[402291][i]

for k in serc.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(serc[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(serc[k][i]))) for i in serc[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./serc/%s.csv' % k)

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
        1993 : pd.read_csv('%s/spp/1993/AECC93' % (fulldir), skiprows=6, skipfooter=1, header=None).iloc[:, -1].values,
        1994 : pd.read_csv('%s/spp/1994/AECC94' % (fulldir), skiprows=8, skipfooter=1, header=None).iloc[:, -1].values,
        1995 : pd.read_csv('%s/spp/1995/AECC95' % (fulldir), skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1996 : pd.read_csv('%s/spp/1996/AECC96' % (fulldir), skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1997 : pd.read_csv('%s/spp/1997/AECC97' % (fulldir), skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1998 : pd.read_csv('%s/spp/1998/AECC98' % (fulldir), skiprows=9, skipfooter=1, header=None).iloc[:, -1].values,
        1999 : pd.read_csv('%s/spp/1999/AECC99' % (fulldir), skiprows=5, skipfooter=1, header=None).iloc[:, -1].values,
        2003 : pd.read_csv('%s/spp/2003/AECC03' % (fulldir), skiprows=5, skipfooter=1, header=None).iloc[:, -2].values,
        2004 : pd.read_csv('%s/spp/2004/AECC04' % (fulldir), skiprows=5, header=None).iloc[:, -2].values
    },
    2777 : {
        1998 : pd.read_excel('%s/spp/1998/CAJN98' % (fulldir), skiprows=4).iloc[:365, 1:].values.ravel(),
        1999 : pd.DataFrame([i.split() for i in open('%s/spp/1999/CAJN99' % (fulldir)).readlines()[:]])[2].astype(float).values
    },
    3265 : {
        1994 : pd.read_fwf('%s/spp/1994/CLEC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.DataFrame([i.split() for i in open('%s/spp/1996/CLEC96' % (fulldir)).readlines()[:]])[0].astype(float).values,
        1997 : pd.read_csv('%s/spp/1997/CLEC97' % (fulldir)).iloc[:, 2].str.replace(',', '').astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('%s/spp/1998/CLEC98' % (fulldir)).readlines()[:]])[1].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('%s/spp/1999/CLEC99' % (fulldir)).readlines()[1:]]).iloc[:, 0].astype(float).values,
        2001 : pd.DataFrame([i.split() for i in open('%s/spp/2001/CLEC01' % (fulldir)).readlines()[:]])[4].replace('NA', '0').astype(float).values,
    },
    5860 : {
        1997 : pd.DataFrame([i.split() for i in open('%s/spp/1997/EMDE97' % (fulldir)).readlines()[:]])[3].astype(float).values,
        1998 : pd.DataFrame([i.split() for i in open('%s/spp/1998/EMDE98' % (fulldir)).readlines()[2:-2]])[2].astype(float).values,
        1999 : pd.DataFrame([i.split() for i in open('%s/spp/1999/EMDE99' % (fulldir)).readlines()[3:8763]])[2].astype(float).values,
        2001 : pd.read_excel('%s/spp/2001/EMDE01' % (fulldir))['Load'].dropna().values,
        2002 : pd.read_excel('%s/spp/2002/EMDE02' % (fulldir))['Load'].dropna().values,
        2003 : pd.read_excel('%s/spp/2003/EMDE03' % (fulldir))['Load'].dropna().values,
        2004 : pd.read_excel('%s/spp/2004/EMDE04' % (fulldir), skiprows=2).iloc[:8784, -1].values
    },
    12506 : {
        1994 : pd.DataFrame([i.split() for i in open('%s/spp/1994/ENTR94' % (fulldir)).readlines()[:]]).iloc[:, 1:-1].astype(float).values.ravel(),
        1995 : pd.DataFrame([i.split() for i in open('%s/spp/1995/ENTR95' % (fulldir)).readlines()[1:-2]]).iloc[:, 1:-1].astype(float).values.ravel(),
        1997 : pd.read_csv('%s/spp/1997/ENTR97' % (fulldir), header=None).iloc[:, 1:-1].astype(float).values.ravel(),
        1998 : pd.read_csv('%s/spp/1998/ENTR98' % (fulldir), header=None)[2].astype(float).values,
        1999 : pd.read_excel('%s/spp/1999/ENTR99' % (fulldir)).iloc[:, -1].values,
        2000 : pd.DataFrame([i.split() for i in open('%s/spp/2000/ENTR00' % (fulldir)).readlines()[4:]]).iloc[:, 3:].astype(float).values.ravel(),
        2001 : pd.read_fwf('%s/spp/2001/ENTR01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
    },
    9996 : {
        1994 : pd.read_fwf('%s/spp/1994/KCPU94' % (fulldir), skiprows=4, header=None).astype(str).apply(lambda x: x.str[-3:]).astype(float).values.ravel(),
        1997 : pd.read_csv('%s/spp/1997/KCPU97' % (fulldir), engine='python', header=None)[0].values,
        1998 : pd.read_csv('%s/spp/1998/KCPU98' % (fulldir), engine='python', header=None)[0].values,
        1999 : pd.read_csv('%s/spp/1999/KCPU99' % (fulldir), skiprows=1, engine='python', header=None)[0].values,
        2000 : pd.read_csv('%s/spp/2000/KCPU00' % (fulldir), engine='python', header=None)[0].values,
        2002 : pd.read_excel('%s/spp/2002/KCPU02' % (fulldir)).iloc[:, -1].values,
        2003 : pd.read_csv('%s/spp/2003/KCPU03' % (fulldir), engine='python', header=None)[0].values,
        2004 : pd.read_csv('%s/spp/2004/KCPU04' % (fulldir), engine='python', header=None)[0].values
    },
    26253 : {
        1993 : pd.read_csv('%s/spp/1993/LEPA93' % (fulldir), skiprows=3, header=None)[0].values,
        1994 : pd.read_csv('%s/spp/1994/LEPA94' % (fulldir), skiprows=3, header=None)[0].values,
        1995 : pd.read_csv('%s/spp/1995/LEPA95' % (fulldir), sep='\t', skiprows=1, header=None)[2].values,
        1996 : pd.read_csv('%s/spp/1996/LEPA96' % (fulldir), sep='\t', skiprows=1, header=None)[2].values,
        1997 : pd.read_csv('%s/spp/1997/LEPA97' % (fulldir), engine='python', header=None)[0].values,
        1998 : pd.read_csv('%s/spp/1998/LEPA98' % (fulldir), sep=' ', skipinitialspace=True, skiprows=2, header=None),
        1998 : pd.Series(pd.read_csv('%s/spp/1998/LEPA98' % (fulldir), sep=' ', skipinitialspace=True, skiprows=2, header=None)[[1,3]].values.ravel(order='F')).dropna().values,
        1999 : pd.read_csv('%s/spp/1999/LEPA99' % (fulldir), sep='\t')['Load'].values,
        2001 : pd.read_csv('%s/spp/2001/LEPA01' % (fulldir), engine='python', sep='\t', header=None)[1].values,
        2002 : pd.read_csv('%s/spp/2002/LEPA02' % (fulldir), engine='python', sep='\t', header=None)[1].values,
        2003 : pd.read_excel('%s/spp/2003/LEPA03' % (fulldir), header=None)[1].values
    },
    9096 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/spp/1993/LUS93' % (fulldir)).readlines()[3:-1]]).iloc[:, -1].astype(float).values,
        1994 : pd.DataFrame([i.split() for i in open('%s/spp/1994/LUS94' % (fulldir)).readlines()[3:-1]]).iloc[:, -1].astype(float).values,
        1995 : pd.DataFrame([i.split() for i in open('%s/spp/1995/LUS95' % (fulldir)).readlines()[4:-1]]).iloc[:, -1].astype(float).values,
        1996 : pd.DataFrame([i.split() for i in open('%s/spp/1996/LUS96' % (fulldir)).readlines()[4:-1]]).iloc[:, -1].astype(float).values,
        1997 : pd.DataFrame([i.split('\t') for i in open('%s/spp/1997/LUS97' % (fulldir)).readlines()[3:-2]]).iloc[:, -1].astype(float).values,
        1998 : pd.DataFrame([i.split('\t') for i in open('%s/spp/1998/LUS98' % (fulldir)).readlines()[4:]]).iloc[:, -1].astype(float).values,
        1999 : pd.DataFrame([i.split('  ') for i in open('%s/spp/1999/LUS99' % (fulldir)).readlines()[4:]]).iloc[:, -1].astype(float).values,
        2000 : pd.read_csv('%s/spp/2000/LUS00' % (fulldir), skiprows=3, skipfooter=1, header=None).iloc[:, -1].values,
        2001 : pd.read_csv('%s/spp/2001/LUS01' % (fulldir), skiprows=3, header=None).iloc[:, -1].values,
        2002 : pd.read_csv('%s/spp/2002/LUS02' % (fulldir), skiprows=3, header=None).iloc[:, -1].values,
        2003 : pd.read_csv('%s/spp/2003/LUS03' % (fulldir), skiprows=3, header=None).iloc[:, -1].values,
        2004 : pd.read_csv('%s/spp/2004/LUS04' % (fulldir), skiprows=4, header=None).iloc[:, -1].values
    },
    7806 : {
        1993 : pd.read_csv('%s/spp/1993/GSU93' % (fulldir), engine='python', header=None)[0].values
    },
    12699 : {
        1993 : pd.read_csv('%s/spp/1993/MPS93' % (fulldir), sep=' ', skipinitialspace=True)['TOTLOAD'].values,
        1996 : pd.read_excel('%s/spp/1996/MPS96' % (fulldir), skiprows=6, header=None).iloc[:, -1].values,
        1998 : pd.read_csv('%s/spp/1998/MPS98' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2000 : pd.read_csv('%s/spp/2000/MPS00' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2001 : pd.read_csv('%s/spp/2001/MPS01' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2002 : pd.read_csv('%s/spp/2002/MPS02' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values,
        2003 : pd.read_excel('%s/spp/2003/MPS03' % (fulldir)).iloc[:, 1:].values.ravel()
    },
    14063 : {
        1994 : pd.read_csv('%s/spp/1994/OKGE94' % (fulldir), header=None).iloc[:, 1:13].values.ravel()
    },
    14077 : {
        1993 : pd.read_csv('%s/spp/1993/OMPA93' % (fulldir), skiprows=2, header=None, sep=' ', skipinitialspace=True, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('%s/spp/1997/OMPA97' % (fulldir), engine='python', header=None)[0].values,
        1998 : pd.read_csv('%s/spp/1998/OMPA98' % (fulldir), skiprows=2, engine='python', header=None)[0].str.replace('\*', '').astype(float).values,
        2000 : pd.read_csv('%s/spp/2000/OMPA00' % (fulldir), skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2001 : pd.read_csv('%s/spp/2001/OMPA01' % (fulldir), skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2002 : pd.read_csv('%s/spp/2002/OMPA02' % (fulldir), skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2003 : pd.read_csv('%s/spp/2003/OMPA03' % (fulldir), skiprows=2, engine='python', header=None)[0].astype(float).values/1000,
        2004 : pd.read_csv('%s/spp/2004/OMPA04' % (fulldir), skiprows=2, engine='python', header=None)[0].astype(float).values/1000
    },
    15474 : {
        1993 : pd.read_fwf('%s/spp/1993/PSOK93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
    },
    18315 : {
        1993 : pd.read_csv('%s/spp/1993/SEPC93' % (fulldir), header=None).iloc[:, 1:].astype(str).apply(lambda x: x.str.replace('NA', '').str.strip()).replace('', '0').astype(float).values.ravel(),
        1997 : (pd.read_fwf('%s/spp/1997/SEPC97' % (fulldir), skiprows=1, header=None)[5]/1000).values,
        1999 : pd.read_csv('%s/spp/1999/SEPC99' % (fulldir), sep='\t', skipinitialspace=True, header=None)[3].str.strip().replace('#VALUE!', '0').astype(float).values,
        2000 : pd.read_csv('%s/spp/2000/SEPC00' % (fulldir), sep='\t', skipinitialspace=True, header=None)[3].apply(lambda x: 0 if len(x) > 3 else x).astype(float).values,
        2001 : pd.read_csv('%s/spp/2001/SEPC01' % (fulldir), sep='\t', skipinitialspace=True, header=None)[3].apply(lambda x: 0 if len(x) > 3 else x).astype(float).values,
        2002 : (pd.read_fwf('%s/spp/2002/SEPC02' % (fulldir), skiprows=1, header=None)[6]).str.replace('"', '').str.strip().astype(float).values,
        2004 : pd.read_csv('%s/spp/2004/SEPC04' % (fulldir), header=None, sep='\t')[5].values
    },
    20447 : {
        1993 : pd.read_csv('%s/spp/1993/WFEC93' % (fulldir)).iloc[:, 0].values,
        2000 : pd.read_csv('%s/spp/2000/WFEC00' % (fulldir), header=None, sep=' ', skipinitialspace=True)[0].values
    },
    20391 : {
        1993 : pd.DataFrame([i.split() for i in open('%s/spp/1993/WPEK93' % (fulldir)).readlines()[:]]).iloc[:365, 1:25].astype(float).values.ravel(),
        1996 : pd.read_excel('%s/spp/1996/WPEK96' % (fulldir), skiprows=2).dropna().iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/spp/1998/WPEK98' % (fulldir), header=None, sep=' ', skipinitialspace=True)[6].values,
        2000 : pd.read_csv('%s/spp/2000/WPEK00' % (fulldir), header=None, sep=' ', skipinitialspace=True)[6].values,
        2001 : pd.read_csv('%s/spp/2001/WPEK01' % (fulldir), header=None, sep=' ', skipinitialspace=True)[6].values,
        2002 : pd.read_csv('%s/spp/2002/WPEK02' % (fulldir), header=None, sep=' ', skipinitialspace=True)[4].values
    },
    3283 : {
        1997 : pd.read_fwf('%s/spp/1997/CSWS97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/spp/1998/CSWS98' % (fulldir), skiprows=4, sep=' ', skipinitialspace=True, header=None)[2].values,
        1999 : pd.read_csv('%s/spp/1999/CSWS99' % (fulldir), skiprows=3, sep=' ', skipinitialspace=True, header=None)[2].values,
        2000 : pd.read_csv('%s/spp/2000/CSWS00' % (fulldir), skiprows=5, sep=' ', skipinitialspace=True, header=None)[2].values
    },
    40233 : {
        2000 : pd.read_fwf('%s/spp/2000/SRGT00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2001 : pd.read_fwf('%s/spp/2001/SRGT01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    7349 : {
        1997 : pd.read_csv('%s/spp/1997/GSEC97' % (fulldir), sep=' ', skipinitialspace=True, skiprows=2, header=None).iloc[:, 1:].values.ravel(),
        1998 : pd.read_csv('%s/spp/1998/GSEC98' % (fulldir), sep=' ', skipinitialspace=True, skiprows=2, header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_csv('%s/spp/1999/GSEC99' % (fulldir), sep='\s', skipinitialspace=True, skiprows=2, header=None)[17].dropna().values,
        2000 : pd.read_csv('%s/spp/2000/GSEC00' % (fulldir), skiprows=1, engine='python', header=None)[0].values,
        2001 : pd.DataFrame([i.split() for i in open('%s/spp/2001/GSEC01' % (fulldir)).readlines()[1:]])[0].astype(float).values,
        2002 : pd.read_csv('%s/spp/2002/GSEC02' % (fulldir), sep=' ', skipinitialspace=True, skiprows=2, header=None)[5].values,
        2003 : pd.read_csv('%s/spp/2003/GSEC03' % (fulldir), header=None)[2].values,
        2004 : (pd.read_csv('%s/spp/2004/GSEC04' % (fulldir), sep=' ', skipinitialspace=True, skiprows=1, header=None)[5]/1000).values
    }
}

for k in spp.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(spp[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(spp[k][i]))) for i in spp[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./spp/%s.csv' % k)

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
        1998 : pd.read_fwf('%s/mapp/1998/CIPC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    4322 : {
        1993 : pd.read_fwf('%s/mapp/1993/CP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/CP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/CP96' % (fulldir), header=None).iloc[:, 2:].values.ravel()
    },
    4363 : {
        1993 : pd.read_fwf('%s/mapp/1993/CBPC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/CBPC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/CBPC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/CBPC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/CBPC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/CB02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    4716 : {
        1993 : pd.read_fwf('%s/mapp/1993/DPC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/DPC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_csv('%s/mapp/1996/DPC96' % (fulldir), sep='\t', skipinitialspace=True, header=None).iloc[:, 6:].values.ravel()
    },
    9130 : {
        1993 : pd.read_fwf('%s/mapp/1993/HUC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/HUC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/HUC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/HUC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/HUC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/HUC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/HUC02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/HUC03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9219 : {
        1993 : pd.read_fwf('%s/mapp/1993/IESC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/IES94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/IESC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/IES97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/IESC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9392 : {
        1993 : pd.read_fwf('%s/mapp/1993/IPW93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/IPW94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/IPW95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/IPW96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/IPW97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/IPW98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    9438 : {
        1993 : pd.read_fwf('%s/mapp/1993/IIGE93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/IIGE94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/IIGE95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    11018 : {
        1993 : pd.read_fwf('%s/mapp/1993/LES93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/LES94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_csv('%s/mapp/1995/LES95' % (fulldir)).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/LES96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/LES97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/LES98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/LES99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2000 : pd.read_excel('%s/mapp/2000/LES00' % (fulldir), skipfooter=3).iloc[:, 1:].values.ravel(),
        2001 : pd.read_excel('%s/mapp/2001/LES01' % (fulldir), skipfooter=3).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/LES02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/LES03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    12647 : {
        1995 : pd.read_fwf('%s/mapp/1995/MPL95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2000 : pd.read_fwf('%s/mapp/2000/MPL00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2001 : pd.read_fwf('%s/mapp/2001/MPL01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    },
    12658 : {
        1993 : pd.read_fwf('%s/mapp/1993/MPC93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/MPC94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/MPC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/MPC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/MPC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/MPC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/MPC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/MPC02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/MPC03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    12819 : {
        1993 : pd.read_fwf('%s/mapp/1993/MDU93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/MDU94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/MDU95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/MDU96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/MDU97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/MDU98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/MDU99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/MDU02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/MDU03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    21352 : {
        1993 : pd.read_fwf('%s/mapp/1993/MEAN93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/MEAN95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/MEAN96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/MEAN97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/MEAN98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/MEAN99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).dropna().values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/MEAN02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/MEAN03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13143 : {
        1993 : pd.read_fwf('%s/mapp/1993/MPW93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/MPW94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/MPW95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/MPW96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/MPW97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:-1, range(1,13)+range(14,26)].values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/MPW98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/MPW99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/MPW02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/MPW03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13337 : {
        1993 : pd.read_fwf('%s/mapp/1993/NPPD93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/NPPD94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/NPPD95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/NPPD96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/NPPD97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/NPPD98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/NPPD99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2000 : pd.read_fwf('%s/mapp/2000/NPPD00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=9, skipfooter=1).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2001 : pd.read_fwf('%s/mapp/2001/NPPD01' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=9, skipfooter=1).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_csv('%s/mapp/2002/NPPD02' % (fulldir), sep='\t', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/NPPD03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    13781 : {
        1993 : pd.read_fwf('%s/mapp/1993/NSP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/NSP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/NSP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/NSP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/NSP98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/NSP99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2000 : pd.read_csv('%s/mapp/2000/NSP00' % (fulldir), sep='\t', skipinitialspace=True, skiprows=2, header=None, skipfooter=1)[2].values
    },
    13809 : {
        1993 : pd.read_fwf('%s/mapp/1993/NWPS93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/NWPS95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/NWPS96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/NWPS97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/NWPS98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/NWPS99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/NWPS02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/NWPS03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
    },
    14127 : {
        1993 : pd.read_fwf('%s/mapp/1993/OPPD93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/OPPD94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_csv('%s/mapp/1995/OPPD95' % (fulldir), sep='\t', skipinitialspace=True, header=None).iloc[:, 7:].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/OPPD96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/OPPD97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/OPPD98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/OPPD99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/OPPD02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/OPPD03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
    },
    14232 : {
        1993 : pd.read_fwf('%s/mapp/1993/OTP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/OTP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_csv('%s/mapp/1995/OTP95' % (fulldir), header=None).iloc[:, -2].values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/OTP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/OTP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/OTP98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/OTP99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2000 : pd.read_fwf('%s/mapp/2000/OTP00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/OTP02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/OTP03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
    },
    40580 : {
        1993 : pd.read_fwf('%s/mapp/1993/SMMP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/SMP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/SMMP96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/SMMP97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/SMMP98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/SMMPA99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2000 : pd.read_csv('%s/mapp/2000/SMMP00' % (fulldir)).iloc[:-1, 3].values,
        2001 : pd.read_csv('%s/mapp/2001/SMMP01' % (fulldir), header=None).iloc[:, 2].values,
        2002 : pd.read_fwf('%s/mapp/2002/SMMPA02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/SMMPA03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
    },
    19514 : {
        1993 : pd.read_fwf('%s/mapp/1993/UPA93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/UPA94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/UPA96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/UPA97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/UPA98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
    },
    20858 : {
        1993 : pd.read_fwf('%s/mapp/1993/WPPI93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/WPPI94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/WPPI96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_csv('%s/mapp/1997/WPPI97' % (fulldir), sep=' ', skipinitialspace=True, header=None).iloc[:, 2:-1].values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/WPPI98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/WPPI99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/WPPI02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/WPPI03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
    },
    9435 : {
        1995 : pd.read_fwf('%s/mapp/1995/MEC95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/MEC96' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1997 : pd.read_fwf('%s/mapp/1997/MEC97' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        1998 : pd.read_fwf('%s/mapp/1998/MEC98' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1999 : pd.read_fwf('%s/mapp/1999/MEC99' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2000 : pd.read_fwf('%s/mapp/2000/MEC00' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        2002 : pd.read_fwf('%s/mapp/2002/MEC02' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel(),
        2003 : pd.read_fwf('%s/mapp/2003/MEC_ALL03' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].dropna().values.ravel()
    },
    4322 : {
        1993 : pd.read_fwf('%s/mapp/1993/CP93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/CP94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1996 : pd.read_fwf('%s/mapp/1996/CP96' % (fulldir), header=None).iloc[:, 2:].values.ravel()
    },
    23333 : {
        1993 : pd.read_fwf('%s/mapp/1993/MPSI93' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1994 : pd.read_fwf('%s/mapp/1994/MPSI94' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel(),
        1995 : pd.read_fwf('%s/mapp/1995/MPSI95' % (fulldir), widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
    }
}

for k in mapp.keys():
    print k
    s = pd.DataFrame(pd.concat([pd.Series(mapp[k][i], index=pd.date_range(start=datetime.date(i, 1, 1), freq='h', periods=len(mapp[k][i]))) for i in mapp[k].keys()]).sort_index(), columns=['load'])
    s.to_csv('./mapp/%s.csv' % k)
