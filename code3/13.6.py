import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')

openurl = urllib.request.urlopen(url)
data = openurl.read().decode()

total = 0
info = json.loads(data)

for name in info["comments"]:
    add = int(name['count'])
    total = total + add
print(total)


#    sum = sum + number
#print(sum)
