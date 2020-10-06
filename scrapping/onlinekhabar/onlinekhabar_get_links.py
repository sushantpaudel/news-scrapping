import requests
import datetime
from bs4 import BeautifulSoup

def scrape(link, lastPage = 1):
  page = 1
  arr = []
  while(page <= lastPage):
    html_string = requests.get(link + str(page)).content
    soup = BeautifulSoup(html_string, "html.parser")
    links = soup.find_all("a", attrs = {"class": "title__regular"})
    for a in links:
      href = str(a['href'])
      arr.append(href)
    page += 1
  saveLinks(arr)

def saveLinks(arr):
  arr2 = list(dict.fromkeys(arr))
  f = open("onlinekhabar_links.txt", "a")
  for href in arr2:
    f.write(href)
    f.write("\n")

# scrape("https://www.onlinekhabar.com/content/market/page/")
# scrape("https://www.onlinekhabar.com/content/bank-main/page/",13)
# scrape("https://www.onlinekhabar.com/content/technology/page/", 18)
# scrape("https://www.onlinekhabar.com/content/rojgar/page/", 8)
# scrape("https://www.onlinekhabar.com/content/tourism/page/", 20)