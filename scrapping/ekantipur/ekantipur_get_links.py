import requests
import datetime
from bs4 import BeautifulSoup

global month
global date
global f
global arr
f = open("ekantipur_links.txt", "a")
month = 4
date = 1
arr = []
while (month < 10):
  while (date <= 31):
    try:
      datestring = datetime.datetime(2020, month, date).date().__format__("%Y/%m/%d")
      html_string = requests.get("http://www.ekantipur.com/business/" + datestring).content
      soup = BeautifulSoup(html_string, "html.parser")
      articles = soup.find_all("article")
      for article in articles:
        link = article.find("h2")
        a = link.find("a")
        if (a != None):
          href = str(a['href'])
          arr.append(href)
      date += 1   
    except:
      date = 32
  print(month)
  date = 1 
  month += 1


arr = list(dict.fromkeys(arr))
for href in arr:
  f.write(href)
  f.write("\n")
# dates = soup.find_all("div", attrs = {"class": "date cat_date"}) # This is the date of the article
# links = soup.find_all("h2")  # This is the Links to the main article of the news
