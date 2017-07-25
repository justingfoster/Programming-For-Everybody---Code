import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL - ')
data = urllib.request.urlopen(url).read()
print('Retreiving', url)
print('Retreived', len(data), 'characters')

clean = ET.fromstring(data)
counts = clean.findall('.//count')
print('Count:', len(counts))

sum = 0
for number in counts:
    number = int(number.text)
    sum = sum + number
print(sum)
