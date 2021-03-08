from Fin_Data import Fin_Data
from Fin_Select import Fin_Select
import pandas as pd
import numpy as np


# Class Fin_Extract, inheritance from Fin_Data and Fin_Select
class Fin_Extract(Fin_Select):
    '''
    The Fin_Extract class allows extraction of data from str/ pandas DataFrame/ pandas Series format. Then, it is able to convert values into scientific values for analysis purposes. Inherits Fin_Select class.
    Attributes are:
        ticker : str
            Specifies which ticker to extract data from. (Required)
    '''
    
    # List of symbols to be checked in class
    list_symbols = [
            'K', 'M', 'B', 'T', '%', '(', '-', '$'
    ]

    # Dictionary of symbols and their values
    dict_symbols = {
        'K' : 1_000,
        'M' : 1_000_000,
        'B' : 1_000_000_000,
        'T' : 1_000_000_000_000,
        '%' : 0.01,
        '(' : -1,
        '-' : 1,
        '$' : 1
    }

    # Initializes Fin_Extract class inherits __init__ args
    def __init__(self, ticker):
        Fin_Select.__init__(self, ticker)
    

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.ticker!r}')


    def __str__(self):
        return f'Selecting {self.ticker} financial data.'


    def determine_symbol(self, cell_val):
        '''
        Determines what symbols are in string specified. Then returns a list of symbols.
        Arguments are:
            cell_val : str
                Specifies what string to get symbols from. (Required)
        Returns: list
            Returns list of symbols available in string.
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
        Converts string which contains symbols to either float or int value. Returns scientific value.
        Arguments are:
            cell_val : str
            Specifies what string to get symbols from. (Required)
        Returns: pandas dtype int64 / float64
            Returns scientific value of string in pandas datatype int64 or float64.
        '''
        # List of symbols in cells
        sym_in_cell = self.determine_symbol(cell_val) 
        
        # If it is a string do not convert anything
        count = 0
        for i in cell_val:
            if(i.isalpha()):
                count = count+1
        
        if count > 1:
            return cell_val
        
        # Else convert accordingly
        else:
            # Get Multiplier List
            multiplier_list = [1]
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
            formatted_val = formatted_val.replace(',', '')

            if '%' in sym_in_cell:
                # Get true cell value
                val = float(formatted_val) * multiplier
            
            elif '-' in sym_in_cell:
                # Val is none
                val = 0

            else:
                # Get true cell value
                val = float(formatted_val) * multiplier
                val = int(val)

            return val
            

    def extract(self, cell_val):
        '''
        Determines what type of data is passed into input. Then returns either a string or pandas Series of scientific values.
        Arguments are:
            cell_val : str / pandas Series
                Specifies what string(s) to get symbols from. (Required)
        Returns: pandas dtype int64 / float64 or pandas Series
            Returns scientific value of string in pandas datatype int64 or float64. Can also return pandas Series if cell_val is a pandas Series.
        '''

        # If input is a string
        if type(cell_val) == str:
            val = self.str_to_val(cell_val)

            return val
        
        # If input is a pandas Series
        if isinstance(cell_val, pd.Series):
            # Initial data series name
            name = cell_val.name

            # Series of cells selected
            series = cell_val

            # Get list from series
            old_val = series.tolist()

            new_val = []
            # Iterate inside list
            for element in old_val:
                val = self.str_to_val(element)
                new_val.append(val)

            # Get index list
            list_index = series.index.values.tolist()

            # If any element = 0, change to numpy.NaN
            new_val = [np.nan if x==0 else x for x in new_val]           
            # Check what kind of data was inputted
            type_check = max(new_val)

            dtype_ = 0
            if type(type_check) == int:
                dtype_ = np.int64
            
            elif type(type_check) == float:
                dtype_ = np.float64
            
            else:
                print('No successful int/float data type check. Please check inputted data again.')

            # Create new pandas Series using new extracted values.
            new_series = pd.Series(new_val, index=list_index, dtype=dtype_, name=name)
            return new_series
        
        else:
            print('Error extracting data. Please check items, year, ticker again.')
            return None         

        
    def extract_columns(self, from_df):
        '''
        Extracts list of columns from pandas DataFrame
        Arguments are:
            from_df : pandas DataFrame
                Specifies what DataFrame to get list of columns from. (Required)
        Returns: list
            Returns list of columns of pandas DataFrame
        '''
        col_list = []

        for col in from_df.columns:
            col_list.append(col)

        return col_list
        