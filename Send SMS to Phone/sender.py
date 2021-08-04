# import required module
import requests
import json
# mention URL
url = "https://www.fast2 sms.com/dev/bulk"
# create a dictionary
my_data = {
    # Your Sender ID
    'sender_id': 'TXTIND',  # FSTSMS is default sender ID
    # PUT YOUR MESSAGE HERE
    'message': 'This is a test message From Syed Haris Ali',
    'language': 'english',
    'route': 'p',
    # YOU CAN SEND SMS TO MULTIPLE NUMBERS
    # SEPARATED BY COMMA
    # e.g=> #'numbers': '9999999, 77777777, 66666666'
    'numbers': '03**********'}
# CREATE A DICTIONARY
headers = {
    "authorization": "YOUR API KEY HERE",
    "Content-Type": "application/x-www-form-urlencoded",
    'Cache=Control': "no-cache"
}
# MAKE A POST REQUEST
response = requests.request("POST", url, data=my_data, headers=headers)
# LOAD JSON DATA FROM SOURCE
returned_msg = json. loads(response. text)
# print THE SEND MSG
print(returned_msg['message'])
