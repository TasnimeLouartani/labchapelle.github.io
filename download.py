# -------------------------------------------
# Author : Nicolas Fortin, 2019
# noise-planet.org / umrae.fr
# UMRAE, Univ Gustave Eiffel, IFSTTAR, CEREMA, Bouguenais, France
# Licence GPLv3
# If you use/improve this code, please feel free to share your comments and results with us.
# Contact contact@noise-planet.org
# -------------------------------------------

import requests
import os

lines = open("C:/Users/louartani/Documents/nc/lachapelle_202324/query.csv", "r").readlines()
for line in lines[1:]:
    url = line.split(",")[1][:-1]
    filename = "C:\\Users\\louartani\\Documents\\nc\\lachapelle_202324"+ os.sep + url[url.rfind("/") + 1:]
    open(filename,"wb").write(requests.get(url).content)

