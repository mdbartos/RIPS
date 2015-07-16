from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from scipy import stats
import matplotlib as mpl
from shapely import geometry

#m.readshapefile('/home/akagi/Dropbox/NSF WSC AZ WEN Team Share/Electricity Demand/plots/util_proj/utility_rcp45', 'utility', drawbounds=False)

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

def plot_linestring(ax, geom, color='black', linewidth=1, **kwargs):
    """ Plot a single LineString geometry """
    a = np.array(geom)
    ax.plot(a[:, 0], a[:, 1], color=color, linewidth=linewidth, **kwargs)

def plot_multilinestring(ax, geom, color='red', linewidth=1):
    """ Can safely call with either LineString or MultiLineString geometry
    """
    if geom_type == 'LineString':
        plot_linestring(ax, geom, color=color, linewidth=linewidth)
    elif geom_type == 'MultiLineString':
        for line in geom.geoms:
            plot_linestring(ax, line, color=color, linewidth=linewidth)

def plot_polygon(ax, polymap, facecolor='red', edgecolor='black', alpha=1, linewidth=1):
    """ Plot a single Polygon geometry """
    from descartes.patch import PolygonPatch
    a = np.asarray(polymap)
    poly = geometry.asPolygon(polymap)
    # without Descartes, we could make a Patch of exterior
    ax.add_patch(PolygonPatch(poly, facecolor=facecolor, alpha=alpha))
    ax.plot(a[:, 0], a[:, 1], color=edgecolor, linewidth=linewidth)
    for p in poly.interiors:
        x, y = zip(*p.coords)
        ax.plot(x, y, color=edgecolor, linewidth=linewidth)


def plot_multipolygon(ax, geom, facecolor='red', edgecolor='black', alpha=0.5):
    """ Can safely call with either Polygon or Multipolygon geometry
    """
    if geom.type == 'Polygon':
        plot_polygon(ax, geom, facecolor=facecolor, edgecolor=edgecolor, alpha=alpha)
    elif geom.type == 'MultiPolygon':
        for poly in geom.geoms:
            plot_polygon(ax, poly, facecolor=facecolor, edgecolor=edgecolor, alpha=alpha)

# colorset (from plot geodataframe

def plot_to_basemap(name, column=None, geom_type='LineString', colormap='rainbow', scheme=None, k=5, fixed_bins=False, man_bins=None,  mn=None, mx=None, linewidth=1, alpha=1, orientation='horizontal', save=False, **kwargs):
    from matplotlib.colors import Normalize
    from matplotlib import cm as mcm
    from matplotlib import colorbar
    from matplotlib import ticker
    from scipy import stats


    fig = plt.figure(figsize=(8,8))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    # create polar stereographic Basemap instance.
    m = Basemap(-125, 31, -102, 50,\
                rsphere=6371200.,resolution='l',area_thresh=10000)
    # draw coastlines, state and country boundaries, edge of map.
    m.drawmapboundary(fill_color='lightsteelblue')
    m.fillcontinents('0.85', lake_color='lightsteelblue')
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    m.readshapefile('/home/akagi/trans_impacts', 'transmission', drawbounds=False)

    values = np.array([i[column] for i in getattr(m, '%s_info' % name)])
    if man_bins:
        valuebins = np.asarray(man_bins)
        k = len(man_bins) - 1
    else:
        valuebins = stats.mstats.mquantiles(values, np.linspace(0,1,k+1))

    if fixed_bins:
        values = np.digitize(values, valuebins)
    else:
        # pysal not working with new colorbar definition
        values = __pysal_choro(values, scheme, k=k)

    cmap_ints = np.arange(len(man_bins) + 1)
    cmap, norm = norm_cmap(values, colormap, Normalize, mcm, mn=cmap_ints[0], mx=cmap_ints[-1])

    for geom, value in zip(getattr(m, name), values):
       if geom_type == 'Polygon' or geom_type == 'MultiPolygon':
           plot_polygon(ax, geom, facecolor=cmap.to_rgba(value), alpha=alpha, linewidth=linewidth, **kwargs)
       elif geom_type == 'LineString' or geom_type == 'MultiLineString':
        plot_linestring(m, geom, color=cmap.to_rgba(value), linewidth=linewidth, **kwargs)
        # TODO: color point geometries
       elif geom_type == 'Point':
           plot_point(ax, geom, **kwargs)

    dcmap = mpl.colors.ListedColormap([cmap.to_rgba(i) for i in cmap_ints][1:-1])
    dcmap.set_under(cmap.to_rgba(0))
    dcmap.set_over(cmap.to_rgba(cmap_ints[-1]))

#    cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
    cax = fig.add_axes([0.1, 0.1, 0.8, 0.02])
    cb = colorbar.ColorbarBase(cax, cmap=dcmap, norm=norm, orientation=orientation, extend='both', spacing='uniform', extendfrac='auto')
    cb.locator = ticker.LinearLocator(numticks=len(cmap_ints)-1)
    cb.formatter = ticker.FixedFormatter(['%.2f' % (i) for i in valuebins.tolist()])
    cb.update_ticks()
    if save:
        fig.savefig('%s.png' % column)
#    plt.close(fig)

    # cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
    # cb = colorbar.ColorbarBase(cax, cmap=colormap, norm=norm, orientation='vertical')
    # cb.locator = ticker.MaxNLocator(nbins=k)
    # cb.formatter = ticker.FixedFormatter(valuebins.astype(str).tolist())
    # cb.update_ticks()
           

man_bins = (-7.5, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0)

#man_bins = (-9.17343664, -4.85376639, -4.4010333 , -3.98366336, -3.53319506, 0.0, 2.42685153)

#man_bins = (1.02, 1.04, 1.06, 1.08, 1.10, 1.12)

plot_to_basemap('transmission', 'pct_decrea', fixed_bins=True, man_bins=man_bins, colormap='jet_r', linewidth=0.1, save=True)

for c in ['pct_decrea', 'pct_decr_1', 'pct_decr_2', 'pct_decr_3', 'pct_decr_4', 'pct_decr_5', 'pct_decr_6', 'pct_decr_7', 'pct_decr_8', 'pct_decr_9']:
    plot_to_basemap('transmission', c, fixed_bins=True, man_bins=man_bins, colormap='jet_r', linewidth=0.1, save=True)



# functions



# RUN

# plot_to_basemap(m, 'transmission', 'pct_decrea', scheme='Quantiles', colormap='jet_r', linewidth=0.1)

# man_bins = (-9.17343664, -4.85376639, -4.4010333 , -3.98366336, -3.53319506, 0.0, 2.42685153)

# plot_to_basemap(m, 'transmission', 'pct_decrea', fixed_bins=True, man_bins=man_bins, colormap='jet_r', linewidth=0.1)

# plot_to_basemap(m, 'utility', 'load_2050', geom_type='Polygon', fixed_bins=True, man_bins=man_bins, colormap='OrRd', linewidth=0.1)

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
man_bins = (-7.5, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0)

from matplotlib.colors import Normalize
from matplotlib import cm as mcm
from matplotlib import colorbar
from matplotlib import ticker
from scipy import stats


fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# create polar stereographic Basemap instance.
m = Basemap(-125, 31, -102, 50,\
	rsphere=6371200.,resolution='l',area_thresh=10000)
# draw coastlines, state and country boundaries, edge of map.
m.drawmapboundary(fill_color='lightsteelblue')
m.fillcontinents('0.85', lake_color='lightsteelblue')
m.drawcoastlines()
m.drawstates()
m.drawcountries()

m.readshapefile('/home/akagi/trans_impacts', 'transmission', drawbounds=False)

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

cmap_ints = np.arange(len(man_bins) + 1)

cmap, norm = norm_cmap(values, colormap, Normalize, mcm, mn=cmap_ints[0], mx=cmap_ints[-1])
# try_discrete

dcmap = mpl.colors.ListedColormap([cmap.to_rgba(i) for i in cmap_ints][1:-1])
dcmap.set_under(cmap.to_rgba(0))
dcmap.set_over(cmap.to_rgba(cmap_ints[-1]))

cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
cb = colorbar.ColorbarBase(cax, cmap=dcmap, norm=norm, orientation='vertical', extend='both', spacing='uniform', extendfrac='auto')
#cb.locator = ticker.MaxNLocator(nbins=k)
cb.locator = ticker.LinearLocator(numticks=len(cmap_ints) - 1)
cb.formatter = ticker.FixedFormatter(valuebins.astype(str).tolist())
#cb.ax.set_yticklabels(valuebins[1].astype(str))
cb.update_ticks()
plt.show()

# 6 colors on colorbar
# digitize produces 7 bins
