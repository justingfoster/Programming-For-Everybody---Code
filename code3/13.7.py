import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) <1: break

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})

    openurl = urllib.request.urlopen(url)
    data = openurl.read().decode()

    print(url)
    js = json.loads(str(data))

    #print(json.dumps(js, indent = 4))

    print(js['results'][0]['place_id'])
