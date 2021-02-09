from Fin_Extract import Fin_Extract
import pandas as pd
import numpy as np


class DBExtract(Fin_Extract):
    '''
    Database Extractor. Able to get files in a JSON format and extract them, in either view format or data format.
    View Format: for viewing, formatted
    Data Format: for analysis, big numbers, floats etc
     - certain rows
     - certain columns
    '''

    def __init__(self, format, DB_PATH='C:/Users/Gavin/Desktop/FinData'):
        '''
        Initialize DBExtract Class and its attributes.
        '''
        self.format = format
        self.DB_PATH = DB_PATH

    
    def __repr__(self):
        '''
        Output when inspecting Class
        # Returns str
        '''

        return f'{self.__class__.__name__}({self.format!r}, {self.DB_PATH})'


    def __str__(self):
        '''      
        Class print's output
        # Returns str
        '''

        return f'''
/----------
# DBExtract Parameters
Extraction Type: {self.format}
Database PATH: {self.DB_PATH}
/----------
        '''

    
    def json_extract(self, exchange = "U.S. Nasdaq", ticker = "TSLA", FILE_NAME='StockInformation'):
        '''
        Extract dataframe from JSON file.
        # Returns pandas DataFrame or pandas Series
        '''

        path = f'{self.DB_PATH}/{exchange}/{ticker[0]}/{ticker}/{FILE_NAME}'
        df = pd.read_json(path, typ='series')
        
        return df


# db = DBExtract("data")
# df = db.json_extract()
# print(df)
