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

aac = [    u'Arbutus',       u'Aster',    u'Bluebell',  u'Bluebonnet',
             u'Canna',   u'Carnation',   u'Cockscomb',   u'Columbine',
         u'Coreopsis',      u'Cosmos',     u'Cowslip',    u'Daffodil',
            u'Dahlia',       u'Daisy',   u'Goldenrod',  u'Goldentuft',
          u'Hawkweed',    u'Hawthorn',    u'Heuchera',        u'Iris',
         u'Jessamine',    u'Larkspur',      u'Laurel',       u'Lilac',
            u'Lupine',    u'Magnolia',    u'Marigold', u'Meadowsweet',
         u'Mistletoe',   u'Narcissus',  u'Nasturtium',      u'Orchid',
             u'Oxlip',       u'Pansy',   u'Peachbell',       u'Peony',
           u'Petunia',       u'Phlox',       u'Poppy',        u'Rose',
        u'Sneezewort',     u'Syringa',    u'Trillium',       u'Tulip',
          u'Valerian',     u'Verbena',      u'Violet',      u'Zinnia']

# Had to remove wood duck because of title() function

# ACSR
# 230
#skylark = cable.cable('Skylark', 'acsr')

acsr_df = pd.DataFrame()

for k in acsr:
    cable_i = cable.cable(k, 'acsr')
    acsr_df[k] = np.asarray([cable_i.I(348, i, 0.61) for i in np.arange(273+0, 273+61)])/(cable_i.I(348, 298, 0.61))

acss_df = pd.DataFrame()

for k in acss:
    cable_i = cable.cable(k, 'acss')
    acss_df[k] = np.asarray([cable_i.I(348, i, 0.61) for i in np.arange(273+0, 273+61)])/(cable_i.I(348, 298, 0.61))

aac_df = pd.DataFrame()

for k in aac:
    cable_i = cable.cable(k, 'aac')
    aac_df[k] = np.asarray([cable_i.I(348, i, 0.61) for i in np.arange(273+0, 273+61)])/(cable_i.I(348, 298, 0.61))

fill_between(acsr_df.index.values, acsr_df.min(axis=1), acsr_df.max(axis=1), color='blue', label='ACSR', alpha=1)
xlabel('Ambient temperature ($^\circ$C)')
ylabel('Fraction of rated capacity')
title('ACSR cable')
clf()


fill_between(acss_df.index.values, acss_df.min(axis=1), acss_df.max(axis=1), color='orange', label='ACSS', alpha=1)
xlabel('Ambient temperature ($^\circ$C)')
ylabel('Fraction of rated capacity')
title('ACSS cable')
clf()

fill_between(aac_df.index.values, aac_df.min(axis=1), aac_df.max(axis=1), color='red', label='AAC', alpha=1)
xlabel('Ambient temperature ($^\circ$C)')
ylabel('Fraction of rated capacity')
title('AAC cable')
ylim(0.4, 1.3)
clf()
#####################

acsr_cat = pd.concat([acsr_df.loc[50], cable_i.models['acsr'].T], axis=1)
acss_cat = pd.concat([acss_df.loc[50], cable_i.models['acss'].T], axis=1)
aac_cat = pd.concat([aac_df.loc[50], cable_i.models['aac'].T], axis=1)

# As cable diameter increases, effect of temperature on ampacity increases
scatter(acsr_cat['cable_d'], acsr_cat[50], color='blue', alpha=0.7, label='ACSR')
scatter(acss_cat['cable_d'], acss_cat[50], color='orange', alpha=0.7, label='ACSS')
scatter(aac_cat['cable_d'], aac_cat[50], color='red', alpha=0.7, label='AAC')
xlabel('Cable diameter (m)')
ylabel('Fraction of rated ampacity at 50 $^\circ$C') # at 50 C
title('Reduction in rated ampacity vs. cable diameter')

# Contour plot

# trange = np.asarray([bluebird.I(348, i, np.arange(0,4,0.01)) for i in np.arange(273+0, 273+60, 0.1)])/bluebird.I(348, 273+25, 0.61)
# trange = pd.DataFrame(trange).fillna(0).values

# cf = contourf(trange.T, cmap='jet_r')
# cb = colorbar()
# cf.ax.set_xticklabels([0, 10, 20, 30, 40, 50])
# cf.ax.set_yticklabels(np.linspace(0, 4, 8, endpoint=False))
# title('Weather effects on ampacity')
# ylabel('Wind speed (m/s)')
# xlabel('Ambient temperature (C)')
# cb.set_label('Fraction of Rated Ampacity')

def contour_plot(name, model, trange, vrange, maxtemp, a_s=0.9, e_s=0.7, levels=[0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]):

    cable_i = cable.cable(name, model)
    a = np.asarray([cable_i.I(maxtemp, i, np.arange(*vrange), a_s=a_s, e_s=e_s) for i in np.arange(*trange)])/cable_i.I(maxtemp, 273+25, 0.61, a_s=a_s, e_s=e_s)
    a = pd.DataFrame(a).fillna(0).values
    
    cf = contourf(a.T, cmap='jet_r', levels=levels)
    cb = colorbar()
    cf.ax.set_xticklabels([0, 10, 20, 30, 40, 50])
    cf.ax.set_yticklabels(np.linspace(0, 4, 8, endpoint=False))
    title('Conductor Temperature: %s $^\circ$C' % (maxtemp - 273))
    ylabel('Wind speed (m/s)')
    xlabel('Ambient temperature ($^\circ$C)')
    cb.set_label('Fraction of Rated Ampacity')

contour_plot('Bluebird', 'acsr', (273+0, 273+60, 0.1), (0,4,0.01),  273+75)


#### contour of ampacity vs. temperature and diameter


trange = (273+0, 273+60, 0.1)
drange = (0.005, 0.05, 0.001)
maxtemp = 273+75

def contour_diam(trange, drange, maxtemp, a_s=0.9, e_s=0.7, levels=[0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]):

    cable_i = cable.cable('Bluebird', 'acsr')
    trange = np.arange(*trange)
    drange = np.arange(*drange)
    
    df = pd.DataFrame()

    for d in drange:
        cable_i.D = d
        a = np.asarray([cable_i.I(maxtemp, i, 0.61, a_s=a_s, e_s=e_s) for i in trange])/cable_i.I(maxtemp, 273+25, 0.61, a_s=a_s, e_s=e_s)
        df[d] = a
#    a = pd.DataFrame(a).fillna(0).values
    a = df.sort_index(axis=1).values
    
    cf = contourf(a, cmap='jet_r', levels=levels)
    cb = colorbar()
    cf.ax.set_yticklabels([0, 10, 20, 30, 40, 50])
    cf.ax.set_xticklabels(100*np.linspace(0, 0.05, 10, endpoint=False))
    title('Conductor Temperature: %s $^\circ$C' % (maxtemp - 273))
    xlabel('Conductor diameter (cm)')
    ylabel('Ambient temperature ($^\circ$C)')
    cb.set_label('Fraction of Rated Ampacity')

contour_diam((273+0, 273+60, 0.1), (0.005, 0.05, 0.001),  273+75)
