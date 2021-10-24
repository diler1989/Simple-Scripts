#!/usr/bin/python3

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://...' #add valid url
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web = urlopen(req).read()
soup = BeautifulSoup(web, 'html.parser')

for a in soup.findAll('span', {'class' : 'dz kp hw fq jy b dj kq kr s ks'}): #adjust html tags from source
    print (a.text.strip())

