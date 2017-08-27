"""simple test of folium on fredericton points of interest map"""
import csv
import folium

MAP = folium.Map(location=[45.9636, -66.6431])

with open('data/poi.csv', 'r') as csvfile:
    READER = csv.reader(csvfile)
    KEYS = READER.__next__()
    for values in READER:

        mark = dict(zip(KEYS, values))
        folium.Marker([mark['Latitude'], mark['Longitude']],
                      popup=mark['Facility']).add_to(MAP)

MAP.save('poi_map.html')
