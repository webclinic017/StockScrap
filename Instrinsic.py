######################################################################
# IMPORTS                                                            #
######################################################################
from Stock_Data import Stock_Data
import pandas as pd
import numpy as np
import time
import datetime

# Initialize Intrinsic Class
class Intrinsic:
    '''
    # Intrinsic Value Screener made by Gavin Loo 2021.
    Uses data from MarketWatch.com
    Returns Intrinsic Value for each stock holding using Diluted EPS.

    Args = ticker name(str), margin of safety in percent(float), average pe ratio over years(float), discount rate in percent(float), dataframe of eps years(pandas DataFrame/ Series), or list of eps years(list)
    returns float
    '''
    
    def __init__(self, margin_safety=0.30, avg_pe_ratio=10.0, discount_rate=0.12, eps_df=None, eps_list=None):
        '''
        Initialize Intrinsic Class.
        '''
        
        self.ticker = ticker
        self.margin_safety = margin_safety
        self.avg_pe_ratio = avg_pe_ratio
        self.discount_rate = discount_rate
        self.eps_df = eps_df
        self.eps_list = eps_list


    def __repr__(self):
        '''
        Output when inspecting Class
        # Returns str
        '''

        return (f'{self.__class__.__name__}('f'{self.margin_safety!r}, {self.avg_pe_ratio!r}, {self.discount_rate!r}, {self.eps_df!r}, {self.eps_list!r}')


    def __str__(self):
        '''      
        Class print's output
        # Returns str
        '''

        return f'''
        Getting Instrinsic value for stock. 
        Average PE RATIO : {self.avg_pe_ratio}
        Margin of Saefety : {self.margin_safety}
        Discount Rate : {self.discount_rate}

        Dataframe : {self.eps_df}
        List : {self.eps_list}
        '''
        

    

        
    

        





     

