import requests
import datetime
from bs4 import BeautifulSoup

f = open("nepalnews.txt", "w")

def updateData(link):
  page_source = requests.get(link).content
  soup = BeautifulSoup(page_source, "html.parser")
  content = soup.find("div", attrs ={"class": "cnc-article-content uk-text-lead"})
  ps = content.find_all("p")
  for p in ps:
    pText = p.getText()
    if (pText != "" and pText != None):
      f.write(pText)
    f.write("\n")

def scrapeAll():
  links = open("nepalnews_links.txt", "r").read().splitlines()
  i = 1
  for link in links:
    print(i, " --> Done")
    href = "https://www.nepalnews.com" + link
    updateData(href)
    i += 1

scrapeAll()

