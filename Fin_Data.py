######################################################################
# IMPORTS                                                            #
######################################################################
# Import BS4 Classes
from bs4 import BeautifulSoup as bs
import requests

# Import WebDriver Class
from WebDriver import WebDriver

# Import selenium and get PATH for chromedriver.exe, initialize driver, give access to enter key, esc key.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Import action chains
from selenium.webdriver.common.action_chains import ActionChains

# Imports selenium wait until expected_conditions required modules.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

# Imports selenium errors and exceptions.
from selenium.common.exceptions import *

# Imports selenium logger, to disable logging on selenium
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

# Import time for sleep functions
import time

# Import datetime for datetime functions and pandas market calendars for stock market holidays
from datetime import datetime, timedelta
import pandas_market_calendars as mcal


# Import pandas and numpy
import pandas as pd
import numpy as np
######################################################################
# CLASS INIT                                                         #
######################################################################

class Fin_Data(WebDriver):
    '''
    # Financial Data Scrapper Made by Gavin Loo 2021.
    Uses data from MarketWatch.com
    Returns pandas DataFrame of income statements, balance sheets, cash flow statements of any stock
    listed on US Stock Exchange.

    Args = ticker name(str), PATH of chromedriver
    Finish with driver_end() to end drawing data.
    '''
    
    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe', ignore_errors=True):
        '''
        Initialize Fin_Data class, intialize self.driver requirements for selenium
        '''

        WebDriver.__init__(self, PATH='C:\Program Files (x86)\chromedriver.exe', ignore_errors=True)
        self.ticker = ticker
        self.PATH = PATH
        self.driver = self.driver()

    def __repr__(self):
        '''
        Output when inspecting Class
        # Returns str
        '''

        return (f'{self.__class__.__name__}('f'{self.ticker!r}, {self.PATH!r}')


    def __str__(self):
        '''      
        Class print's output
        # Returns str
        '''

        return f'Financial Data for {self.ticker}, Chromedriver PATH = {self.PATH}'

    
    def remove_logging(self):
        '''
        Disables logging from selenium
        # Returns None
        '''
        LOGGER.setLevel(logging.WARNING)
        
        options = webdriver.ChromeOptions()


        return None


    def reorder_df(self, from_df, reverse=False):
        df = from_df.reindex(columns=sorted(from_df.columns, reverse=reverse))
        return df


    def check_ticker(self):
        '''
        Check if ticker exists? use price element to get boolean value.
        # Returns bool
        '''

        self.remove_logging()

        # URL to check if ticker exists
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

        # Navigate to QUOTE URL
        self.driver.get(URL)

        # Implicit Buffer
        self.driver.implicitly_wait(1)

        if URL == self.driver.current_url:
            exist = True
        
        else:
            exist = False

        # Returns True or False depending whether self.ticker exists in database.
        return exist


    def name(self):
        '''
        Get stock name
        # returns str
        '''

        self.remove_logging()

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for stock name
        name_loc = "//h1[contains(@class, 'company__name')]"

        # get name val and convert to text
        val = self.driver.find_element_by_xpath(name_loc).text

        return val


    def industry(self):
        '''
        Get stock industry
        # returns str
        '''

        self.remove_logging()

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for stock industry
        name_loc = "//li[contains(@class, 'kv__item w100')][1]/span"

        # get industry val and convert to text
        val = self.driver.find_element_by_xpath(name_loc).text

        return val


    def sector(self):
        '''
        Get stock sector
        # returns str
        '''
        
        self.remove_logging()

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for stock industry
        name_loc = "//li[contains(@class, 'kv__item w100')][2]/span"

        # get industry val and convert to text
        val = self.driver.find_element_by_xpath(name_loc).text

        return val


    def exchange(self):
        '''
        Get stock exchange
        # returns str
        '''

        self.remove_logging()

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for stock industry
        exchange_loc = "//div[contains(@class,'company__symbol')]/span[2]"

        # get industry val and convert to text
        val = self.driver.find_element_by_xpath(exchange_loc).text

        val = val.replace(":", "")

        return val


    def ceo(self):
        '''
        Get stock CEO
        # returns str
        '''

        self.remove_logging()

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for stock industry
        ceo_loc = "//div[contains(@class,'group right')]/div/ul/li[1]/a"

        # get industry val and convert to text
        val = self.driver.find_element_by_xpath(ceo_loc).text

        return val


    def business_model(self):
        '''
        Get information of businesss model
        # returns str
        '''

        self.remove_logging()

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for stock industry
        bm_loc = "//p[contains(@class, 'description__text')]"

        # get industry val and convert to text
        val = self.driver.find_element_by_xpath(bm_loc).text

        return val

    
    def stock_info(self):
        '''
        Summarises all the main info in a stock into a dataframe.
        # Returns pandas Series
        '''

        # Name, Sector, Industry, 
        name = self.name()
        sector = self.sector()
        industry = self.industry()
        exchange = self.exchange()
        ceo = self.ceo()
        business_model = self.business_model()

        index = ['Name', 'Sector', 'Industry', 'Exchange', 'CEO', 'Business Model']
        val = [name, sector, industry, exchange, ceo, business_model]

        # Create pandas Series using index list and val list.
        stock_s = pd.Series(val, index, dtype='string', name=f'{self.ticker} Information')

        return stock_s


    def price(self):
        '''
        Get current price of stock, regardless of PreMarket, PostMarket or OpenMarket.
        # returns float
        '''

        self.remove_logging()

        # URL to check for stock price.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for price
        check_price = "//h3[contains(@class, 'intraday__price')]/bg-quote"

        # Value of stock in str
        check_price_val = self.driver.find_element_by_xpath(check_price).text

        # Get Price of Stock in float
        price = float(check_price_val)
        
        return price
    
    
    def valuations(self):
        '''
        Get current valuations of the stock.
        # returns pandas DataFrame
        '''

        self.remove_logging()

        # URL to check for valuations table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for header, columns and values
        header = "//div[contains(@class, 'column column--primary')]/div[2]/div[1]/header/h2/span"
        # loop through tr to get vals
        column = "//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr/td[1]"
        
        # loop through tr to get vals
        data = "//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr/td[2]"

        # Scraped Data
        column_loc = self.driver.find_elements_by_xpath(column)
        data_loc = self.driver.find_elements_by_xpath(data)

        # Get length of columns
        column_len = len(column_loc)
        data_len = len(data_loc)

        # Lists to add into dataframe
        column_list = []
        data_list = []

        # Get index of dataframe
        for i in range(1, column_len + 1):
            column = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]").text
            column_list.append(column)
        
        for i in range(1, data_len + 1):
            data = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[2]").text
            data_list.append(data)
        
        # Create series for viewing
        val_series = pd.Series(data_list, index=column_list)

        return val_series


    def efficiency(self):
        '''
        Get current efficiency of the stock.
        # returns pandas DataFrame
        '''

        self.remove_logging()

        # URL to check for efficiency table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for header, columns and values
        header = "//div[contains(@class, 'column column--primary')]/div[2]/div[2]/header/h2/span"
        # loop through tr to get vals
        column = "//div[contains(@class, 'column column--primary')]/div[2]/div[2]/table/tbody/tr/td[1]"
        
        # loop through tr to get vals
        data = "//div[contains(@class, 'column column--primary')]/div[2]/div[2]/table/tbody/tr/td[2]"

        # Scraped Data
        column_loc = self.driver.find_elements_by_xpath(column)
        data_loc = self.driver.find_elements_by_xpath(data)

        # Get length of columns
        column_len = len(column_loc)
        data_len = len(data_loc)

        # Lists to add into dataframe
        column_list = []
        data_list = []

        # Get index of dataframe
        for i in range(1, column_len + 1):
            column = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]").text
            column_list.append(column)
        
        for i in range(1, data_len + 1):
            data = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[2]").text
            data_list.append(data)
        
        # Create series for viewing
        eff_series = pd.Series(data_list, index=column_list)

        return eff_series


    def liquidity(self):
        '''
        Get current liquidity of the stock.
        # returns pandas DataFrame
        '''

        self.remove_logging()

        # URL to check for liquidity table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for header, columns and values
        header = "//div[contains(@class, 'column column--primary')]/div[2]/div[3]/header/h2/span"
        # loop through tr to get vals
        column = "//div[contains(@class, 'column column--primary')]/div[2]/div[3]/table/tbody/tr/td[1]"
        
        # loop through tr to get vals
        data = "//div[contains(@class, 'column column--primary')]/div[2]/div[3]/table/tbody/tr/td[2]"

        # Scraped Data
        column_loc = self.driver.find_elements_by_xpath(column)
        data_loc = self.driver.find_elements_by_xpath(data)

        # Get length of columns
        column_len = len(column_loc)
        data_len = len(data_loc)

        # Lists to add into dataframe
        column_list = []
        data_list = []

        # Get index of dataframe
        for i in range(1, column_len + 1):
            column = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]").text
            column_list.append(column)
        
        for i in range(1, data_len + 1):
            data = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[2]").text
            data_list.append(data)
        
        # Create series for viewing
        liq_series = pd.Series(data_list, index=column_list)

        return liq_series


    def profitability(self):
        '''
        Get current profitability of the stock.
        # returns pandas DataFrame
        '''

        self.remove_logging()

        # URL to check for profitability table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for header, columns and values
        header = "//div[contains(@class, 'column column--primary')]/div[3]/div[1]//header/h2/span"
        # loop through tr to get vals
        column = "//div[contains(@class, 'column column--primary')]/div[3]/div[1]/table/tbody/tr/td[1]"
        
        # loop through tr to get vals
        data = "//div[contains(@class, 'column column--primary')]/div[3]/div[1]/table/tbody/tr/td[2]"

        # Scraped Data
        column_loc = self.driver.find_elements_by_xpath(column)
        data_loc = self.driver.find_elements_by_xpath(data)

        # Get length of columns
        column_len = len(column_loc)
        data_len = len(data_loc)

        # Lists to add into dataframe
        column_list = []
        data_list = []

        # Get index of dataframe
        for i in range(1, column_len + 1):
            column = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]").text
            column_list.append(column)
        
        for i in range(1, data_len + 1):
            data = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[2]").text
            data_list.append(data)
        
        # Create series for viewing
        pft_series = pd.Series(data_list, index=column_list)

        return pft_series


    def captialization(self):
        '''
        Get current captialization of the stock.
        # returns pandas DataFrame
        '''

        self.remove_logging()

        # URL to check for profitability table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for header, columns and values
        header = "//div[contains(@class, 'column column--primary')]/div[3]/div[2]//header/h2/span"
        # loop through tr to get vals
        column = "//div[contains(@class, 'column column--primary')]/div[3]/div[2]/table/tbody/tr/td[1]"
        
        # loop through tr to get vals
        data = "//div[contains(@class, 'column column--primary')]/div[3]/div[2]/table/tbody/tr/td[2]"

        # Scraped Data
        column_loc = self.driver.find_elements_by_xpath(column)
        data_loc = self.driver.find_elements_by_xpath(data)

        # Get length of columns
        column_len = len(column_loc)
        data_len = len(data_loc)

        # Lists to add into dataframe
        column_list = []
        data_list = []

        # Get index of dataframe
        for i in range(1, column_len + 1):
            column = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]").text
            column_list.append(column)
        
        for i in range(1, data_len + 1):
            data = self.driver.find_element_by_xpath(f"//div[contains(@class, 'column column--primary')]/div[2]/div[1]/table/tbody/tr[{i}]/td[2]").text
            data_list.append(data)
        
        # Create dataframe for viewing
        cap_series = pd.Series(data_list, index=column_list)

        return cap_series


    def main_page(self):
        '''
        Get Main Data
        # Returns pandas Series
        '''

        self.remove_logging()

        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # get xpath values for main page
        # Main values
        
        quote_header = "//*[contains(@class, 'kv__item')]//following::small"
        quote_value = "//*[contains(@class, 'kv__item')]/span[contains(@class, 'primary ')]"
        quote_header_loc = self.driver.find_elements_by_xpath(quote_header)
        quote_val_loc = self.driver.find_elements_by_xpath(quote_value)

        # Lists of data for quote page
        quote_headers = []
        quote_data = []

        # Find headers in main Quote page, remove last column as it does not contain data
        for locator in quote_header_loc:
            header = locator.text
            quote_headers.append(header)

        # try to remove "Competitor Data Provided By"
        try:    
            quote_headers.remove('Competitor Data Provided By')
        except ValueError:
            print("'Competitor Data Provided By' data not available, will continue running code")
            pass

        # Find values in main Quote page
        for val in quote_val_loc:
            data_vals = val.text
            quote_data.append(data_vals)

        # Series to store values
        quote_s = pd.Series(quote_data, index=quote_headers, name=f'{self.ticker} Key Data', dtype='string')


        # Returns dataframe table
        return quote_s
            
    
    def income_statement(self):
        '''
        Get Income Statement from Financials page
        # Returns pandas DataFrame
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[0]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)

        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def balance_sheet_assets(self):
        '''
        Get Balance Sheet, Assets from Financials page
        # Returns pandas DataFrame
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/balance-sheet'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[0]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)

        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df
        
    
    def balance_sheet_lia(self):
        '''
        Get Balance Sheet, Libabilities from Financials page
        # Returns pandas DataFrame
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/balance-sheet'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[1]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)
        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def cash_flow_opr(self):
        '''
        Get Cash Flow, Operating Activies from Financials page
        # Returns pandas DataFrame
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[0]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)
        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def cash_flow_inv(self):
        '''
        Get Cash Flow, Investing Activies from Financials page
        # Returns pandas DataFrame
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[1]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)
        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def cash_flow_fin(self):
        '''
        Get Cash Flow, Financing Activities from Financials page
        # Returns pandas DataFrame
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[2]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)

        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df
    
    
    def balance_sheet(self):
        '''
        Get Full Balance Sheet from Financials page
        # Returns str
        '''
        asset = self.balance_sheet_assets()
        time.sleep(3)
        lia = self.balance_sheet_lia()
        print(asset)
        print(lia)
        
        return 'Printed balance sheet successfully.'
    
    
    def cash_flow(self):
        '''
        Get Full Cash Flow Statement from Cash Flow page
        # Returns str
        '''
        opr = self.cash_flow_opr()
        time.sleep(2)
        inv = self.cash_flow_inv()
        time.sleep(2)
        fin = self.cash_flow_fin()
        print(opr)
        print(inv)
        print(fin)

        return 'Printed cash flow statement successfully.'


    def years(self):
        '''
        Get list of years with scraped financial data.
        # Returns list
        '''

        # Use income statement DataFrame
        df = self.income_statement()

        # Add years into years list
        years = []
        for cols in df.columns:
            years.append(cols)

        # Sort by years
        years.sort(reverse=False)
        # Return
        return years
    

    def fiscal_month(self):
        '''
        Get starting month of Fiscal Year for stock.
        # Returns int
        '''

        self.remove_logging()

        # URL to check for valuations table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        if URL == self.driver.current_url:
            pass

        else: 
            # Navigate to QUOTE URL
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

        # xpath for fiscal year
        fiscal = "//div[contains(@class, 'group left')]/div/ul/li[3]/span"

        # locate fiscal value using xpath
        fiscal_val = self.driver.find_element_by_xpath(fiscal).text

        # Get month start
        month = int(fiscal_val.split("/")[0])
        
        # Get fiscal year's month start date
        if month != 12:
            month = month + 1
        
        elif month == 12:
            month = 1
        
        return month


    def fiscal_year_dates(self):
        '''
        Get a list of stock Fiscal Year Start Dates
        # Returns list
        '''

        # For each date get price of each stock into a list
        month = self.fiscal_month()
        years = self.years()

        # List to add in fiscal year dates
        fiscal_year_list = []
        for year in years:
            year = int(year)
            day = 1
            date = datetime(year, month, day)

            
            f_date = date.strftime("%Y-%m-%d") # 2020-01-01

            # Get pandas market holidays calendar
            nyse = mcal.get_calendar('NYSE')
            # Get start of year + end of year + 1 
            cal_df = nyse.schedule(start_date=f'{years[0]}-01-01', end_date=f'{int(years[-1]) + 1}-01-01')

            # Get Working Days calendars in list
            cal_list = cal_df.index.tolist()

            # If not in append, else + 1 or + 2
            if date in cal_list:
                fiscal_year_list.append(f_date)
                
                
            else:
                # make a loop, break once date is in cal_list
                for i in range(1,100):
                    date = date + timedelta(days=i)
                    f_date = date.strftime("%Y-%m-%d")

                    if date in cal_list:
                        fiscal_year_list.append(f_date)
                        break
                    
        return fiscal_year_list
        

    def driver_end(self):
        '''
        Quits Google Chrome browser.
        # Returns str
        '''
        time.sleep(0.5)
        self.driver.quit()
        return 'Driver successfully quit.'

