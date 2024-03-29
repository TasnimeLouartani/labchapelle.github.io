import folium

lachapelle_nord = [48.8983, 2.3639]

m = folium.Map(location=lachapelle_nord, zoom_start=16.5)

folium.TileLayer('CartoDB positron',attr='CartoDB positron',name='Neutre').add_to(m)

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



m.save('C:/Users/louartani/Documents/nc/plan_situation.html')