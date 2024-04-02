import folium
from folium.plugins import FeatureGroupSubGroup
import pandas as pd
import os
import zipfile
import json
from folium.features import GeoJson, GeoJsonTooltip
from folium import plugins

############# FONCTIONS

def recup_files_nc(dossier, longitude_min, latitude_min, longitude_max, latitude_max, markers_list, map):
      
      """
              permet de récupérer les fichiers dans un dossier spécifique et les lire (extrait de zip)
      """
      
      liste_fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f)) and f.lower().endswith('.zip')]
      # pour cela, doit parcourir la liste des zips
      for lf in range(len(liste_fichiers)):
              chemin_complet = os.path.join(dossier, liste_fichiers[lf])
              with zipfile.ZipFile(chemin_complet, "r") as thezip :
                     with thezip.open('track.geojson') as myfile :
                            data = json.load(myfile)
                            for i in range(len(data['features'])):
                                   if data['features'][i]['geometry']!=None:
                                          longitude = data['features'][i]['geometry']['coordinates'][0]
                                          latitude = data['features'][i]['geometry']['coordinates'][1]
                                          leq_mean = str(round(data['features'][i]['properties']['leq_mean'],1)) + " dB"
                                          marker_color = data['features'][i]['properties']['marker-color']
                                          popup = folium.Popup(leq_mean, max_width=300)
                                          #ajout marker test de noise capture
                                          #avec le filtre sur les données
                                          if longitude >= longitude_min and longitude <= longitude_max and latitude >= latitude_min and latitude <= latitude_max :
                                                 folium.CircleMarker(location=[latitude,longitude],radius = 2,fill=True, popup=popup,color=marker_color,fill_color=marker_color,fill_opacity=1).add_to(markers_list)
                                          markers_list.add_to(map)

def markers_travaux(name,coords, grp_markers,map):
      """
            Permet de récupérer les coordonnées et le nom du chantier et le nom apparaît en popup (et l'ajoute dans le groupement de markers) puis l'ajoute dans la map
      """
      folium.Marker(location=coords, icon=folium.Icon(color='orange', icon='person-digging',  prefix='fa'), popup=name).add_to(grp_markers)
      grp_markers.add_to(map)




########################## Coordonnées, points stratégiques ################################
lachapelle_nord = [48.8983, 2.3639]
lab_chapelle = [48.89687365722607, 2.357454377626761]
plateau_urba = [48.8968, 2.3569]
arena = [48.89943676791121, 2.3598736170067465]
campus = [48.899474222466615, 2.357906582996598]
chapelle_charbon = [48.89729786802816, 2.363923812455709]
carrefour = [48.890228683839844, 2.3599663365046366]
rue_lachapelle = [48.89805636846962, 2.3591213798424184]
rondpt_lachapelle = [48.895319515378254, 2.3592602726719436]

#################### création de la carte ##############################

m = folium.Map(location=lachapelle_nord, zoom_start=16.5)

# Ajout de différents fonds de plan
# folium.TileLayer('Stamen Terrain',attr='Stamen Terrain',name='Stamen Terrain').add_to(m)
# folium.TileLayer('Stamen Toner',attr='Stamen Toner',name='Stamen Toner').add_to(m)
# folium.TileLayer('Stamen Watercolor',attr='Stamen Watercolor',name='Stamen Watercolor').add_to(m)
folium.TileLayer('CartoDB dark_matter',attr='CartoDB dark_matter',name='Sombre').add_to(m)
folium.TileLayer(tiles='https://tile.thunderforest.com/transport/{z}/{x}/{y}.png?apikey=cd29583c0e954c55b822ac0ecbf4c3ec', attr='Thunderforest',name='Transport').add_to(m)
#folium.TileLayer(tiles = 'https://tile.thunderforest.com/outdoors/{z}/{x}/{y}.png?apikey=cd29583c0e954c55b822ac0ecbf4c3ec',attr='Thunderforest',name='Outdoors').add_to(m)
# folium.TileLayer(tiles = 'https://tile.thunderforest.com/neighbourhood/{z}/{x}/{y}.png?apikey=cd29583c0e954c55b822ac0ecbf4c3ec',attr='Thunderforest',name='Informatif').add_to(m)
#folium.TileLayer(tiles = 'https://tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey=cd29583c0e954c55b822ac0ecbf4c3ec',attr='Thunderforest',name='cycle').add_to(m)
tile = folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr = 'Esri',name ='Images satellitaires',overlay = False,control = True).add_to(m)
folium.TileLayer('CartoDB positron',attr='CartoDB positron',name='Neutre').add_to(m)

     
# apiKey = "6rjmfea1gj14g1dr260t25rs"
# layer = 'ORTHOIMAGERY.ORTHOPHOTOS'  # Exemple: 'GEOGRAPHICALGRIDSYSTEMS.MAPS'
# style = "normal"
# format = "image/jpeg"  # Ou "image/png" selon ce que supporte la couche
# tileMatrixSet = "PM"
# tile_url = f"https://wxs.ign.fr/{apiKey}/geoportail/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER={layer}&STYLE=normal&FORMAT=image/jpeg&TILEMATRIXSET={tileMatrixSet}&TILEMATRIX={{z}}&TILEROW={{y}}&TILECOL={{x}}"
# folium.TileLayer(
#     tiles=tile_url,
#     attr='IGN',
#     name='IGN Maps',
#     overlay=False,
#     control=True,
# ).add_to(m)

# contour du quartier de la chapelle
polygon_chapelle_coord = [
                            [48.89849882559383, 2.359005588047533],  # Point 1
                            [48.898592932363925, 2.3706508631230383],   # Point 2
                            [48.89763259941668, 2.3703408711395015],   # Point 3
                            [48.896586505891385, 2.3704592081130156],    # Point 4
                            [48.895356129837594, 2.3719280016243807],   # Point 5
                            [48.89480633767935, 2.370710502232361], #Point 6
                            [48.89411100364355, 2.3702062853124337], # Point 7
                            [48.88633995435842, 2.3666128583826946], # Point 8
                            [48.88427666193788, 2.3647127530293], # Point 9
                            [48.884410437691386, 2.359400132024397], # Point 10
                            [48.88606013901714, 2.359350940142708], # Point 11
                            [48.88749953981218, 2.3600642226148003], # Point 12
                            [48.89140325971149, 2.3599567472107803], # Point 13
                            [48.89849882559383, 2.359005588047533] # retour au point 1
                            ]

lat_min, long_min = 48.88420, 2.35835
lat_max, long_max = 48.89865, 2.36918

folium.Polygon(
    locations=polygon_chapelle_coord ,
    color='gray',
    weight=0,
    dash_array = '5, 5',
    popup="Quartier de la Chapelle"
).add_to(m)

# polygone des projets urbains

# projet chapelle international

polygon_chapelle_international = [
                                    [48.8977,2.3564],
                                    [48.8979, 2.3590],
                                    [48.8950, 2.3593],
                                    [48.8944, 2.3580],
                                    [48.8943, 2.3574],
                                    [48.8977,2.3564]
                                ]

folium.Polygon(
    locations=polygon_chapelle_international ,
    color='purple',
    weight=1,
    dash_array = '5, 5',
    fill_color='purple'
).add_to(m)

folium.map.Marker(
    [48.8963, 2.3574],
    # Utiliser un icon invisible ou très discret, ici un exemple avec une icône simple de taille réduite
    icon=folium.DivIcon(html='<div style="font-size: 10pt; color : black">Chapelle International</div>')
).add_to(m)

# projet chapelle gare des mines fillette

polygon_chapelle_gdm = [
                            [48.8988,2.3596],
                            [48.900,2.3596],
                            [48.9006,2.3649],
                            [48.9006, 2.3683],
                            [48.9009,2.3683],
                            [48.9009,2.3642],
                            [48.9012,2.3623],
                            [48.9014,2.3622],
                            [48.9017,2.3625],
                            [48.9018,2.3701],
                            [48.8989,2.3703],
                            [48.8988,2.3596]
                                ]

folium.Polygon(
    locations=polygon_chapelle_gdm ,
    color='gray',
    weight=2,
    dash_array = '5, 5',
    fill_color='light_gray'
).add_to(m)

folium.map.Marker(
    [48.9000, 2.3635],
    # Utiliser un icon invisible ou très discret, ici un exemple avec une icône simple de taille réduite
    icon=folium.DivIcon(html='<div style="font-size: 10pt; color : black; width : 200px">Gare des Mines - Fillettes</div>')
).add_to(m)

# polygone projet Hébert

polygon_hebert = [
                            [48.8932,2.3637],
                            [48.8944,2.3663],
                            [48.8956,2.3711],
                            [48.8955, 2.3711],
                            [48.8940,2.3684],
                            [48.8921,2.3660],
                            [48.8932,2.3637]
                                ]

folium.Polygon(
    locations=polygon_hebert ,
    color='blue',
    weight=1,
    dash_array = '5, 5',
    fill_color='blue',
).add_to(m)

folium.map.Marker(
    [48.8940, 2.3666],
    # Utiliser un icon invisible ou très discret, ici un exemple avec une icône simple de taille réduite
    icon=folium.DivIcon(html='<div style="font-size: 10pt; color : black">Quartier Hébert</div>')
).add_to(m)

# projet chapelle charbon

polygon_charbon = [
                            [48.8963,2.3607],
                            [48.8970,2.3606],
                            [48.8978,2.3616],
                            [48.8975, 2.3640],
                            [48.8972,2.3697],
                            [48.8967,2.3700],
                            [48.8959,2.3708],
                            [48.8946,2.3665],
                            [48.8959,2.3657],
                            [48.8963,2.3607]
                                ]

folium.Polygon(
    locations=polygon_charbon ,
    color='green',
    weight=1,
    dash_array = '5, 5',
    fill_color='green'
).add_to(m)

folium.map.Marker(
    [48.8968, 2.3651],
    # Utiliser un icon invisible ou très discret, ici un exemple avec une icône simple de taille réduite
    icon=folium.DivIcon(html='<div style="font-size: 10pt; color : black">Chapelle Charbon</div>')
).add_to(m)

# markers fixes

rivp_img = 'C:/Users/louartani/Documents/nc/icon_rivp.png'
rivp_icon = folium.CustomIcon(rivp_img, icon_size=(50, 50))
lab_chapelle_marker = folium.Marker(location=[lab_chapelle[0],lab_chapelle[1]], icon=rivp_icon, popup='Lab Chapelle')
lab_chapelle_marker.add_to(m)
plateau_img = 'C:/Users/louartani/Documents/nc/plateau_icon.png'
plateau_icon = folium.CustomIcon(plateau_img, icon_size=(100, 100))
plateau_urba_marker = folium.Marker(location=[plateau_urba[0],plateau_urba[1]], icon=plateau_icon, popup='Plateau Urba')
plateau_urba_marker.add_to(m)

# groupement de markers
noise_markers = folium.FeatureGroup(name='Niveau sonore')

nc_avant_markers = FeatureGroupSubGroup(noise_markers,name='Données bruit avant janvier 2023')
nc_travaux_markers = FeatureGroupSubGroup(noise_markers,name='Données bruit depuis janvier 2023')

travaux_markers = folium.FeatureGroup(name='Principaux travaux à la Chapelle')

urban_markers = folium.FeatureGroup(name='Urbanisme', show=False)
velib_markers = FeatureGroupSubGroup(urban_markers, 'Stations velib autour de La Chapelle')
fontaine_markers = FeatureGroupSubGroup(urban_markers, 'Fontaines à boire')

culture_markers = folium.FeatureGroup('Culturel', show=False)
events = FeatureGroupSubGroup(culture_markers,'Evenements culturels') # à enlever
biblio = FeatureGroupSubGroup(culture_markers,'Bibliothèques')
theatre = FeatureGroupSubGroup(culture_markers,'Théâtres')

education = folium.FeatureGroup('Education', show=False)
creches_markers = FeatureGroupSubGroup(education,'Crèches')
primaires_markers = FeatureGroupSubGroup(education,'Ecoles élémentaires')
colleges =FeatureGroupSubGroup(education,'Collèges')
lycees = FeatureGroupSubGroup(education,'Lycées')

sante = folium.FeatureGroup('Santé', show=False)
pharma = FeatureGroupSubGroup(sante,'Pharmacies & Parapharmacies')
hopitaux = FeatureGroupSubGroup(sante,'Hôpitaux')
centre_sante = FeatureGroupSubGroup(sante,'Autres centres de santé')

sport_markers = folium.FeatureGroup('Sport', show=False)
gymn = FeatureGroupSubGroup(sport_markers,'Gymnases')
piscines = FeatureGroupSubGroup(sport_markers,'Piscines')
stades =  FeatureGroupSubGroup(sport_markers,'Stades')
association_markers = FeatureGroupSubGroup(sport_markers,'Associations sportives')

commerce = folium.FeatureGroup('Commerces', show=False)
social = folium.FeatureGroup('Social', show=False)

############# DONNEES ######################

### NOISE CAPTURE (BRUIT)

# récupérer les donnnées de noise capture
dossier_courant = os.path.dirname(os.path.abspath(__file__))

# avant les travaux :
avant_files = dossier_courant+'\\lachapelle_202122'
recup_files_nc(avant_files, long_min, lat_min, long_max, lat_max, nc_avant_markers, noise_markers)

# depuis le début des travaux
travaux_files = dossier_courant+'\\lachapelle_202324'
recup_files_nc(travaux_files, long_min, lat_min, long_max, lat_max, nc_travaux_markers, noise_markers)

noise_markers.add_to(m)

# récupérer les données velib
velib_file = 'velib.geojson'
velib_path = dossier_courant+'\\'+velib_file
with open(velib_path) as velibs:
    data_velib = json.load(velibs)
for i in range(len(data_velib["features"])):
    long_velib = data_velib['features'][i]['geometry']['coordinates'][0]
    lat_velib = data_velib['features'][i]['geometry']['coordinates'][1]
    if long_velib >= long_min and long_velib <= long_max and lat_velib >= lat_min and lat_velib <= lat_max:
       folium.Marker(location=[lat_velib,long_velib], icon=folium.Icon(color='black', icon='bicycle', prefix='fa')).add_to(velib_markers)
velib_markers.add_to(urban_markers)


# récupérer les fontaines à boire
# fontaines_file = 'fontaines-a-boire.geojson'
# fontaines_path = dossier_courant+'\\'+fontaines_file
# with open(fontaines_path) as fontaines:
#     data_fontaines = json.load(fontaines)
# for i in range(len(data_fontaines["features"])):
#     long_fontaines = data_fontaines['features'][i]['geometry']['coordinates'][0]
#     lat_fontaines = data_fontaines['features'][i]['geometry']['coordinates'][1]
#     dispo = data_fontaines['features'][i]['properties']['dispo']
#     if long_fontaines >= long_min and long_fontaines <= long_max and lat_fontaines >= lat_min and lat_fontaines <= lat_max:
#           if dispo == "OUI":
#             folium.Marker(location=[lat_fontaines,long_fontaines], icon=folium.Icon(color='blue', icon='droplet', prefix='fa')).add_to(fontaine_markers)
#           else:
#                folium.Marker(location=[lat_fontaines,long_fontaines], icon=folium.Icon(color='red', icon='droplet', prefix='fa')).add_to(fontaine_markers)

# fontaine_markers.add_to(urban_markers)

urban_markers.add_to(m)

# recuperer les données cultures
events_file = 'events.geojson'
events_path = dossier_courant+'\\'+events_file
with open(events_path) as e:
    data_ev = json.load(e)
for i in range(len(data_ev["features"])):
    long_ev = data_ev['features'][i]['geometry']['coordinates'][0]
    lat_ev = data_ev['features'][i]['geometry']['coordinates'][1]
    type_e = data_ev['features'][i]['properties']['title']
    if long_ev >= long_min and long_ev <= long_max and lat_ev >= lat_min and lat_ev <= lat_max:
       folium.Marker(location=[lat_ev,long_ev], icon=folium.Icon(color='pink', icon='masks-theater', prefix='fa'),popup=type_e).add_to(events)
#events.add_to(culture_markers)

culture_markers.add_to(m)

# récupérer les données ecoles
ecoles_file = 'ecoles.geojson'
ecoles_path = dossier_courant+'\\'+ecoles_file
with open(ecoles_path) as ecol:
    data_ecoles = json.load(ecol)
for i in range(len(data_ecoles["features"])):
    long_ecoles = data_ecoles['features'][i]['geometry']['coordinates'][0]
    lat_ecoles = data_ecoles['features'][i]['geometry']['coordinates'][1]
    details = data_ecoles['features'][i]['properties']['libelle']
    if long_ecoles >= long_min and long_ecoles <= long_max and lat_ecoles >= lat_min and lat_ecoles <= lat_max:
       folium.Marker(location=[lat_ecoles,long_ecoles], icon=folium.Icon(color='orange', icon='school', prefix='fa'), popup=details).add_to(primaires_markers)
primaires_markers.add_to(education)

# recupérer les données creches
cr_file = 'creches.json'
cr_path = dossier_courant+'\\'+cr_file
with open(cr_path) as cr:
    data_cr = json.load(cr)
for i in range(len(data_cr["features"])):
    long_cr = data_cr['features'][i]['geometry']['coordinates'][0]
    lat_cr = data_cr['features'][i]['geometry']['coordinates'][1]
    details_cr = data_cr['features'][i]['properties']['libelle']
    if long_cr >= long_min and long_cr <= long_max and lat_cr >= lat_min and lat_cr <= lat_max:
       folium.Marker(location=[lat_cr,long_cr], icon=folium.Icon(color='green', icon='baby', prefix='fa'), popup=details_cr).add_to(creches_markers)
creches_markers.add_to(education)
education.add_to(m)

# recuperer les données sport
capoeira_coord = [48.8951, 2.3652]
capoeira_img = 'C:/Users/louartani/Documents/nc/capoeira.png'
capoeira_icon = folium.CustomIcon(capoeira_img, icon_size=(80, 80))
capoeira_marker = folium.Marker(location=[capoeira_coord[0],capoeira_coord[1]], icon=capoeira_icon, popup='Capoeria Viola')
capoeira_marker.add_to(m)

sport_file = 'sport.json'
sport_path = dossier_courant+'\\'+sport_file
with open(sport_path) as sp:
    sport_data = json.load(sp)
for i in range(len(sport_data)-1):
    if 'equgpsy_x' in sport_data[i]['fields']:
        long_sp = sport_data[i]['fields']['equgpsy_x'][1]
        lat_sp = sport_data[i]['fields']['equgpsy_x'][0]
        details_sp = sport_data[i]['fields']['equnom']
        if long_sp >= long_min and long_sp <= long_max and lat_sp >= lat_min and lat_sp <= lat_max:
            folium.Marker(location=[lat_sp,long_sp], icon=folium.Icon(color='blue', icon='volleyball', prefix='fa'), popup=details_sp).add_to(gymn)
gymn.add_to(sport_markers)


sport_markers.add_to(m)

# récupérer les données santé
labo_file = 'labos.geojson'
labo_path = dossier_courant+'\\'+labo_file
with open(labo_path) as la:
    labo_data = json.load(la)
for i in range(len(labo_data)):
        long_la = labo_data['features'][i]['geometry']['coordinates'][0]
        lat_la = labo_data['features'][i]['geometry']['coordinates'][1]
        details_la = labo_data['features'][i]['properties']['laboratoire']
        #if long_la >= long_min and long_la <= long_max and lat_la >= lat_min and lat_la <= lat_max:
        folium.Marker(location=[lat_la,long_la], icon=folium.Icon(color='purple', icon='medical-house', prefix='fa'), popup=details_la).add_to(centre_sante)
centre_sante.add_to(sante)

# recupérer les données centres de santé
centre_file = 'centres_sante.json'
centre_path = dossier_courant+'\\'+centre_file
with open(centre_path) as ce:
    data_ce = json.load(ce)
for i in range(len(data_ce["features"])):
    long_ce = data_ce['features'][i]['geometry']['coordinates'][0]
    lat_ce = data_ce['features'][i]['geometry']['coordinates'][1]
    details_ce = data_ce['features'][i]['properties']['libelle']
    if long_ce >= long_min and long_ce <= long_max and lat_ce >= lat_min and lat_ce <= lat_max:
       folium.Marker(location=[lat_ce,long_ce], icon=folium.Icon(color='red', icon='heart-pulse', prefix='fa'), popup=details_ce).add_to(centre_sante)
centre_sante.add_to(sante)

sante.add_to(m)

# récupérer les données social
activ18_coord = [48.8950, 2.3656]
activ18_img = 'C:/Users/louartani/Documents/nc/activ18.png'
activ18_icon = folium.CustomIcon(activ18_img, icon_size=(70, 70))
activ18_marker = folium.Marker(location=activ18_coord, icon=activ18_icon, popup='Activ18')
activ18_marker.add_to(m)

# lire le fichier excel pour les associations

file_asso = 'C:/Users/louartani/Documents/nc/associations_1.xlsx'
data_asso = pd.read_excel(file_asso)
for it in range(len(data_asso)):
    long_a=data_asso['longitude'][it]
    lat_a=data_asso['latitude'][it]
    details_it = data_asso['Nom'][it]#+'<br>'+data_asso['Type'][it]
    if long_a >= long_min and long_a <= long_max and lat_a >= lat_min and lat_a <= lat_max:
       folium.Marker(location=[lat_a,long_a], icon=folium.Icon(color='darkblue', icon='people-roof', prefix='fa'), popup=details_it).add_to(social)

social.add_to(m)

# récupérer les coordonnées des travaux pour les mettre dans le groupement de markers travaux
# work_img = 'C:/Users/louartani/Documents/nc/work_icon.png'
# work_icon = folium.CustomIcon(work_img, icon_size=(50, 50))
# travaux_markers = folium.Marker(location=arena, icon=work_icon, popup='Arena')
# travaux_markers.add_to(m)
arena_txt = '<h4>Adidas Arena</h4><img src="arena.jpg" width="200"><p>Lieu de référence des cultures urbaines où fait se rencontrer musique, sport, culture et lifestyle pour tous.</p>'
markers_travaux(arena_txt,arena, travaux_markers,m)
condorcet_txt = '<h4>Campus Condorcet</h4><img src="condorcet.jpg" width="200"><p>Un campus international pour répondre aux défis pédagogiques, scientifiques et numériques du XXIe siècle.</p>'
markers_travaux(condorcet_txt, campus, travaux_markers,m)
charbon_txt = '<h4>Chapelle Charbon</h4><img src="chapelle_charbon.jpg" width="200"><p>Transformation d’un ancien site logistique ferroviaire du 18e arrondissement pour créer un grand parc bordé d’un ensemble résidentiel qui vient achever le quartier Évangile.</p>'
markers_travaux(charbon_txt, chapelle_charbon, travaux_markers,m)
markers_travaux(folium.Popup('Carrefour rue Ordener/Riquet et désamiantage de la rue Marx Dormoy',max_width=400), carrefour, travaux_markers,m)
rue_txt = '<h4>Végétalisation de la rue de la Chapelle</h4><img src="rue.jpg" width="200"><p>Cet axe majeur du quartier va être métamorphosé en une vaste promenade. Aménagement de pistes cyclables, réduction de la place de la voiture, végétalisation, nouvel éclairage public...</p>'
markers_travaux(rue_txt, rue_lachapelle, travaux_markers,m)
rondpoint_txt = folium.Popup('Réhabilitation du rond-point de la Chapelle',max_width=400)
markers_travaux(rondpoint_txt, rondpt_lachapelle, travaux_markers,m)

###################### AJOUT DE LA LEGENDE ET CONTROLE DES LAYERS GROUPS

legend_html = '''
     <div style="
     position: fixed; 
     bottom: 50px; left: 50px; 
     width: 130px; height: 230px; 
     border:2px solid grey; z-index:9999; 
     font-size:14px;
     background-color:white;
     opacity: 0.8;
     ">
     &nbsp; Niveau sonore <br>
     <img class="legend_nc" src="./legend.png" />
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))

# legend_layer = folium.FeatureGroup(name='Légende')
# legend_marker = folium.Marker(location=[0,0], icon=folium.DivIcon(icon_size=(0,0), icon_anchor=(0,0), html=legend_html))
# legend_html.add_to(legend_layer)
# # legend_layer.add_child(folium.Marker(location=[0,0], icon=folium.DivIcon(icon_size=(0,0), icon_anchor=(0,0), html=legend_html)))

# legend_layer.add_to(m)

logos_html = '''
     <div style="
     position: fixed; 
     bottom: 20px; right: 0px; 
     width: 430px; height: 50px;
     padding: 5px;
     border:2px solid grey; z-index:9999; 
     font-size:14px;
     background-color:white;
     opacity: 0.9;
     ">
     <img class="legend_nc" src="./uge_logo.png" style="width:100px"/>
     <img class="legend_nc" src="./Logotype-rouge-bleu.png" style="width:35px"/>
     <img class="legend_nc" src="./logo_paris.png" style="width:30px"/>
     <img class="legend_nc" src="./Logo-RIVP.svg.png" style="width:30px"/>
     <img class="legend_nc" src="./plateau_urbain.png" style="width:60px"/>
     <img class="legend_nc" src="./capoeira_logo.jpg" style="width:30px"/>
     <img class="legend_nc" src="./activ18_logo.png" style="width:50px"/>
     <img class="legend_nc" src="./cropped-la-permanence-choregraphique-2.png" style="width:30px"/>
     </div>
     '''
m.get_root().html.add_child(folium.Element(logos_html))

m.get_root().html.add_child(folium.Element("""
    <script>
    document.addEventListener("DOMContentLoaded", function() {
      document.querySelector(".leaflet-control-layers").classList.add("leaflet-control-layers-expanded");
    });
    </script>
    """))

# coords_popup = folium.LatLngPopup()
# m.add_child(coords_popup)

folium.LayerControl().add_to(m)
#folium.LayerControl(collapsed=False).add_to(m)

plugins.MeasureControl(primary_length_unit='kilometers').add_to(m)

######################### Sauvegarde de la carte en HTML
m.save('C:/Users/louartani/Documents/nc/autour_lachapelle.html')