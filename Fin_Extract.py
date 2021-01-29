from Fin_Data import Fin_Data
from Fin_Select import Fin_Select
import pandas as pd
import numpy as np


# Class Fin_Extract, inheritance from Fin_Data and Fin_Select
class Fin_Extract(Fin_Select):
    '''
    # Financial Data Scrapper Made by Gavin Loo 2021.
    Uses data from MarketWatch.com
    Uses Fin_Select Class to extract individual data in str/pandas format. Then converts it into values

    "K" = Thousand, 1_000
    "M" = Million, 1_000_000
    "B" = Billion, 1_000_000_000
    "T" = Trillion, 1_000_000_000_000
    "%" = 0.01
    "()" = -, Negative
    "-" = NaN, No Values

    Args = None
    '''
    
    # List of symbols to be checked in class
    list_symbols = [
            'K', 'M', 'B', 'T', '%', '(', '-'
    ]

    # Dictionary of symbols and their values
    dict_symbols = {
        'K' : 1_000,
        'M' : 1_000_000,
        'B' : 1_000_000_000,
        'T' : 1_000_000_000_000,
        '%' : 0.01,
        '(' : -1,
        '-' : None
    }

    # Initializes Fin_Extract class inherits __init__ args
    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe'):
        Fin_Select.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe')
    

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


    def determine_symbol(self, cell_val):
        '''
        Determines symbol in table cell. Gets symbol of cell, 
        cell_val = str
        # Returns list of str
        '''

        # Output list of symbols found
        list_extract = []

        # For loop to check whether symbol exists in cell
        for sym in self.list_symbols:
            # If symbol corresponds to either symbol in list, extracted_symbol = sym
            if f"{sym}" in cell_val:
                extracted_symbol = sym
                list_extract.append(extracted_symbol)
            
            # Else, extracted_symbol = "" aka none.
            else:
                extracted_symbol = None

        return list_extract


    def str_to_val(self, cell_val):
        '''
        Converts string with symbols to value.
        # Returns float64
        '''
        # List of symbols in cells
        sym_in_cell = self.determine_symbol(cell_val)

        # Get Multiplier List
        multiplier_list = []
        for sym in sym_in_cell:
            m_val = self.dict_symbols.get(sym)
            multiplier_list.append(m_val)

        # Multiplies all elements in multiplier_list by converting all data into 64bit data to store larger denominations
        multiplier = np.prod(np.array(multiplier_list, dtype=np.float64))  

        # Initalize formatted_val var
        formatted_val = cell_val
        # Remove all unwanted symbols from cell_val
        for sym in sym_in_cell:
            formatted_val = formatted_val.replace(sym, '')
        
        # Other symbol to remove
        formatted_val = formatted_val.replace(')', '')
        
        # Get true cell value
        val = float(formatted_val) * multiplier
        val = int(val)

        return val

    def cell_true_val(self, cell_val):
        '''
        Determines value in table cell. Must cell value or pandas Series, 
        symbol = str, cell_val = str
        # Returns float64
        '''
        # If input is a string, and not % or -
        if type(cell_val) == str and ('%' and '-') not in self.determine_symbol(cell_val):
            val = self.str_to_val(cell_val)
            val = int(val)
            return val

        if type(cell_val) == str and '%' in self.determine_symbol(cell_val):
            val = self.str_to_val(cell_val)
            val = float(val)
            return val
        
        if type(cell_val) == str and '-' in self.determine_symbol(cell_val):
            return None
        
        # If input is a pandas Series, not % or -
        if isinstance(cell_val, pd.Series) and ('%' and '-') not in self.determine_symbol(cell_val):
            series = cell_val
            # Get list from series
            old_val = series.tolist()

            new_val = []
            # Iterate inside list
            for element in old_val:
                val = self.str_to_val(element)
                val = int(val)
                new_val.append(val)

            print(new_val)
            # Get index list
            list_index = series.index.values.tolist()
            
            new_series = pd.Series(new_val, index=list_index, dtype=np.int64)
            return new_series

        # If input is a pandas Series, %
        if isinstance(cell_val, pd.Series) and '%' in self.determine_symbol(cell_val):
            series = cell_val
            # Get list from series
            old_val = series.tolist()

            new_val = []
            # Iterate inside list
            for element in old_val:
                val = self.str_to_val(element)
                val = float(val)
                new_val.append(val)

            print(new_val)
            # Get index list
            list_index = series.index.values.tolist()
            
            new_series = pd.Series(new_val, index=list_index, dtype=np.float64)
            return new_series

        # If input is a pandas Series, -
        if isinstance(cell_val, pd.Series) and '-' in self.determine_symbol(cell_val):
            series = cell_val
            # Get list from series
            old_val = series.tolist()

            print(new_val)
            # Get index list
            list_index = series.index.values.tolist()
            
            new_series = pd.Series(0, index=list_index, dtype=np.int64)
            return new_series
        
        else:
            return 'Symbol not defined. Please check dataframe again.'                
        