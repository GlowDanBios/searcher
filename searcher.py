from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('mongodb+srv://hhsl:As123456@mempedia-ptiit.mongodb.net/test?retryWrites=true')
with client:
    db = client.sites
    sites = (db.indexes.find())
    urls = (db.urls.find())


def robot(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    text = soup.get_text()
    db.indexes.insert_one({'link': url, 'text': text})
    links = soup.find_all('a', href=True)
    for link in links:
        link = link['href']
        if str(link)[0] != '/' and str(link)[0] != '#':
            print(link)
            try:
                if link not in lurls:
                    if requests.head(link).headers['content-type'] != 'text/html; charset=UTF-8':
                        db.urls.insert_one({'link': link})
            except:
                    db.urls.insert_one({'link': link})


i = 202
while True:
    with client:
        db = client.sites
        sites = (db.indexes.find())
        lurls = list(db.urls.find())
    robot(lurls[i]['link'])
    i += 1

