from Fin_Data import Fin_Data
import pandas as pd

# Class Fin_Select, inheritance from Fin_Data
class Fin_Select:
    '''
    The Fin_Select class allows selection of specific cells or rows Then, it is able to convert values into scientific values for analysis purposes. Inherits Fin_Select class.
    Attributes are:
        ticker : str
            Specifies which ticker to select data from. (Required)
    '''

    def __init__(self, ticker):
        self.ticker = ticker


    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.ticker!r}')


    def __str__(self):
        return f'Selecting {self.ticker} financial data.'

    
    def select_isolate(self, from_df, year=None, item=None):
        '''
        Selects pandas DataFrame specific column and row for respective arguments.
        Arguments are:
            from_df : pandas DataFrame
                Specifies what DataFrame to get list of columns from. (Required)
            year : int
                Specifies which column to get data from. Default is None (Optional)
            item : str
                Specifies which row to get data from. Default is None (Optional)
        Returns: str
            Returns string of specific cell.
        '''
        if year and item != None:
            try:
                val = from_df.loc[f'{item}',f'{year}']
                return val
            except KeyError:
                print('Input does not exist. Please double check args year and item again.')

        else:
            return None


    def select_item(self, from_df, item=None):
        '''
        Selects pandas DataFrame specific row for respective arguments.
        Arguments are:
            from_df : pandas DataFrame
                Specifies what DataFrame to get list of columns from. (Required)
            item : str
                Specifies which row to get data from. Default is None (Optional)
        Returns: pandas Series
            Returns pandas Series of row.
        '''
        if item != None:
            try:
                val = from_df.loc[f'{item}']
                return val
            except KeyError:
                print('Input does not exist. Please double check args year and item again.')
        
        else: 
            return None


    def select_year(self, from_df, year=None):
        '''
        Selects pandas DataFrame specific column for respective arguments.
        Arguments are:
            from_df : pandas DataFrame
                Specifies what DataFrame to get list of columns from. (Required)
            year  : int
                Specifies which row to get data from. Default is None (Optional)
        Returns: pandas Series
            Returns pandas Series of row.
        '''
        if item != None:
            try:
                val = from_df.loc[year]
                return val
            except KeyError:
                print('Input does not exist. Please double check args year and item again.')
        
        else: 
            return None
