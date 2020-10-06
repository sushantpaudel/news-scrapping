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
driver.get("http://annapurnapost.com/economy")

while (True):
  more_buttons = driver.find_elements_by_class_name("btn-transparent")
  if (len(more_buttons) > 0):
    driver.execute_script("arguments[0].click();", more_buttons[0])

  isLast = False
  try:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    dateStamps = soup.find_all("small")
    lastStamp = dateStamps[len(dateStamps) - 4]
    print(lastStamp)
    if "चैत २०७६" in lastStamp.getText():
      isLast = True
    else:
      isLast = False
  except:
    print("Index out of range")

  if (isLast):
    break
  time.sleep(1)

def getData(pageSource):
  f = open("annapurnapost_links.txt", "w")
  soup = BeautifulSoup(pageSource, "html.parser")
  articles = soup.find_all("div", attrs = {"class": "media-right"})
  for article in articles:
    link = article.find("h1")
    a = link.find("a")
    if (a != None):
      href = str(a['href'])
      f.write(href)
      f.write("\n")

getData(page_source)