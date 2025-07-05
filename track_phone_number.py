import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests


number = "+8801721650560"
url = "http://ip-api.com/json/"
data = requests.get(url).json()

if data['status'] == 'fail':
    print("Failed to retrieve location data.")


call_number = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(call_number, "en")
service_provider = carrier.name_for_number(call_number, "en")
time_zone = timezone.time_zones_for_number(call_number)

print(f"Location: {location}")
print(f"Service Provider: {service_provider}")
print(f"Time Zone: {time_zone}")
print(f"Your IP Location: {data['country']}, {data['regionName']}, {data['city']}")