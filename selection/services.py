import requests
from bs4 import BeautifulSoup

def getWikiData(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  infobox = soup.find("table", class_='infobox')
  photo = infobox.find_all("img")

  print("Soup - ", photo[0]['src'])
  wikiData = {
    'photo': photo[0]['src']
  }
  return wikiData
