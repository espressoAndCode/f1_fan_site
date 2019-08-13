import requests, os
from bs4 import BeautifulSoup
from googlesearch import search
from requests.compat import urljoin
from urllib.parse import urlencode

seId = os.environ.get('SEARCH_ENGINE_ID')
seKey = os.environ.get('CUSTOM_SEARCH_API_KEY')

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
  searchParams ={ "q": [driver, str(year), race]}
  urlParams = urlencode(searchParams, doseq=True)
  urlString = f'https://www.googleapis.com/customsearch/v1?q={urlParams}&cx={seId}&lr=lang_en&key={seKey}'
  pages = requests.get(urlString).json()
  return pages

def getFrontPageResults():
  searchParams ={ "q": "formula 1 today"}
  urlParams = urlencode(searchParams)
  urlString = f'https://www.googleapis.com/customsearch/v1?q={urlParams}&cx={seId}&lr=lang_en&key={seKey}'
  pages = requests.get(urlString).json()
  return pages
