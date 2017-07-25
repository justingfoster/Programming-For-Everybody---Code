import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = int(input('Enter Count - '))
position = int(input('Enter Position - '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

counts = 0
while counts < count:
    url2 = soup.find_all('a')[(position -1)]["href"]
    html2 = urllib.request.urlopen(url2, context=ctx).read()
    soup = BeautifulSoup(html2, 'html.parser')
    counts = counts + 1
    print(url2)
