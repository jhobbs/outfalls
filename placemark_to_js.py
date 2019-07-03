#!/usr/bin/env python3


import xml.etree.ElementTree as ET
import json

tree = ET.parse('doc.kml')
root = tree.getroot()

placemarks = root.findall('.//Folder/Placemark')

placemark_data = []

for i, placemark in enumerate(placemarks):
    data = {
        'title': placemark.find('name').text,
    }
    coordinates = placemark.find('Point/coordinates').text
    lng, lat, _ = coordinates.split(',')
    position = {
        'lng': float(lng),
        'lat': float(lat),
    }
    data['position'] = position
    placemark_data.append(data)

print("var wwtps = ")
print(json.dumps(placemark_data, sort_keys=True, indent=2))
