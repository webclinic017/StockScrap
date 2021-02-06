from TData import TData
from FData import FData
from ToJson import ToJson
import pandas as pd
import numpy as np
import datetime as datetime
import time
from pathlib import Path


class Stock_Data(TData, FData, ToJson):

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


    def export(self):
        '''
        Exports stock data as a JSON file to database.
        # Returns None
        '''

        exp_datetime = datetime.datetime.today()
        exp_date = exp_datetime.strftime("%Y-%m-%d")

        ticker_index = self.ticker[0]
        
        # Get path for data export
        # data_path = fr'C:\\Users\\Dennis Loo.000\\Desktop\\Value_Investing_Screener\\Data\\{ticker_index}\{self.ticker}\{exp_date}'
        ## Create directory if directory does not exist
        p = Path(f'C:/Users/Dennis Loo.000/Desktop/Value_Investing_Screener/Data/{ticker_index}/{self.ticker}/{exp_date}')
        p.mkdir(parents=True, exist_ok=True)

        # Output to run
        print(f'''

********************************************************************************************************************
Data Downloaded from MarketWatch.com
Beginning Data Download for {self.ticker}.
        ''')
        # Price Data ----------------------------------------------------------------------------------------------
        # Export Price Datas
        price_data_df = self.get_data(self.ticker)
        price_data_name = 'PriceData'

        self.json(from_obj=price_data_df, export_to=p, filename=price_data_name)
        print('PriceData exported')

        # Stock Info ----------------------------------------------------------------------------------------------
        # Export Stock_Info
        stock_info_df = self.stock_info()
        stock_info_name = 'StockInformation'

        self.json(from_obj=stock_info_df, export_to=p, filename=stock_info_name)
        print('StockInfo exported')
        
        # Fiscal Year ----------------------------------------------------------------------------------------------
        # Export Fiscal Year Start Dates, and prices
        fiscal_df = self.fiscal_year_prices()
        fiscal_name = 'FiscalYear'

        self.json(from_obj=fiscal_df, export_to=p, filename=fiscal_name)
        print('FiscalYear exported')
        
        # Key Data ----------------------------------------------------------------------------------------------
        # Export KeyData
        keydata_df = self.main_page()
        keydata_name = 'KeyData'

        self.json(from_obj=keydata_df, export_to=p, filename=keydata_name)
        print('KeyData exported')

        # Profile Data ----------------------------------------------------------------------------------------------
        # Export Valuation
        val_df = self.valuations()
        val_name = 'Profile_Valuations'

        self.json(from_obj=val_df, export_to=p, filename=val_name)
        print('Profile_Valuations exported')
        #------------------------------
        # Export Efficiency
        eff_df = self.efficiency()
        eff_name = 'Profile_Efficiency'

        self.json(from_obj=eff_df, export_to=p, filename=eff_name)
        print('Profile_Efficiency exported')
        #------------------------------
        # Export Liquidity
        liq_df = self.liquidity()
        liq_name = 'Profile_Liquidity'

        self.json(from_obj=liq_df, export_to=p, filename=liq_name)
        print('Profile_Liquidity exported')
        #------------------------------
        # Export Profitability
        pro_df = self.profitability()
        pro_name = 'Profile_Profitability'

        self.json(from_obj=pro_df, export_to=p, filename=pro_name)
        print('Profile_Profitability exported')
        #------------------------------
        # Export Capitalization
        cap_df = self.captialization()
        cap_name = 'Profile_Capitalization'

        self.json(from_obj=cap_df, export_to=p, filename=cap_name)
        print('Profile_Capitalization exported')
        #------------------------------

        # IncomeStatement Data ----------------------------------------------------------------------------------------------
        inc_df = self.income_statement()
        inc_name = 'IncomeStatement'

        self.json(from_obj=inc_df, export_to=p, filename=inc_name)
        print('IncomeStatement exported')

        # BalanceSheet Data ----------------------------------------------------------------------------------------------
        # Export Assets
        balass_df = self.balance_sheet_assets()
        balass_name = 'BalanceSheet_Assets'

        self.json(from_obj=balass_df, export_to=p, filename=balass_name)
        print('BalanceSheet_Assets exported')
        #------------------------------
        # Export Liabilities
        ballib_df = self.balance_sheet_lia()
        ballib_name = 'BalanceSheet_Liabilities'

        self.json(from_obj=ballib_df, export_to=p, filename=ballib_name)
        print('BalanceSheet_Liabilities exported')
        #------------------------------

        # CashFlowStatement Data ----------------------------------------------------------------------------------------------
        # Export Operating Activities
        cfsopr_df = self.cash_flow_opr()
        cfsopr_name = 'CashFlow_Operating'

        self.json(from_obj=cfsopr_df, export_to=p, filename=cfsopr_name)
        print('CashFlow_Operating exported')
        #------------------------------
        # Export Investing Activities
        cfsinv_df = self.cash_flow_inv()
        cfsinv_name = 'CashFlow_Investing'

        self.json(from_obj=cfsinv_df, export_to=p, filename=cfsinv_name)
        print('CashFlow_Investing exported')
        #------------------------------
        # Export Financing Activities
        cfsfin_df = self.cash_flow_fin()
        cfsfin_name = 'CashFlow_Financing'

        self.json(from_obj=cfsfin_df, export_to=p, filename=cfsfin_name)
        print('CashFlow_Financing exported')
        #------------------------------

        
        # Output to run
        print(f'''
Finished Data Download for {self.ticker}, closing browser now.
********************************************************************************************************************

        ''')

        for i in range(10):
            print(f"[{10-i}] Waiting for next ticker.....")

        return None


        