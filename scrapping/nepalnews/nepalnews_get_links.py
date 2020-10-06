import requests
import datetime
from bs4 import BeautifulSoup

global f
global arr
f = open("nepalnews_links.txt", "a")
arr = []
pageCount = 460
while (pageCount >= 0):
  html_string = requests.get("https://www.nepalnews.com/economy?start=" + str(pageCount)).content
  soup = BeautifulSoup(html_string, "html.parser")
  links = soup.find_all("a", attrs={"class": "uk-h3"})
  for a in links:
    if (a != None):
      href = str(a['href'])
      f.write(href)
      f.write("\n")
  pageCount -= 20


# arr = list(dict.fromkeys(arr))
# for href in arr:
#   f.write(href)
#   f.write("\n")
# dates = soup.find_all("div", attrs = {"class": "date cat_date"}) # This is the date of the article
# links = soup.find_all("h2")  # This is the Links to the main article of the news
