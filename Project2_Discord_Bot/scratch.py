from flashgeotext.geotext import GeoText

geotext = GeoText()

content = input().title()

places = geotext.extract(input_text=content)
print(places['cities'])
if places['cities'] == {}:
    print("NONE")