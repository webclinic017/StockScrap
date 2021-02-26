from Fin_Extract import Fin_Extract
import pandas as pd
import numpy as np


class DBExtract(Fin_Extract):
    '''
    The DBExtract class is the database extraction component. It allows one to pull data from database and display in a string or pandas DataFrame format. Inherits Fin_Extract class.
    Attributes are:
        DB_PATH : str
            Specifies database directory to extract data from. Default is 'C:/Users/rawsashimi1604/Desktop/FinData' (Optional)
    '''

    def __init__(self, DB_PATH='C:/Users/Gavin/Desktop/FinData'):
        self.DB_PATH = DB_PATH

    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.format!r}, {self.DB_PATH})'


    def __str__(self):
        return f'''
/----------
# DBExtract Parameters
Extraction Type: {self.format}
Database PATH: {self.DB_PATH}
/----------
        '''
    

    def json_extract(self, format, country = "U.S.", ticker = "TSLA", FILE_NAME='StockInformation', dtype='object'):
        '''
        Extracts pandas DataFrame from JSON file.
        Arguments are:
            format : str
                Specifies which format to view in dataframe. (Required) Available parameters are:
                    "view" - view in default format.
                    "data" - view in scientific data format.
            ticker : str
                Specifies which ticker to extract. (Required)
            country : str
                Specifies which country ticker is from. Default is "U.S." (Optional)
            FILE_NAME : str
                Specifies which data file to pull from. Default is "StockInformation" (Optional) Available "FILE_NAME":
                    "BalanceSheet_Assets"
                    "BalanceSheet_Liabilities"
                    "CashFlow_Financing"
                    "CashFlow_Investing"
                    "CashFlow_Operating"
                    "IncomeStatement"
                    "KeyData"
                    "PriceData"
                    "Profile_Capitalization"
                    "Profile_Efficiency"
                    "Profile_Liquidity"
                    "Profile_Profitability"
                    "Profile_Valuations"
                    "StockInformation"
            dtype : str
                Specifies what type of data. Default is "object" (Optional)

        Returns: pandas DataFrame or pandas Series
            Returns dataframe or series of extracted file.
        '''

        path = f'{self.DB_PATH}/{country}/{ticker[0]}/{ticker}/{FILE_NAME}'
        try:
            df = pd.read_json(path, dtype='object')
            if format == 'data': 
                df = df.applymap(self.str_to_val)
            # If dosen't work, json object is a series.
        except ValueError:
            df = pd.read_json(path, typ='series', dtype='object')
            if format == 'data': 
                df = df.map(self.str_to_val)

        
        return df
