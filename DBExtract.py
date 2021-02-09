from Fin_Extract import Fin_Extract
import pandas as pd
import numpy as np


class DBExtract(Fin_Extract):
    '''
    Database Extractor. Able to get files in a JSON format and extract them, in either view format or data format.
    Methods:
        select_item()
        - Get certain rows
        select_isolate()
        - Get specific cell
    '''

    def __init__(self, DB_PATH='C:/Users/Gavin/Desktop/FinData'):
        '''
        Initialize DBExtract Class and its attributes.
        '''
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
    

    def json_extract(self, format, country = "U.S.", ticker = "TSLA", FILE_NAME='StockInformation'):
        '''
        Extract dataframe/series from JSON file.
        # Returns pandas DataFrame or pandas Series
        Format Args:
            "view" Format: for viewing, formatted
            "data" Format: for analysis, big numbers, floats etc
        
        '''

        path = f'{self.DB_PATH}/{country}/{ticker[0]}/{ticker}/{FILE_NAME}'
        try:
            df = pd.read_json(path)
            if format == 'data': 
                df = df.applymap(self.str_to_val)
            # If dosen't work, json object is a series.
        except ValueError:
            df = pd.read_json(path, typ='series')
            if format == 'data': 
                df = df.map(self.str_to_val)

        
        return df
