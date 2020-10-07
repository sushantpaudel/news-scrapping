import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
global f
global page_source
driver.get("https://nagariknews.nagariknetwork.com/economy")

while (True):
  more_buttons = driver.find_elements_by_class_name("morelink")
  if (len(more_buttons) > 0):
    driver.execute_script("arguments[0].click();", more_buttons[0])

  isLast = True
  try:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    dateStamps = soup.find_all("time")
    lastStamp = dateStamps[len(dateStamps) - 2].getText()
    print(lastStamp)
    if "फाल्गुन २०७६" in lastStamp:
      isLast = True
    else:
      isLast = False
  except:
    print("Index out of range")

  if (isLast):
    break
  time.sleep(1)

def getData(pageSource):
  f = open("nagariknews_links.txt", "w")
  soup = BeautifulSoup(pageSource, "html.parser")
  articles = soup.find_all("div", attrs = {"class": "text"})
  for article in articles:
    link = article.find("h1")
    a = link.find("a")
    if (a != None):
      href = str(a['href'])
      f.write(href)
      f.write("\n")

getData(page_source)