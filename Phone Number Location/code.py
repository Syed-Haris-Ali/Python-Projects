# By Codred Tech
import phonenumbers
# geocoder: to know the specific
# location to that phone number
from phonenumbers import geocoder

# Pakistani phone number example: +92***********
phone_number = phonenumbers.parse("+92**********")


# this will print the countrry name
print(geocoder.description_for_number(phone_number, 'en'))
