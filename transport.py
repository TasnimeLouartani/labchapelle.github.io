import folium


m = folium.Map(location=[48.8983, 2.3639], zoom_start=17)
folium.TileLayer('CartoDB positron',attr='CartoDB positron',name='Neutre').add_to(m)

lab_chapelle = [48.89674636731587, 2.357115558565473]
metro = [48.89806051272368, 2.358928177599751]
bus = [48.89751231933662, 2.3590163888968663]
tram = [48.898343073655695, 2.3584565871161454]
b_302 = [48.89850297138475, 2.3584697346255656]
b38 = [48.89688702646572, 2.3593629346219642]

folium.map.Marker(
    lab_chapelle,
    icon=folium.Icon(color='red', icon='circle', prefix='fa')
    # Utiliser un icon invisible ou très discret, ici un exemple avec une icône simple de taille réduite
).add_to(m)

metro_img = 'C:/Users/louartani/Documents/nc/m12.png'
metro_icon = folium.CustomIcon(metro_img, icon_size=(80, 80))
metro_marker = folium.Marker(location=metro, icon=metro_icon).add_to(m)

bus_img = 'C:/Users/louartani/Documents/nc/bus_60.png'
bus_icon = folium.CustomIcon(bus_img, icon_size=(60, 60))
bus_marker = folium.Marker(location=bus, icon=bus_icon).add_to(m)

t_img = 'C:/Users/louartani/Documents/nc/t3b.png'
t_icon = folium.CustomIcon(t_img, icon_size=(30, 30))
t_marker = folium.Marker(location=tram, icon=t_icon).add_to(m)

b_img = 'C:/Users/louartani/Documents/nc/b302.png'
b_icon = folium.CustomIcon(b_img, icon_size=(60, 60))
b_marker = folium.Marker(location=b_302, icon=b_icon).add_to(m)

b38_img = 'C:/Users/louartani/Documents/nc/b38.png'
b38_icon = folium.CustomIcon(b38_img, icon_size=(60, 60))
b38_marker = folium.Marker(location=b38, icon=b38_icon).add_to(m)

m.save('C:/Users/louartani/Documents/nc/autre_carte.html')