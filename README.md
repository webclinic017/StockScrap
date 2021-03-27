# Stock Data Scrapper using MarketWatch and Yahoo Finance!
*Made by rawsashimi1604*

## Table of Contents
- [Stock Data Scrapper using MarketWatch and Yahoo Finance!](#stock-data-scrapper-using-marketwatch-and-yahoo-finance-)
  * [Table of Contents](#table-of-contents)
    + [Introduction](#introduction)
    + [Contributing](#contributing)
    + [Ongoing Tasks](#ongoing-tasks)
    + [Required modules](#required-modules)
    + [GUI Update](#gui-update)
    + [How to use this module and Examples](#how-to-use-this-module-and-examples)
      - [Downloader class](#downloader-class)
      - [DBExtract class](#dbextract-class)
      - [Intrinsic class](#intrinsic-class)
    + [Documentation](#documentation)

### Introduction

Hey everyone! :wave: This project is a stock data scrapper that I made for my own analysis purposes! It uses **Python** to extract financial and technical data from stocks and stores them into a database on your local computer. :smile:

> *For the technical data side, we are using yfinance module that scraps data from Yahoo Finance.*

> *For the financial data side, we are using BeautifulSoup4 to scrap data from MarketWatch.com. Then we organise the data using pandas and export it to a JSON file in our database.*

We then use these 2 components to build a complete stock data database; afterwhich you can use for your own analysis or research purposes. :grin: 	:moneybag:
    
*For now I will be adding my own analysis features in periodically into this project.*

### Contributing

All pull requests are welcome! :upside_down_face: However, changes to the code are not available for now. 

*Do drop me a message if you want to contribute and we can work something out!*

### Ongoing Tasks
- [x] Download stock data to database
- [x] Create extraction module to pull data from database (in both data and view format)
- [ ] Create module for installation across folders
- [x] Remove selenium dependency from code
- [x] Add analysis and viewing features
- [x] Calcuate intrinsic value using Discounted Cash Flow (DCF) model
- [x] Add specific documentation of different class methods and their usage
- [x] Create Graphic User Interface

### Required modules
- pandas
- numpy
- bs4
- requests
- pandas_market_calendars
- pprint
- yfinance
- PyQt5

### GUI Update
In the most recent update, I have created a GUI using PyQt5 to facilitate an easier time using the program. Simply run *main_ui.py* to run the GUI. Enjoy! :grin: Thanks to [Wanderson](https://www.youtube.com/c/WandersonIsMe/) for Circular Splash UI. 

### How to use this module and Examples
*Before starting, pip install all required modules, or simply run setup.py*

After that, open a new python file in the folder. Then import the **Downloader** class and the **DBExtract** class.

```python
from DBExtract import DBExtract
from Download import Downloader
```

#### Downloader class

> The Downloader class is the stock data downloader component. It allows one to download financial data from MarketWatch or technical data from YahooFinance.
```python
# Downloads data for Microsoft Stock, stores it in C:\Users\rawsashimi1604\FinData
d = Downloader()
d.download(type_="string", ticker="MSFT", DB_PATH=r'C:\Users\rawsashimi1604\FinData')
```

#### DBExtract class

> The DBExtract class is the database extraction component. It allows one to pull data from database and display in a string or pandas DataFrame format.
```python
# Extracts IncomeStatement data for Microsoft Stock, from C:\Users\rawsashimi1604\FinData
extract = DBExtract(DB_PATH=r'C:\Users\rawsashimi1604\FinData')
df = extract.json_extract("view", ticker="MSFT", FILE_NAME="IncomeStatement") # returns pandas DataFrame
```
#### Intrinsic class
> The Intrinsic class allows you to get intrinsic value of stock using Discounted Cash Flow Model. Required downloading of stock data using Downloader class before using.
```python
# Gets Intrinsic Value for Microsoft Stock, database is C:\Users\rawsashimi1604\FinData
i = Intrinsic()
i.intrinsic("MSFT", DB_PATH = r'C:\Users\rawsashimi1604\FinData') # returns intrinsic value of MSFT stock
```

### Documentation
#### Downloader class
> The Downloader class is the stock data downloader component. It allows one to download financial data from MarketWatch or technical data from YahooFinance.
```python
class Downloader:
    def __init__(self):
        pass
```
- Attributes are:
  - *None*

##### method Downloader.download
```python
Downloader.download(type_, DB_PATH=None, max=None, ticker=None, list_=None, csv=None, buffer=5, download="ALL")
```
> *Downloads data from MarketWatch and YahooFinance.*
- Arguments are:
  - type_ : *str*
    - Specifies which tickers to download. **(Required)** Available parameters are:
      - *"string"* - downloads single ticker
      - *"list"* - downloads list of tickers
      - *"csv"* - downloads list of tickers from csv
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
    - Specifies what data to download. Default is *"ALL"* *(Optional)* Available parameters are:
      - *"ALL"* - download all data available
      - *"PRICE"* - download price data
      - *"MAIN"* - download stock information and key data
      - *"PROFILE"* - download stock profile data
      - *"INCOME"* - download income statement
      - *"BALANCE"* - download balance sheet
      - *"CASHFLOW"* - download cash flow statement
      - ~*"FISCALYEAR"* - download fiscal year information~
- Returns: *list*
  - Returns list of stock that had errors downloading.

#### DBExtract(Fin_Extract) class
> The DBExtract class is the database extraction component. It allows one to pull data from database and display in a string or pandas DataFrame format. Inherits Fin_Extract class.
```python
class DBExtract(Fin_Extract):
    def __init__(self, DB_PATH='C:/Users/rawsashimi1604/Desktop/FinData'):
        self.DB_PATH = DB_PATH
```
- Attributes are:
  - DB_PATH : *str*
    - Specifies database directory to extract data from. Default is *'C:/Users/rawsashimi1604/Desktop/FinData'* *(Optional)*

##### method DBExtract.json_extract
```python
DBExtract.json_extract(format, ticker, country = "U.S.", FILE_NAME='StockInformation', dtype='object')
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
    - Specifies which data file to pull from. Default is *"StockInformation"* *(Optional)* Available *"FILE_NAME"*:
      - *"BalanceSheet_Assets"*
      - *"BalanceSheet_Liabilities"*
      - *"CashFlow_Financing"*
      - *"CashFlow_Investing"*
      - *"CashFlow_Operating"*
      - *"IncomeStatement"*
      - *"KeyData"*
      - *"PriceData"*
      - *"Profile_Capitalization"*
      - *"Profile_Efficiency"*
      - *"Profile_Liquidity"*
      - *"Profile_Profitability"*
      - *"Profile_Valuations"*
      - *"StockInformation"*
  - dtype : *str*
    - Specifies what type of data. Default is *"object"* *(Optional)*
- Returns: *pandas DataFrame or pandas Series*
  -  Returns dataframe or series of extracted file.

#### Fin_Extract(Fin_Select) class
> The Fin_Extract class allows extraction of data from str/ pandas DataFrame/ pandas Series format. Then, it is able to convert values into scientific values for analysis purposes. Inherits Fin_Select class.
```python
class Fin_Extract(Fin_Select):
    def __init__(self, ticker):
        self.ticker = ticker
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to extract data from. **(Required)**
    
##### method Fin_Extract.determine_symbol
```python
Fin_Extract.determine_symbol(cell_val)
```
> *Determines what symbols are in string specified. Then returns a list of symbols.*
- Arguments are:
  - cell_val : *str*
    - Specifies what string to get symbols from. **(Required)**
- Returns: *list*
  - Returns list of symbols available in string.

##### method Fin_Extract.str_to_val
```python
Fin_Extract.str_to_val(cell_val)
```
> *Converts string which contains symbols to either float or int value. Returns scientific value.*
- Arguments are:
  - cell_val : *str*
    - Specifies what string to get symbols from. **(Required)**
- Returns: *pandas dtype int64 / float64*
  - Returns scientific value of string in pandas datatype int64 or float64.
 
##### method Fin_Extract.extract
```python
Fin_Extract.extract(cell_val)
```
> *Determines what type of data is passed into input. Then returns either a string or pandas Series of scientific values.*
- Arguments are:
  - cell_val : *str / pandas Series*
    - Specifies what string(s) to get symbols from. **(Required)**
- Returns: *pandas dtype int64 / float64 or pandas Series*
  - Returns scientific value of string in pandas datatype int64 or float64. Can also return pandas Series if *cell_val* is a pandas Series.

##### method Fin_Extract.extract_columns
```python
Fin_Extract.extract_columns(from_df)
```
> *Extracts list of columns from pandas DataFrame*
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**
- Returns: *list*
  - Returns list of columns of pandas DataFrame

#### Fin_Select class
> The Fin_Select class allows selection of specific cells or rows  Then, it is able to convert values into scientific values for analysis purposes. Inherits Fin_Select class.
```python
class Fin_Select:
    def __init__(self, ticker):
        self.ticker = ticker
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to select data from. **(Required)**
    
##### method Fin_Select.select_isolate
```python
Fin_Select.select_isolate(from_df, year=None, item=None)
```
> *Selects pandas DataFrame specific column and row for respective arguments.*
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**
  - year : *int*
    - Specifies which column to get data from. Default is *None* *(Optional)*
  - item : *str*
    - Specifies which row to get data from. Default is *None* *(Optional)*
- Returns: *str*
  - Returns string of specific cell.

##### method Fin_Select.select_item
```python
Fin_Select.select_item(from_df, item=None)
```
> *Selects pandas DataFrame specific row for respective arguments.*
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**
  - item : *str*
    - Specifies which row to get data from. Default is *None* *(Optional)*
- Returns: *pandas Series*
  - Returns pandas Series of row.

##### method Fin_Select.select_year
```python
Fin_Select.select_item(from_df, year=None)
```
> *Selects pandas DataFrame specific column for respective arguments.*
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**
  - year : *int*
    - Specifies which column to get data from. Default is *None* *(Optional)*
- Returns: *pandas Series*
  - Returns pandas Series of column.

#### Fin_Data class
> The Fin_Data class allows for scraping of financial data from MarketWatch. It then returns it in a pandas DataFrame or Series format.
```python
class Fin_Data(WebDriver):
    def __init__(self, ticker):
        self.ticker = ticker
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to draw financial data from. **(Required)**
 
##### method Fin_Data.reorder_df
```python
Fin_Data.reorder_df(from_df, reverse=False)
```
> *Reorders pandas DataFrame columns in descending order.*
- Arguments are:
  - from_df : *pandas DataFrame*
    - Specifies what DataFrame to get list of columns from. **(Required)**
  - reverse : *boolean*
    - Specifies whether to reorder in descending. False = descending. Default is *False* *(Optional)*
- Returns: *pandas DataFrame*
  - Returns reordered pandas DataFrame

##### method Fin_Data.name
```python
Fin_Data.name()
```
> *Get stock's name.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns stock name in string value.

##### method Fin_Data.industry
```python
Fin_Data.industry()
```
> *Get stock's industry.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns stock's industry in string value.

##### method Fin_Data.sector
```python
Fin_Data.sector()
```
> *Get stock's sector.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns stock's sector in string value.

##### method Fin_Data.exchange
```python
Fin_Data.exchange()
```
> *Get stock's exchange location.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns stock's exchange location in string value.
  
##### method Fin_Data.ceo
```python
Fin_Data.ceo()
```
> *Get stock's CEO name.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns stock's CEO name in string value.
  
##### method Fin_Data.business_model
```python
Fin_Data.business_model()
```
> *Get stock's business_model overview.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns stock's business_model overview in string value.
  
##### method Fin_Data.stock_info
```python
Fin_Data.stock_info()
```
> *Get stock's information overview. Includes name, sector, industry, exchange, ceo and business model.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns stock's main information in pandas DataFrame format.

##### method Fin_Data.price
```python
Fin_Data.price()
```
> *Get stock's current price.*
- Arguments are:
  - *None*
- Returns: *float*
  - Returns stock's price in float value.

##### method Fin_Data.check_ticker
```python
Fin_Data.check_ticker()
```
> *Uses stock price and sector to check whether the ticker exists in MarketWatch database.*
- Arguments are:
  - *None*
- Returns: *bool*
  - Returns True or False depending on whether the stock exists. Returns True for exist.

##### method Fin_Data.valuations
```python
Fin_Data.valuations()
```
> *Get table of valuation metrics under MarketWatch Profile page.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of valuation metrics.

##### method Fin_Data.efficiency
```python
Fin_Data.efficiency()
```
> *Get table of efficiency metrics under MarketWatch Profile page.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of efficiency metrics.
  
##### method Fin_Data.liquidity
```python
Fin_Data.liquidity()
```
> *Get table of liquidity metrics under MarketWatch Profile page.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of liquidity metrics.

##### method Fin_Data.profitability
```python
Fin_Data.profitability()
```
> *Get table of profitability metrics under MarketWatch Profile page.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of profitability metrics.

##### method Fin_Data.captialization
```python
Fin_Data.captialization()
```
> *Get table of captialization metrics under MarketWatch Profile page.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of captialization metrics.
  
##### method Fin_Data.main_page
```python
Fin_Data.main_page()
```
> *Get table of stock information from MarketWatch landing page.*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of stock information.
  
##### method Fin_Data.income_statement
```python
Fin_Data.income_statement()
```
> *Get dataframe of stock income statement*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of stock income statement.
  
##### method Fin_Data.balance_sheet_assets
```python
Fin_Data.balance_sheet_assets()
```
> *Get dataframe of stock balance sheet assets*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of stock balance sheet assets.
  
##### method Fin_Data.balance_sheet_lia
```python
Fin_Data.balance_sheet_lia()
```
> *Get dataframe of stock balance sheet liabilities*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of stock balance sheet liabilities.
  
##### method Fin_Data.cash_flow_opr
```python
Fin_Data.cash_flow_opr()
```
> *Get dataframe of stock cash flow operating activities*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of cash flow operating activities.
  
##### method Fin_Data.cash_flow_inv
```python
Fin_Data.cash_flow_inv()
```
> *Get dataframe of stock cash flow investing activities*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of cash flow investing activities.
  
##### method Fin_Data.cash_flow_fin
```python
Fin_Data.cash_flow_fin()
```
> *Get dataframe of stock cash flow financing activities*
- Arguments are:
  - *None*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of cash flow financing activities.
  
##### method Fin_Data.balance_sheet
```python
Fin_Data.balance_sheet()
```
> *Prints full balance sheet for viewing.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns 'Printed balance sheet successfully.'

##### method Fin_Data.cash_flow
```python
Fin_Data.cash_flow()
```
> *Prints full cash flow statement for viewing.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns 'Printed cash flow statement successfully.'

##### method Fin_Data.years
```python
Fin_Data.years()
```
> *Gets list of years of availble scrapped data from MarketWatch using income statement.*
- Arguments are:
  - *None*
- Returns: *list*
  - Returns list of years.

##### method Fin_Data.fiscal_month
```python
Fin_Data.fiscal_month()
```
> *Gets first month of fiscal year of stock.*
- Arguments are:
  - *None*
- Returns: *int*
  - Returns first month of fiscal year.

##### method Fin_Data.fiscal_year_dates
```python
Fin_Data.fiscal_year_dates()
```
> *Gets list of start fiscal year dates*
- Arguments are:
  - *None*
- Returns: *list*
  - Returns list of start fiscal year dates.

#### FData(Fin_Data, Fin_Extract) class
> The FData class merges Financial Data methods with extraction methods. Inherits Fin_Data and Fin_Extract.
```python
class FData(Fin_Data, Fin_Extract):
    def __init__(self, ticker):
        Fin_Data.__init__(self, ticker)
        Fin_Extract.__init__(self,ticker)
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to extract data from. **(Required)**
 
#### TData class
> The TData class uses yfinance module to extract technical price data for stocks. 
```python
class FData(Fin_Data, Fin_Extract):
    def __init__(self, ticker):
        self.ticker = ticker
        pass
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to extract data from. **(Required)**

##### method TData.check_name
```python
TData.check_name()
```
> *Checks if ticker name contains '.'. If it does, change to '-' for yfinance portability.*
- Arguments are:
  - *None*
- Returns: *str*
  - Returns str of new ticker name for yfinance portability.

##### method TData.get_info
```python
TData.get_info(command="nil", print=False)
```
> *Gets stock data metric depending on command.*
- Arguments are:
  - command : *str*
    - Specifies which metric to get. *(Optional)* Default is *"nil"* Available parameters are:
      - *"nil"* - all information printed
      - *"averageVolume"* - stock average volume
      - *"currency"* - stock currency
      - *"dividendYield"* - stock dividend yield
      - *"forwardEps"* - stock forward EPS
      - *"forwardPE"* - stock forward P/E Ratio
      - *"longBusinessSummary"* - stock business summary
      - *"longName"* - stock name
      - *"marketCap"* - stock market capitalization
      - *"pegRatio"* - stock PEG Ratio
      - *"previousClose"* - stock previous closing price
      - *"priceToBook"* - stock price to book ratio
      - *"quoteType"* - type of asset
  - print : *bool*
    - Specifies whether to print data using pprint. Default is *False* *(Optional)*
- Returns: *dict or int or float or str*
  - Returns various values depending on command

##### method TData.get_data
```python
TData.get_data(candle_interval=1, print=False)
```
> *Gets stock max period technical data depending on interval of each candlestick. Default is 1D candles.*
- Arguments are:
  - candle_interval : *int*
    - Specifies interval of each candlestick. Default is *1* *(Optional)*
  - print : *bool*
    - Specifies whether to print data using pprint. Default is *False* *(Optional)*
- Returns: *pandas DataFrame*
  - Returns pandas DataFrame of stock data. Open, High, Low, Close, Volume, Dividends, Stock Splits.

##### method TData.get_close
```python
TData.get_close(candle_interval=1, print=False)
```
> *Gets stock max period close price data depending on interval of each candlestick. Default is 1D candles.*
- Arguments are:
  - candle_interval : *int*
    - Specifies interval of each candlestick. Default is *1* *(Optional)*
  - print : *bool*
    - Specifies whether to print data using pprint. Default is *False* *(Optional)*
- Returns: *pandas Series*
  - Returns pandas Series of stock data.
 
##### method TData.get_open
```python
TData.get_open(candle_interval=1, print=False)
```
> *Gets stock max period open price data depending on interval of each candlestick. Default is 1D candles.*
- Arguments are:
  - candle_interval : *int*
    - Specifies interval of each candlestick. Default is *1* *(Optional)*
  - print : *bool*
    - Specifies whether to print data using pprint. Default is *False* *(Optional)*
- Returns: *pandas Series*
  - Returns pandas Series of stock data.
  
##### method TData.get_prevclose
```python
TData.get_prevclose(candle_interval=1, print=False)
```
> *Gets stock previous candlestick's close price data depending on interval of each candlestick. Default is 1D candles.*
- Arguments are:
  - candle_interval : *int*
    - Specifies interval of each candlestick. Default is *1* *(Optional)*
  - print : *bool*
    - Specifies whether to print data using pprint. Default is *False* *(Optional)*
- Returns: *float*
  - Returns price of previous candlestick's close price.

#### ToJson class
> The ToJson class stores pandas DataFrames and Series' into JSON files and stores it in a database.
```python
class ToJson:
    def __init__(self):
        pass
```
- Attributes are:
  - *None*
  
##### method ToJson.json
```python
ToJson.json(from_obj=None, export_to=None, filename=None, orient='columns')
```
> *Stores pandas DataFrame or Series into JSON file and store into database.*
- Arguments are:
  - from_obj : *pandas DataFrame or pandas Series*
    - Specifies object type to store as JSON. Default is *None* *(Optional)*
  - export_to : *str*
    - Specifies directory to store JSON file at. Default is *None* *(Optional)*
  - filename : *str* 
    - Specifies file name of JSON file. Default is *None* *(Optional)*
  - orient : *str*
    - Specifies orient of pandas.to_json function. Default is *columns* *(Optional)*
- Returns: *None*
  - Returns None.

#### Stock_Data(TData, FData, ToJson) class
> The Stock_Data class is a combination of all methods found to scrap technical and financial data. It also allows for JSON file storage. Inherits TData, FData, ToJson classes.
```python
class Stock_Data(TData, FData, ToJson):
    def __init__(self, ticker):
        TData.__init__(self, ticker)
        FData.__init__(self, ticker)
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to extract data from. **(Required)**

##### method Stock_Data.fiscal_year_prices
```python
Stock_Data.fiscal_year_prices()
```
> *Get fiscal year start dates and their respective open prices.*
- Arguments are:
  - *None*
- Returns: *pandas Series*
  - Returns pandas Series of fiscal year start dates and their respective open prices.
  
#### StockDL(Stock_Data) class
> The StockDL class is a optimized downloader class. It allows for download of scrapped data in a consolidated fashion, then stores the data into JSON files and finally store it in a database.
```python
class StockDL:
    def __init__(self, ticker):
        Stock_Data.__init__(self, ticker)
```
- Attributes are:
  - ticker : *str*
    - Specifies which ticker to extract data from. **(Required)**

##### method Stock_Data.stockdl
```python
StockDL.stockdl(DB_PATH='C:/Users/rawsashimi1604/Desktop/FinData', download="ALL", buffer=5)
```
> *Downloads data, stores into JSON, finally storing it into database.*
- Arguments are:
  - DB_PATH : *str*
    - Specifies database directory to extract data from. Default is *'C:/Users/rawsashimi1604/Desktop/FinData'* *(Optional)*
  - download : *str*
    - Specifies what data to download. Default is *"ALL"* *(Optional)* Available parameters are:
      - *"ALL"* - download all data available
      - *"PRICE"* - download price data
      - *"MAIN"* - download stock information and key data
      - *"PROFILE"* - download stock profile data
      - *"INCOME"* - download income statement
      - *"BALANCE"* - download balance sheet
      - *"CASHFLOW"* - download cash flow statement
      - ~*"FISCALYEAR"* - download fiscal year information~
  - buffer : *int*
    - Specifies buffer time in seconds in between each download. Default is *5* *(Optional)*
- Returns: *bool*
  - Returns whether stock ticker exists. exist = True

#### BondRate class
> The BondRate class allows you to get US 10 year bond rates (Risk Free Rate).
```python
class BondRate:
    def __init__(self):
        pass
```
- Attributes are:
  - None

##### method BondRate.bondrate
```python
BondRate.bondrate()
```
> *Get current US 10 year bond rate.*
- Arguments are:
  - None
- Returns: *float*
  - Returns float value of US 10 year bond rate.

#### Intrinsic(BondRate) class
> The Intrinsic class allows you to get the intrinsic value of a stock using the DCF (Discounted Cash Flow) model. Inherits BondRate class. Currently does not work for bank stocks.
```python
class Intrinsic(BondRate):
    def __init__(self):
        pass
```
- Attributes are:
  - None

##### method Intrinsic.intrinsic
```python
Intrinsic.intrinsic(ticker, DB_PATH, estimated_yrs = 4, expected_rate_return = 0.1, perpetual_growth = 0.025, margin_safety = 0.5, download = True)
```
> *Get intrinsic value of stock using Discounted Cash Flow Model. Required downloading of stock data using Downloader class before using. Currently does not work for bank stocks.*
- Arguments are:
  - ticker : *str*
    - Specifies which ticker to extract. **(Required)**
  - DB_PATH : *str*
    - Specifies database directory to extract data from. **(Required)**
  - estimated_yrs : *int*
    - Specifies number of years to estimate using DCF model. Default is *4* *(Optional)*
  - expected_rate_return : *float*
    - Specifies expected rate of return of the stock market in percent. Default is *0.1* *(Optional)*
  - perpetual_growth : *float*
    - Specifies rate of perpetual growth (est) of companies Free Cash Flow in percent. Default is *0.025* *(Optional)*
  - margin_safety : *float*
    - Specifies personal margin of safety to stock price in percent. Default is *0.5* *(Optional)*
  - download : *bool*
    - Specifies whether to download stock data. Default is *True* *(Optional)*
- Returns: *float*
  - Returns float value of intrinsic value of stock.
