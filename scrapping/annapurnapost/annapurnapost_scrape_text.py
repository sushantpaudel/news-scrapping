import requests
import datetime
from bs4 import BeautifulSoup

global f
f = open("annapurnapost.txt", "a")
def updateData(link):
  page_source = requests.get(link).content
  soup = BeautifulSoup(page_source, "html.parser")
  content = soup.find("p", attrs ={"class": "drop-cap change-font"})
  try:
    pText = content.getText()
    f.write(pText)
    f.write("\n")
  except:
    print(content)

def scrapeAll():
  links = open("annapurnapost_links.txt", "r").read().splitlines()
  for i in range(58, len(links)):
    href = "http://annapurnapost.com" + links[i]
    updateData(href)
    print(i, " --> Done")
    i += 1

scrapeAll()
# updateData("http://annapurnapost.com/news/164885")


