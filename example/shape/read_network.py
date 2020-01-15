import geopandas as gpd
from shapely.wkt import loads
import pandas as pd
import matplotlib.pyplot as plt

# read csv file
df = pd.read_csv('shape_network.csv', index_col=[0])
# convert string in geometry column to shapely object
df['geometry'] = df.apply(lambda _: loads(_['mv_grid_district_geom']), axis=1)
# convert to geopandas dataframe for easy plotting (plots `geometry` column)
df = gpd.GeoDataFrame(df)
df.plot()
plt.show()
