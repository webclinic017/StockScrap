from TData import TData
from FData import FData
from ToJson import ToJson
import pandas as pd
import numpy as np
import datetime as datetime
import time
from pathlib import Path


class Stock_Data(TData, FData, ToJson):
    '''
    Full stock data information scraper by Gavin Loo
    Uses data from YahooFinance and MarketWatch.com
    '''

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

        return (f'{self.__class__.__name__}('f'{self.ticker!r}, {self.PATH!r}, {self.candle_interval!r}, {self.print!r}')

    
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
        price_ticker = self.ticker
        try:
            # Check if YFinance Ticker exists
            price = self.get_prevclose(price_ticker)
            prices = self.get_open(price_ticker)
        
        except IndexError:
            # Change ticker name
            price_ticker = price_ticker.replace(".", "-")
            prices = self.get_open(price_ticker)

        price_list = prices.index.tolist()

        # Convert date_list[0] to datetime object
        ###
        check_date = date_list[0]
        datetime_obj = datetime.datetime.strptime(check_date, '%Y-%m-%d')

        # If date_list in price_list(series)
        if datetime_obj in price_list:
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

        else:
            raise KeyError('Price data not available at fiscal year date. Check company fundamentals for more information.')

    

    def download(self, PATH='C:/Users/Dennis Loo.000/Desktop/FinData'):
        '''
        Exports stock data as a JSON file to database. Returns stock exists?
        # Returns booleans
        '''
        time.sleep(1)
        
        # Check if stock ticker exists
        exists = self.check_ticker()

       
        if exists == True:
            ## Create directory if directory does not exist
            exp_datetime = datetime.datetime.today()
            exp_date = exp_datetime.strftime("%Y-%m-%d")
            
            # Stock Exchange DIR Path
            exchange = self.exchange()
            exchange_path = exchange.replace(':', '')

            # Ticker Alphabet DIR Path
            ticker_index = self.ticker[0]

            # Path Class
            p = Path(f'{PATH}/{exchange_path}/{ticker_index}/{self.ticker}')
            p.mkdir(parents=True, exist_ok=True)

            # Output to run
            print(f'''

********************************************************************************************************************
Data Downloaded from MarketWatch.com
Beginning Data Download for {self.ticker}.
            ''')
            # Price Data ----------------------------------------------------------------------------------------------
            # Export Price Data
            price_ticker = self.ticker

            try:
                # Check if YFinance Ticker exists
                price = self.get_prevclose(price_ticker)

                price_data_df = self.get_data(price_ticker)
                

            except IndexError:
                # Change ticker name
                price_ticker = price_ticker.replace(".", "-")
                price_data_df = self.get_data(price_ticker)
                print(f"Got Data for {price_ticker}.")
    

            price_data_name = 'PriceData'

            self.json(from_obj=price_data_df, export_to=p, filename=price_data_name)
            print('PriceData exported')

            # Stock Info ----------------------------------------------------------------------------------------------
            # Export Stock_Info
            stock_info_df = self.stock_info()
            stock_info_name = 'StockInformation'

            self.json(from_obj=stock_info_df, export_to=p, filename=stock_info_name)
            print('StockInfo exported')
            
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
            # Fiscal Year ----------------------------------------------------------------------------------------------
            # Export Fiscal Year Start Dates, and prices
            try:
                fiscal_df = self.fiscal_year_prices()
                fiscal_name = 'FiscalYear'

                self.json(from_obj=fiscal_df, export_to=p, filename=fiscal_name)
                print('FiscalYear exported')
            
            except KeyError:
                print(f'Unable to retrieve information about {self.ticker}. Continuing to download data for other stocks.')
                pass
            #------------------------------

            # Output to run
            print(f'''
Finished Data Download for {self.ticker}, closing browser now.
********************************************************************************************************************

            ''')

        # If ticker is not found, pass.
        else:
            print(f'{self.ticker} not found in MarketWatch.com Database. Will continue downloading next ticker.')
            pass

        # End browser session
        self.driver_end()

        # Buffer
        for i in range(1,5):
            time.sleep(1)
            print(f"[{5-i}] Waiting for next ticker.....")
            

        return exists

        