from StockDL import StockDL
from datetime import datetime
import pandas as pd

class Downloader:
    '''
    Download Scraped Market Data formatter.
    '''
    def __init__(self):
        '''
        Initialize Downloader Class. Downloads from StockDL. Download data in a individual, list, csv format.
        '''
        pass
    

    def download(self,  type_, Driver_PATH='C:\Program Files (x86)\chromedriver.exe', DB_PATH=None, max=None, ticker=None, list_=None, csv=None, buffer=5, download="ALL", from_=None):
        '''
        Download Stock Data supplied by tickers in either string, list or csv.
        type_ keys:
            "string" : Download from specific ticker. Must specifiy arg* ticker.
            "list" : Download from a list. Must specify arg* list.
            "csv" : Download from a csv. Must specify arg* csv. CSV must contain column "Ticker"
        DB_PATH = Place to store downloaded JSON files
        Minimum buffer = 2 second
        From = Start downloading from. Please provide a string.
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
        # Start time of code
        start_time = datetime.now()

        download_list = []
        error_list = []

        if DB_PATH == None:
            print("Please specify a Database Path for downloads. Use DB_PATH var.")
            exit()

        # IF string
        if type_ == "string":
            stock = StockDL(ticker, PATH=Driver_PATH)
            try:
                dl = stock.stockdl(DB_PATH=DB_PATH, download=download, buffer=buffer)
                if dl == False:
                    error_list.append(ticker)
            # Error handling
            except ValueError or KeyError:
                error_list.append(ticker)
            
            if dl == True:
                download_list.append(ticker)

        # IF list
        if type_ == "list":
            components_list = list_
            dl = False

            if from_ != None:
                    index_ticker = components_list.index(from_)
                    components_list = components_list[index_ticker:]
            
            for ticker in components_list:
                stock = StockDL(ticker, PATH=Driver_PATH)
                try:
                    dl = stock.stockdl(DB_PATH=DB_PATH, download=download, buffer=buffer)
                    if dl == False:
                        error_list.append(ticker)
                # Error handling
                except ValueError or KeyError:
                    error_list.append(ticker)

                if dl == True:
                    download_list.append(ticker)

                # index
                idx_element = components_list.index(ticker)
                max_elements = len(components_list)
                prc_complete = round(idx_element/max_elements *100, 2)

                print(f'---Download Progress: {idx_element}/{max_elements}. {prc_complete}%/100%... ')

                print(f'Download List = {download_list}')
                print(f'Error List = {error_list}')

        # IF csv
        if type_ == "csv":
            with open(csv, 'r') as csv_:
                # Read CSV
                df = pd.read_csv(csv_)
                df = df.set_index('Ticker')

                # chunks of 10 lists
                components_list = df.index.tolist()

                if from_ != None:
                    index_ticker = components_list.index(from_)
                    components_list = components_list[index_ticker:]

                # If stock does not exist, add into error_list
                for ticker in components_list:
                    # Starting time
                    start_time_csv = datetime.now()
                    stock = StockDL(ticker, PATH=Driver_PATH)
                    try:
                        dl = stock.stockdl(DB_PATH=DB_PATH, download=download, buffer=buffer)

                        if dl == False:
                            error_list.append(ticker)
                            
                    # Error handling
                    except ValueError or KeyError:
                        error_list.append(ticker)

                    if dl == True:
                        download_list.append(ticker)

                    #Time
                    time_taken_csv = datetime.now() - start_time_csv    


                    # Ending time
                    print(f'---Time taken to download {ticker} = {time_taken_csv}')

                    # index
                    idx_element = components_list.index(ticker) +1
                    max_elements = len(components_list)
                    prc_complete = round(idx_element/max_elements *100, 2)

                    print(f'---Download Progress: {idx_element}/{max_elements}. {prc_complete}%/100%... ')

                    print(f'Download List = {download_list}')
                    print(f'Error List = {error_list}')


        time_taken = datetime.now() - start_time
        
        print(f'---Time taken = {time_taken}---')

        return None
