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
f = open("ekantipur.txt", "a")

def updateData(link):
  print(link)
  driver.get(link)
  more_buttons = driver.find_elements_by_class_name("icon-close")
  driver.execute_script("arguments[0].click();", more_buttons[0])
  time.sleep(1)
  page_source = driver.page_source
  soup = BeautifulSoup(page_source, "html.parser")
  content = soup.find("div", attrs ={"class": "description portrait"})
  ps = content.find_all("p")
  for p in ps:
    pText = p.getText()
    if (pText != "" and pText != None):
      f.write(pText)
    f.write("\n")
# dates = soup.find_all("div", attrs = {"class": "date cat_date"}) # This is the date of the article
# links = soup.find_all("h2")  # This is the Links to the main article of the news

def scrapeAll():
  links = open("ekantipur_links.txt", "r").read().splitlines()
  i = 1
  for link in links:
    print(i, " --> Done")
    href = "https://www.ekantipur.com" + link
    updateData(href)
    i += 1

scrapeAll()

