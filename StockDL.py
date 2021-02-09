from Stock_Data import Stock_Data
import pandas as pd
import numpy as np
from datetime import datetime
import time
from pathlib import Path


class StockDL(Stock_Data):
    '''
    Full optimized stock data information scraper by Gavin Loo
    Stores data into JSON format on folder
    Uses data from YahooFinance and MarketWatch.com
    '''

    # Initialize StockDL Class
    def __init__(self, ticker, PATH=r'C:\Program Files (x86)\chromedriver.exe', ignore_errors=True):
        '''
        Initialize StockDL Class, consolidated from Stock_Data class and added Database PATH
        '''
        Stock_Data.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe', ignore_errors=True)

    def stockdl(self, DB_PATH='C:/Users/Dennis Loo.000/Desktop/FinData', download="ALL", buffer=5):
        '''    
        DB_PATH = Place to store downloaded JSON files
        Minimum buffer = 1 second
        Download parameters:
            - 'ALL' - Download All Parameters
            - 'PRICE' Download PriceData
            - 'MAIN' Download StockInfo and KeyData
            - 'PROFILE' Download all Profile Data
            - 'INCOME' Download IncomeStatement
            - 'BALANCE' Download BalanceSheet
            - 'CASHFLOW' Download CashFlow
            - 'FISCALYEAR' Download FiscalYear
        '''  
        #--------------------------------------------------------------------------------------------------------------
        #       Create Directory
        #--------------------------------------------------------------------------------------------------------------
        
        # Ticker download time
        tickstart_time = datetime.now()

        # Check if stock ticker exists
        exists = self.check_ticker()

        if exists == True:
            ## Create directory if directory does not exist
            exp_datetime = datetime.today()
            exp_date = exp_datetime.strftime("%Y-%m-%d")
            
            # Stock Exchange DIR Path
            exchange = self.exchange()
            exchange_path = exchange.replace(':', '')

            # Ticker Alphabet DIR Path
            ticker_index = self.ticker[0]

            # Path Class
            p = Path(f'{DB_PATH}/{exchange_path}/{ticker_index}/{self.ticker}')
            p.mkdir(parents=True, exist_ok=True)
            #--------------------------------------------------------------------------------------------------------------
            #       Download Functions
            #--------------------------------------------------------------------------------------------------------------
            def PRICE():
                # Price Data ----------------------------------------------------------------------------------------------
                # Get TData
                price_data_df = self.get_data()
                print(f"Got Data for {self.ticker}.")
        
                price_data_name = 'PriceData'

                self.json(from_obj=price_data_df, export_to=p, filename=price_data_name)
                print('PriceData exported')
                
            
            def MAIN():
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
            

            def PROFILE():
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
            

            def INCOME():
                # IncomeStatement Data ----------------------------------------------------------------------------------------------
                inc_df = self.income_statement()
                inc_name = 'IncomeStatement'
                
                self.json(from_obj=inc_df, export_to=p, filename=inc_name)
                print('IncomeStatement exported')
                #------------------------------

            
            def BALANCE():
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
            

            def CASHFLOW():
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

            
            def FISCALYEAR():
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

            
            def ALL():
                print(f'''

Initializing ALL download.
DOWNLOADING {self.ticker}...


                ''')
                # All Download
                dl_list = [PRICE(), MAIN(), PROFILE(), INCOME(), BALANCE(), CASHFLOW()]
                for i in range(len(dl_list)):
                    try:
                        dl_list[i]
                    except IndexError:
                        dl_list[i]
                    

            #------------------------------------------------------------------------------------------------------------------
            download_dict = {
                'ALL' : ALL,
                'PRICE' : PRICE,
                'MAIN' : MAIN,
                'PROFILE' : PROFILE,
                'INCOME' : INCOME,
                'BALANCE' : BALANCE,
                'CASHFLOW' : CASHFLOW,
                'FISCALYEAR' : FISCALYEAR

            }
            
            
            

            # Output to run
            print(f'''

********************************************************************************************************************
Data Downloaded from MarketWatch.com
Beginning Data Download for {self.ticker}.
            ''')
        
            if download != 'ALL':
                print(f'''

Initializing Individual download.
DOWNLOADING {download}...


                ''')
                # Use dictionary key to execute function
                download_dict[download]()
            
            elif download == 'ALL':
                ALL()

            else:
                print('''
Invalid keyword "download", please use proper keywords specified in the following list:
Download parameters:
- 'ALL' - Download All Parameters
- 'PRICE' Download PriceData
- 'MAIN' Download StockInfo and KeyData
- 'PROFILE' Download all Profile Data
- 'INCOME' Download IncomeStatement
- 'BALANCE' Download BalanceSheet
- 'CASHFLOW' Download CashFlow
- 'FISCALYEAR' Download FiscalYear
Thank you.

                ''')

            # Output to run
            print(f'''
Finished Data Download for {self.ticker}, closing browser now.
********************************************************************************************************************

            ''')

        # If ticker is not found, pass.
        else:
            print(f'{self.ticker} not found in MarketWatch.com Database. Will continue downloading next ticker.')
            pass

        # # End browser session
        # self.driver_end()

        # Buffer
        for i in range(1,buffer):
            time.sleep(1)
            print(f"[{buffer-i}] Waiting for next ticker.....")
        
        tickertime_taken = datetime.now() - tickstart_time
        print(f'''
                                                                    --Time Taken to Download {self.ticker}: ---{tickertime_taken}
        ''')

        # Returns whether ticker existed
        return exists

