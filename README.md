# Stock Data Scrapper using MarketWatch and Yahoo Finance!
### :computer: *Made by rawsashimi1604 (c) 2021* :computer:

Hey everyone! :wave: This project is a stock data scrapper that I made for my own analysis purposes! It uses **Python** to extract financial and technical data from stocks and stores them into a database on your local computer. :smile:

> *For the technical data side, we are using yfinance module that scraps data from Yahoo Finance.*

> *For the financial data side, we are using BeautifulSoup4 to scrap data from MarketWatch.com. Then we organise the data using pandas and export it to a JSON file in our database.*

We then use these 2 components to build a complete stock data database; afterwhich you can use for your own analysis or research purposes. :grin:

*For now I will be adding my own analysis features in periodically into this project.*

## :+1: Contributing

All pull requests are welcome! :upside_down_face: However, changes to the code are not available for now. 

*Do drop me a message if you want to contribute and we can work something out!*

## :calendar: Ongoing Tasks
- [x] Download stock data to database
- [x] Create extraction module to pull data from database (in both data and view format)
- [ ] Create module for usage across different folders
- [ ] Remove selenium dependency from code
- [ ] Add analysis and viewing features
- [ ] Calcuate intrinsic value using Discounted Cash Flow (DCF) model
- [ ] Add specific documentation of different class methods and their usage


## :books: Required modules
- pandas
- numpy
- BeautifulSoup4
- selenium (***needed for installation, but not in use currently. Will remove in a later update***)
- pandas_market_calendars
- pprint
- yfinance

### :question: How to use this module
*Before starting, install the Chromium WebDriver for Google Chrome. Then put the driver into C:\Program Files (x86)\chromedriver.exe*

After that, open a new python file in the folder. Then import the **Downloader** class and the **DBExtract** class.

```python
from DBExtract import DBExtract
from Download import Downloader
```

#### :floppy_disk: *Downloader* class

> The Downloader class is the stock data downloader component. It allows one to download financial data from MarketWatch or technical data from YahooFinance.
```python
# Downloads data for Microsoft Stock, stores it in C:\Users\rawsashimi1604\FinData
d = Downloader()
d.download(type_="string", ticker="MSFT", DB_PATH=r'C:\Users\rawsashimi1604\FinData')
```

#### :electric_plug: *DBExtract* class

> The DBExtract class is the database extraction component. It allows one to pull data from database and display in a string or pandas DataFrame format.
```python
# Extracts IncomeStatement data for Microsoft Stock, from C:\Users\rawsashimi1604\FinData
extract = DBExtract(DB_PATH=r'C:\Users\rawsashimi1604\FinData')
df = extract.json_extract("view", ticker="MSFT", FILE_NAME="IncomeStatement") # returns pandas DataFrame
```

