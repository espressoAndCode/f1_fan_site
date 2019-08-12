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
  urlString = 'https://www.googleapis.com/customsearch/v1?q=' + urlParams + '&cx=016700597778999691736:clhkunuoizk&lr=lang_en&key=AIzaSyDIKEbCJ5dihD-1HoGFYo2eI-WaFtVhtD8'
  print("urlString - ", urlString)
  pages = requests.get(urlString).json()
  return pages


# CUSTOM_SEARCH_API_KEY='AIzaSyDIKEbCJ5dihD-1HoGFYo2eI-WaFtVhtD8'
# SEARCH_ENGINE_ID='016700597778999691736:clhkunuoizk'
