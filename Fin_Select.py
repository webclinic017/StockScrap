from Fin_Data import Fin_Data
import pandas as pd

# Class Fin_Select, inheritance from Fin_Data
class Fin_Select(Fin_Data):
    '''
    # Financial Data Scrapper Made by Gavin Loo 2021.
    Uses data from MarketWatch.com
    Selects data from dataFrame provided by Fin_Data class. Then returns output.

    Args = ticker(str), year(int), item(str)
    '''
    def __init__(self, ticker, year, item):
        '''
        Initialize Fin_Select class, intialize ticker, year and item for DataFrame extraction.
        
        '''
        self.ticker = ticker
        self.year = year
        self.item = item


    def __repr__(self):
        '''
        Output when inspecting Class
        # Returns str
        '''

        return (f'{self.__class__.__name__}('f'{self.ticker!r}, {self.year!r}, {self.item!r}')


    def __str__(self):
        '''      
        Class print's output
        # Returns str
        '''

        return f'Selecting {self.item} data, Year {self.year} for stock {self.ticker}.'

    
    def select_isolate(self, from_df):
        '''
        Select's dataframe specific column and row for respective class arguments.
        # Returns str
        '''
        val = from_df.loc[f'{self.item}',f'{self.year}']
        return val


    def select_year(self, from_df):
        '''
        Select's dataframe column for respective class arguments.
        # Returns pd.Series of rows
        '''
        val = from_df.loc[f'{self.year}']
        return val
    

    def select_item(self, from_df):
        '''
        Select's dataframe row for respective class arguments.
        # Returns pd.Series of rows
        '''
        val = from_df.loc[f'{self.item}']
        return val


ticker = 'D05'
stock = Fin_Data(ticker)
select = Fin_Select(ticker, 2020, 'EPS (Diluted)')
income_statement = stock.income_statement()

sales = select.select_item(income_statement)
sales_2020 = sales[-1]
print(sales_2020)
print(type(sales_2020))
print(type(sales))

print(select)
stock.driver_end()




