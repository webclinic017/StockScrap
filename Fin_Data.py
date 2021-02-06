######################################################################
# IMPORTS                                                            #
######################################################################
# Import selenium and get PATH for chromedriver.exe, initialize driver, give access to enter key, esc key.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Import action chains
from selenium.webdriver.common.action_chains import ActionChains

# Imports selenium wait until expected_conditions required modules.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

class Fin_Data:
    '''
    # Financial Data Scrapper Made by Gavin Loo 2021.
    Uses data from MarketWatch.com
    Returns pandas DataFrame of income statements, balance sheets, cash flow statements of any stock
    listed on US Stock Exchange.

    Args = ticker name(str), PATH of chromedriver
    Finish with driver_end() to end drawing data.
    '''
    
    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe'):
        '''
        Initialize Fin_Data class, intialize self.driver requirements for selenium
        '''

        self.ticker = ticker
        self.PATH = PATH
        self.driver = webdriver.Chrome(self.PATH)

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
        return None

    def check_ticker(self):
        '''
        Check if ticker exists? use price element to get boolean value.
        # Returns bool
        '''
        
        # URL to check if ticker exists
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

        # Navigate to QUOTE URL
        self.remove_logging()
        self.driver.get(URL)

        # Implicit Buffer
        self.driver.implicitly_wait(3)

        # xpath for check_price
        check_price = "//h3[contains(@class, 'intraday__price')]/bg-quote"

        try:
            # Check price if exists?
            check_price_val = self.driver.find_element_by_xpath(check_price).text
            # print(check_price_val)

        except NoSuchElementException:
            print("No such ticker. Check for typos in ticker argument?")
            exist = False
        
        else:
            # print(f"{self.ticker} exists in database!")
            exist = True
        
        finally: 
            # Buffer
            time.sleep(3)

        # Returns True or False depending whether self.ticker exists in database.
        return exist

    def name(self):
        '''
        Get stock name
        # returns str
        '''
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

            # Navigate to QUOTE URL
            self.remove_logging()
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
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

            # Navigate to QUOTE URL
            self.remove_logging()
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
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

            # Navigate to QUOTE URL
            self.remove_logging()
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

            # xpath for stock industry
            name_loc = "//li[contains(@class, 'kv__item w100')][2]/span"

            # get industry val and convert to text
            val = self.driver.find_element_by_xpath(name_loc).text
<<<<<<< HEAD

            return val


    def exchange(self):
        '''
        Get stock exchange
        # returns str
        '''
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

            # Navigate to QUOTE URL
            self.remove_logging()
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
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to QUOTE URL
            self.remove_logging()
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
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to QUOTE URL
            self.remove_logging()
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

            # xpath for stock industry
            bm_loc = "//p[contains(@class, 'description__text')]"

            # get industry val and convert to text
            val = self.driver.find_element_by_xpath(bm_loc).text

            return val

=======

            return val


    def exchange(self):
        '''
        Get stock exchange
        # returns str
        '''
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

            # Navigate to QUOTE URL
            self.remove_logging()
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

            # xpath for stock industry
            exchange_loc = "//div[contains(@class,'company__symbol')]/span[2]"

            # get industry val and convert to text
            val = self.driver.find_element_by_xpath(exchange_loc).text

            return val


    def ceo(self):
        '''
        Get stock CEO
        # returns str
        '''
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to QUOTE URL
            self.remove_logging()
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
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock name.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to QUOTE URL
            self.remove_logging()
            self.driver.get(URL)

            # Implicit Buffer
            self.driver.implicitly_wait(3)

            # xpath for stock industry
            bm_loc = "//p[contains(@class, 'description__text')]"

            # get industry val and convert to text
            val = self.driver.find_element_by_xpath(bm_loc).text

            return val

>>>>>>> ae22376bf90ed8a8a62af3f9c17077b0fc90dacd
    
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
<<<<<<< HEAD

=======
>>>>>>> ae22376bf90ed8a8a62af3f9c17077b0fc90dacd

    def price(self):
        '''
        Get current price of stock, regardless of PreMarket, PostMarket or OpenMarket.
        # returns float
        '''
        exist = self.check_ticker()
        if exist == True:
            # URL to check for stock price.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

            # Navigate to QUOTE URL
            self.remove_logging()
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

        else:
            raise ValueError('Ticker does not exist. Please check again.')
    
    
    def valuations(self):
        '''
        Get current valuations of the stock.
        # returns pandas DataFrame
        '''

        exist = self.check_ticker()
        if exist == True:
            # URL to check for valuations table.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to PROFILE URL
            self.remove_logging()
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

        else:
            raise ValueError('Ticker does not exist. Please check again.')


    def efficiency(self):
        '''
        Get current efficiency of the stock.
        # returns pandas DataFrame
        '''

        exist = self.check_ticker()
        if exist == True:
            # URL to check for efficiency table.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to PROFILE URL
            self.remove_logging()
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

        else:
            raise ValueError('Ticker does not exist. Please check again.')


    def liquidity(self):
        '''
        Get current liquidity of the stock.
        # returns pandas DataFrame
        '''

        exist = self.check_ticker()
        if exist == True:
            # URL to check for liquidity table.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to PROFILE URL
            self.remove_logging()
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

        else:
            raise ValueError('Ticker does not exist. Please check again.')


    def profitability(self):
        '''
        Get current profitability of the stock.
        # returns pandas DataFrame
        '''

        exist = self.check_ticker()
        if exist == True:
            # URL to check for profitability table.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to PROFILE URL
            self.remove_logging()
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

        else:
            raise ValueError('Ticker does not exist. Please check again.')


    def captialization(self):
        '''
        Get current captialization of the stock.
        # returns pandas DataFrame
        '''

        exist = self.check_ticker()
        if exist == True:
            # URL to check for profitability table.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to PROFILE URL
            self.remove_logging()
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

        else:
            raise ValueError('Ticker does not exist. Please check again.')


    def main_page(self):
        '''
        Get Main Data
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # Buffer of 5 seconds
            time.sleep(3)

            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'
            driver = self.driver

            # Navigate to QUOTE URL
            self.remove_logging()
            driver.get(URL)

            # Buffer of 5 seconds for website to load
            driver.implicitly_wait(3)

            # get xpath values for main page
            # Main values
            
            quote_header = "//*[contains(@class, 'kv__item')]//following::small"
            quote_value = "//*[contains(@class, 'kv__item')]/span[contains(@class, 'primary ')]"
            quote_header_loc = driver.find_elements_by_xpath(quote_header)
            quote_val_loc = driver.find_elements_by_xpath(quote_value)

            # # Pop up button
            # quote_button = "//img[contains(@src, 'icon-close2x')]"

            # try:
            #     pop_up_loc = driver.find_element_by_xpath(quote_button)
            #     # Clear popup from screen
            #     pop_up_loc.click()
            # except NoSuchElementException:
            #     # If no popups continue next line of code.
            #     # print("No popups detected. Continue code.")
            #     pass

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


            # # Dataframe to store values
            # quote_df = pd.DataFrame(quote_data, index=quote_headers, columns=['MAIN PAGE VALUE'])
            # # SET Index as {ticker} MAIN PAGE DATA
            # quote_df = quote_df.rename_axis(f'{self.ticker} Main Page Data')

            # Series to store values
            quote_s = pd.Series(quote_data, index=quote_headers, name=f'{self.ticker} Key Data', dtype='string')

            driver.implicitly_wait(3)

            # Returns dataframe table
            return quote_s

        else:
            raise ValueError('Ticker does not exist. Please check again.')
            

    
    def income_statement(self):
        '''
        Get Income Statement from Financials page
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials'
            driver = self.driver

            # Navigate to FINANCIALS, INCOME STATEMENT URL
            self.remove_logging()
            driver.get(URL)

            # Buffer
            driver.implicitly_wait(3)

            # get xpath values for income statement page
            # table element
            income_table = "//table[contains(@class, 'table table--overflow align--right')]"
            # elements of header
            income_headers = "//table[contains(@class, 'table table--overflow align--right')]//th"
            # elements of rows
            income_rows = "//table[contains(@class, 'table table--overflow align--right')]/tbody/tr"

            # Dataframe = Rows, Index, Columns
            # Locate income statement headers
            income_headers_loc = driver.find_elements_by_xpath(income_headers)
            income_headers_len = len(income_headers_loc)

            # Locate dataframe index
            income_rows_loc = driver.find_elements_by_xpath(income_rows)
            income_rows_len = len(income_rows_loc)

            # Lists to add into dataframe
            income_column_list = []
            income_row_index_list = []
            # Create lists of lists depending on how many rows are there.
            income_data_list = [[] for i in range(income_headers_len-1)]

            #### GET COLUMNS OF DATAFRAME ####
            # //table[contains(@class, 'table table--overflow align--right')]//th[i]/div
            for i in range(1,income_headers_len + 1):
                headers = driver.find_element_by_xpath(f"//table[contains(@class, 'table table--overflow align--right')]//th[{i}]/div").text
                income_column_list.append(headers)
                # print(f"Header name : {headers}.")

            #### GET ROW INDEX OF DATAFRAME ####
            for i in range(0, income_rows_len):
                # //table[contains(@class, 'table table--overflow align--right')]/tbody/tr[{i+1}]/td[1]/div[2], xpath link, then converts to text
                row_index = driver.find_element_by_xpath(f"//table[contains(@class, 'table table--overflow align--right')]/tbody/tr[{i+1}]/td[1]/div[1]").text
                income_row_index_list.append(row_index)
                # print(f"Index name : {row_index}.")

                #### GET DATA OF DATAFRAME ####
                for x in range(2, income_headers_len + 1):
                    # loop html td from 2 - 7, get xpath link, then convert value to text
                    data = driver.find_element_by_xpath(f"//table[contains(@class, 'table table--overflow align--right')]/tbody/tr[{i+1}]/td[{x}]/div").text
                    # Append x-2 list depending on which data is being pulled
                    income_data_list[x-2].append(data)

            # Create dataframe for viewing
            income_df = pd.DataFrame(index=income_row_index_list, columns=income_column_list)

            # REMOVE 0 index of income_column_list
            income_column_list.pop(0)

            # Add data into dataframe, for index 0, 1, 2, 3, 4, 5
            for i in range(0, income_headers_len-1):
                income_df[f'{income_column_list[i]}'] = income_data_list[i]
                # print(f"Data added to {income_column_list[i]}.")

            # Drop last column of dataframe
            income_df = income_df.drop(columns=[f'{income_column_list[-1]}'])
            # print(f"{income_column_list[-1]} COLUMN dropped.")

            # SET Index as {ticker} Income Statement
            income_df = income_df.rename_axis(f'{self.ticker} Income Statement')

            # Drop first column
            income_df = income_df.drop(columns='ITEM')

            # Output to run
            # print("Income Statement Table:")
            # print(income_df)

            # Returns dataframe
            return income_df

        else:
            raise ValueError('Ticker does not exist. Please check again.')

    
    def balance_sheet_assets(self):
        '''
        Get Balance Sheet, Assets from Financials page
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/balance-sheet'
            driver = self.driver

            # Navigate to FINANCIALS, BALANCE SHEET URL
            self.remove_logging()
            driver.get(URL)

            # Buffer
            driver.implicitly_wait(3)

            ######## ASSETS TABLE ########
            # get xpath values for assets, balance sheet statement page
            # table element
            assets_table = "//table[contains(@class, 'table table--overflow align--right')]"
            # elements of header (index 1-7 for HTML Assets), use th to iterate
            assets_headers = "//div[contains(@class, 'element element--table table--data')][1]/div/div/table/thead/tr/th"
            # elements of rows , use tr to iterate
            assets_rows = "//div[contains(@class, 'element element--table table--data')][1]/div/div/table/tbody/tr"

            # Dataframe = Rows, Index, Columns
            # Locate assets, balance sheet headers
            assets_headers_loc = driver.find_elements_by_xpath(assets_headers)
            assets_headers_len = len(assets_headers_loc)

            # Locate dataframe index
            assets_rows_loc = driver.find_elements_by_xpath(assets_rows)
            assets_rows_len = len(assets_rows_loc)

            # Lists to add into dataframe
            assets_column_list = []
            assets_row_index_list = []
            # Create lists of lists depending on how many rows are there.
            assets_data_list = [[] for i in range(assets_headers_len-1)]

            #### GET COLUMNS OF DATAFRAME ####
            # Uses xpath to get header string val
            for i in range(1,assets_headers_len + 1):
                headers = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][1]/div/div/table/thead/tr/th[{i}]/div").text
                assets_column_list.append(headers)
                # print(f"Header name : {headers}.")

            #### GET ROW INDEX OF DATAFRAME ####
            for i in range(0, assets_rows_len):
                # Uses xpath to get table index vals
                row_index = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][1]/div/div/table/tbody/tr[{i+1}]/td[1]/div[1]").text
                assets_row_index_list.append(row_index)
                # print(f"Index name : {row_index}.")

                #### GET DATA OF DATAFRAME ####
                for x in range(2, assets_headers_len + 1):
                    # loop html td from 2 - 7, get xpath link, then convert value to text
                    data = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][1]/div/div/table/tbody/tr[{i+1}]/td[{x}]/div[1]").text
                    # Append x-2 list depending on which data is being pulled
                    assets_data_list[x-2].append(data)

            # Create dataframe for viewing
            assets_df = pd.DataFrame(index=assets_row_index_list, columns=assets_column_list)

            # REMOVE 0 index of assets_column_list
            assets_column_list.pop(0)

            # Add data into dataframe, for index 0, 1, 2, 3, 4, 5
            for i in range(0, assets_headers_len-1):
                assets_df[f'{assets_column_list[i]}'] = assets_data_list[i]
                # print(f"Data added to {assets_column_list[i]}.")

            # Drop last column of dataframe
            assets_df = assets_df.drop(columns=[f'{assets_column_list[-1]}'])
            # print(f"{assets_column_list[-1]} COLUMN dropped.")

            # SET Index as {ticker} Assets, Balance sheet
            assets_df = assets_df.rename_axis(f'{self.ticker} Assets, Balance Sheet')

            # Drop first column
            assets_df = assets_df.drop(columns='ITEM')

            # Output to run
            # print("Assets Balance Sheet Table: ")
            # print(assets_df)

            # Returns dataframe
            return assets_df
        
        else:
            raise ValueError('Ticker does not exist. Please check again.')
    
    
    
    def balance_sheet_lia(self):
        '''
        Get Balance Sheet, Libabilities from Financials page
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/balance-sheet'
            driver = self.driver

            # Navigate to FINANCIALS, BALANCE SHEET URL
            self.remove_logging()
            driver.get(URL)

            # get xpath values for liabilities, balance sheet statement page
            # table element
            lia_table = "//table[contains(@class, 'table table--overflow align--right')]"
            # elements of header (index 1-7 for HTML Liabilities), use th to iterate
            lia_headers = "//div[contains(@class, 'element element--table table--data')][2]/div/div/table/thead/tr/th"
            # elements of rows , use tr to iterate
            lia_rows = "//div[contains(@class, 'element element--table table--data')][2]/div/div/table/tbody/tr"

            # Dataframe = Rows, Index, Columns
            # Locate liabilities, balance sheet headers
            lia_headers_loc = driver.find_elements_by_xpath(lia_headers)
            lia_headers_len = len(lia_headers_loc)

            # Locate dataframe index
            lia_rows_loc = driver.find_elements_by_xpath(lia_rows)
            lia_rows_len = len(lia_rows_loc)

            # Lists to add into dataframe
            lia_column_list = []
            lia_row_index_list = []
            # Create lists of lists depending on how many rows are there.
            lia_data_list = [[] for i in range(lia_headers_len-1)]

            #### GET COLUMNS OF DATAFRAME ####
            # Uses xpath to get header string val
            for i in range(1,lia_headers_len + 1):
                headers = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][2]/div/div/table/thead/tr/th[{i}]/div").text
                lia_column_list.append(headers)
                # print(f"Header name : {headers}.")

            #### GET ROW INDEX OF DATAFRAME ####
            for i in range(0, lia_rows_len):
                # Uses xpath to get table index vals
                row_index = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][2]/div/div/table/tbody/tr[{i+1}]/td[1]/div[1]").text
                lia_row_index_list.append(row_index)
                # print(f"Index name : {row_index}.")

                #### GET DATA OF DATAFRAME ####
                for x in range(2, lia_headers_len + 1):
                    # loop html td from 2 - 7, get xpath link, then convert value to text
                    data = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][2]/div/div/table/tbody/tr[{i+1}]/td[{x}]/div[1]").text
                    # Append x-2 list depending on which data is being pulled
                    lia_data_list[x-2].append(data)

            # Create dataframe for viewing
            lia_df = pd.DataFrame(index=lia_row_index_list, columns=lia_column_list)

            # REMOVE 0 index of lia_column_list
            lia_column_list.pop(0)

            # Add data into dataframe, for index 0, 1, 2, 3, 4, 5
            for i in range(0, lia_headers_len-1):
                lia_df[f'{lia_column_list[i]}'] = lia_data_list[i]
                # print(f"Data added to {lia_column_list[i]}.")

            # Drop last column of dataframe
            lia_df = lia_df.drop(columns=[f'{lia_column_list[-1]}'])
            # print(f"{lia_column_list[-1]} COLUMN dropped.")

            # SET Index as {ticker} Liabilities, Balance sheet
            lia_df = lia_df.rename_axis(f'{self.ticker} Liabilities, Balance Sheet')

            # Drop first column
            lia_df = lia_df.drop(columns='ITEM')

            # Output to run
            # print("Liabilities Balance Sheet Table: ")
            # print(lia_df)

            # Returns dataframe
            return lia_df

        else:
            raise ValueError('Ticker does not exist. Please check again.')

    
    def cash_flow_opr(self):
        '''
        Get Cash Flow, Operating Activies from Financials page
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'
            driver = self.driver

            # Navigate to FINANCIALS, CASH FLOW URL
            self.remove_logging()
            driver.get(URL)

            # Buffer
            driver.implicitly_wait(3)

            # get xpath values for operating activities, cash flow statement page
            # table element
            opr_table = "//table[contains(@class, 'table table--overflow align--right')][1]"
            # elements of header (index 1-7 for HTML Operating Activities), use th to iterate
            opr_headers = "//div[contains(@class, 'element element--table table--data')][1]/div/div/table/thead/tr/th"
            # elements of rows , use tr to iterate
            opr_rows = "//div[contains(@class, 'element element--table table--data')][1]/div/div/table/tbody/tr"

            # Dataframe = Rows, Index, Columns
            # Locate Operating Activities, cash flow headers
            opr_headers_loc = driver.find_elements_by_xpath(opr_headers)
            opr_headers_len = len(opr_headers_loc)

            # Locate dataframe index
            opr_rows_loc = driver.find_elements_by_xpath(opr_rows)
            opr_rows_len = len(opr_rows_loc)

            # Lists to add into dataframe
            opr_column_list = []
            opr_row_index_list = []
            # Create lists of lists depending on how many rows are there.
            opr_data_list = [[] for i in range(opr_headers_len-1)]

            #### GET COLUMNS OF DATAFRAME ####
            # Uses xpath to get header string val
            for i in range(1,opr_headers_len + 1):
                headers = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][1]/div/div/table/thead/tr/th[{i}]/div").text
                opr_column_list.append(headers)
                # print(f"Header name : {headers}.")

            #### GET ROW INDEX OF DATAFRAME ####
            for i in range(0, opr_rows_len):
                # Uses xpath to get table index vals
                row_index = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][1]/div/div/table/tbody/tr[{i+1}]/td[1]/div[1]").text
                opr_row_index_list.append(row_index)
                # print(f"Index name : {row_index}.")

                #### GET DATA OF DATAFRAME ####
                for x in range(2, opr_headers_len + 1):
                    # loop html td from 2 - 7, get xpath link, then convert value to text
                    data = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][1]/div/div/table/tbody/tr[{i+1}]/td[{x}]/div[1]").text
                    # Append x-2 list depending on which data is being pulled
                    opr_data_list[x-2].append(data)

            # Create dataframe for viewing
            opr_df = pd.DataFrame(index=opr_row_index_list, columns=opr_column_list)

            # REMOVE 0 index of opr_column_list
            opr_column_list.pop(0)

            # Add data into dataframe, for index 0, 1, 2, 3, 4, 5
            for i in range(0, opr_headers_len-1):
                opr_df[f'{opr_column_list[i]}'] = opr_data_list[i]
                # print(f"Data added to {opr_column_list[i]}.")

            # Drop last column of dataframe
            opr_df = opr_df.drop(columns=[f'{opr_column_list[-1]}'])
            # print(f"{opr_column_list[-1]} COLUMN dropped.")

            # SET Index as {ticker} Operating Activities, Cash Flow
            opr_df = opr_df.rename_axis(f'{self.ticker} Operating Activities, Cash Flow')

            # Drop first column
            opr_df = opr_df.drop(columns='ITEM')

            # Output to run
            # print("Operating Activies, Cash Flow Table: ")
            # print(opr_df)

            # Returns dataframe
            return opr_df

        else:
            raise ValueError('Ticker does not exist. Please check again.')

    
    def cash_flow_inv(self):
        '''
        Get Cash Flow, Investing Activies from Financials page
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'
            driver = self.driver

            # Navigate to FINANCIALS, CASH FLOW URL
            self.remove_logging()
            driver.get(URL)

            # Buffer
            driver.implicitly_wait(3)

            # get xpath values for investing activities, cash flow statement page
            # table element
            inv_table = "//table[contains(@class, 'table table--overflow align--right')][2]"
            # elements of header (index 1-7 for HTML Investing Activities), use th to iterate
            inv_headers = "//div[contains(@class, 'element element--table table--data')][2]/div/div/table/thead/tr/th"
            # elements of rows , use tr to iterate
            inv_rows = "//div[contains(@class, 'element element--table table--data')][2]/div/div/table/tbody/tr"

            # Dataframe = Rows, Index, Columns
            # Locate Investing Activities, cash flow headers
            inv_headers_loc = driver.find_elements_by_xpath(inv_headers)
            inv_headers_len = len(inv_headers_loc)

            # Locate dataframe index
            inv_rows_loc = driver.find_elements_by_xpath(inv_rows)
            inv_rows_len = len(inv_rows_loc)

            # Lists to add into dataframe
            inv_column_list = []
            inv_row_index_list = []
            # Create lists of lists depending on how many rows are there.
            inv_data_list = [[] for i in range(inv_headers_len-1)]

            #### GET COLUMNS OF DATAFRAME ####
            # Uses xpath to get header string val
            for i in range(1,inv_headers_len + 1):
                headers = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][2]/div/div/table/thead/tr/th[{i}]/div").text
                inv_column_list.append(headers)
                # print(f"Header name : {headers}.")

            #### GET ROW INDEX OF DATAFRAME ####
            for i in range(0, inv_rows_len):
                # Uses xpath to get table index vals
                row_index = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][2]/div/div/table/tbody/tr[{i+1}]/td[1]/div[1]").text
                inv_row_index_list.append(row_index)
                # print(f"Index name : {row_index}.")

                #### GET DATA OF DATAFRAME ####
                for x in range(2, inv_headers_len + 1):
                    # loop html td from 2 - 7, get xpath link, then convert value to text
                    data = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][2]/div/div/table/tbody/tr[{i+1}]/td[{x}]/div[1]").text
                    # Append x-2 list depending on which data is being pulled
                    inv_data_list[x-2].append(data)

            # Create dataframe for viewing
            inv_df = pd.DataFrame(index=inv_row_index_list, columns=inv_column_list)

            # REMOVE 0 index of inv_column_list
            inv_column_list.pop(0)

            # Add data into dataframe, for index 0, 1, 2, 3, 4, 5
            for i in range(0, inv_headers_len-1):
                inv_df[f'{inv_column_list[i]}'] = inv_data_list[i]
                # print(f"Data added to {inv_column_list[i]}.")

            # Drop last column of dataframe
            inv_df = inv_df.drop(columns=[f'{inv_column_list[-1]}'])
            # print(f"{inv_column_list[-1]} COLUMN dropped.")

            # SET Index as {ticker} Investing Activities, Cash Flow
            inv_df = inv_df.rename_axis(f'{self.ticker} Investing Activies, Cash Flow')

            # Drop first column
            inv_df = inv_df.drop(columns='ITEM')

            # Output to run
            # print("Investing Activies, Cash Flow Table: ")
            # print(inv_df)

            # Returns dataframe
            return inv_df

        else:
            raise ValueError('Ticker does not exist. Please check again.')

    
    def cash_flow_fin(self):
        '''
        Get Cash Flow, Financing Activities from Financials page
        # Returns pandas DataFrame
        '''

        # Check if ticker exists
        exist = self.check_ticker()
        if exist == True:
            # URL Settings and initialise driver as self.driver
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'
            driver = self.driver

            # Navigate to FINANCIALS, CASH FLOW URL
            self.remove_logging()
            driver.get(URL)

            # Buffer
            driver.implicitly_wait(3)

            # get xpath values for financing activities, cash flow statement page
            # table element
            fin_table = "//table[contains(@class, 'table table--overflow align--right')][3]"
            # elements of header (index 1-7 for HTML Financing Activities), use th to iterate
            fin_headers = "//div[contains(@class, 'element element--table table--data')][3]/div/div/table/thead/tr/th"
            # elements of rows , use tr to iterate
            fin_rows = "//div[contains(@class, 'element element--table table--data')][3]/div/div/table/tbody/tr"

            # Dataframe = Rows, Index, Columns
            # Locate Financing Activities, cash flow headers
            fin_headers_loc = driver.find_elements_by_xpath(fin_headers)
            fin_headers_len = len(fin_headers_loc)

            # Locate dataframe index
            fin_rows_loc = driver.find_elements_by_xpath(fin_rows)
            fin_rows_len = len(fin_rows_loc)

            # Lists to add into dataframe
            fin_column_list = []
            fin_row_index_list = []
            # Create lists of lists depending on how many rows are there.
            fin_data_list = [[] for i in range(fin_headers_len-1)]

            #### GET COLUMNS OF DATAFRAME ####
            # Uses xpath to get header string val
            for i in range(1,fin_headers_len + 1):
                headers = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][3]/div/div/table/thead/tr/th[{i}]/div").text
                fin_column_list.append(headers)
                # print(f"Header name : {headers}.")

            #### GET ROW INDEX OF DATAFRAME ####
            for i in range(0, fin_rows_len):
                # Uses xpath to get table index vals
                row_index = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][3]/div/div/table/tbody/tr[{i+1}]/td[1]/div[1]").text
                fin_row_index_list.append(row_index)
                # print(f"Index name : {row_index}.")

                #### GET DATA OF DATAFRAME ####
                for x in range(2, fin_headers_len + 1):
                    # loop html td from 2 - 7, get xpath link, then convert value to text
                    data = driver.find_element_by_xpath(f"//div[contains(@class, 'element element--table table--data')][3]/div/div/table/tbody/tr[{i+1}]/td[{x}]/div[1]").text
                    # Append x-2 list depending on which data is being pulled
                    fin_data_list[x-2].append(data)

            # Create dataframe for viewing
            fin_df = pd.DataFrame(index=fin_row_index_list, columns=fin_column_list)

            # REMOVE 0 index of fin_column_list
            fin_column_list.pop(0)

            # Add data into dataframe, for index 0, 1, 2, 3, 4, 5
            for i in range(0, fin_headers_len-1):
                fin_df[f'{fin_column_list[i]}'] = fin_data_list[i]
                # print(f"Data added to {fin_column_list[i]}.")

            # Drop last column of dataframe
            fin_df = fin_df.drop(columns=[f'{fin_column_list[-1]}'])
            # print(f"{fin_column_list[-1]} COLUMN dropped.")

            # SET Index as {ticker} Financing Activities, Cash Flow
            fin_df = fin_df.rename_axis(f'{self.ticker} Financing Activies, Cash Flow')

            # Drop first column
            fin_df = fin_df.drop(columns='ITEM')

            # Output to run
            # print("Financing Activies, Cash Flow Table: ")
            # print(fin_df)

            # Returns dataframe
            return fin_df

        else:
            raise ValueError('Ticker does not exist. Please check again.')
    
    
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

        # Return
        return years
    

    def fiscal_month(self):
        '''
        Get starting month of Fiscal Year for stock.
        # Returns int
        '''

        exist = self.check_ticker()
        if exist == True:
            # URL to check for valuations table.
            URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

            # Navigate to PROFILE URL
            self.remove_logging()
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
        time.sleep(1)
        self.driver.quit()
        return 'Driver successfully quit.'

