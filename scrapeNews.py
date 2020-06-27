# Example search https://news.google.com/search?q=CNN&hl=en-US&gl=US&ceid=US:en

# Classes:
# Article
# Title and link are in this: ipQwMb ekueJc gEATFF RD0gLb
# Link in this: VDXfz
# Beginning of article: xBbh9
# Square image: tvs3Id QwxBBf
# Publisher: wEwyrc AVN2gc uQIVzc Sksgp
# Time (in a datetime element): WW6dff uQIVzc Sksgp

import requests
from bs4 import BeautifulSoup
import lxml
from bs4 import SoupStrainer
from dateutil import parser
import json
import random
import binascii
import os

URL = 'https://news.google.com/search?q=CNN&hl=en-US&gl=US&ceid=US:en'
page = requests.get(URL)

newId = str(binascii.b2a_hex(os.urandom(30)))
newId = newId.strip("b'")
newId = newId.strip("'")
filename = str(newId) + '.json'
data = {}
data['articles'] = []

soup = BeautifulSoup(page.text, 'lxml')
articles = soup.find_all('div', class_='NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc')
data['articles'] = []
for article in articles:
    # print(title, '\n\n\n\n')
    title_elem = article.find('h3', class_='ipQwMb ekueJc gEATFF RD0gLb')
    article_link = article.find('a', class_='DY5T1d')
    article_snippet = article.find('span', class_='xBbh9')
    image_url = article.find('img', class_='tvs3Id QwxBBf')
    publisher = article.find('a', class_='wEwyrc AVN2gc uQIVzc Sksgp')
    time = article.find('time', class_='WW6dff uQIVzc Sksgp')

    url = article_link['href'].replace('./', 'https://news.google.com/', 1)

    data['articles'].append({
        "source": publisher.text, 
        "title": title_elem.text, 
        "articlePreview": article_snippet.text, 
        "url": url, 
        "urlToImage": image_url['src'], 
        "timePublished": time['datetime']})
with open(filename, "w") as outfile:
    json.dump(data, outfile)
