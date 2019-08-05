import requests
from bs4 import BeautifulSoup
from googlesearch import search


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
  # searchParams = "'formula 1' +'"+driver+"' '"+ str(year) +"' '"+race+"'"
  searchParams = 'Ayrton Senna, 1992, Monaco Grand Prix'

  print("Search params - ", searchParams)
  results = []
  for url in search(searchParams, stop=20):
    # results.append(url)
    print(url)
    return results
