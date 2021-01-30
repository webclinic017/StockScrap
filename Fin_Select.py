from Fin_Data import Fin_Data
import pandas as pd

# Class Fin_Select, inheritance from Fin_Data
class Fin_Select:
    '''
    # Financial Data Scrapper Made by Gavin Loo 2021.
    Uses data from MarketWatch.com
    Selects data from dataFrame provided by Fin_Data class. Then returns output.

    Args = year(int), item(str)
    '''

    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe'):
        '''
        Initialize Fin_Select class from Fin_Data (and other __init__ arguments) for DataFrame extraction.
        
        '''
        # Gets Fin_Data class inherits __init__ args
        self.ticker = ticker
        self.PATH = PATH


    def __repr__(self):
        '''
        Output when inspecting Class
        # Returns str
        '''

        return (f'{self.__class__.__name__}('f'{self.ticker!r}')


    def __str__(self):
        '''      
        Class print's output
        # Returns str
        '''

        return f'Selecting {self.ticker} financial data.'

    
    def select_isolate(self, from_df, year=None, item=None):
        '''
        Select's dataframe specific column and row for respective class arguments.
        # Returns str
        '''
        if year and item != None:
            try:
                val = from_df.loc[f'{item}',f'{year}']
                return val
            except KeyError:
                print('Input does not exist. Please double check args year and item again.')

        else:
            return None

    def select_year(self, from_df, year=None):
        '''
        Select's dataframe column for respective class arguments.
        # Returns pd.Series of rows
        '''
        if year != None:
            try:
                val = from_df.loc[f'{year}']
                return val
            except KeyError:
                print('Input does not exist. Please double check args year and item again.')

        
        else:
            return None
    

    def select_item(self, from_df, item=None):
        '''
        Select's dataframe row for respective class arguments.
        # Returns pd.Series of rows
        '''
        if item != None:
            try:
                val = from_df.loc[f'{item}']
                return val
            except KeyError:
                print('Input does not exist. Please double check args year and item again.')
        
        else: 
            return None


# ticker = 'D05'
# stock = Fin_Data(ticker)
# select = Fin_Select(ticker, 2020, 'EPS (Diluted)')
# income_statement = stock.income_statement()

# sales = select.select_item(income_statement)
# sales_2020 = sales[-1]
# print(sales_2020)
# print(type(sales_2020))
# print(type(sales))

# print(select)
# stock.driver_end()



