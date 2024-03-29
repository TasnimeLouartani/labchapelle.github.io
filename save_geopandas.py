import geopandas as gpd

# Charger ou créer votre GeoDataFrame
gdf = gpd.read_file('autour_lachapelle.html')  # ou toute autre source de données

# Vous pouvez effectuer des manipulations sur votre GeoDataFrame ici

# Exporter en GeoJSON
gdf.to_file('test.geojson', driver='GeoJSON')
