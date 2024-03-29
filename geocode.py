from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="http")

# lire le fichier excel

data = 'C:/Users/louartani/Documents/nc/associations.xlsx'

file = pd.read_excel(data)
file['longitude']=1.0
file['latitude']=2.0

for i in range(len(file)):
    # faire le géocodage de l'adresse file['Adresse'][i]
    adresse = file['Adresse'][i]
    location = geolocator.geocode(adresse)
    file['longitude'][i]=location.longitude
    file['latitude'][i]=location.latitude

file.to_excel('C:/Users/louartani/Documents/nc/associations_1.xlsx', index=False)


# location = geolocator.geocode("175 5th Avenue NYC")

# print(location.address)
# print((location.latitude, location.longitude))

# from geopy.geocoders import Nominatim

# # Adresse à géocoder
# address = "1600 Amphitheatre Parkway, Mountain View, CA"

# # Effectuez la recherche de géocodage
# location = geolocator.geocode(address)

# # Affichez les résultats
# if location:
#     print("Adresse:", address)
#     print("Latitude:", location.latitude)
#     print("Longitude:", location.longitude)
# else:
#     print("L'adresse n'a pas pu être géocodée.")
