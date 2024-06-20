import phonenumbers
from phonenumbers import timezone,geocoder,carrier
import opencage,folium
phone_number = input('Type your phone number: ')
phone = phonenumbers.parse(phone_number) 
time = timezone.time_zones_for_number(phone)
cr = carrier.name_for_number(phone,'en')
reg = geocoder.description_for_number(phone,'en')
print(phone_number,phone,time,cr,reg)

from opencage.geocoder import OpenCageGeocode
key = 'a777a3e478c14609a713e6ef62e0758d'
geo = OpenCageGeocode(key)
query = str(reg)
results = geo.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
# print(lat,lng)
mymap = folium.Map(location=[lat,lng], zoom_start = 9)
folium.Marker([lat,lng],popup = reg).add_to(mymap)
mymap.save('mylocation.html')