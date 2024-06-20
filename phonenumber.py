import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phone_number = input('Type your phone number: ')
phone = phonenumbers.parse(phone_number) 
location = geocoder.description_for_number(phone,'en')
num_carrier = carrier.name_for_number(phone,'en')
time = timezone.time_zones_for_geographical_number(phone)
print(f'Location: {location}')
print(f'Company: {num_carrier}')
print(f'Time Zone: {time}')
