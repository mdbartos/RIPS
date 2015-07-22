import numpy as np
import pandas as pd
import os

homedir = os.path.expanduser('~')
datadir = 'github/RIPS_kircheis/data/eia_form_714/processed/'
fulldir = homedir + '/' + datadir

###### NPCC

# BECO

beco = {
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
}

# BHE

bhe = {
        1993 : pd.read_csv('./1993/BHE93', sep=' ', skiprows=2, skipinitialspace=True).loc[:, '0000':].values.ravel(),
        1994 : pd.read_csv('./1994/BHE94').dropna(how='all').loc[:729, '1/13':'12/24'].values.ravel(),
        1995 : pd.read_fwf('./1995/BHE95').loc[:729, '1/13':'1224'].values.ravel(),
        2001 : pd.read_excel('./2001/BHE01', skiprows=2).iloc[:, 1:24].values.ravel(),
        2003 : pd.read_excel('./2003/BHE03', skiprows=3).iloc[:, 1:24].values.ravel()
}

# CELC

celc = {
        1999 : pd.read_csv('./1999/CELC99', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
        2000 : pd.read_csv('./2000/CELC00', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
        2001 : pd.read_csv('./2001/CELC01', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
        2002 : pd.read_csv('./2002/CELC02', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
        2003 : pd.read_csv('./2003/CELC03', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values,
        2004 : pd.read_csv('./2004/CELC04', skiprows=3, sep=' ', skipinitialspace=True, header=None)[4].values
}

# CHGE

chge = {
        1993 : pd.read_csv('./1993/CHGE93', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)[2].values,
        1994 : pd.read_fwf('./1994/CHGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/CHGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/CHGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_csv('./1997/CHGE97', sep ='\s', skipinitialspace=True,  header=None, skipfooter=1).iloc[:, 4:].values.ravel(),
        1998 : pd.read_excel('./1998/CHGE98', skipfooter=1, header=None).iloc[:, 2:].values.ravel(),
}

# CMP

cmp = {
        1993 : pd.read_fwf('./1993/CMP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/CMP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/CMP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/CMP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/CMP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/CMP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        2002 : pd.read_fwf('./2002/CMP02', header=None).iloc[:, 1:].values.ravel(),
        2003 : pd.read_fwf('./2003/CMP03', header=None).iloc[:, 1:].values.ravel()
}

# COED

coed = {
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
}

coed[1995] = pd.concat([coed[1995][2].dropna(), coed[1995][6]]).values.ravel()

# COEL

coel = {
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
}

# CVPS

# 1994 Can't read
cvps = {
1995 : pd.read_fwf('./1995/CVPS95', header=None).iloc[:, 1:].values.ravel(),
1996 : pd.read_csv('./1996/CVPS96', header=None, skipfooter=1)[1].values,
1997 : pd.read_csv('./1997/CVPS97', header=None)[2].values,
1998 : pd.read_csv('./1998/CVPS98', header=None, skipfooter=1)[4].values,
1999 : pd.read_csv('./1999/CVPS99')['Load'].values
}

# EUA

eua = {
        1993 : pd.read_fwf('./1993/EUA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1994 : pd.read_fwf('./1994/EUA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/EUA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/EUA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/EUA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1999 : pd.read_fwf('./1999/EUA99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
}

# GMP

gmp = {
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
}

# 2001 : # 2001 WEIRD FORMAT,


# ISONY

isony = {
2002 : pd.read_csv('./2002/ISONY02', sep='\t')['mw'].values,
2003 : pd.read_excel('./2003/ISONY03')['Load'].values,
2004 : pd.read_excel('./2004/ISONY04').loc[:, 'HR1':].values.ravel()
}

# LILC

lilc = {
        1994 : pd.read_fwf('./1994/LILC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/LILC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/LILC97', skiprows=4, widths=[8,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
}

# 1996 : pd.read_fwf('./1996/LILC96', header=None, skipfooter=1)[4].str.split('\t').apply(pd.Series),


# MMWE

mmwe = {
1998 : pd.read_fwf('./1998/MMWE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
1999 : pd.read_fwf('./1999/MMWE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
2000 : pd.read_fwf('./2000/MMWE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
2001 : pd.read_fwf('./2001/MMWE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
2002 : pd.read_fwf('./2002/MMWE02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
2003 : pd.read_fwf('./2003/MMWE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel(),
2004 : pd.read_fwf('./2004/MMWE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel()
}

# NEES

nees = {
1993 : pd.read_fwf('./1993/NEES93', widths=(8,7), header=None, skipfooter=1)[1].values,
1994 : pd.read_csv('./1994/NEES94', header=None, skipfooter=1, sep=' ', skipinitialspace=True)[3].values
}
# 1995 can't read

# NEPOOL

nepool = {
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
}

# NMPC

nmpc = {
        1993 : pd.read_csv('./1993/NMPC93', skiprows=11, header=None, sep=' ', skipinitialspace=True).iloc[:, 3:27].values.ravel(), 
        1995 : pd.read_fwf('./1995/NMPC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/NMPC96', header=None).iloc[:, 2:14].astype(int).values.ravel(),
        1998 : pd.read_fwf('./1998/NMPC98', header=None).iloc[:, 2:].astype(int).values.ravel(),
        1999 : pd.read_fwf('./1999/NMPC99', header=None).iloc[:, 2:14].astype(int).values.ravel(),
        2000 : pd.read_excel('./2000/NMPC00', sheetname=1, skiprows=10, skipfooter=3).iloc[:, 1:].values.ravel(),
        2002 : pd.read_excel('./2002/NMPC02', sheetname=1, skiprows=2, header=None).iloc[:, 2:].values.ravel(),
        2003 : pd.concat([pd.read_excel('./2003/NMPC03', sheetname=i, skiprows=1, header=None) for i in range(1,13)]).iloc[:, 2:].values.ravel()
}

#1994 : # 1994 WEIRD FORMAT,
#1997 : # 1997 WEIRD FORMAT,

# NU

nu = {
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
}

#2001, 2001, 2003 has extra hour

# NYPA

nypa = {
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
}

# NYPP

nypp = {
        1993 : pd.read_fwf('./1993/NYPP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
}
# A lot more than one file should have ^^

# 1996 WEIRD FORMAT

# NYS

nys = {
        1996 : pd.read_fwf('./1996/NYS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1997 : pd.read_fwf('./1997/NYS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1999 : pd.read_excel('./1999/NYS99').iloc[:, 1:].values.ravel(),
        2000 : pd.read_csv('./2000/NYS00', sep='\t').iloc[:, -1].values,
        2001 : pd.read_csv('./2001/NYS01', sep='\t', skiprows=3).dropna(how='all').iloc[:, -1].values,
        2002 : pd.read_csv('./2002/NYS02', sep='\t', skiprows=3).iloc[:, -1].values,
        2003 : pd.read_csv('./2003/NYS03', sep=' ', skipinitialspace=True, skiprows=5, header=None).iloc[:, -1].values,
        2004 : pd.read_csv('./2004/NYS04', sep=' ', skipinitialspace=True, skiprows=5, header=None).dropna(how='all').iloc[:, -1].values
}

        # 1993 : pd.read_fwf('./1993/NYS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1, skipfooter=1).iloc[:, 1:].values.ravel(),
        # 1994 : pd.read_fwf('./1994/NYS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1, skipfooter=1).iloc[:, 1:].values.ravel(),


# OR

o_r = {
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
}

# RGE

rge = {
        1994 : pd.read_fwf('./1994/RGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1995 : pd.read_fwf('./1995/RGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        1996 : pd.read_fwf('./1996/RGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel(),
        2002 : pd.read_csv('./2002/RGE02', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values,
        2003 : pd.read_csv('./2003/RGE03', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values,
        2004 : pd.read_csv('./2004/RGE04', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all').iloc[:, -1].values
}

# UI

ui = {
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

###### ERCOT

# AUST

pd.read_fwf('./1993/AUST93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/AUST94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/AUST95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/AUST96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/AUST97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['AENX'].loc[2:].astype(float)/1000).values
(pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['AENX'].astype(float)/1000).values
(pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[3].str.replace(',', '').astype(float)/1000).values


# CPL


pd.read_fwf('./1993/CPL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/CPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/CPL96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/CPL97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['CPLC'].loc[2:].astype(int)/1000).values

# HLP

pd.read_fwf('./1993/HLP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/HLP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/HLP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/HLP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/HLP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['HLPC'].loc[2:].astype(int)/1000).values

# LCRA

pd.read_fwf('./1993/LCRA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_csv('./1994/LCRA94', skiprows=4).iloc[:, -1].values
pd.read_fwf('./1995/LCRA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/LCRA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/LCR97', header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['LCRA'].loc[2:].astype(int)/1000).values
(pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['LCRA'].astype(float)/1000).values
(pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[6].str.replace(',', '').astype(float)/1000).values

# NTEC

pd.read_csv('./1993/NTEC93', sep=' ', skipinitialspace=True, header=None)[1].values
pd.read_fwf('./1994/NTEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/NTEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/NTEC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/NTEC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./2001/NTEC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()

# PUB

pd.read_fwf('./1993/PUB93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/PUB94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/PUB95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/PUB96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/PUB97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['PUBX'].loc[2:].astype(int)/1000).values
(pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['PUBX'].astype(float)/1000).values
(pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[7].str.replace(',', '').astype(float)/1000).values


# SRGT

pd.read_csv('./1993/SRGT93', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values
pd.read_fwf('./1994/SRGT94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/SRGT95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/SRGT96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/SRGT97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()

# STEC

pd.read_fwf('./1993/STEC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()

(pd.read_excel('./1998/FERC714.xls', skiprows=3)['STEC'].loc[2:].astype(int)/1000).values
(pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['STEC'].astype(float)/1000).values
(pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[9].str.replace(',', '').astype(float)/1000).values

# TUEC

pd.read_fwf('./1993/TUEC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/TUEC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/TUEC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/TUE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/TUE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['TUEC'].loc[2:].astype(int)/1000).values
#(pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['TUET'].astype(float)/1000).values
#(pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[12].str.replace(',', '').astype(float)/1000).values
# TUET contains TUEC

# TMPP

pd.read_fwf('./1993/TMPP93', skiprows=6, header=None).dropna(how='all')
pd.read_fwf('./1995/TMPP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/TMPP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1999/ERCOT99HRLD060800.xls', skiprows=14)['TMPP'].astype(float)/1000).values
(pd.read_csv('./2000/ERCOT00HRLD.txt', skiprows=18, header=None, skipinitialspace=True, sep='\t')[10].str.replace(',', '').astype(float)/1000).values

# TXLA

pd.read_csv('./1993/TEXLA93', sep=' ', skipinitialspace=True, header=None).iloc[:, -1].values
pd.read_fwf('./1995/TXLA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/TXLA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/TXLA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['TXLA'].loc[2:].astype(int)/1000).values

# WTU

pd.read_fwf('./1993/WTU93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:]
pd.read_fwf('./1994/WTU94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/WTU96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/WTU97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
(pd.read_excel('./1998/FERC714.xls', skiprows=3)['WTUC'].loc[2:].astype(int)/1000).values

wtu[1993][2] = wtu[1993][2].str[-3:]


###### FRCC

# GAIN


pd.read_fwf('./1993/GAIN93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_csv('./1994/GAIN94', header=None, sep=' ', skipinitialspace=True, skipfooter=2, skiprows=5).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/GAIN95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_csv('./1996/GAIN96', sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/GAIN97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_csv('./1998/GAIN98', sep=' ', skipinitialspace=True, skiprows=3, header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1999/GAIN99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./2000/GAIN00', header=None).iloc[:, 4:].values.ravel()
pd.read_excel('./2002/GAIN02', sheetname=1, skiprows=3, header=None).iloc[:730, 8:20].values.ravel()
pd.read_excel('./2003/GAIN03', sheetname=2, skiprows=3, header=None).iloc[:730, 8:20].values.ravel()
pd.read_excel('./2004/GAIN04', sheetname=0, header=None).iloc[:, 8:].values.ravel()

# LAKE


pd.read_fwf('./1993/LAKE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/LAKE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/LAKE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/LAKE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/LAKE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1998/LAKE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1999/LAKE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./2000/LAKE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./2001/LAKE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./2002/LAKE02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()

# TAL
# EXTREMELY ODD FORMAT

# FMPA

pd.read_fwf('./1993/FMPA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/FMPA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/FMPA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/FMPA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/FMPA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel()
pd.read_fwf('./1998/FMPA98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=5).iloc[:, 1:].values.ravel()
pd.read_fwf('./1999/FMPA99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=6).iloc[:, 1:].values.ravel()
pd.read_csv('./2001/FMPA01', header=None, sep=' ', skipinitialspace=True, skiprows=6).iloc[:, 2:-1].values.ravel()
pd.read_csv('./2002/FMPA02', header=None, sep='\t', skipinitialspace=True, skiprows=7).iloc[:, 1:].values.ravel()
pd.read_csv('./2003/FMPA03', header=None, sep='\t', skipinitialspace=True, skiprows=7).iloc[:, 1:].values.ravel()
pd.read_csv('./2004/FMPA04', header=None, sep=' ', skipinitialspace=True, skiprows=6, skipfooter=1).iloc[:, 1:].values.ravel()

# FPC

pd.read_csv('./1993/FPC93', sep=' ', skipinitialspace=True, header=None)[1].values
pd.read_csv('./1994/FPC94', sep=' ', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel()
pd.read_csv('./1995/FPC95', engine='python', header=None).values
pd.read_excel('./1996/FPC96', header=None, skiprows=2, skipfooter=1).iloc[:, 6:].values.ravel()
#1997 weird format
pd.read_excel('./1998/FPC98', header=None, skiprows=5).iloc[:, 7:].values.ravel()
pd.read_excel('./1999/FPC99', header=None, skiprows=4).iloc[:, 7:].values.ravel()
pd.read_excel('./2000/FPC00', header=None, skiprows=4).iloc[:, 7:].values.ravel()
pd.read_excel('./2001/FPC01', header=None, skiprows=5).iloc[:, 7:].values.ravel()
pd.read_excel('./2002/FPC02', header=None, skiprows=4).iloc[:, 7:].values.ravel()
pd.read_excel('./2004/FPC04', header=None, skiprows=4).iloc[:, 7:].values.ravel()

# FPL

pd.DataFrame([i.split('\t') for i in open('./1993/FPL93', 'r').readlines()]).iloc[:365, :24].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./1994/FPL94', 'r').readlines()]).iloc[3:, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./1995/FPL95', 'r').readlines()[3:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./1996/FPL96', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./1997/FPL97', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./1998/FPL98', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./1999/FPL99', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./2000/FPL00', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./2001/FPL01', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./2002/FPL02', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./2003/FPL03', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()
pd.DataFrame([i.split('\t') for i in open('./2004/FPL04', 'r').readlines()[4:]]).iloc[:730, 1:13].apply(lambda x: x.str.replace('\r\n', '').str.replace('"', '').str.replace(',', '')).replace('', np.nan).astype(float).values.ravel()

# JEA

pd.read_csv('./1993/JEA93', sep=' ', skipinitialspace=True, header=None)[2].values
pd.read_csv('./1994/JEA94', sep=' ', skipinitialspace=True, header=None)[2].values
pd.read_fwf('./1996/JEA96', header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/JEA97', header=None).iloc[:, 1:].values.ravel()
pd.read_csv('./1998/JEA98', sep='\t', header=None)[2].values
pd.read_csv('./1999/JEA99', sep='\t', header=None)[2].values
pd.read_excel('./2000/JEA00', header=None)[2].values
pd.read_excel('./2001/JEA01', header=None, skiprows=2)[2].values
pd.read_excel('./2002/JEA02', header=None, skiprows=1)[2].values
pd.read_excel('./2003/JEA03', header=None, skiprows=1)[2].values
pd.read_excel('./2004/JEA04', header=None, skiprows=1)[2].values

# KUA

pd.read_csv('./1994/KUA94', sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel()
pd.read_csv('./1995/KUA95', sep=' ', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel()
#1996 multiple excel sheets
pd.read_csv('./1997/KUA97', sep='\t', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel()
#1998 weird formatting
#pd.read_csv('./1998/KUA98', sep='\s', skipinitialspace=True, header=None).iloc[:, 1:].values.ravel()
#pd.read_csv('./2000/KUA00', sep='\t', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel()
pd.read_csv('./2001/KUA01', skiprows=1, header=None, sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel()
pd.read_csv('./2002/KUA02', skipfooter=1, header=None, sep=' ', skipinitialspace=True).iloc[:, 1:].values.ravel() # Only goes to september

# OUC


pd.read_fwf('./1993/OUC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/OUC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/OUC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1996/OUC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1997/OUC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1998/OUC98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1999/OUC99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./2000/OUC00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()
pd.read_fwf('./2001/OUC01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2).iloc[:, 1:].values.ravel()
pd.read_fwf('./2002/OUC02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, 1:].values.ravel()

# TECO


pd.read_fwf('./1993/TECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/TECO94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1).iloc[:, 1:].values.ravel()

pd.read_csv('./1998/TECO98', engine='python', skiprows=3, header=None)[0].values
pd.read_csv('./1999/TECO99', engine='python', skiprows=3, header=None)[0].values
pd.read_csv('./2000/TECO00', engine='python', skiprows=3, header=None)[0].str[:4].astype(int).values
pd.read_csv('./2001/TECO01', skiprows=3, header=None)[0].values
pd.read_csv('./2002/TECO02', sep='\t').loc[:, 'HR1':].values.ravel()
pd.read_csv('./2003/TECO03', skiprows=2, header=None, sep=' ', skipinitialspace=True).iloc[:, 2:].values.ravel()

###### ECAR

li = []

for d1 in os.listdir('.'):
    for fn in os.listdir('./%s' % d1):
        li.append(fn)

ecar_u = pd.Series(li).str[:-2].order().unique()


# AEP

aep = {
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
}

# APS


aps = {
1993 : pd.read_fwf('./1993/APS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/APS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/APS95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# AMPO

ampo = {
2001 : pd.read_fwf('./2001/AMPO01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2002 : pd.read_csv('./2002/AMPO02', header=None)[1].values,
2003 : pd.read_fwf('./2003/AMPO03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2004 : pd.read_fwf('./2004/AMPO04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# BREC

brec = {
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
}

# BPI


bpi = {
1994 : pd.read_fwf('./1994/BPI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1999 : pd.read_fwf('./1999/BPI99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2000 : pd.read_fwf('./2000/BPI00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2001 : pd.read_fwf('./2001/BPI01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2002 : pd.read_csv('./2002/BPI02', header=None)[1].values,
2003 : pd.read_fwf('./2003/BPI03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2004 : pd.read_fwf('./2004/BPI04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# CEI

cei = {
1993 : pd.read_fwf('./1993/CEI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/CEI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/CEI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1996 : pd.read_fwf('./1996/CEI96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# CGE


cge = {
1993 : pd.read_fwf('./1993/CEI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/CEI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/CEI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# CP


cp = {
1993 : pd.read_fwf('./1993/CP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/CP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/CP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1996 : pd.read_fwf('./1996/CP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# DPL


dpl = {
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
}

# DECO


deco = {
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
}

# DLCO


dlco = {
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
}

# EKPC


ekpc = {
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
}

# HEC


hec = {
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
}

# IPL


ipl = {
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
}

# KUC


kuc = {
1993 : pd.read_fwf('./1993/KUC93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/KUC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/KUC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1996 : pd.read_fwf('./1996/KUC96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1997 : pd.read_fwf('./1997/KUC97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# LGE


lge = {
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
}

# NIPS

nips = {
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
}

# OE


oe = {
1993 : pd.read_fwf('./1993/OES93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/OES94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/OES95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1996 : pd.read_fwf('./1996/OES96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# OVEC


ovec = {
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
}

# PSI


psi = {
1993 : pd.read_fwf('./1993/PSI93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/PSI94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/PSI95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# SIGE


sige = {
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
}

# TE


te = {
1993 : pd.read_fwf('./1993/TECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1994 : pd.read_fwf('./1994/TECO94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1995 : pd.read_fwf('./1995/TECO95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1996 : pd.read_fwf('./1996/TECO96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# WVPA


wvpa = {
1994 : pd.read_fwf('./1994/WVPA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2003 : pd.read_fwf('./2003/WVPA03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2004 : pd.read_fwf('./2004/WVPA04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# CINRGY


cin = {
1996 : pd.read_fwf('./1996/CIN96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1997 : pd.read_fwf('./1997/CIN97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1998 : pd.read_fwf('./1998/CIN98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1999 : pd.read_fwf('./1999/CIN99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2000 : pd.read_fwf('./2000/CIN00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2001 : pd.read_fwf('./2001/CIN01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2002 : pd.read_csv('./2002/CIN02', header=None)[1].values,
2003 : pd.read_fwf('./2003/CIN03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2004 : pd.read_fwf('./2004/CIN04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# FE


fe = {
1997 : pd.read_fwf('./1997/FE97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1998 : pd.read_fwf('./1998/FE98', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1999 : pd.read_fwf('./1999/FE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2000 : pd.read_fwf('./2000/FE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2001 : pd.read_fwf('./2001/FE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2002 : pd.read_csv('./2002/FE02', header=None)[1].values,
2003 : pd.read_fwf('./2003/FE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2004 : pd.read_fwf('./2004/FE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}

# MCCP


mccp = {
1993 : pd.read_fwf('./1993/MCCP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1996 : pd.read_fwf('./1996/MCCP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
1997 : pd.read_fwf('./1997/MCCP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2000 : pd.read_fwf('./2000/MCCP00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2001 : pd.read_fwf('./2001/MCCP01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2002 : pd.read_csv('./2002/MCCP02', header=None)[1].values,
2003 : pd.read_fwf('./2003/MCCP03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel(),
2004 : pd.read_fwf('./2004/MCCP04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
}


###### MAIN


li = []

for d1 in os.listdir('.'):
    for fn in os.listdir('./%s' % d1):
        li.append(fn)

main_u = pd.Series(li).str[:-2].order().unique()

# CECO

pd.read_fwf('./1993/CECO93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2, skipfooter=1).iloc[:, 1:].values.ravel()
# 1994 WEIRD FORMAT
pd.read_csv('./1995/CECO95', skiprows=3, header=None)[0].values
pd.read_csv('./1996/CECO96', skiprows=4, header=None)[1].values
pd.read_csv('./1997/CECO97', sep=' ', skipinitialspace=True, skiprows=4, header=None)[3].values
pd.read_csv('./1998/CECO98', sep='\s', skipinitialspace=True, skiprows=5, header=None)[5].values
pd.read_csv('./1999/CECO99', sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values
pd.read_csv('./2000/CECO00', sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values
pd.read_csv('./2001/CECO01', sep='\t', skipinitialspace=True, skiprows=5, header=None)[1].values
pd.read_csv('./2002/CECO02', sep=' ', skipinitialspace=True, skiprows=5, header=None)[2].values

# CILC

pd.read_fwf('./1993/CILC93', header=None).iloc[:, 2:].values.ravel()
pd.read_fwf('./1994/CILC94', header=None).iloc[:, 2:].values.ravel()
pd.read_fwf('./1995/CILC95', header=None).iloc[:, 2:].values.ravel()
pd.read_fwf('./1996/CILC96', header=None).iloc[:, 2:].values.ravel()
pd.read_fwf('./1997/CILC97', header=None).iloc[:, 2:].values.ravel()
pd.read_fwf('./1998/CILC98', header=None).iloc[:, 2:].values.ravel()
pd.read_fwf('./1999/CILC99', header=None).iloc[:, 2:].values.ravel()
pd.read_excel('./2000/CILC00', skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel()
pd.read_excel('./2001/CILC01', skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel()
pd.read_excel('./2002/CILC02', skiprows=4).loc[:, 'Hour 1':'Hour 24'].values.ravel()
pd.read_csv('./2003/CILC03', skiprows=1, sep='\t').iloc[:, -1].values


# CIPS

pd.read_fwf('./1993/CIPS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1994/CIPS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1).iloc[:, 1:].values.ravel()
pd.read_fwf('./1995/CIPS95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
pd.read_fwf('./1996/CIPS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
pd.read_fwf('./1997/CIPS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()


# IPC
pd.read_csv('./1993/IPC93', skipfooter=1, header=None)[2].values
pd.read_csv('./1994/IPC94', skipfooter=1, header=None)[2].values
pd.read_csv('./1995/IPC95', skipfooter=1, header=None)[4].astype(str).str.replace('.', '0').astype(float).values
pd.read_csv('./1996/IPC96').iloc[:, -1].values
pd.read_csv('./1997/IPC97').iloc[:, -1].values
pd.read_excel('./1998/IPC98').iloc[:, -1].values
pd.read_csv('./1999/IPC99', skiprows=2, header=None)[1].values
pd.read_excel('./2000/IPC00', skiprows=1).iloc[:, -1].values
pd.read_excel('./2001/IPC01', skiprows=1).iloc[:, -1].values
pd.read_excel('./2002/IPC02', skiprows=4).iloc[:, -1].values
pd.read_excel('./2003/IPC03', skiprows=1).iloc[:, -1].values
pd.read_excel('./2004/IPC04', skiprows=1).iloc[:, -1].values

# MGE

pd.read_fwf('./1993/MGE93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=4).iloc[:, 1:].dropna().astype(float).values.ravel()
# 1994 WEIRD FORMAT
pd.read_csv('./1995/MGE95', sep=' ', skipinitialspace=True, header=None)[2].values
# 1996 WEIRD FORMAT
pd.read_csv('./1997/MGE97', sep=' ', skipinitialspace=True, skiprows=12, header=None).iloc[:-1, 2].astype(float).values
pd.read_csv('./1998/MGE98', sep=' ', skipinitialspace=True).iloc[:-1]['LOAD'].astype(float).values
pd.read_csv('./1999/MGE99', sep=' ', skiprows=2, header=None, skipinitialspace=True).iloc[:-2, 2].astype(float).values
pd.read_csv('./2000/MGE00', sep=' ', skiprows=2, header=None, skipinitialspace=True).iloc[:-2, 2].astype(float).values
pd.read_fwf('./2000/MGE00', skiprows=2)['VMS_DATE'].iloc[:-2].str.split().str[-1].astype(float).values
pd.read_fwf('./2001/MGE01', skiprows=1, header=None).iloc[:-2, 2].values
pd.read_fwf('./2002/MGE02', skiprows=4, header=None).iloc[:-1, 0].str.split().str[-1].astype(float).values
#2003 and 2004 can save for later


# SIPC

pd.read_csv('./1994/SIPC94', engine='python', skipfooter=1, header=None)[0].values
pd.read_csv('./1996/SIPC96', engine='python', header=None)[0].values
pd.read_csv('./1997/SIPC97', engine='python', header=None)[0].values
pd.read_csv('./1998/SIPC98', engine='python', header=None)[0].values
pd.read_csv('./1999/SIPC99', engine='python', header=None)[0].replace('no data', '0').astype(float).values
pd.read_csv('./2000/SIPC00', engine='python', header=None)[0].astype(str).str[:3].astype(float).values
pd.read_csv('./2001/SIPC01', engine='python', header=None)[0].str.strip().str[:3].astype(float).values
pd.read_csv('./2002/SIPC02', sep='\t', skiprows=3, header=None)[1].values
pd.read_csv('./2003/SIPC03', engine='python', header=None)[0].str.strip().str[:3].astype(float).values
pd.read_csv('./2004/SIPC04', engine='python', header=None)[0].str.strip().str[:3].astype(float).values

# SPIL

pd.read_csv('./1993/SPIL93', sep=' ', skipinitialspace=True, skiprows=4, header=None).iloc[:, 3:].values.ravel()
pd.read_csv('./1994/SPIL94', sep=' ', skipinitialspace=True, skiprows=6, header=None).iloc[:, 3:].values.ravel()
pd.read_csv('./1995/SPIL95', sep=' ', skipinitialspace=True, skiprows=7, header=None).iloc[:, 3:].values.ravel()
pd.read_csv('./1996/SPIL96', sep=' ', skipinitialspace=True, skiprows=5, header=None).iloc[:366, 3:].astype(float).values.ravel()
pd.read_csv('./1997/SPIL97', sep=' ', skipinitialspace=True, skiprows=7, header=None).iloc[:, 3:].values.ravel()
pd.read_csv('./1998/SPIL98', sep='\t', skipinitialspace=True, skiprows=8, header=None).iloc[:, 4:].values.ravel()
pd.read_csv('./1999/SPIL99', skiprows=4, header=None)[0].values
pd.read_csv('./2000/SPIL00', skiprows=4, header=None)[0].values
pd.read_csv('./2001/SPIL01', sep='\t', skipinitialspace=True, skiprows=7, header=None).iloc[:, 5:-1].values.ravel()
pd.read_excel('./2002/SPIL02', sheetname=2, skiprows=5).iloc[:, 3:].values.ravel()
pd.read_excel('./2003/SPIL03', sheetname=2, skiprows=5).iloc[:, 3:].values.ravel()
pd.read_excel('./2004/SPIL04', sheetname=0, skiprows=5).iloc[:, 3:].values.ravel()

# UE

# Bizarre formatting for 93 and 94
pd.read_fwf('./1995/UE95', header=None)[2].values
pd.read_fwf('./1996/UE96', header=None)[2].values
pd.read_fwf('./1997/UE97', header=None)[2].values

# WEPC

pd.read_csv('./1993/WEPC93', engine='python', skipfooter=1, header=None)[0].values
pd.read_csv('./1994/WEPC94', engine='python', skipfooter=1, header=None)[0].values
pd.read_csv('./1995/WEPC95', engine='python', skipfooter=1, header=None)[0].values
pd.read_csv('./1996/WEPC96', engine='python', header=None)[0].values
pd.read_excel('./1997/WEPC97', header=None)[0].astype(str).str.strip().replace('NA', '0').astype(float).values
pd.read_csv('./1998/WEPC98', engine='python', header=None)[0].str.strip().replace('NA', 0).astype(float).values
pd.read_excel('./1999/WEPC99', header=None).iloc[:, 1:].values.ravel()
pd.read_excel('./2000/WEPC00', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
pd.read_excel('./2001/WEPC01', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
pd.read_excel('./2002/WEPC02', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
pd.read_excel('./2003/WEPC03', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()
pd.read_excel('./2004/WEPC04', header=None).iloc[:, 1:].replace('.', '0').astype(float).values.ravel()

# WPL


pd.read_fwf('./1993/WPL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
pd.read_fwf('./1994/WPL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5], header=None).iloc[:, range(1,13)+range(14,26)].values.ravel()
pd.read_fwf('./1995/WPL95', header=None).iloc[:, 1:].values.ravel()
pd.read_csv('./1996/WPL96', header=None, sep='\t').iloc[:, 1:].values.ravel()
pd.read_csv('./1997/WPL97', sep=' ', skipinitialspace=True, skiprows=1, header=None)[2].str.replace(',', '').astype(float).values

# WPS

pd.read_csv('./1993/WPS93', sep=' ', header=None, skipinitialspace=True, skipfooter=1).values.ravel()
(pd.read_csv('./1994/WPS94', sep=' ', header=None, skipinitialspace=True, skipfooter=1).iloc[:, 1:-1]/100).values.ravel()
pd.read_csv('./1995/WPS95', sep=' ', skipinitialspace=True, skiprows=8, header=None, skipfooter=7)[2].values
pd.read_csv('./1996/WPS96', sep='\t', skiprows=2).loc[:365, '100':'2400'].astype(float).values.ravel()
pd.read_csv('./1997/WPS97', sep='\s', header=None, skipfooter=1)[2].values
pd.read_csv('./1998/WPS98', sep='\s', header=None)[2].values
pd.read_excel('./1999/WPS99', skiprows=8, skipfooter=8, header=None)[1].values
pd.read_excel('./2000/WPS00', sheetname=1, skiprows=5, skipfooter=8, header=None)[2].values
pd.read_excel('./2001/WPS01', sheetname=0, skiprows=5, header=None)[2].values
pd.read_csv('./2002/WPS02', sep='\s', header=None, skiprows=5)[2].values
pd.read_excel('./2003/WPS03', sheetname=1, skiprows=6, header=None)[2].values

# UPP
pd.read_csv('./1996/UPP96', header=None, skipfooter=1).iloc[:, -1].values
pd.read_excel('./2004/UPP04').iloc[:, -1].values

# WPPI

pd.read_csv('./1997/WPPI97', skiprows=5, sep=' ', skipinitialspace=True, header=None).iloc[:, 1:-1].values.ravel()
pd.DataFrame([i.split() for i in open('./1999/WPPI99').readlines()[5:]]).iloc[:, 1:-1].astype(float).values.ravel()
pd.DataFrame([i.split() for i in open('./2000/WPPI00').readlines()[5:]]).iloc[:, 1:-1].astype(float).values.ravel()
pd.read_excel('./2001/WPPI01', sheetname=1, skiprows=4).iloc[:, 1:-1].values.ravel()
pd.read_excel('./2002/WPPI02', sheetname=1, skiprows=4).iloc[:, 1:-1].values.ravel()

# AMER

pd.read_csv('./1998/AMER98', sep='\t').iloc[:, -1].str.strip().replace('na', 0).astype(float).values
pd.read_csv('./1999/AMER99', sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values
pd.read_csv('./2000/AMER00', sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values
pd.read_csv('./2001/AMER01', sep='\t').iloc[:, -1].astype(str).str.strip().replace('n/a', 0).astype(float).values
pd.read_csv('./2002/AMER02', sep='\t').iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values
pd.read_csv('./2003/AMER03', sep='\t', skiprows=1).iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values
pd.read_csv('./2004/AMER04', sep='\t', skiprows=1).iloc[:, -1].astype(str).str.strip().replace('na', 0).astype(float).values

# CWL


pd.read_excel('./2001/CWL01', skiprows=1).iloc[:, 0].values
pd.read_excel('./2002/CWL02', header=None).iloc[:, 0].values
pd.read_excel('./2003/CWL03', header=None).iloc[:, 0].values

# EEI
# Bizarre formatting until 1998


###### MAAC

# ALL UTILS

maac93 = pd.read_fwf('./1993/PJM93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
maac94 = pd.read_fwf('./1994/PJM94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
maac95 = pd.read_csv('./1995/PJM95', sep='\t', header=None, skipfooter=1)
maac96 = pd.read_csv('./1996/PJM96', sep='\t', header=None, skipfooter=1)

# AE

maac93[maac93[0].str.contains('AE')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('AE')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('AE')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('AE')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='ACE_LOAD').iloc[:, 1:25].values.ravel()

# BC

maac93[maac93[0].str.contains('BC')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('BC')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('BC')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('BC')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='BC_LOAD').iloc[:, 1:25].values.ravel()

# DPL

maac93[maac93[0].str.contains('DP')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('DP')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('DP')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('DP')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='DPL_LOAD').iloc[:366, 1:25].values.ravel()

# PU

maac93[maac93[0].str.contains('PU')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('PU')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('PU')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('PU')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='GPU_LOAD').iloc[:366, 1:25].values.ravel()

# PN

pd.read_excel('./1997/PJM97', sheetname='PN_LOAD').iloc[:366, 1:25].values.ravel()

# PE

maac93[maac93[0].str.contains('PE$')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('PE$')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('PE$')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('PE$')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='PE_Load').iloc[:366, 1:25].values.ravel()

# PEP

maac93[maac93[0].str.contains('PEP')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('PEP')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('PEP')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('PEP')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='PEP_LOAD').iloc[:366, 1:25].values.ravel()

# PS

maac93[maac93[0].str.contains('PS')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('PS')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('PS')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('PS')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='PS_Load').iloc[:366, 1:25].values.ravel()

# PJM

maac93[maac93[0].str.contains('PJM')].iloc[:, 1:].values.ravel()
maac94[maac94[0].str.contains('PJM')].iloc[:, 1:].values.ravel()
maac95[maac95[1].str.contains('PJM')].iloc[:, 2:].values.ravel()
maac96[maac96[1].str.contains('PJM')].iloc[:, 2:].values.ravel()
pd.read_excel('./1997/PJM97', sheetname='PJM_LOAD').iloc[:366, 1:25].values.ravel()
pd.read_csv('./1998/PJM98', sep=' ', skipinitialspace=True, header=None).iloc[:, 2:].values.ravel()
pd.read_excel('./1999/PJM99', header=None)[2].values
pd.read_excel('./2000/PJM00', header=None)[2].values

