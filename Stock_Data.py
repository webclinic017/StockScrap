from TData import TData
from FData import FData
from ToJson import ToJson
import pandas as pd
import numpy as np
import datetime as datetime
import time
from pathlib import Path


class Stock_Data(TData, FData, ToJson):
    '''
    Full stock data information scraper by Gavin Loo
    Uses data from YahooFinance and MarketWatch.com
    '''

    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe', ignore_errors=True):
        '''
        Initialize FData and TData class then consolidate into Stock_Data class.
        '''
        TData.__init__(self, ticker)
        FData.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe', ignore_errors=True)


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

        return f'''
        Returning Stock Data
        Financial / Technical Data for {self.ticker}, Chromedriver PATH = {self.PATH}
        '''

    def fiscal_year_prices(self):
        '''
        Gets fiscal year dates and open prices in a series
        # Returns pandas Series
        '''
        # Gets a list of fiscal year dates
        date_list = self.fiscal_year_dates()
        
        try:
            # Check if YFinance Ticker exists
            price = self.get_prevclose()
            prices = self.get_open()
            price_list = prices.index.tolist()

            # Convert date_list[0] to datetime object
            ###
            check_date = date_list[-1]
            datetime_obj = datetime.datetime.strptime(check_date, '%Y-%m-%d')

            # If date_list in price_list(series)
            if datetime_obj in price_list:
                # Create a list of selected prices and append it with prices
                sel_price = []
                # From fiscal year dates get prices
                for date in date_list:
                    price = prices.loc[f'{date}']
                    price = float(round(price, 2))
                    sel_price.append(price)
                
                # Create a pandas Series using prices and dates
                series = pd.Series(sel_price, index=date_list, name=f'Beginning of Fiscal Year Date and Corresponding Prices for {self.ticker}')
                return series
        
        except IndexError:
            print('Unable to get TData using current ticker. Please check for typos')
            pass

        else:
            raise KeyError('Price data not available at fiscal year date. Check company fundamentals for more information.')


        