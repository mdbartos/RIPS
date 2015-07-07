import numpy as np
import pandas as pd
import os
import sys

sys.path.append('/home/akagi/github/RIPS_kircheis/RIPS')
import rect_grid
import cable

acsr = [  u'Bittern',  u'Bluebird',   u'Bluejay',  u'Bobolink',   u'Bunting',
          u'Canary',  u'Cardinal', u'Chickadee',    u'Chukar',    u'Cochin',
            u'Condor',      u'Coot',    u'Curlew',    u'Dipper',   u'Dorking',
            u'Dotterel',      u'Dove',     u'Drake',     u'Eagle',     u'Egret',
              u'Falcon',     u'Finch',  u'Flamingo',   u'Flicker',   u'Grackle',
              u'Grosbeak',    u'Grouse',    u'Guinea',      u'Hawk',       u'Hen',
                  u'Ibis',  u'Kingbird',      u'Kiwi',   u'Lapwing',      u'Lark',
           u'Leghorn',    u'Linnet',   u'Mallard',    u'Martin',    u'Merlin',
            u'Minorca',    u'Oriole',   u'Ortolan',    u'Osprey',  u'Parakeet',
           u'Partridge',   u'Peacock',   u'Pelican',   u'Penguin',    u'Petrel',
           u'Pheasant',    u'Pigeon',     u'Quail',      u'Rail',     u'Raven',
            u'Redwing',     u'Robin',      u'Rook',     u'Ruddy',   u'Sparate',
             u'Sparrow',  u'Starling',      u'Swan',   u'Swanate',     u'Swift',
                 u'Tern',    u'Turkey',   u'Waxwing']

acss = [     u'Avocet',     u'Bittern',    u'Bluebird',
           u'Bluejay',    u'Bobolink',       u'Brant',   u'Bullfinch',
              u'Bunting',      u'Canary',  u'Canvasback',    u'Cardinal',
                  u'Chukar',      u'Condor',   u'Cormorant',   u'Corncrake',
              u'Cuckoo',      u'Curlew',      u'Dipper',       u'Diver',
                    u'Dove',       u'Drake',       u'Eagle',       u'Egret',
                u'Falcon',       u'Finch',    u'Flamingo',     u'Flicker',
            u'Gannet',   u'Goldfinch',     u'Grackle',    u'Grosbeak',
                  u'Hawk',         u'Hen',       u'Heron',    u'Hornbill',
                u'Ibis',       u'Joree',       u'Junco',        u'Kiwi',
           u'Lapwing',        u'Lark',      u'Linnet',       u'Macaw',
              u'Mallard',      u'Martin', u'Mockingbird',    u'Nuthatch',
                  u'Oriole',     u'Ortolan',     u'Ostrich',      u'Oxbird',
            u'Parakeet',      u'Parrot',   u'Partridge',     u'Peacock',
              u'Pheasant',     u'Phoenix',      u'Plover',    u'Popinjay',
               u'Ptarmigan',      u'Puffin',        u'Rail',      u'Ratite',
                  u'Redbird',     u'Redwing',    u'Ringdove',  u'Roadrunner',
                u'Rook',       u'Ruddy',   u'Sapsucker',       u'Scaup',
       u'Scissortail',      u'Scoter',     u'Seahawk',    u'Snowbird',
                u'Spoonbill',       u'Squab',    u'Starling',       u'Stilt',
             u'Stork',  u'Tailorbird',        u'Teal',        u'Tern',
               u'Thrasher',        u'Tody',      u'Toucan',      u'Towhee',
                   u'Trogon',     u'Turacos',      u'Turbit',     u'Wagtail',
              u'Whooper',     u'Widgeon',    u'Woodcock']

# Had to remove wood duck because of title() function

# ACSR
# 230
#skylark = cable.cable('Skylark', 'acsr')

acsr_df = pd.DataFrame()

for k in acsr:
    cable_i = cable.cable(k, 'acsr')
    acsr_df[k] = np.asarray([cable_i.I(348, i, 0.61) for i in np.arange(273+0, 273+60)])/(cable_i.I(348, 298, 0.61))

acss_df = pd.DataFrame()

for k in acss:
    cable_i = cable.cable(k, 'acss')
    acss_df[k] = np.asarray([cable_i.I(348, i, 0.61) for i in np.arange(273+0, 273+60)])/(cable_i.I(348, 298, 0.61))

#####################

acsr_df.idxmin(axis=1) # ACSR BLUEBIRD HEATS UP THE FASTEST

acsr_cat = pd.concat([acsr_df.loc[59], cable_i.models['acsr'].T], axis=1)

# As cable diameter increases, effect of temperature on ampacity increases
scatter(acsr_cat['cable_d'], acsr_cat[59])

# Contour plot
trange = np.asarray([bluebird.I(348, i, np.arange(0,4,0.01)) for i in np.arange(273+0, 273+60, 0.1)])/bluebird.I(348, 273+25, 0.61)
trange = pd.DataFrame(trange).fillna(0).values

cf = contourf(trange.T, cmap='jet_r')
cb = colorbar()
cf.ax.set_xticklabels([0, 10, 20, 30, 40, 50])
cf.ax.set_yticklabels(np.linspace(0, 4, 8, endpoint=False))
title('Weather effects on ampacity')
ylabel('Wind speed (m/s)')
xlabel('Ambient temperature (C)')
cb.set_label('Fraction of Rated Ampacity')
