from geopandas import read_file

from matplotlib.pyplot import subplots, savefig

world = read_file("../../data/natural-earth/ne_50m_admin_0_countries.shp")

print(world.head())

print(world.columns)

# create map axis object
my_fig, my_ax = subplots(1, 1, figsize=(16, 10))

# turn off the visible axes on the map
my_ax.axis('off')

graticule = read_file("../../data/natural-earth/ne_110m_graticules_15.shp")
bbox = read_file("../../data/natural-earth/ne_110m_wgs84_bounding_box.shp")

#CRS Pejection import
ea_proj = "+proj=wag4 +lon_0=10 +datum=WGS84 +units=m +no_defs"

my_ax.set(title="GDP Per Capita: Equal Earth Coordinate Reference System")

# reproject all three layers to equal earth
world = world.to_crs(ea_proj)
graticule = graticule.to_crs(ea_proj)
bbox = bbox.to_crs(ea_proj)

world['GDP_Per_Capita'] = world['GDP_MD_EST']*1000000 / world['POP_EST']

print(world.GDP_Per_Capita)

# add bounding box and graticule layers
bbox.plot(
    ax = my_ax,
    color = 'GRAY',
    linewidth = 0,
    )

# plot the countries
world.plot(								# plot the world dataset
    ax = my_ax,						# specify the axis object to draw it to
    column = 'GDP_Per_Capita',		# specify the column used to style the dataset
    cmap = 'GnBu',				# specify the colour map used to style the dataset based on POP_EST
    scheme = 'quantiles',	# specify how the colour map will be mapped to the values in POP_EST
    linewidth = 0.5,			# specify the line width for the country outlines
    edgecolor = 'gray',
legend = True,
legend_kwds = {
    'loc': 'lower left',
    'title': 'GDP per Capita'
    }		# specify the line colour for the country outlines
    )

# plot the graticule
graticule.plot(
    ax = my_ax,
    color = 'black',
    linewidth = 0.5,
    )

# save the result
savefig('./out/1.png')
print("done!")