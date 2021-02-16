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

### :question: How to use this module / Examples
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

### :open_file_folder: Documentation
#### *Downloader* class
- method *downloader.download*
```python
download(type_, Driver_PATH='C:\Program Files (x86)\chromedriver.exe', DB_PATH=None, max=None, ticker=None, list_=None, csv=None, buffer=5, download="ALL")
```
> *Downloads data from MarketWatch and YahooFinance.*
- Parameters are:
  - type_ : *str*
    - Specifies which tickers to download. Available parameters are:
      - *"string"* - downloads single ticker
      - *"list"* - downloads list of tickers
      - *"csv"* - downloads list of tickers from csv
  - Driver_PATH : *str*
    - Directory path of Chorimum WebDriver. Default is *'C:\Program Files (x86)\chromedriver.exe'* *(Optional)*
  - DB_PATH : *str*
    - Directory path to store downloaded files in. Also known as the database path. Default is *None* *(Optional)*
  - max : *int*
    - Limit number of tickers to download at once. Default is *None* *(Optional)*
  - ticker : *str*
    - Specifies which ticker to download when using type_ = *"string"*. Default is *None* *(Optional)*
  - list_ : *list*
    - Specifies list of tickers to download when using type_ = *"list"*. Default is *None* *(Optional)*
  - csv : *str*
    - Specifies directory of CSV file. Downloads list of tickers to download from csv when using type_ = *"csv"*. Make sure that ticker symbols are available and under a column called "Ticker" Default is *None* *(Optional)*
  - buffer : *int*
    - Specifies buffer time in seconds in between each download. Default is *5* *(Optional)*
  - download : *str*
    - Specifies what data to download. Available parameters are:
      - *"ALL"* - download all data available
      - *"PRICE"* - download price data
      - *"MAIN"* - download stock information and key data
      - *"PROFILE"* - download stock profile data
      - *"INCOME"* - download income statement
      - *"BALANCE"* - download balance sheet
      - *"CASHFLOW"* - download cash flow statement
      - ~*"FISCALYEAR"* - download fiscal year information~
