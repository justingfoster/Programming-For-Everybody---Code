import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://stores.advanceautoparts.com/index.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Find all state URLs
tags = soup.find_all('a', class_='c-directory-list-content-item-link')
count = 0

while count <48:
    for tag in tags:
        url2 = 'https://stores.advanceautoparts.com/' + soup.find_all('a', class_='c-directory-list-content-item-link')[count]["href"]
        count = count + 1
        print(url2)
        #html2 = urllib.request.urlopen(url2, context=ctx).read()
        #soup = BeautifulSoup(html2, 'html.parser')
        #print(soup)



#    print(tag.get('href', None))
