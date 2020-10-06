import requests
import datetime
from bs4 import BeautifulSoup

f = open("onlinekhabar.txt", "a")

def updateData(link):
  page_source = requests.get(link).content
  soup = BeautifulSoup(page_source, "html.parser")
  content = soup.find("div", attrs ={"class": "col colspan3 main__read--content ok18-single-post-content-wrap"})
  ps = content.find_all("p")
  for p in ps:
    pText = p.getText()
    if (pText != "" and pText != None):
      f.write(pText)
    f.write("\n")

def scrapeAll():
  links = open("onlinekhabar_links.txt", "r").read().splitlines()
  i = 1
  for link in links:
    updateData(link)
    print(i, " --> Done")
    i += 1

scrapeAll()

