from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from scipy import stats
import matplotlib as mpl

fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# create polar stereographic Basemap instance.
m = Basemap(-130, 20, -60, 50,\
            rsphere=6371200.,resolution='l',area_thresh=10000)
# draw coastlines, state and country boundaries, edge of map.
m.drawmapboundary()
m.fillcontinents('0.85')
m.drawcoastlines()
m.drawstates()
m.drawcountries()

m.readshapefile('/home/akagi/trans_impacts', 'transmission', drawbounds=False)

# for info, shape in zip(m.transmission_info, m.transmission):
#     if info['pct_decrea'] < -3.3:
#         x, y = zip(*shape)
#         m.plot(x, y, marker=None, color='m', linewidth=0.1)
#     else:
#         x, y = zip(*shape)
#         m.plot(x, y, marker=None, color='b', linewidth=0.1)

# t = gpd.read_file('/home/akagi/trans_impacts.shp')

def gencolor(N, colormap='Set1'):
    """
    Color generator intended to work with one of the ColorBrewer
    qualitative color scales.
    Suggested values of colormap are the following:
        Accent, Dark2, Paired, Pastel1, Pastel2, Set1, Set2, Set3
    (although any matplotlib colormap will work).
    """
    from matplotlib import cm
    # don't use more than 9 discrete colors
    n_colors = min(N, 9)
    cmap = cm.get_cmap(colormap, n_colors)
    colors = cmap(range(n_colors))
    for i in xrange(N):
        yield colors[i % n_colors]

def norm_cmap(values, cmap, normalize, cm, mn, mx):

    """ Normalize and set colormap
        Parameters
        ----------
        values
            Series or array to be normalized
        cmap
            matplotlib Colormap
        normalize
            matplotlib.colors.Normalize
        cm
            matplotlib.cm
        Returns
        -------
        n_cmap
            mapping of normalized values to colormap (cmap)
    """

    if (mn is None) and (mx is None):
        mn, mx = min(values), max(values)
    norm = normalize(vmin=mn, vmax=mx)
    n_cmap = cm.ScalarMappable(norm=norm, cmap=cmap)
    return n_cmap, norm

def __pysal_choro(values, scheme, k=5):
    """ Wrapper for choropleth schemes from PySAL for use with plot_dataframe
        Parameters
        ----------
        values
            Series to be plotted
        scheme
            pysal.esda.mapclassify classificatin scheme ['Equal_interval'|'Quantiles'|'Fisher_Jenks']
        k
            number of classes (2 <= k <=9)
        Returns
        -------
        values
            Series with values replaced with class identifier if PySAL is available, otherwise the original values are used
    """

    try:
        from pysal.esda.mapclassify import Quantiles, Equal_Interval, Fisher_Jenks
        schemes = {}
        schemes['equal_interval'] = Equal_Interval
        schemes['quantiles'] = Quantiles
        schemes['fisher_jenks'] = Fisher_Jenks
        s0 = scheme
        scheme = scheme.lower()
        if scheme not in schemes:
            scheme = 'quantiles'
            print('Unrecognized scheme: ', s0)
            print('Using Quantiles instead')
        if k < 2 or k > 9:
            print('Invalid k: ', k)
            print('2<=k<=9, setting k=5 (default)')
            k = 5
        binning = schemes[scheme](values, k)
        values = binning.yb
    except ImportError:
        print('PySAL not installed, setting map to default')

    return values

def plot_linestring(ax, geom, color='black', **kwargs):
    """ Plot a single LineString geometry """
    a = np.array(geom)
    ax.plot(a[:, 0], a[:, 1], color=color, **kwargs)

# colorset (from plot geodataframe

def plot_to_basemap(m, name, column=None, geom_type='LineString', colormap='rainbow', scheme=None, k=5, fixed_bins=False, man_bins=None,  mn=None, mx=None, **kwargs):
    from matplotlib.colors import Normalize
    from matplotlib import cm as mcm
    from matplotlib import colorbar
    from matplotlib import ticker
    from scipy import stats

    values = np.array([i[column] for i in getattr(m, '%s_info' % name)])
    if man_bins:
        valuebins = np.asarray(man_bins)
        k = len(man_bins) - 1
    else:
        valuebins = stats.mstats.mquantiles(values, np.linspace(0,1,k+1))

    if fixed_bins:
        values = np.digitize(values, valuebins)
    else:
        values = __pysal_choro(values, scheme, k=k)
    cmap, norm = norm_cmap(values, colormap, Normalize, mcm, mn=mn, mx=mx)

    for geom, value in zip(getattr(m, name), values):
       if geom_type == 'Polygon' or geom_type == 'MultiPolygon':
           plot_multipolygon(ax, geom, facecolor=cmap.to_rgba(value), **kwargs)
       elif geom_type == 'LineString' or geom_type == 'MultiLineString':
        plot_linestring(m, geom, color=cmap.to_rgba(value), **kwargs)
        # TODO: color point geometries
       elif geom_type == 'Point':
           plot_point(ax, geom, **kwargs)

    dcmap = mpl.colors.ListedColormap([cmap.to_rgba(i) for i in range(k+1)][1:-1])
    dcmap.set_under(cmap.to_rgba(0))
    dcmap.set_over(cmap.to_rgba(k+1))

    cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
    cb = colorbar.ColorbarBase(cax, cmap=dcmap, norm=norm, orientation='vertical', extend='both', spacing='uniform', extendfrac='auto')
    cb.locator = ticker.LinearLocator(numticks=k)
    cb.formatter = ticker.FixedFormatter(valuebins.astype(str).tolist()[:-1])
    cb.update_ticks()

    # cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
    # cb = colorbar.ColorbarBase(cax, cmap=colormap, norm=norm, orientation='vertical')
    # cb.locator = ticker.MaxNLocator(nbins=k)
    # cb.formatter = ticker.FixedFormatter(valuebins.astype(str).tolist())
    # cb.update_ticks()
           

man_bins = (-9.17343664, -4.85376639, -4.4010333 , -3.98366336, -3.53319506, 0.0, 2.42685153)

# functions


def plot_multilinestring(ax, geom, color='red', linewidth=1):
    """ Can safely call with either LineString or MultiLineString geometry
    """
    if geom_type == 'LineString':
        plot_linestring(ax, geom, color=color, linewidth=linewidth)
    elif geom_type == 'MultiLineString':
        for line in geom.geoms:
            plot_linestring(ax, line, color=color, linewidth=linewidth)

# RUN

# plot_to_basemap(m, 'transmission', 'pct_decrea', scheme='Quantiles', colormap='jet_r', linewidth=0.1)

# man_bins = (-9.17343664, -4.85376639, -4.4010333 , -3.98366336, -3.53319506, 0.0, 2.42685153)

# plot_to_basemap(m, 'transmission', 'pct_decrea', fixed_bins=True, man_bins=man_bins, colormap='jet_r', linewidth=0.1)

# THINGS

name='transmission'
column='pct_decrea'
# scheme='Quantiles'
scheme=None
colormap='jet_r'
linewidth=0.1
mn=None
mx=None
k=5
fixed_bins=True
man_bins = (-9.17343664, -4.85376639, -4.4010333 , -3.98366336, -3.53319506, 0.0, 2.42685153)

from matplotlib.colors import Normalize
from matplotlib import cm as mcm
from matplotlib import colorbar
from matplotlib import ticker

values = np.array([i[column] for i in getattr(m, '%s_info' % name)])
#valuebins = stats.mstats.mquantiles(values, np.linspace(0,1,k+1))

if fixed_bins:
    valuebins = np.asarray(man_bins)
    k = len(man_bins) - 1
else:
    valuebins = stats.mstats.mquantiles(values, np.linspace(0,1,k+1))

if fixed_bins:
    values = np.digitize(values, valuebins)
else:
    values = __pysal_choro(values, scheme, k=k)

cmap, norm = norm_cmap(values, colormap, Normalize, mcm, mn=mn, mx=mx)
# try_discrete

dcmap = mpl.colors.ListedColormap([cmap.to_rgba(i) for i in range(k+1)][1:-1])
dcmap.set_under(cmap.to_rgba(0))
dcmap.set_over(cmap.to_rgba(k+1))

# cmap = mpl.colors.ListedColormap(['r', 'g', 'b', 'c'])
# cmap.set_over('0.25')
# cmap.set_under('0.75')

cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
cb = colorbar.ColorbarBase(cax, cmap=dcmap, norm=norm, orientation='vertical', extend='both', spacing='uniform', extendfrac='auto')
#cb.locator = ticker.MaxNLocator(nbins=k)
cb.locator = ticker.LinearLocator(numticks=k)
cb.formatter = ticker.FixedFormatter(valuebins.astype(str).tolist()[:-1])
#cb.ax.set_yticklabels(valuebins[1].astype(str))
cb.update_ticks()
plt.show()

# 6 colors on colorbar
# digitize produces 7 bins
