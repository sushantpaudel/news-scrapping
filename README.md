# News Scrapping

This is a collection of simple `python` scripts that uses **`selenium`** and **`beautifulsoap`** to scrape data from `Nepali News Portals`.

> Scrapping from news portals was quite challenging because of the placing of many advertisements, the difference in the interface and the tags of each news portal. One of the main problem I faced was scrapping links for the infinite scroll pages which was sorted by the use selenium.

## Prerequisities

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Selenium](https://pypi.org/project/selenium/)
- [Chrome Driver for Selenium](http://chromedriver.chromium.org/getting-started)
- [Matplotlib](https://pypi.org/project/matplotlib/)

## Analysis

1. First, go to the scrapping directory

```sh
cd scrapping
```

2. Then, you have to run `ready.sh` commands on linux. If your PC is windows then you can do it manually, similar to the script.

```sh
./ready.sh
```

3. After that you can go to the analysis directory to analyse the data

```sh
cd ../analysis
```

4. Then, you can execute `create_csv.py` using following command, should work on both linux and windows:

```sh
python3 create_csv.py
```

> As you might have notices I've used `python3` because I am using Python3 to run these scripts. I have not checked with Python2.7 so it would be better if you'd also use Python3.

5. After creating the CSV dataset you can run `analyze.py` to generate the graph and term frequency graph for this dataset.

```sh
python3 analyze.py
```

## Workflow

1. Extract string from the content of different news portal ranging from different dates. `In this case I've extracted data from around January 2020 to Oct 2020`
2. Copy the data from extracted folder for analysis.
3. Generate CSV by removing all the `stopwords` and some `invalid words` you encountered during extraction.
4. Use `matlplotlib` and few lines of code to generate **`term frequency`** graph for the dataset for 20 words

## Again! Welcome to my Github !!!

Thank you for the support!

#### Give a 🌟 if you like it

I have listed all the references I have gone through to write these scripts.

#### Programming is fun! You get to learn new stuffs.

All the best for whatever you are doing.

### References

- [Web scraping with Python & BeautifulSoup](https://towardsdatascience.com/web-scraping-with-python-beautifulsoup-40d2ce4b6252)
- [In 10 minutes: Web Scraping with Beautiful Soup and Selenium for Data Professionals](https://towardsdatascience.com/in-10-minutes-web-scraping-with-beautiful-soup-and-selenium-for-data-professionals-8de169d36319?gi=a344c652fa92)
- [Web Scraping using Beautiful Soup and Selenium for dynamic page](https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25 "Web Scraping using Beautiful Soup and Selenium for dynamic page")
- [Link clicking during scrapping](https://stackoverflow.com/a/23679526)
- [Matplotlib Bar | Creating Bar Charts Using Bar Function](https://www.pythonpool.com/matplotlib-bar/)
- [TF(Term Frequency)-IDF(Inverse Document Frequency) from scratch in python](https://towardsdatascience.com/tf-term-frequency-idf-inverse-document-frequency-from-scratch-in-python-6c2b61b78558)
