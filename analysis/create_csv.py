import os
import re

stopwords = open("stopwords.txt", "r").read().splitlines()
invalidWords = ["।","\n","।&nbsp;", "।\n", ]

def getWord(w):
  word = w.strip()
  for sub in ["\n", "।", "?","’"]:
    word = word.replace(sub, "")
  isValid = True
  for stopW in stopwords:
    if (word == stopW):
      isValid = False
      break

  for invalidW in invalidWords:
    if (word == invalidW):
      isValid = False
      break

  if (word == ""):
    isValid = False

  if (isValid):
    return word
  else:
    return None

def getCSVArr(string):
  csv = []
  string=string.lower()
  # Whenever we encounter a space, break the string
  string=string.split(" ")
  # Initializing a dictionary to store the frequency of words
  for w in string:
    word = getWord(w)
    if(word != None):
      csv.append(word)
  return csv

def getCSV(string):
  arr = getCSVArr(string)
  csv = ",".join(str(x) for x in arr)
  return csv

def createCsv():
  try:
    os.remove("dataset.csv")
  except:
    print("No data file! Proceeding...")

  for a, b, files in os.walk("data"):
    for item in files:
      f = open("data/" + item, "r").read()
      data = getCSV(f)
      open("dataset.csv", "a").write(data +",")

createCsv()
# print(getWord("किलो,बजारमा,मूल्यमा,मासु,बिक्री,भईरहेको,।\nकिन,बढ्यो,मूल्य,?\nराष्ट्रिय,कुखुरा,व्यवसायी,संघले,ब"))