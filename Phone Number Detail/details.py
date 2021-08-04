import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from phonenumbers import phonenumber

phoneNumber = phonenumbers.parse("+923182670238")

timeZone = timezone.time_zones_for_number(phoneNumber)

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)
