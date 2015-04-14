# RIPS
Files:

eia_getter: Constructs time series of electricity load for each electric utility.

elec_temp_join: Joins utility service areas with temperature forcings based on location of major urban areas.

get_util_eia_code: Queries NREL api to determine EIA code for each utility service area.

line_to_sub: Matches transmission lines with corresponding start and end nodes (substations).

substation_voronoi: DEPRECATED -- creates voronoi polygons for each electrical substation.

voronoi_stats: Applies raster stats to determine fraction of load at each voronoi polygon in a utility service area.
