import requests

from bs4 import BeautifulSoup
from googlesearch import search
from requests.compat import urljoin
from urllib.parse import urlencode

def getWikiData(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  infobox = soup.find("table", class_='infobox')
  photo = infobox.find_all("img")
  wikiData = {
    'photo': photo[0]['src']
  }
  return wikiData


def getWebSearchResults(driver, year, race):
  print(driver, year, race)
  searchParams ={ "q": [driver, str(year), race]}
  urlParams = urlencode(searchParams, doseq=True)
  print("url - ", urlParams)

  print("urlString - ", urlString)
  pages = requests.get(urlString).json()
  return pages
