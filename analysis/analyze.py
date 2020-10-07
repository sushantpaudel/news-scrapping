import matplotlib
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

dataset = open("dataset.csv", "r").read()
data = dataset.split(",")
font_path = 'fonts/mangal.ttf'
font = FontProperties(fname=font_path)

def sortSecond(val): 
    return val[1]

def countWords(data=[]):
  return Counter(data)

def start():
  f = open("word_count.csv", "w")
  word_count = countWords(data)
  sortData = []
  for a, b in word_count.items():
    if (a != ""):
      sortData.append([a,b])
  sortData.sort(key=sortSecond, reverse=True)

  # f.write("Word,Count\n")
  for i in range(0, 40):
    f.write(str(sortData[i][0])+ "," + str(sortData[i][1]))
    f.write("\n")
  f.close()

def generateGraph():
  data = open("word_count.csv", "r").read().splitlines()
  sortData = []
  for d in data:
    sortData.append(d.split(","))

  x = []
  y = []
  length = len(sortData) - 1
  for i in range(0, 20):
    x.append(sortData[i][0])
    y.append(sortData[i][1])
    
  x.reverse()
  y.reverse()
  plotData(x, y)

def plotData(x=[], y=[]):
  fig,ax = plt.subplots()
  plt.bar(x=x, height=y)
  for label in ax.get_xticklabels():
    label.set_fontproperties(font)
  plt.title('Term Frequency Graph')
  plt.xlabel("Word")
  plt.ylabel("Count")
  plt.xticks(rotation=90)
  plt.savefig("plot.png")


start()
generateGraph()