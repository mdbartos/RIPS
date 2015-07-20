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

