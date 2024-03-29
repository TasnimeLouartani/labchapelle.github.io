import zipfile
import json
import geopandas as gpd

### LECTURE D UN FICHIER ZIP NOISE CAPTURE
# with zipfile.ZipFile("C:/Users/louartani/Documents/nc/track_0fab2856-f7a6-4cb9-9aca-5273a6e0b90e.zip", "r") as thezip :
#     # with thezip.open('track.geojson',mode='r') as thefile :
#     #     print(thefile.read())
#     with thezip.open('track.geojson') as myfile :
#         data = json.load(myfile)

# for i in range(len(data['features'])):
#     latitude = data['features'][i]['geometry']['coordinates'][0]
#     longitude = data['features'][i]['geometry']['coordinates'][1]
#     leq_mean = data['features'][i]['properties']['leq_mean']
#     marker_color = data['features'][i]['properties']['marker-color']

### LECTURE DU GEJSON
# with open('C:/Users/louartani/Documents/nc/fontaines-a-boire.geojson') as myfile:
#     data = json.load(myfile)
data = gpd.read_file('C:/Users/louartani/Documents/nc/fontaines-a-boire.geojson') 
data['longitude']=0.0
data['latitude']=0.0


for i in range(len(data)):
    latitude = data['geometry'][i].coords.xy[1][0]
    longitude = data['geometry'][i].coords.xy[0][0]
    autre = data['dispo'][i]
    data['longitude'][i]=longitude
    data['latitude'][i]=latitude


data.to_file('C:/Users/louartani/Documents/nc/fontaines.geojson', index=False)
    


    