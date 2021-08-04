# Get HTML CODE OF ANY WEBSITE
import requests

url = 'https://www.google.com' # Your URL Here

# In CASE YOU NEED A SESSION
#CD = {'SESSION': '123...'}
#r = request.get(url,Cookies=cd)

# or without a session:

r = requests.get(url)
print(r.content)
