import geopandas as gpd
import geodatasets

dublin = gpd.read_file(geodatasets.get_path('geoda.nepal'))
dublin = dublin.rename(columns={"name_2": "zone"})
print(dublin[["zone", "geometry"]].head())