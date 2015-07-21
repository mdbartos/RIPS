import numpy as np
import pandas as pd
import os

homedir = os.path.expanduser('~')
datadir = 'github/RIPS_kircheis/data/eia_form_714/processed/'
fulldir = homedir + '/' + datadir

###### NPCC

# BECO
pd.read_fwf('./1993/BECO93', header=None)
pd.read_csv('./1994/BECO94', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)
pd.read_csv('./1995/BECO95', sep =' ', skipinitialspace=True,  header=None)
pd.read_csv('./1996/BECO96', sep =' ', skipinitialspace=True,  header=None)
pd.read_csv('./1997/BECO97', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)
pd.read_csv('./1998/BECO98', sep =' ', skipinitialspace=True,  header=None)
pd.read_csv('./1999/BECO99', sep =' ', skipinitialspace=True,  header=None, skiprows=3)
pd.read_csv('./2000/BECO00', sep =' ', skipinitialspace=True,  header=None, skiprows=3)
pd.read_csv('./2001/BECO01', sep =' ', skipinitialspace=True,  header=None, skiprows=3)
pd.read_csv('./2002/BECO02', sep =' ', skipinitialspace=True,  header=None, skiprows=3)
pd.read_csv('./2003/BECO03', sep =' ', skipinitialspace=True,  header=None, skiprows=3)
pd.read_csv('./2004/BECO04', sep =' ', skipinitialspace=True,  header=None, skiprows=3)

# BHE

pd.read_csv('./1993/BHE93', sep=' ', skiprows=2, skipinitialspace=True)
pd.read_csv('./1994/BHE94').dropna(how='all')
pd.read_fwf('./1995/BHE95')
pd.read_excel('./2001/BHE01', skiprows=2)
pd.read_excel('./2003/BHE03', skiprows=3)

# CELC

pd.read_csv('./1999/CELC99', skiprows=3, sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./2000/CELC00', skiprows=3, sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./2001/CELC01', skiprows=3, sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./2002/CELC02', skiprows=3, sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./2003/CELC03', skiprows=3, sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./2004/CELC04', skiprows=3, sep=' ', skipinitialspace=True, header=None)

# CHGE

pd.read_csv('./1993/CHGE93', sep =' ', skipinitialspace=True,  header=None, skipfooter=1)
pd.read_fwf('./1994/CHGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1995/CHGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_fwf('./1996/CHGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_csv('./1997/CHGE97', sep ='\s', skipinitialspace=True,  header=None, skipfooter=1)
pd.read_excel('./1998/CHGE98', skipfooter=1)

# CMP

pd.read_fwf('./1993/CMP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1994/CMP94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1995/CMP95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1996/CMP96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1997/CMP97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1999/CMP99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./2002/CMP02')
pd.read_fwf('./2003/CMP03')

# COED

pd.read_csv('./1993/COED93', skipfooter=1, skiprows=10, skipinitialspace=True)
pd.read_fwf('./1994/COED94', skipfooter=1)
pd.read_csv('./1995/COED95', skiprows=2)
pd.read_excel('./1996/COED96')
pd.read_excel('./1997/COED97', skiprows=1)
pd.read_excel('./1998/COED98', skiprows=1)
pd.read_csv('./1999/COED99', skiprows=1, sep='\t')  #String MW
pd.read_csv('./2000/COED00', sep='\t') #String MW
pd.read_csv('./2001/COED01', sep='\t', skipfooter=1) #String MW
pd.read_csv('./2002/COED02', sep='\t', skipfooter=1, skiprows=1) #String MW
pd.read_csv('./2003/COED03', sep='\t')
pd.read_csv('./2004/COED04')

# COEL

pd.read_fwf('./1993/COEL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1995/COEL95', header=None) #Day split into three parts
pd.read_csv('./1996/COEL96', sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./1997/COEL97', sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./1998/COEL98', sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./1999/COEL99', sep=' ', skipinitialspace=True, header=None, skiprows=3)
pd.read_csv('./2000/COEL00', sep=' ', skipinitialspace=True, header=None, skiprows=3)
pd.read_csv('./2001/COEL01', sep=' ', skipinitialspace=True, header=None, skiprows=3)
pd.read_csv('./2002/COEL02', sep=' ', skipinitialspace=True, header=None, skiprows=3)
pd.read_csv('./2003/COEL03', sep=' ', skipinitialspace=True, header=None, skiprows=3)
pd.read_csv('./2004/COEL04', sep=' ', skipinitialspace=True, header=None, skiprows=3)

# CVPS

# 1994 Can't read
pd.read_fwf('./1995/CVPS95', header=None)
pd.read_csv('./1996/CVPS96', header=None, skipfooter=1)
pd.read_csv('./1997/CVPS97', header=None)
pd.read_csv('./1998/CVPS98', header=None, skipfooter=1)
pd.read_csv('./1999/CVPS99', header=None)

# EUA

pd.read_fwf('./1993/EUA93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1994/EUA94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1995/EUA95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1996/EUA96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1997/EUA97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1999/EUA99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)

# GMP

pd.read_csv('./1993/GMP93', sep=' ', skipinitialspace=True, header=None, skiprows=4)
pd.read_fwf('./1994/GMP94')
pd.read_csv('./1995/GMP95', sep=' ', skipinitialspace=True, header=None)
pd.read_csv('./1996/GMP96', sep='\t', skipinitialspace=True, header=None)
pd.read_csv('./1997/GMP97', sep='\t', skipinitialspace=True, header=None)
pd.read_csv('./1998/GMP98', sep='\t', skipinitialspace=True, header=None)
pd.read_csv('./1999/GMP99', sep=' ', skipinitialspace=True, header=None, skipfooter=1)
# 2001 WEIRD FORMAT
pd.read_excel('./2002/GMP02', skiprows=6, skipfooter=1)
pd.read_excel('./2003/GMP03', skiprows=6, skipfooter=1)
pd.read_csv('./2004/GMP04', skiprows=13, sep='\s')

# ISONY

pd.read_csv('./2002/ISONY02', sep='\t')
pd.read_excel('./2003/ISONY03')
pd.read_excel('./2004/ISONY04')

# LILC

pd.read_fwf('./1994/LILC94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_fwf('./1995/LILC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
#pd.read_fwf('./1996/LILC96', header=None, skipfooter=1)[4].str.split('\t').apply(pd.Series)
pd.read_fwf('./1997/LILC97', skiprows=4)

# MMWE

pd.read_fwf('./1998/MMWE98', skiprows=1)
pd.read_fwf('./1999/MMWE99', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_fwf('./2000/MMWE00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_fwf('./2001/MMWE01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_fwf('./2002/MMWE02', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_fwf('./2003/MMWE03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_fwf('./2004/MMWE04', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)

# NEES

pd.read_fwf('./1993/NEES93', widths=(8,7), header=None, skipfooter=1)
pd.read_csv('./1994/NEES94', header=None, skipfooter=1, sep=' ', skipinitialspace=True)
# 1995 can't read

# NEPOOL

pd.read_fwf('./1993/NEPOOL93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=2)
pd.read_fwf('./1994/NEPOOL94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_fwf('./1995/NEPOOL95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=3)
pd.read_csv('./1996/NEPOOL96', sep=' ', skipinitialspace=True)
pd.read_fwf('./1997/NEPOOL97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_excel('./1998/NEPOOL98')
pd.read_csv('./1999/NEPOOL99', engine='python', skiprows=1)
pd.read_fwf('./2000/NEPOOL00', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_fwf('./2001/NEPOOL01', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_csv('./2002/NEPOOL02', sep='\t')
pd.read_fwf('./2003/NEPOOL03', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_csv('./2004/NEPOOL04', sep='\t', header=None, skiprows=10)


# NMPC

pd.read_fwf('./1993/NMPC93', skiprows=11, header=None)
# 1994 WEIRD FORMAT
pd.read_fwf('./1995/NMPC95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_fwf('./1996/NMPC96', header=None)
# 1997 WEIRD FORMAT
pd.read_fwf('./1998/NMPC98', header=None)
pd.read_fwf('./1999/NMPC99', header=None)
pd.read_excel('./2000/NMPC00', sheetname=1, skiprows=10, skipfooter=3)
pd.read_excel('./2002/NMPC02', sheetname=1, skiprows=2, header=None)
pd.concat([pd.read_excel('./2003/NMPC03', sheetname=i, skiprows=1, header=None) for i in range(1,13)])

# NU

pd.read_fwf('./1993/NU93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
pd.read_excel('./1994/NU94', header=None, skipfooter=1)
pd.read_excel('./1995/NU95', header=None, skipfooter=5)
pd.read_excel('./1996/NU96', header=None, skipfooter=1) 
pd.read_excel('./1997/NU97', header=None, skipfooter=4) 
pd.read_excel('./1998/NU98', header=None) 
pd.read_excel('./1999/NU99', header=None) 
pd.read_csv('./2000/NU00', sep='\t', header=None)
pd.read_excel('./2001/NU01') 
pd.read_excel('./2002/NU02') 
pd.read_excel('./2003/NU03') 

# NYPA

pd.read_csv('./1993/NYPA93', engine='python', header=None)
pd.read_csv('./1994/NYPA94', engine='python', header=None)
pd.read_csv('./1995/NYPA95', engine='python', header=None)
pd.read_csv('./1996/NYPA96', engine='python', header=None)
pd.read_csv('./1997/NYPA97', engine='python', header=None)
pd.read_csv('./1998/NYPA98', engine='python', header=None)
pd.read_excel('./1999/NYPA99', header=None)
pd.read_csv('./2000/NYPA00', engine='python', header=None)
pd.read_csv('./2001/NYPA01', engine='python', header=None)
pd.read_csv('./2002/NYPA02', engine='python', header=None)
pd.read_csv('./2003/NYPA03', engine='python', header=None)

# NYPP

pd.read_fwf('./1993/NYPP93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skipfooter=1)
# 1996 WEIRD FORMAT

# NYS

pd.read_fwf('./1993/NYS93', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1, skipfooter=1)
pd.read_fwf('./1994/NYS94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1, skipfooter=1)
pd.read_fwf('./1996/NYS96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_fwf('./1997/NYS97', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None, skiprows=1)
pd.read_excel('./1999/NYS99')
pd.read_csv('./2000/NYS00', sep='\t')
pd.read_csv('./2001/NYS01', sep='\t', skiprows=3).dropna(how='all')
pd.read_csv('./2002/NYS02', sep='\t', skiprows=3).dropna(how='all')
pd.read_csv('./2003/NYS03', sep=' ', skipinitialspace=True, skiprows=5, header=None).dropna(how='all')
pd.read_csv('./2004/NYS04', sep=' ', skipinitialspace=True, skiprows=5, header=None).dropna(how='all')

# OR

pd.read_csv('./1993/OR93', skiprows=5, header=None)
pd.read_csv('./1995/OR95', header=None)
pd.read_csv('./1996/OR96', header=None)
pd.read_csv('./1997/OR97', header=None)
pd.read_fwf('./1998/OR98', skiprows=1, header=None).dropna(axis=1, how='all')
pd.read_csv('./1999/OR99', sep='\t', skiprows=1, header=None)
pd.read_csv('./2000/OR00', sep='\t')
pd.read_csv('./2002/OR02', sep='\t', skiprows=2)
pd.read_csv('./2003/OR03', sep='\t')
pd.read_csv('./2004/OR04', header=None)

# RGE

pd.read_fwf('./1994/RGE94', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_fwf('./1995/RGE95', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_fwf('./1996/RGE96', widths=[20,5,5,5,5,5,5,5,5,5,5,5,5], header=None)
pd.read_csv('./2002/RGE02', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all')
pd.read_csv('./2003/RGE03', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all')
pd.read_csv('./2004/RGE04', skiprows=4, sep=' ', skipinitialspace=True).dropna(axis=1, how='all')

# UI

pd.read_fwf('./1993/UI93', header=None, skipfooter=1)
pd.read_fwf('./1994/UI94', header=None, skipfooter=1)
pd.read_fwf('./1995/UI95', header=None, skipfooter=1)
pd.read_fwf('./1996/UI96', header=None, skipfooter=1)
pd.read_fwf('./1997/UI97', header=None, skipfooter=1)
pd.read_excel('./1998/UI98')
pd.read_excel('./1999/UI99')
pd.read_excel('./2000/UI00', sheetname=1) #2000
pd.read_excel('./2001/UI01', sheetname=0) #2001
pd.read_excel('./2002/UI02', sheetname=0) #2002
pd.read_excel('./2003/UI03', sheetname=0, skipfooter=2) #2003
pd.read_excel('./2004/UI04', sheetname=0, skipfooter=1) #2004

