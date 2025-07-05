import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

number = "+8801797703787"

call_number = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(call_number, "en")
print(f"Location: {location}")


service_provider = carrier.name_for_number(call_number, "en")
print(f"Service Provider: {service_provider}")

key = "9507e995af80400491e69d7325ce5a84"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("location_map.html")