# Stock Data Scrapper using MarketWatch and Yahoo Finance!
*Made by rawsashimi1604*

## :scroll: Table of Contents
- [Stock Data Scrapper using MarketWatch and Yahoo Finance!](#stock-data-scrapper-using-marketwatch-and-yahoo-finance-)
    + [:chart_with_upwards_trend: Introduction](#chart-with-upwards-trend--introduction)
    + [:+1: Contributing](#--1--contributing)
    + [:calendar: Ongoing Tasks](#calendar--ongoing-tasks)
    + [:books: Required modules](#books--required-modules)
    + [:question: How to use this module / Examples](#question--how-to-use-this-module---examples)
      - [:floppy_disk: *Downloader* class](#floppy-disk---downloader--class)
      - [:electric_plug: *DBExtract* class](#electric-plug---dbextract--class)
    + [:open_file_folder: Documentation](#open-file-folder--documentation)
      - [***Downloader*** class](#---downloader----class)
        * [*method* **Downloader**.*download*](#-method----downloader---download-)
      - [***DBExtract***(*Fin_Extract*) class](#---dbextract-----fin-extract---class)
        * [*method* **DBExtract**.*json_extract*](#-method----dbextract---json-extract-)
      - [***Fin_Extract***(*Fin_Select*) class](#---fin-extract-----fin-select---class)
        * [*method* **Fin_Extract**.*determine_symbol*](#-method----fin-extract---determine-symbol-)
        * [*method* **Fin_Extract**.*str_to_val*](#-method----fin-extract---str-to-val-)
        * [*method* **Fin_Extract**.*extract*](#-method----fin-extract---extract-)
        * [*method* **Fin_Extract**.*extract_columns*](#-method----fin-extract---extract-columns-)
      - [***Fin_Select*** class](#---fin-select----class)
        * [*method* **Fin_Select**.*select_isolate*](#-method----fin-select---select-isolate-)
        * [*method* **Fin_Select**.*select_item*](#-method----fin-select---select-item-)
        * [*method* **Fin_Select**.*select_year*](#-method----fin-select---select-year-)

### :chart_with_upwards_trend: Introduction

Hey everyone! :wave: This project is a stock data scrapper that I made for my own analysis purposes! It uses **Python** to extract financial and technical data from stocks and stores them into a database on your local computer. :smile:

> *For the technical data side, we are using yfinance module that scraps data from Yahoo Finance.*

> *For the financial data side, we are using BeautifulSoup4 to scrap data from MarketWatch.com. Then we organise the data using pandas and export it to a JSON file in our database.*

We then use these 2 components to build a complete stock data database; afterwhich you can use for your own analysis or research purposes. :grin:

*For now I will be adding my own analysis features in periodically into this project.*

### :+1: Contributing

All pull requests are welcome! :upside_down_face: However, changes to the code are not available for now. 

*Do drop me a message if you want to contribute and we can work something out!*

### :calendar: Ongoing Tasks
- [x] Download stock data to database
- [x] Create extraction module to pull data from database (in both data and view format)
- [ ] Create module for usage across different folders
- [ ] Remove selenium dependency from code
- [ ] Add analysis and viewing features
- [ ] Calcuate intrinsic value using Discounted Cash Flow (DCF) model
- [ ] Add specific documentation of different class methods and their usage
- [ ] Add table of contents for README.md to navigate through documentation easily


### :books: Required modules
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
#### ***Downloader*** class
> The Downloader class is the stock data downloader component. It allows one to download financial data from MarketWatch or technical data from YahooFinance.
##### *method* **Downloader**.*download*
```python
download(type_, Driver_PATH='C:\Program Files (x86)\chromedriver.exe', DB_PATH=None, max=None, ticker=None, list_=None, csv=None, buffer=5, download="ALL")
```
> *Downloads data from MarketWatch and YahooFinance.*
- Arguments are:
  - type_ : *str*
    - Specifies which tickers to download. **(Required)** Available parameters are:
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
- Returns: *None*

#### ***DBExtract***(*Fin_Extract*) class
> The DBExtract class is the database extraction component. It allows one to pull data from database and display in a string or pandas DataFrame format. Inherits Fin_Extract class.
##### *method* **DBExtract**.*json_extract*
```python
json_extract(format, ticker, country = "U.S.", FILE_NAME='StockInformation')
```
> *Extracts pandas DataFrame from JSON file.*
- Arguments are:
  - format : *str*
    - Specifies which format to view in dataframe. **(Required)** Available parameters are:
      - *"view"* - view in default format.
      - *"data"* - view in scientific data format.
  - ticker : *str*
    - Specifies which ticker to extract. **(Required)**
  - country : *str*
    - Specifies which country ticker is from. Default is *"U.S."* *(Optional)*
  - FILE_NAME : *str*
    - Specifies which data file to pull from. Default is *"StockInformation"* *(Optional)*
- Returns: *pandas DataFrame or pandas Series*
  -  Returns dataframe or series of extracted file.

#### ***Fin_Extract***(*Fin_Select*) class
> The Fin_Extract class allows extraction of data from str/ pandas DataFrame/ pandas Series format. Then, it is able to convert values into scientific values for analysis purposes. Inherits Fin_Select class.
##### *method* **Fin_Extract**.*determine_symbol*
```python
determine_symbol(cell_val)
```
> *Determines what symbols are in string specified. Then returns a list of symbols.*
- Arguments are:
  - cell_val : *str*
    - Specifies what string to get symbols from. **(Required)**
- Returns: *list*
  - Returns list of symbols available in string.

##### *method* **Fin_Extract**.*str_to_val*
```python
str_to_val(cell_val)
```
> *Converts string which contains symbols to either float or int value. Returns scientific value.*
- Arguments are:
  - cell_val : *str*
    - Specifies what string to get symbols from. **(Required)**
- Returns: *pandas dtype int64 / float64*
  - Returns scientific value of string in pandas datatype int64 or float64.
 
##### *method* **Fin_Extract**.*extract*
```python
extract(cell_val)
```
> *Determines what type of data is passed into input. Then returns either a string or pandas Series of scientific values.*
- Arguments are:
  - cell_val : *str / pandas Series*
    - Specifies what string(s) to get symbols from. **(Required)**
- Returns: *pandas dtype int64 / float64 or pandas Series*
  - Returns scientific value of string in pandas datatype int64 or float64. Can also return pandas Series if *cell_val* is a pandas Series.

##### *method* **Fin_Extract**.*extract_columns*
```python
extract_columns(from_df)
```
> *Extracts list of columns from pandas DataFrame*
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**
- Returns: *list*
  - Returns list of columns of pandas DataFrame

#### ***Fin_Select*** class
> The Fin_Select class allows selection of specific cells or rows  Then, it is able to convert values into scientific values for analysis purposes. Inherits Fin_Select class.
##### *method* **Fin_Select**.*select_isolate*
```python
select_isolate(from_df, year=None, item=None)
```
> *Selects pandas DataFrame specific column and row for respective arguments.
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**'
  - year : *int*
    - Specifies which column to get data from. Default is *None* *(Optional)*
  - item : *str*
    - Specifies which row to get data from. Default is *None* *(Optional)*
- Returns: *str*
  - Returns string of specific cell.

##### *method* **Fin_Select**.*select_item*
```python
select_item(from_df, item=None)
```
> *Selects pandas DataFrame specific row for respective arguments.
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**'
  - item : *str*
    - Specifies which row to get data from. Default is *None* *(Optional)*
- Returns: *pandas Series*
  - Returns pandas Series of row.

##### *method* **Fin_Select**.*select_year*
```python
select_item(from_df, year=None)
```
> *Selects pandas DataFrame specific column for respective arguments.
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**'
  - year : *int*
    - Specifies which column to get data from. Default is *None* *(Optional)*
- Returns: *pandas Series*
  - Returns pandas Series of column.

