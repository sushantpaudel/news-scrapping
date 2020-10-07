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
f = open("nagariknews.txt", "a")

def updateData(link):
  driver.get(link)
  more_buttons = driver.find_elements_by_class_name("close")
  driver.execute_script("arguments[0].click();", more_buttons[0])
  time.sleep(1)
  page_source = driver.page_source
  soup = BeautifulSoup(page_source, "html.parser")
  content = soup.find("article")
  ps = content.find_all("p")
  for p in ps:
    pText = p.getText()
    if (pText != "" and pText != None):
      f.write(pText)
    f.write("\n")

def scrapeAll():
  links = open("nagariknews_links.txt", "r").read().splitlines()
  for i in range(1289, len(links)):
    href = "https://nagariknews.nagariknetwork.com" + links[i]
    updateData(href)
    print(i, " --> Done")
    i += 1

scrapeAll()
# updateData("https://nagariknews.nagariknetwork.com/economy/351981-1601719910.html")


