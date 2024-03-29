import folium

# Initialiser la carte avec une localisation et un niveau de zoom de départ
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

lab_chapelle = [48.89687365722607, 2.357454377626761]
plateau_urba = [48.8968, 2.3569]

# Ajouter le fond de carte CartoDB Positron en utilisant son URL de tuiles directement
cartodb_positron = folium.TileLayer(
    tiles='',
    attr='CartoDB Positron',
    name='CartoDB Positron',
    subdomains='abcd',
    max_zoom=19
)
cartodb_positron.add_to(m)

# Ajouter OpenStreetMap comme une autre couche de fond de carte
# folium.TileLayer(
#     tiles='OpenStreetMap',
#     name='OpenStreetMap'
# ).add_to(m)

# Ajouter le contrôle de couche pour permettre à l'utilisateur de choisir entre les fonds de carte
folium.LayerControl().add_to(m)

# capoeira_coord = [48.8951, 2.3652]
# capoeira_img = 'C:/Users/louartani/Documents/nc/capoeira.png'
# capoeira_icon = folium.CustomIcon(capoeira_img, icon_size=(180, 180))
# capoeira_marker = folium.Marker(location=[capoeira_coord[0],capoeira_coord[1]], icon=capoeira_icon, popup='Capoeria Viola')
# capoeira_marker.add_to(m)

activ18_coord = [48.8950, 2.3656]
activ18_img = 'C:/Users/louartani/Documents/nc/activ18.png'
activ18_icon = folium.CustomIcon(activ18_img, icon_size=(200, 200))
activ18_marker = folium.Marker(location=activ18_coord, icon=activ18_icon, popup='Activ18')
activ18_marker.add_to(m)

# Afficher la carte
m.save('C:/Users/louartani/Documents/nc/map_with_cartodb_and_osm.html')
