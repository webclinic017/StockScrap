from TData import TData
from FData import FData
import pandas as pd
import numpy as np
import datetime as datetime


class Stock_Data(TData, FData):

    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe', candle_interval=1, print=False):
        '''
        Initialize FData and TData class then consolidate into Stock_Data class.
        '''
        TData.__init__(self, candle_interval=1, print=False)
        FData.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe')


    def __repr__(self):
        '''
        Output when inspecting Class
        # Returns str
        '''

        return (f'{self.__class__.__name__}('f'{self.ticker!r}, {self.PATH!r}, {self.period_years!r}, {self.candle_interval!r}, {self.print!r}')

    
    def __str__(self):
        '''      
        Class print's output
        # Returns str
        '''

        return f'''
        Returning Stock Data
        Financial Data for {self.ticker}, Chromedriver PATH = {self.PATH}
        Technical Data for years : {self.period_years}, Interval : {self.candle_interval}d
        '''

    def fiscal_year_prices(self):
        '''
        Gets fiscal year dates and open prices in a series
        # Returns pandas Series
        '''
        # Gets a list of fiscal year dates
        date_list = self.fiscal_year_dates()

        # Gets a series of prices
        prices = self.get_open(self.ticker)

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
        