from geopandas import read_file

from matplotlib.pyplot import subplots, savefig

world = read_file("../../data/natural-earth/ne_50m_admin_0_countries.shp")

print(world.head())

# create map axis object
my_fig, my_ax = subplots(1, 1, figsize=(16, 10))

# turn off the visible axes on the map
my_ax.axis('off')

graticule = read_file("../../data/natural-earth/ne_110m_graticules_15.shp")
bbox = read_file("../../data/natural-earth/ne_110m_wgs84_bounding_box.shp")
# add bounding box and graticule layers
bbox.plot(
    ax = my_ax,
    color = 'green',
    linewidth = 0,
    )

# plot the countries
world.plot(
    ax = my_ax,
    color = 'blue',
    linewidth = 0.5,
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